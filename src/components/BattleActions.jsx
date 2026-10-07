import React from 'react'
import { ArrowLeft, ArrowRight, RotateCcw } from 'lucide-react'
import Button from './Button'

/**
 * Bottom action controls for the AI Decision Battle page.
 */
export default function BattleActions({ isCompleted, onProceed, onRestart }) {
  if (!isCompleted) return null

  return (
    <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-6 border-t border-slate-200/70">
      <div className="flex items-center gap-3 w-full sm:w-auto order-2 sm:order-1">
        <Button
          to="/requirements"
          variant="secondary"
          className="w-full sm:w-auto gap-2 text-sm"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Edit Requirements</span>
        </Button>

        <button
          type="button"
          onClick={onRestart}
          className="inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-600 text-xs font-semibold transition-colors cursor-pointer"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>Re-run Battle</span>
        </button>
      </div>

      <Button
        onClick={onProceed}
        variant="primary"
        className="w-full sm:w-auto px-8 py-3.5 text-base shadow-sm hover:shadow-md order-1 sm:order-2"
      >
        <span>See Final Decision</span>
        <ArrowRight className="w-4 h-4 ml-2" />
      </Button>
    </div>
  )
}
