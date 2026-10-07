import React from 'react'
import { ShieldCheck, Info } from 'lucide-react'

/**
 * Clean Decision Confidence rating card with transparent demo disclaimer.
 */
export default function ConfidenceCard({ confidenceLevel = 'High' }) {
  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 shadow-xs mb-10">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100 mb-4">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-1">
            Statistical Alignment
          </span>
          <h3 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
            Decision Confidence
          </h3>
        </div>

        <div className="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 px-4 py-2 rounded-2xl self-start sm:self-auto">
          <ShieldCheck className="w-5 h-5 text-emerald-600" />
          <span className="text-base font-extrabold text-emerald-800">
            {confidenceLevel}
          </span>
        </div>
      </div>

      <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal mb-3">
        Confidence is based on how consistently the AI perspectives support the recommendation and how well the option matches your weighted priorities.
      </p>

      <div className="flex items-center gap-1.5 text-[11px] text-slate-400">
        <Info className="w-3.5 h-3.5 flex-shrink-0" />
        <span>Demonstration metric based on standard deviation among agent scores.</span>
      </div>
    </div>
  )
}
