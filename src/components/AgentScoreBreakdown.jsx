import React from 'react'
import { HelpCircle } from 'lucide-react'
import * as LucideIcons from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

const PALETTE = [
  { bar: 'bg-indigo-600', icon: 'text-indigo-600 bg-indigo-50 border-indigo-100' },
  { bar: 'bg-emerald-500', icon: 'text-emerald-600 bg-emerald-50 border-emerald-100' },
  { bar: 'bg-blue-500', icon: 'text-blue-600 bg-blue-50 border-blue-100' },
  { bar: 'bg-violet-500', icon: 'text-violet-600 bg-violet-50 border-violet-100' },
  { bar: 'bg-amber-500', icon: 'text-amber-600 bg-amber-50 border-amber-100' },
]

/**
 * Breakdown of each autonomous agent's score with clean progress bars and one-line conclusions.
 * Category-aware agent representation.
 */
export default function AgentScoreBreakdown({ category = 'electronics', subcategory = '', agents = [] }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const activeAgents = agents.length > 0 ? agents : categoryConfig.agents

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 shadow-xs mb-10">
      <div className="mb-6">
        <h3 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
          How the {categoryConfig.label} AI agents scored it
        </h3>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          Independent evaluations across the specialized analysis criteria.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {activeAgents.map((agent, idx) => {
          const Icon = LucideIcons[agent.iconName] || HelpCircle
          const color = PALETTE[idx % PALETTE.length]

          return (
            <div
              key={agent.id || agent.name}
              className="p-5 rounded-2xl bg-slate-50/70 border border-slate-200/80 hover:bg-white hover:border-slate-300 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-2.5">
                    <div className={`w-8 h-8 rounded-xl border flex items-center justify-center ${color.icon}`}>
                      <Icon className="w-4 h-4" />
                    </div>
                    <div>
                      <h4 className="text-sm font-bold text-slate-900 truncate">
                        {agent.name}
                      </h4>
                      <span className="text-[11px] text-slate-400 block line-clamp-1">
                        {agent.specialization}
                      </span>
                    </div>
                  </div>

                  <div className="font-mono text-base font-bold text-slate-900 bg-white border border-slate-200 px-2.5 py-0.5 rounded-lg shadow-2xs">
                    {agent.score} <span className="text-xs text-slate-400 font-normal">/ 100</span>
                  </div>
                </div>

                {/* Progress Bar */}
                <div className="w-full bg-slate-200/80 rounded-full h-2 mb-3 overflow-hidden">
                  <div
                    className={`h-full rounded-full ${color.bar} transition-all duration-700 ease-out`}
                    style={{ width: `${agent.score}%` }}
                  />
                </div>
              </div>

              {/* Conclusion snippet */}
              <p className="text-xs text-slate-600 italic bg-white p-2.5 rounded-xl border border-slate-100">
                &ldquo;{agent.conclusion}&rdquo;
              </p>
            </div>
          )
        })}
      </div>
    </div>
  )
}
