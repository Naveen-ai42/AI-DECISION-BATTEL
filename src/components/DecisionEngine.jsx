import React from 'react'
import { Cpu, Award, CheckCircle2 } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Decision Engine synthesizer displaying the mathematical weighting flow:
 * Agent Results -> Your Priority Weights -> Decision Engine -> Overall Score
 * Dynamically computes factor scores based on category.
 */
export default function DecisionEngine({ category = 'electronics', subcategory = '', agents = [], priorities = {}, decisionEngineResult }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const factors = categoryConfig.factors

  // Match each factor to its corresponding agent
  const factorCalculations = factors.map((factor, idx) => {
    const matchedAgent = agents.find((a) =>
      a.id?.toLowerCase() === factor.key.toLowerCase() ||
      factor.key.toLowerCase().includes((a.id || '').toLowerCase()) ||
      (a.id || '').toLowerCase().includes(factor.key.toLowerCase()) ||
      a.name?.toLowerCase().includes(factor.name.toLowerCase()) ||
      factor.name.toLowerCase().includes((a.name || '').toLowerCase().replace(' agent', ''))
    ) || agents[idx]

    const score = matchedAgent?.score ?? 85
    const weight = priorities[factor.key] ?? 20
    const points = Number(((score * weight) / 100).toFixed(1))

    return {
      key: factor.key,
      name: factor.name,
      score,
      weight,
      points,
    }
  })

  // Mathematical sum of weighted contributions
  const calculatedWeightedSum = factorCalculations.reduce((sum, item) => sum + item.points, 0)

  // Authoritative score from backend if available
  const backendScore = decisionEngineResult?.overallScore
  const overallScore = backendScore !== undefined && backendScore !== null
    ? (Number.isInteger(backendScore) ? backendScore : Number(backendScore.toFixed(1)))
    : Number(calculatedWeightedSum.toFixed(1))

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-9 shadow-xs mb-10">
      {/* Title */}
      <div className="text-center max-w-xl mx-auto mb-8">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-bold uppercase tracking-wider mb-2">
          <Cpu className="w-3.5 h-3.5" />
          <span>Synthesizer</span>
        </div>
        <h3 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
          Decision Engine
        </h3>
        <p className="text-sm text-slate-600 mt-1">
          Combining {categoryConfig.label} AI agent perspectives with your priorities.
        </p>
      </div>

      {/* Visual Flow Stages */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        {/* Stage 1 */}
        <div className="bg-slate-50/70 border border-slate-200 rounded-2xl p-4 text-center flex flex-col justify-between">
          <div>
            <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1">
              Stage 01
            </span>
            <div className="text-sm font-bold text-slate-900 mb-2">
              Agent Results
            </div>
            <p className="text-xs text-slate-500">
              5 independent expert evaluations
            </p>
          </div>
          <div className="mt-3 pt-3 border-t border-slate-200/60 font-mono text-xs text-indigo-600 font-bold truncate">
            {factorCalculations.map((f) => f.score).join(', ')}
          </div>
        </div>

        {/* Stage 2 */}
        <div className="bg-slate-50/70 border border-slate-200 rounded-2xl p-4 text-center flex flex-col justify-between">
          <div>
            <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1">
              Stage 02
            </span>
            <div className="text-sm font-bold text-slate-900 mb-2">
              Your Priority Weights
            </div>
            <p className="text-xs text-slate-500">
              User-calibrated weight allocations
            </p>
          </div>
          <div className="mt-3 pt-3 border-t border-slate-200/60 font-mono text-xs text-indigo-600 font-bold">
            Sum = 100%
          </div>
        </div>

        {/* Stage 3 */}
        <div className="bg-slate-900 text-white rounded-2xl p-4 text-center flex flex-col justify-between shadow-xs">
          <div>
            <span className="text-[11px] font-bold uppercase tracking-wider text-indigo-300 block mb-1">
              Stage 03
            </span>
            <div className="text-sm font-bold text-white mb-2">
              Decision Engine
            </div>
            <p className="text-xs text-slate-300">
              Dynamic multi-criteria matrix
            </p>
          </div>
          <div className="mt-3 pt-3 border-t border-slate-800 font-mono text-xs text-emerald-400 font-bold">
            Running synthesis
          </div>
        </div>

        {/* Stage 4 */}
        <div className="bg-emerald-50/70 border-2 border-emerald-500/30 rounded-2xl p-4 text-center flex flex-col justify-between shadow-xs">
          <div>
            <span className="text-[11px] font-bold uppercase tracking-wider text-emerald-700 block mb-1">
              Consensus
            </span>
            <div className="text-sm font-bold text-slate-900 mb-2">
              Overall Score
            </div>
            <p className="text-xs text-slate-600">
              Weighted composite verdict
            </p>
          </div>
          <div className="mt-3 pt-3 border-t border-emerald-200/60 font-mono text-base text-emerald-800 font-extrabold">
            {overallScore} / 100
          </div>
        </div>
      </div>

      {/* Weighted Calculation Breakdown */}
      <div className="bg-slate-50/60 border border-slate-200 rounded-2xl p-5 mb-8">
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
            Weighted Synthesis Breakdown
          </span>
          <span className="text-xs text-slate-400">
            Formula: Score &times; (Weight / 100)
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-5 gap-2.5">
          {factorCalculations.map((item) => (
            <div
              key={item.key}
              className="bg-white border border-slate-200 rounded-xl p-3 text-center"
            >
              <div className="text-xs font-semibold text-slate-800 truncate mb-1">
                {item.name}
              </div>
              <div className="text-[11px] text-slate-500">
                {item.score} &times; {item.weight}%
              </div>
              <div className="mt-1 font-mono text-xs font-bold text-indigo-600">
                +{item.points} pts
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Overall Score Highlight Card */}
      <div className="bg-gradient-to-br from-indigo-50/50 via-white to-emerald-50/40 border border-slate-200 rounded-2xl p-6 sm:p-7 flex flex-col sm:flex-row items-center justify-between gap-6">
        <div className="flex items-center gap-4 text-center sm:text-left">
          <div className="w-14 h-14 rounded-2xl bg-indigo-600 text-white flex items-center justify-center flex-shrink-0 shadow-md shadow-indigo-500/20">
            <Award className="w-7 h-7" />
          </div>
          <div>
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-xs font-semibold mb-1">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
              <span>Overall Match</span>
            </div>
            <h4 className="text-xl sm:text-2xl font-extrabold text-slate-900">
              Calculated Decision Consensus
            </h4>
            <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
              Synthesized evaluation across {factors.map((f) => f.name).join(', ')} according to your calibrated weights.
            </p>
          </div>
        </div>

        <div className="bg-white border border-slate-200 px-6 py-4 rounded-2xl text-center shadow-xs flex-shrink-0 min-w-[140px]">
          <span className="text-4xl font-extrabold text-slate-900 font-mono block">
            {overallScore}
          </span>
          <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
            out of 100
          </span>
        </div>
      </div>
    </div>
  )
}
