import React from 'react'
import { Check, Loader2, Circle } from 'lucide-react'

/**
 * Live Battle status banner tracking real-time status of all 5 agents.
 */
export default function BattleProgress({ agents, isCompleted }) {
  return (
    <div className="w-full bg-slate-50/90 border border-slate-200/90 rounded-2xl p-4 sm:p-5 mb-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3.5">
        <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
          Live Deliberation Matrix
        </span>
        <span className="text-xs font-medium text-slate-600">
          {isCompleted
            ? 'All perspectives analyzed.'
            : '5 AI perspectives are analyzing your decision'}
        </span>
      </div>

      {/* Agents status pills row */}
      <div className="grid grid-cols-2 sm:grid-cols-5 gap-2">
        {agents.map((agent) => {
          const isDone = agent.status === 'completed'
          const isAnalyzing = agent.status === 'analyzing'
          const isWaiting = agent.status === 'waiting'

          return (
            <div
              key={agent.id}
              className={`flex items-center gap-2 px-3 py-2 rounded-xl border text-xs transition-all duration-200 ${
                isDone
                  ? 'bg-white border-emerald-200 text-emerald-800 shadow-2xs'
                  : isAnalyzing
                  ? 'bg-indigo-50 border-indigo-300 text-indigo-700 font-semibold ring-2 ring-indigo-500/10'
                  : 'bg-white/60 border-slate-200 text-slate-400'
              }`}
            >
              {isDone && (
                <div className="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center flex-shrink-0">
                  <Check className="w-2.5 h-2.5 stroke-[3]" />
                </div>
              )}
              {isAnalyzing && (
                <Loader2 className="w-4 h-4 text-indigo-600 animate-spin flex-shrink-0" />
              )}
              {isWaiting && (
                <Circle className="w-3.5 h-3.5 text-slate-300 flex-shrink-0" />
              )}

              <div className="truncate">
                <span className="font-semibold block truncate">
                  {agent.name.replace(' Agent', '')}
                </span>
                {isAnalyzing && (
                  <span className="text-[10px] text-indigo-500 block">
                    analyzing...
                  </span>
                )}
                {isDone && (
                  <span className="text-[10px] text-emerald-600 font-mono block">
                    {agent.score} / 100
                  </span>
                )}
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
