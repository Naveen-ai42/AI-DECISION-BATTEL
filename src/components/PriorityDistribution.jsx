import React from 'react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Clean segmented horizontal distribution bar representing the 100% priority breakdown.
 * Category-aware colors and factor labels.
 */
export default function PriorityDistribution({ category = 'electronics', subcategory = '', priorities = {} }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const factors = categoryConfig.factors

  const total = factors.reduce((sum, f) => sum + (priorities[f.key] || 0), 0)

  return (
    <div className="w-full bg-slate-50/80 border border-slate-200/90 rounded-2xl p-4 sm:p-5">
      <div className="flex items-center justify-between mb-2.5">
        <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">
          Weight Distribution ({categoryConfig.label})
        </span>
        <span className="text-xs font-mono font-bold text-slate-700">
          Total: {total}%
        </span>
      </div>

      {/* Segmented bar */}
      <div className="w-full h-3.5 rounded-full bg-slate-200 overflow-hidden flex shadow-inner">
        {factors.map((f) => {
          const pct = priorities[f.key] || 0
          if (pct <= 0) return null
          return (
            <div
              key={f.key}
              className={`h-full ${f.bg} transition-all duration-200`}
              style={{ width: `${pct}%` }}
              title={`${f.name}: ${pct}%`}
            />
          )
        })}
      </div>

      {/* Legend */}
      <div className="flex flex-wrap items-center justify-between gap-y-2 gap-x-4 mt-3 pt-3 border-t border-slate-200/60 text-xs">
        {factors.map((f) => {
          const pct = priorities[f.key] || 0
          return (
            <div key={f.key} className="flex items-center gap-1.5">
              <span className={`w-2.5 h-2.5 rounded-full ${f.bg}`} />
              <span className="font-medium text-slate-600">{f.name}:</span>
              <span className="font-mono font-bold text-slate-900">{pct}%</span>
            </div>
          )
        })}
      </div>
    </div>
  )
}
