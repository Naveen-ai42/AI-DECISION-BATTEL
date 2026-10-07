import React from 'react'
import ProgressSteps from './ProgressSteps'
import { Swords } from 'lucide-react'

/**
 * Header for the AI Decision Battle page with Progress Indicator and title hierarchy.
 */
export default function BattleHeader() {
  return (
    <div className="w-full mb-8">
      {/* 5-Step Progress Bar: Step 4 Active */}
      <ProgressSteps currentStep={4} />

      {/* Title & Tagline */}
      <div className="text-center max-w-2xl mx-auto">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100/90 text-indigo-700 text-xs font-bold uppercase tracking-wider mb-3">
          <Swords className="w-3.5 h-3.5 text-indigo-600" />
          <span>Decision Arena</span>
        </div>

        <h1 className="text-3xl sm:text-5xl font-extrabold text-slate-900 tracking-tight mb-3">
          Let the experts debate.
        </h1>

        <p className="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
          Each AI agent evaluates your decision from a different perspective. The Decision Engine combines their findings.
        </p>
      </div>
    </div>
  )
}
