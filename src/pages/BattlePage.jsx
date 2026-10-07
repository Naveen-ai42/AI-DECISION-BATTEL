import React, { useState, useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { HelpCircle, ArrowRight } from 'lucide-react'
import BattleHeader from '../components/BattleHeader'
import BattleDecisionSummary from '../components/BattleDecisionSummary'
import BattleControls from '../components/BattleControls'
import BattleProgress from '../components/BattleProgress'
import AgentGrid from '../components/AgentGrid'
import AgentDetailModal from '../components/AgentDetailModal'
import DecisionEngine from '../components/DecisionEngine'
import DisagreementSection from '../components/DisagreementSection'
import BattleActions from '../components/BattleActions'
import Button from '../components/Button'
import { useDecision } from '../hooks/useDecision'
import { getCategoryConfig } from '../config/categoryConfig'
import { startDecisionAnalysis } from '../services/api'

/**
 * AI Decision Battle Page (/battle)
 * Orchestrates category-aware multi-agent analysis connected to the FastAPI backend.
 */
export default function BattlePage() {
  const navigate = useNavigate()
  const { decision, updateDecision } = useDecision()

  const category = decision?.category || 'electronics'
  const subcategory = decision?.subcategory || ''
  const categoryConfig = getCategoryConfig(category, subcategory)

  // Track state: 'idle' | 'running' | 'completed' | 'error'
  const [battleState, setBattleState] = useState('idle')
  const [errorMessage, setErrorMessage] = useState(null)
  const [isConnectionError, setIsConnectionError] = useState(false)

  // Current category/subcategory-specific agent cards state
  const [agents, setAgents] = useState(() =>
    categoryConfig.agents.map((a) => ({ ...a, status: 'waiting' }))
  )

  // Keep visual agents aligned if category or subcategory changes
  useEffect(() => {
    setAgents(categoryConfig.agents.map((a) => ({ ...a, status: 'waiting' })))
  }, [category, subcategory])

  // Backend response cache
  const [backendData, setBackendData] = useState(null)

  // Currently inspected agent modal
  const [inspectedAgent, setInspectedAgent] = useState(null)

  const timerRef = useRef([])
  const backendPromiseRef = useRef(null)

  const clearAllTimers = () => {
    timerRef.current.forEach((t) => clearTimeout(t))
    timerRef.current = []
  }

  useEffect(() => {
    return () => clearAllTimers()
  }, [])

  // Handle direct navigation empty state
  if (!decision?.description || decision.description.trim().length === 0) {
    return (
      <div className="flex-1 w-full py-16 px-4 flex items-center justify-center">
        <div className="max-w-md w-full bg-white border border-slate-200 rounded-3xl p-8 sm:p-10 text-center shadow-xs">
          <div className="w-14 h-14 rounded-2xl bg-amber-50 border border-amber-100 text-amber-600 flex items-center justify-center mx-auto mb-4">
            <HelpCircle className="w-7 h-7" />
          </div>
          <h2 className="text-2xl font-bold text-slate-900 mb-2">
            No decision found.
          </h2>
          <p className="text-sm text-slate-500 mb-6">
            Please define what you are trying to decide before entering the arena.
          </p>
          <Button to="/create" variant="primary" className="w-full justify-center">
            <span>Create a Decision</span>
            <ArrowRight className="w-4 h-4 ml-1.5" />
          </Button>
        </div>
      </div>
    )
  }

  /**
   * Helper to merge backend agent results into our visual agent list
   */
  const mergeBackendResults = (rawBackendData) => {
    const categoryAgents = getCategoryConfig(decision?.category, decision?.subcategory).agents
    if (!rawBackendData) return categoryAgents.map((a) => ({ ...a, status: 'completed' }))

    const backendAgents = rawBackendData.agents || []
    return categoryAgents.map((initial) => {
      // Find matching backend agent by normalized name or agent id
      const matched = backendAgents.find((ba) =>
        ba.agent?.toLowerCase().includes(initial.id.toLowerCase()) ||
        ba.agent?.toLowerCase() === initial.name.toLowerCase() ||
        initial.name.toLowerCase().includes(ba.agent?.toLowerCase())
      )

      if (matched) {
        return {
          ...initial,
          score: matched.score ?? initial.score,
          conclusion: matched.conclusion || initial.conclusion,
          strengths: matched.strengths?.length > 0 ? matched.strengths : initial.strengths,
          concerns: matched.concerns?.length > 0 ? matched.concerns : initial.concerns,
          factors: matched.factors?.length > 0 ? matched.factors : initial.factors,
          status: 'completed',
        }
      }
      return { ...initial, status: 'completed' }
    })
  }

  // Start controlled visual simulation + backend API call
  const handleStartSimulation = () => {
    // Prevent duplicate triggers
    if (battleState === 'running') return

    clearAllTimers()
    setErrorMessage(null)
    setIsConnectionError(false)
    setBattleState('running')

    const categoryAgents = getCategoryConfig(decision?.category, decision?.subcategory).agents

    // Reset visual agents to waiting
    setAgents(categoryAgents.map((a) => ({ ...a, status: 'waiting' })))

    // 1. Concurrently call FastAPI backend
    const apiPromise = startDecisionAnalysis(decision)
      .then((data) => {
        setBackendData(data)
        return data
      })
      .catch((err) => {
        console.error('Decision Arena API error:', err)
        clearAllTimers()
        setBattleState('error')
        setIsConnectionError(Boolean(err.isConnectionError))
        setErrorMessage(
          err.isConnectionError
            ? 'Make sure the FastAPI server is running on http://127.0.0.1:8001.'
            : (err.message || 'Analysis could not be completed.')
        )
        throw err
      })

    backendPromiseRef.current = apiPromise

    // 2. Controlled visual animation stepping through 5 agents (total ~5.5s)
    const stepInterval = 1100

    categoryAgents.forEach((agent, index) => {
      // Step A: Mark current agent as analyzing
      const startTimer = setTimeout(() => {
        setAgents((prev) =>
          prev.map((a, i) => {
            if (i === index) return { ...a, status: 'analyzing' }
            if (i < index) return { ...a, status: 'completed' }
            return { ...a, status: 'waiting' }
          })
        )
      }, index * stepInterval)

      // Step B: Mark current agent as completed
      const doneTimer = setTimeout(() => {
        setAgents((prev) =>
          prev.map((a, i) => (i <= index ? { ...a, status: 'completed' } : a))
        )

        // When visual steps for the last agent conclude
        if (index === categoryAgents.length - 1) {
          // Await API response before finalizing
          apiPromise
            .then((data) => {
              const mergedAgents = mergeBackendResults(data)
              setAgents(mergedAgents)
              setBattleState('completed')

              const engineResult = data.decisionEngine || data.decision || {}
              updateDecision({
                analysisResults: {
                  agents: mergedAgents,
                  decisionEngine: engineResult,
                  overallScore: engineResult.overallScore,
                  recommendation: engineResult.recommendation,
                  confidence: engineResult.confidence || 'High',
                  rankings: data.rankings || [],
                  bestOverall: data.bestOverall || null,
                  comparison: data.comparison || null,
                  candidateCount: data.candidateCount || (data.rankings?.length || 0),
                  filteredCandidateCount: data.filteredCandidateCount || (data.rankings?.length || 0),
                  topN: data.topN || 5,
                  dataSource: data.dataSource || 'demo',
                  isDemoData: data.isDemoData ?? true,
                  completedAt: new Date().toISOString(),
                },
              })
            })
            .catch(() => {
              // Error handled in catch above
            })
        }
      }, (index + 1) * stepInterval)

      timerRef.current.push(startTimer, doneTimer)
    })
  }

  // Fast-forward / Skip simulation
  const handleSkipSimulation = () => {
    clearAllTimers()

    if (backendPromiseRef.current) {
      backendPromiseRef.current
        .then((data) => {
          const mergedAgents = mergeBackendResults(data)
          setAgents(mergedAgents)
          setBattleState('completed')

          const engineResult = data.decisionEngine || data.decision || {}
          updateDecision({
            analysisResults: {
              agents: mergedAgents,
              decisionEngine: engineResult,
              overallScore: engineResult.overallScore,
              recommendation: engineResult.recommendation,
              confidence: engineResult.confidence || 'High',
              rankings: data.rankings || [],
              bestOverall: data.bestOverall || null,
              comparison: data.comparison || null,
              candidateCount: data.candidateCount || (data.rankings?.length || 0),
              filteredCandidateCount: data.filteredCandidateCount || (data.rankings?.length || 0),
              topN: data.topN || 5,
              dataSource: data.dataSource || 'demo',
              isDemoData: data.isDemoData ?? true,
              completedAt: new Date().toISOString(),
            },
          })
        })
        .catch(() => {
          // Error handled in API catch
        })
    }
  }

  // Restart simulation
  const handleRestart = () => {
    clearAllTimers()
    const categoryAgents = getCategoryConfig(decision?.category, decision?.subcategory).agents
    setAgents(categoryAgents.map((a) => ({ ...a, status: 'waiting' })))
    setBackendData(null)
    setErrorMessage(null)
    setIsConnectionError(false)
    setBattleState('idle')
  }

  // Navigate to /results
  const handleProceedToResults = () => {
    const engineResult = backendData?.decisionEngine || backendData?.decision || {}
    const authoritativeScore = engineResult.overallScore ?? 88

    updateDecision({
      analysisResults: {
        agents,
        decisionEngine: engineResult,
        overallScore: authoritativeScore,
        recommendation: engineResult.recommendation || getCategoryConfig(decision?.category, decision?.subcategory).defaultRecommendation,
        confidence: engineResult.confidence || 'High',
        rankings: backendData?.rankings || decision?.analysisResults?.rankings || [],
        bestOverall: backendData?.bestOverall || decision?.analysisResults?.bestOverall || null,
        comparison: backendData?.comparison || decision?.analysisResults?.comparison || null,
        candidateCount: backendData?.candidateCount || decision?.analysisResults?.candidateCount || (backendData?.rankings?.length || 0),
        filteredCandidateCount: backendData?.filteredCandidateCount || decision?.analysisResults?.filteredCandidateCount || (backendData?.rankings?.length || 0),
        topN: backendData?.topN || decision?.analysisResults?.topN || 5,
        dataSource: backendData?.dataSource || decision?.analysisResults?.dataSource || 'demo',
        isDemoData: backendData?.isDemoData ?? true,
        completedAt: new Date().toISOString(),
      },
    })

    navigate('/results')
  }

  const isCompleted = battleState === 'completed'
  const currentEngineResult = backendData?.decisionEngine || backendData?.decision || decision?.analysisResults?.decisionEngine

  return (
    <div className="flex-1 w-full py-10 sm:py-14 px-4 sm:px-6 lg:px-8">
      <div className="max-w-[960px] mx-auto">
        {/* Progress Header */}
        <BattleHeader />

        {/* Compact Decision Summary Card */}
        <BattleDecisionSummary decision={decision} />

        {/* Battle Controls with API status and error handling */}
        <BattleControls
          battleState={battleState}
          errorMessage={errorMessage}
          isConnectionError={isConnectionError}
          onStart={handleStartSimulation}
          onSkip={handleSkipSimulation}
          onRetry={handleStartSimulation}
        />

        {/* Live Status Matrix during analysis & post-completion */}
        {(battleState === 'running' || battleState === 'completed') && (
          <BattleProgress agents={agents} isCompleted={isCompleted} />
        )}

        {/* Agent Cards Grid */}
        <AgentGrid
          agents={agents}
          onInspect={(agent) => setInspectedAgent(agent)}
          canInspect={isCompleted}
        />

        {/* Post-battle sections: Decision Engine & Disagreement Analysis */}
        {isCompleted && (
          <>
            <DecisionEngine
              category={category}
              subcategory={subcategory}
              agents={agents}
              priorities={decision.priorities}
              decisionEngineResult={currentEngineResult}
            />

            <DisagreementSection
              category={category}
              subcategory={subcategory}
              agents={agents}
            />
          </>
        )}

        {/* Bottom Actions */}
        <BattleActions
          isCompleted={isCompleted}
          onProceed={handleProceedToResults}
          onRestart={handleRestart}
        />

        {/* Modal for inspecting individual agent breakdowns */}
        <AgentDetailModal
          agent={inspectedAgent}
          onClose={() => setInspectedAgent(null)}
        />
      </div>
    </div>
  )
}
