import React from 'react'
import ProgressSteps from './ProgressSteps'
import { Award, CheckCircle2 } from 'lucide-react'

/**
 * Header for the Results page with Step 5 indicator and celebration badge.
 */
export default function ResultsHeader() {
  return (
    <div className="w-full mb-8">
      {/* 5-Step Progress Bar: Step 5 Active */}
      <ProgressSteps currentStep={5} />

      {/* Main Success Title */}
      <div className="text-center max-w-2xl mx-auto">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold uppercase tracking-wider mb-3 shadow-2xs">
          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
          <span>Decision Complete</span>
        </div>

        <h1 className="text-3xl sm:text-5xl font-extrabold text-slate-900 tracking-tight mb-3">
          Your Decision is Ready
        </h1>

        <p className="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
          Five AI perspectives have been combined with your priorities to find the strongest match.
        </p>
      </div>
    </div>
  )
}
