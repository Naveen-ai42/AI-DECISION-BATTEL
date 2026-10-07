import React from 'react'
import { Sparkles } from 'lucide-react'

/**
 * Clean executive summary bottom-line card.
 */
export default function BottomLine() {
  return (
    <div className="w-full bg-slate-900 text-white rounded-3xl p-6 sm:p-8 shadow-xs mb-10 relative overflow-hidden">
      <div className="flex items-start gap-4">
        <div className="w-10 h-10 rounded-2xl bg-indigo-500/20 text-indigo-400 border border-indigo-400/30 flex items-center justify-center flex-shrink-0 mt-0.5">
          <Sparkles className="w-5 h-5" />
        </div>
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-indigo-300 block mb-1">
            Bottom line
          </span>
          <p className="text-base sm:text-lg font-medium text-slate-100 leading-relaxed">
            Based on your priorities, requirements and the combined AI perspectives, this option provides the strongest overall match.
          </p>
        </div>
      </div>
    </div>
  )
}
