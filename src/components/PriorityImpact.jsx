import React from 'react'
import PriorityDistribution from './PriorityDistribution'
import { Sliders, Sparkles } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Section demonstrating how user's custom weight allocations directly steered the recommendation.
 * Dynamically resolves factor labels based on category.
 */
export default function PriorityImpact({ category = 'electronics', subcategory = '', priorities = {} }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const factors = categoryConfig.factors

  // Build key-to-name lookup
  const factorNameMap = {}
  factors.forEach((f) => {
    factorNameMap[f.key] = f.name
  })

  // Normalize priorities
  const p = { ...priorities }
  factors.forEach((f) => {
    if (p[f.key] === undefined) p[f.key] = 20
  })

  // Find the top 2 weighted factors dynamically
  const sorted = Object.entries(p)
    .filter(([k]) => factorNameMap[k])
    .sort((a, b) => b[1] - a[1])

  const top1 = sorted[0] || [factors[0]?.key, 20]
  const top2 = sorted[1] || [factors[1]?.key, 20]

  const isBalanced = top1[1] === top2[1] && top1[1] === 20

  const getDynamicExplanation = () => {
    if (isBalanced) {
      return `Because your priorities were balanced equally across all dimensions, every AI agent contributed an equal 20% weight to the synthesized ${categoryConfig.label} recommendation.`
    }
    const name1 = factorNameMap[top1[0]] || top1[0]
    const name2 = factorNameMap[top2[0]] || top2[0]
    return `Because ${name1.toLowerCase()} (${top1[1]}%) and ${name2.toLowerCase()} (${top2[1]}%) had the highest weights, options excelling in these areas exerted the greatest influence on the winning score.`
  }

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 shadow-xs mb-10">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
        <div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-bold uppercase tracking-wider mb-2">
            <Sliders className="w-3.5 h-3.5" />
            <span>Weight Steering</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
            Your priorities shaped the result ({categoryConfig.label})
          </h3>
          <p className="text-xs sm:text-sm text-slate-500 mt-1">
            The decision engine calculates composite rankings using your exact percentage distribution.
          </p>
        </div>
      </div>

      {/* Segmented bar & percentages */}
      <div className="mb-6">
        <PriorityDistribution category={category} subcategory={subcategory} priorities={p} />
      </div>

      {/* Dynamic Explanation Box */}
      <div className="p-4 sm:p-5 rounded-2xl bg-indigo-50/60 border border-indigo-100 flex items-start gap-3.5">
        <div className="w-8 h-8 rounded-xl bg-indigo-600 text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-2xs">
          <Sparkles className="w-4 h-4" />
        </div>
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-indigo-950 block mb-0.5">
            Weight Influence Analysis
          </span>
          <p className="text-xs sm:text-sm text-indigo-950 font-medium leading-relaxed">
            {getDynamicExplanation()}
          </p>
        </div>
      </div>
    </div>
  )
}
