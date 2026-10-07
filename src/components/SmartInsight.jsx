import React from 'react'
import { Sparkles } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Dynamic AI consensus preview message based on category and priority distribution.
 */
export default function SmartInsight({ category = 'electronics', subcategory = '', priorities = {} }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const factors = categoryConfig.factors

  const getInsight = () => {
    const values = factors.map((f) => priorities[f.key] ?? 20)
    const maxVal = Math.max(...values)
    const minVal = Math.min(...values)

    // If all are approximately equal
    if (maxVal - minVal <= 4) {
      return `Your priorities are balanced, so the ${categoryConfig.label} decision engine will consider every factor equally.`
    }

    // Find the factor with max weight
    const topFactor = factors.find((f) => (priorities[f.key] ?? 20) === maxVal)
    if (topFactor) {
      return `You are prioritizing ${topFactor.name} (${maxVal}%). Agents focusing on ${topFactor.desc.toLowerCase()} will have the greatest influence on the recommendation.`
    }

    return `Your priorities are balanced, so the final decision will evaluate every factor equally.`
  }

  return (
    <div className="bg-indigo-50/70 border border-indigo-100/90 rounded-2xl p-4 sm:p-4.5 flex items-start gap-3">
      <div className="w-8 h-8 rounded-xl bg-indigo-600 text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
        <Sparkles className="w-4 h-4" />
      </div>
      <div>
        <div className="text-xs font-bold uppercase tracking-wider text-indigo-900 mb-0.5">
          AI Consensus Preview
        </div>
        <p className="text-sm text-indigo-950 font-medium leading-relaxed">
          {getInsight()}
        </p>
      </div>
    </div>
  )
}
