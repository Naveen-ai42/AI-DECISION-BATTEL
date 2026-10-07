import {
  Loader2,
  ChevronRight,
  HelpCircle
} from 'lucide-react'
import * as LucideIcons from 'lucide-react'

/**
 * Individual Agent card showing identity, status, score, and conclusion.
 */
export default function AgentCard({ agent, onInspect, canInspect }) {
  const Icon = LucideIcons[agent.iconName] || HelpCircle
  const isDone = agent.status === 'completed'
  const isAnalyzing = agent.status === 'analyzing'
  const isWaiting = agent.status === 'waiting'

  return (
    <div
      onClick={() => {
        if (canInspect && isDone) onInspect(agent)
      }}
      className={`relative bg-white border rounded-2xl p-5 sm:p-6 transition-all duration-200 flex flex-col justify-between ${
        isDone
          ? 'border-slate-200/90 hover:border-indigo-300 hover:shadow-md cursor-pointer group shadow-2xs'
          : isAnalyzing
          ? 'border-indigo-400 bg-indigo-50/20 shadow-sm ring-2 ring-indigo-500/10'
          : 'border-slate-200/60 bg-white/60 opacity-80'
      }`}
    >
      <div>
        {/* Top Header: Icon & Score or Status indicator */}
        <div className="flex items-center justify-between gap-2 mb-3.5">
          <div
            className={`w-10 h-10 rounded-xl flex items-center justify-center transition-colors ${
              isDone
                ? `${agent.accentBg} ${agent.accentText}`
                : isAnalyzing
                ? 'bg-indigo-600 text-white'
                : 'bg-slate-100 text-slate-400'
            }`}
          >
            <Icon className="w-5 h-5" />
          </div>

          {/* Status / Score Badge */}
          {isDone && (
            <div className="flex items-baseline gap-1 bg-slate-50 border border-slate-200 px-2.5 py-1 rounded-lg">
              <span className="text-lg font-bold text-slate-900 font-mono">
                {agent.score}
              </span>
              <span className="text-[10px] text-slate-400 font-medium">/ 100</span>
            </div>
          )}

          {isAnalyzing && (
            <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-indigo-50 text-indigo-700 text-xs font-semibold">
              <Loader2 className="w-3.5 h-3.5 animate-spin" />
              <span>Analyzing...</span>
            </div>
          )}

          {isWaiting && (
            <span className="text-[11px] font-medium text-slate-400 bg-slate-50 px-2 py-0.5 rounded-md">
              Waiting in queue
            </span>
          )}
        </div>

        {/* Agent Name & Specialization */}
        <h4 className="text-base font-bold text-slate-900 mb-1 flex items-center justify-between">
          <span>{agent.name}</span>
        </h4>
        <p className="text-xs text-slate-500 mb-4 leading-relaxed line-clamp-2">
          {agent.specialization}
        </p>

        {/* Evaluating text or Conclusion */}
        {isAnalyzing && (
          <div className="p-3 rounded-xl bg-indigo-50/60 border border-indigo-100/70 text-xs text-indigo-900 leading-snug">
            {agent.evaluatingText}
          </div>
        )}

        {isDone && (
          <div className="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs text-slate-700 leading-snug">
            &ldquo;{agent.conclusion}&rdquo;
          </div>
        )}

        {isWaiting && (
          <div className="p-3 rounded-xl bg-slate-50/50 border border-dashed border-slate-200 text-xs text-slate-400 italic">
            Pending agent activation...
          </div>
        )}
      </div>

      {/* Inspect prompt footer when completed */}
      {isDone && canInspect && (
        <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-indigo-600 font-semibold group-hover:text-indigo-700">
          <span>Inspect breakdown</span>
          <ChevronRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" />
        </div>
      )}
    </div>
  )
}
