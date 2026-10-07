import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import ProgressSteps from '../components/ProgressSteps'
import DecisionSummary from '../components/DecisionSummary'
import RequirementInput from '../components/RequirementInput'
import DealBreakerInput from '../components/DealBreakerInput'
import PrioritySlider from '../components/PrioritySlider'
import AdvancedPreferences from '../components/AdvancedPreferences'
import Button from '../components/Button'
import { useDecision } from '../hooks/useDecision'
import { getCategoryConfig, getDefaultPrioritiesForCategory } from '../config/categoryConfig'

/**
 * Step 2 of Decision Arena: Requirements & Priorities (/requirements).
 * Dynamically displays factors, agent metrics, and suggestion tags according to the selected category.
 */
export default function RequirementsPage() {
  const navigate = useNavigate()
  const { decision, updateDecision } = useDecision()

  const category = decision?.category || 'electronics'
  const subcategory = decision?.subcategory || ''
  const categoryConfig = getCategoryConfig(category, subcategory)

  // Requirements state
  const [requirements, setRequirements] = useState(decision.requirements || [])
  const [dealBreakers, setDealBreakers] = useState(decision.dealBreakers || [])

  // Priority state initialized dynamically for current category & subcategory
  const [priorities, setPriorities] = useState(() => {
    const existing = decision?.priorities || {}
    const hasAllKeys = categoryConfig.factors.every((f) => existing[f.key] !== undefined)
    return hasAllKeys ? existing : getDefaultPrioritiesForCategory(category, subcategory)
  })

  // Keep priorities in sync if category or subcategory changed
  useEffect(() => {
    const hasAllKeys = categoryConfig.factors.every((f) => priorities[f.key] !== undefined)
    if (!hasAllKeys) {
      setPriorities(getDefaultPrioritiesForCategory(category, subcategory))
    }
  }, [category, subcategory])

  // Advanced preferences
  const [riskTolerance, setRiskTolerance] = useState(
    decision.riskTolerance || 'balanced'
  )
  const [decisionStyle, setDecisionStyle] = useState(
    decision.decisionStyle || 'best-overall'
  )

  // Add / remove requirement
  const handleAddRequirement = (newReq) => {
    setRequirements((prev) => [...prev, newReq])
  }
  const handleRemoveRequirement = (reqToRemove) => {
    setRequirements((prev) => prev.filter((r) => r !== reqToRemove))
  }

  // Add / remove deal breaker
  const handleAddDealBreaker = (newDb) => {
    setDealBreakers((prev) => [...prev, newDb])
  }
  const handleRemoveDealBreaker = (dbToRemove) => {
    setDealBreakers((prev) => prev.filter((d) => d !== dbToRemove))
  }

  // Reset priorities to balanced (20% each) for the active category & subcategory
  const handleResetPriorities = () => {
    setPriorities(getDefaultPrioritiesForCategory(category, subcategory))
  }

  // Handle advanced preferences change
  const handleAdvancedChange = (field, value) => {
    if (field === 'riskTolerance') setRiskTolerance(value)
    if (field === 'decisionStyle') setDecisionStyle(value)
  }

  // Submit and proceed to /battle
  const handleStartBattle = (e) => {
    e.preventDefault()

    const fullDecisionPayload = {
      ...decision,
      requirements,
      dealBreakers,
      priorities,
      riskTolerance,
      decisionStyle,
    }

    updateDecision(fullDecisionPayload)
    navigate('/battle')
  }

  return (
    <div className="flex-1 w-full py-10 sm:py-14 px-4 sm:px-6 lg:px-8">
      <div className="max-w-[900px] mx-auto">
        {/* Progress Indicator: Step 2 active */}
        <ProgressSteps currentStep={2} />

        {/* Top Header */}
        <div className="text-center max-w-2xl mx-auto mb-8">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-2">
            Tell us what matters.
          </h1>
          <p className="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
            Calibrate the priority weights for {categoryConfig.label}. The AI agents will score your options against these criteria.
          </p>
        </div>

        {/* 1. Summary of Previous Step Decision */}
        <DecisionSummary decision={decision} />

        <div className="space-y-8">
          {/* 2. Must-have Requirements */}
          <RequirementInput
            category={category}
            subcategory={subcategory}
            requirements={requirements}
            onAdd={handleAddRequirement}
            onRemove={handleRemoveRequirement}
          />

          {/* 3. Deal Breakers */}
          <DealBreakerInput
            category={category}
            subcategory={subcategory}
            dealBreakers={dealBreakers}
            onAdd={handleAddDealBreaker}
            onRemove={handleRemoveDealBreaker}
          />

          {/* 4. Priority Section (Dynamic factors for this category) */}
          <PrioritySlider
            category={category}
            subcategory={subcategory}
            priorities={priorities}
            onChange={setPriorities}
            onReset={handleResetPriorities}
          />

          {/* 5. Optional Advanced Preferences */}
          <AdvancedPreferences
            riskTolerance={riskTolerance}
            decisionStyle={decisionStyle}
            onChange={handleAdvancedChange}
          />

          {/* 6. Bottom Actions */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-slate-200/60">
            <Button
              to="/create"
              variant="secondary"
              className="w-full sm:w-auto gap-2 text-sm order-2 sm:order-1"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Back</span>
            </Button>

            <Button
              onClick={handleStartBattle}
              variant="primary"
              className="w-full sm:w-auto px-8 py-3.5 text-base shadow-sm hover:shadow-md order-1 sm:order-2"
            >
              <span>Start AI Battle</span>
              <ArrowRight className="w-4 h-4 ml-2" />
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}
