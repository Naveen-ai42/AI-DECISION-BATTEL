import React from 'react'
import { Play, FastForward, Swords, Info, AlertTriangle, RotateCcw } from 'lucide-react'
import Button from './Button'

/**
 * Controller bar for initiating, skipping, or viewing simulation and backend request status.
 */
export default function BattleControls({
  battleState, // 'idle' | 'running' | 'completed' | 'error'
  errorMessage,
  isConnectionError,
  onStart,
  onSkip,
  onRetry,
}) {
  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-7 shadow-xs mb-8 text-center">
      {/* 1. Error State */}
      {battleState === 'error' && (
        <div className="max-w-md mx-auto">
          <div className="w-12 h-12 rounded-2xl bg-rose-50 border border-rose-200 text-rose-600 flex items-center justify-center mx-auto mb-3 shadow-2xs">
            <AlertTriangle className="w-6 h-6 stroke-[2]" />
          </div>

          <h3 className="text-xl font-bold text-slate-900 mb-1.5">
            {isConnectionError
              ? 'Unable to connect to Decision Arena backend.'
              : 'Analysis could not be completed.'}
          </h3>

          <p className="text-xs sm:text-sm text-slate-500 mb-6 leading-relaxed">
            {isConnectionError
              ? 'Make sure the FastAPI server is running on http://127.0.0.1:8001.'
              : errorMessage || 'An unexpected error occurred while communicating with the backend.'}
          </p>

          <Button
            onClick={onRetry || onStart}
            variant="primary"
            className="w-full sm:w-auto px-7 py-3 text-sm shadow-sm hover:shadow-md cursor-pointer"
          >
            <RotateCcw className="w-4 h-4 mr-2" />
            <span>Try Again</span>
          </Button>
        </div>
      )}

      {/* 2. Idle State */}
      {battleState === 'idle' && (
        <div className="max-w-md mx-auto">
          <div className="w-12 h-12 rounded-2xl bg-indigo-50 border border-indigo-100 text-indigo-600 flex items-center justify-center mx-auto mb-3 shadow-2xs">
            <Swords className="w-6 h-6 stroke-[2]" />
          </div>

          <h3 className="text-xl font-bold text-slate-900 mb-1.5">
            Ready to analyze your decision?
          </h3>
          <p className="text-xs sm:text-sm text-slate-500 mb-6">
            Dispatch 5 specialized agents to benchmark your options simultaneously.
          </p>

          <Button
            onClick={onStart}
            variant="primary"
            className="w-full sm:w-auto px-8 py-3.5 text-base shadow-sm hover:shadow-md cursor-pointer"
          >
            <Play className="w-4 h-4 mr-2" />
            <span>Start AI Battle</span>
          </Button>

          {/* Demo disclaimer badge */}
          <div className="mt-4 flex items-center justify-center gap-1.5 text-[11px] text-slate-400">
            <Info className="w-3 h-3 text-slate-400" />
            <span>Connected to FastAPI backend &mdash; AI agents ready.</span>
          </div>
        </div>
      )}

      {/* 3. Running State */}
      {battleState === 'running' && (
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="text-left flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-indigo-600 text-white flex items-center justify-center animate-pulse">
              <Swords className="w-5 h-5 animate-spin" />
            </div>
            <div>
              <div className="text-sm font-bold text-slate-900">
                AI agents are analyzing your decision...
              </div>
              <div className="text-xs text-slate-500">
                Evaluating criteria across 5 autonomous perspectives via FastAPI
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3 w-full sm:w-auto">
            <button
              type="button"
              onClick={onSkip}
              className="inline-flex items-center justify-center gap-1.5 px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 transition-colors w-full sm:w-auto cursor-pointer"
            >
              <FastForward className="w-3.5 h-3.5" />
              <span>Skip simulation</span>
            </button>
          </div>
        </div>
      )}

      {/* 4. Completed State */}
      {battleState === 'completed' && (
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="text-left flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center">
              <Swords className="w-5 h-5" />
            </div>
            <div>
              <div className="text-sm font-bold text-slate-900">
                All Perspectives Analyzed
              </div>
              <div className="text-xs text-slate-500">
                Authoritative findings calculated by the Decision Engine below
              </div>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
              ✓ Backend Consensus Ready
            </span>
          </div>
        </div>
      )}
    </div>
  )
}
