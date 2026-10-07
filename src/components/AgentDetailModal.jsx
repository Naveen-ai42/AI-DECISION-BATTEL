import {
  X,
  CheckCircle2,
  AlertTriangle,
  HelpCircle
} from 'lucide-react'
import * as LucideIcons from 'lucide-react'

/**
 * Clean detail modal inspecting an individual agent's evaluated evidence, strengths, and concerns.
 */
export default function AgentDetailModal({ agent, onClose }) {
  if (!agent) return null

  const Icon = LucideIcons[agent.iconName] || HelpCircle

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-fadeIn">
      <div className="bg-white rounded-3xl border border-slate-200 max-w-lg w-full p-6 sm:p-8 shadow-2xl relative max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between pb-4 border-b border-slate-100 mb-5">
          <div className="flex items-center gap-3">
            <div className={`w-11 h-11 rounded-xl ${agent.accentBg} ${agent.accentText} flex items-center justify-center`}>
              <Icon className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-slate-900">
                {agent.name}
              </h3>
              <p className="text-xs text-slate-500">
                {agent.specialization}
              </p>
            </div>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors cursor-pointer"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Score & Verdict Banner */}
        <div className="flex items-center justify-between p-4 rounded-2xl bg-slate-50 border border-slate-200 mb-5">
          <div>
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-0.5">
              Agent Score
            </span>
            <div className="text-xs font-semibold text-slate-700">
              Evaluated Match Index
            </div>
          </div>
          <div className="flex items-baseline gap-1">
            <span className="text-3xl font-extrabold text-slate-900 font-mono">
              {agent.score}
            </span>
            <span className="text-sm font-semibold text-slate-400">/ 100</span>
          </div>
        </div>

        {/* What it evaluated */}
        <div className="mb-5">
          <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-1.5">
            Evaluation Scope
          </span>
          <p className="text-xs sm:text-sm text-slate-700 bg-white border border-slate-200 p-3 rounded-xl leading-relaxed">
            {agent.evaluated}
          </p>
        </div>

        {/* Top positive factors */}
        <div className="mb-5">
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 block mb-2 flex items-center gap-1">
            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
            <span>Top Positive Factors ({agent.strengths?.length || 0})</span>
          </span>
          <ul className="space-y-2">
            {agent.strengths?.map((str, idx) => (
              <li
                key={idx}
                className="text-xs sm:text-sm text-slate-700 bg-emerald-50/50 border border-emerald-100 p-2.5 rounded-xl flex items-start gap-2"
              >
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-2 flex-shrink-0" />
                <span>{str}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Potential concerns */}
        <div className="mb-5">
          <span className="text-xs font-bold uppercase tracking-wider text-amber-700 block mb-2 flex items-center gap-1">
            <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
            <span>Potential Concerns</span>
          </span>
          <ul className="space-y-2">
            {agent.concerns?.map((con, idx) => (
              <li
                key={idx}
                className="text-xs sm:text-sm text-slate-700 bg-amber-50/50 border border-amber-100 p-2.5 rounded-xl flex items-start gap-2"
              >
                <span className="w-1.5 h-1.5 rounded-full bg-amber-500 mt-2 flex-shrink-0" />
                <span>{con}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Conclusion */}
        <div className="mb-6 pt-3 border-t border-slate-100">
          <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-1">
            Agent Conclusion
          </span>
          <p className="text-sm font-medium text-slate-900 italic">
            &ldquo;{agent.conclusion}&rdquo;
          </p>
        </div>

        {/* Close Button */}
        <button
          type="button"
          onClick={onClose}
          className="w-full py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-sm font-semibold transition-colors cursor-pointer shadow-xs"
        >
          Close Breakdown
        </button>
      </div>
    </div>
  )
}
