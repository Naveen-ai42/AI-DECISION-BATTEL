import React from 'react'
import { useNavigate } from 'react-router-dom'
import { HelpCircle, ArrowRight } from 'lucide-react'
import ResultsHeader from '../components/ResultsHeader'
import WinnerCard from '../components/WinnerCard'
import RankedOptionsList from '../components/RankedOptionsList'
import UseCaseRankings from '../components/UseCaseRankings'
import ProductReviews from '../components/ProductReviews'
import OptionComparisonTable from '../components/OptionComparisonTable'
import WhyItWon from '../components/WhyItWon'
import PriorityImpact from '../components/PriorityImpact'
import AgentScoreBreakdown from '../components/AgentScoreBreakdown'
import DisagreementSection from '../components/DisagreementSection'
import RequirementsCheck from '../components/RequirementsCheck'
import DealBreakerCheck from '../components/DealBreakerCheck'
import ConfidenceCard from '../components/ConfidenceCard'
import DetailedAnalysis from '../components/DetailedAnalysis'
import BottomLine from '../components/BottomLine'
import ResultActions from '../components/ResultActions'
import Button from '../components/Button'
import { useDecision } from '../hooks/useDecision'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Final Decision Results Page (/results).
 * Synthesizes winning recommendation, ranked candidate options list,
 * comparative factor matrix, why it won, weighted priority impacts,
 * agent breakdown, disagreements, and requirement checks dynamically for any category.
 */
export default function ResultsPage() {
  const navigate = useNavigate()
  const { decision, resetDecision } = useDecision()

  // Missing data state check
  if (!decision?.description || decision.description.trim().length === 0) {
    return (
      <div className="flex-1 w-full py-16 px-4 flex items-center justify-center">
        <div className="max-w-md w-full bg-white border border-slate-200 rounded-3xl p-8 sm:p-10 text-center shadow-xs">
          <div className="w-14 h-14 rounded-2xl bg-amber-50 border border-amber-100 text-amber-600 flex items-center justify-center mx-auto mb-4">
            <HelpCircle className="w-7 h-7" />
          </div>
          <h2 className="text-2xl font-bold text-slate-900 mb-2">
            No decision result found.
          </h2>
          <p className="text-sm text-slate-500 mb-6">
            You must enter a decision and run the analysis before viewing results.
          </p>
          <Button to="/create" variant="primary" className="w-full justify-center">
            <span>Start a Decision</span>
            <ArrowRight className="w-4 h-4 ml-1.5" />
          </Button>
        </div>
      </div>
    )
  }

  const category = decision.category || 'electronics'
  const subcategory = decision.subcategory || ''
  const categoryConfig = getCategoryConfig(category, subcategory)

  // Active agents (from analysis results if completed, or categoryConfig definitions)
  const agents = decision.analysisResults?.agents || categoryConfig.agents

  // Authoritative backend Decision Engine results (Source of truth)
  const backendEngine = decision.analysisResults?.decisionEngine || decision.analysisResults
  const backendScore = backendEngine?.overallScore
  const confidenceLevel = backendEngine?.confidence || 'High'
  const winnerName = backendEngine?.recommendation || categoryConfig.defaultRecommendation

  // Multiple Ranked Options from backend analysis
  const rawRankings = decision.analysisResults?.rankings || []
  const comparison = decision.analysisResults?.comparison || null

  // Dynamic Overall Weighted Score fallback if backend score is unavailable
  const priorities = decision.priorities || {}
  const fallbackScore = Math.round(
    categoryConfig.factors.reduce((sum, factor, idx) => {
      const matchedAgent = agents.find(
        (a) =>
          a.id?.toLowerCase() === factor.key.toLowerCase() ||
          factor.key.toLowerCase().includes((a.id || '').toLowerCase()) ||
          (a.id || '').toLowerCase().includes(factor.key.toLowerCase()) ||
          a.name?.toLowerCase().includes(factor.name.toLowerCase()) ||
          factor.name.toLowerCase().includes((a.name || '').toLowerCase().replace(' agent', ''))
      ) || agents[idx]
      const score = matchedAgent?.score ?? 85
      const weight = (priorities[factor.key] ?? 20) / 100
      return sum + score * weight
    }, 0)
  )

  const overallScore =
    typeof backendScore === 'number' ? Math.round(backendScore) : fallbackScore

  // Backend rankings are the source of truth.
  // Never invent fixed candidate options on the frontend.
  const rankings = rawRankings
  const phoneType = rankings.some((item) => item.subcategory === 'smartphone')
    ? 'smartphone'
    : rankings.some((item) => item.subcategory === 'laptop')
      ? 'laptop'
      : 'generic'
  const factorDefinitions = comparison?.factors?.length
    ? comparison.factors
    : Object.keys(rankings[0]?.factorScores || {}).map((key) => ({
      key,
      name: key.replace(/([A-Z])/g, ' $1'),
    }))
  const rankedItemLabel = phoneType === 'generic' ? categoryConfig.label || category : undefined

  const candidateCount =
    decision.analysisResults?.candidateCount || rankings.length
  const topN = decision.analysisResults?.topN || 5
  const dataSource = decision.analysisResults?.dataSource || 'demo'

  return (
    <div className="flex-1 w-full py-10 sm:py-14 px-4 sm:px-6 lg:px-8">
      <div className="max-w-[960px] mx-auto">
        <ResultsHeader />

        <WinnerCard
          winnerName={winnerName}
          overallScore={overallScore}
          category={category}
          subcategory={subcategory}
        />

        {rankings.length > 0 && (
          <UseCaseRankings
            key={`${category}-${subcategory}-factor-rankings`}
            rankings={rankings}
            productType={phoneType}
            factorDefinitions={factorDefinitions}
            itemLabel={rankedItemLabel}
          />
        )}

        <RankedOptionsList
          rankings={rankings}
          candidateCount={candidateCount}
          topN={topN}
          dataSource={dataSource}
          category={category}
          subcategory={subcategory}
        />

        {rankings.length > 0 && (
          <ProductReviews rankings={rankings} winnerName={winnerName} />
        )}

        {comparison && (
          <OptionComparisonTable
            comparison={comparison}
            rankings={rankings}
          />
        )}

        <WhyItWon category={category} subcategory={subcategory} />

        <PriorityImpact
          category={category}
          subcategory={subcategory}
          priorities={decision.priorities}
        />

        <AgentScoreBreakdown
          category={category}
          subcategory={subcategory}
          agents={agents}
        />

        <DisagreementSection
          category={category}
          subcategory={subcategory}
          agents={agents}
        />

        <RequirementsCheck
          category={category}
          subcategory={subcategory}
          requirements={decision.requirements}
        />

        <DealBreakerCheck dealBreakers={decision.dealBreakers} />

        <ConfidenceCard confidenceLevel={confidenceLevel} />

        <DetailedAnalysis agents={agents} />

        <BottomLine />

        <ResultActions
          decision={decision}
          winnerName={winnerName}
          overallScore={overallScore}
          onReset={resetDecision}
        />
      </div>
    </div>
  )
}