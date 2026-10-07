import React from 'react'
import { GitCompare, AlertCircle, HelpCircle } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'
import * as LucideIcons from 'lucide-react'

/**
 * Section highlighting consensus friction and where AI agent perspectives diverged.
 * Dynamically contrasts divergent agents for any category.
 */
export default function DisagreementSection({ category = 'electronics', subcategory = '', agents = [] }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const activeAgents = agents.length > 0 ? agents : categoryConfig.agents

  // Sort agents by score to find divergent perspectives
  const sorted = [...activeAgents].sort((a, b) => b.score - a.score)
  const topAgent = sorted[0] || categoryConfig.agents[0]
  const bottomAgent = sorted[sorted.length - 1] || categoryConfig.agents[1]
  const midAgent = sorted[Math.floor(sorted.length / 2)] || categoryConfig.agents[2]

  const featured = [topAgent, bottomAgent, midAgent].filter(Boolean)

  const getAgentIcon = (iconName) => {
    return LucideIcons[iconName] || HelpCircle
  }

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-9 shadow-xs mb-10">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
        <div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-bold uppercase tracking-wider mb-2">
            <GitCompare className="w-3.5 h-3.5 text-indigo-600" />
            <span>Friction Analysis</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
            Where the agents disagree ({categoryConfig.label})
          </h3>
          <p className="text-xs sm:text-sm text-slate-500 mt-1">
            Different AI perspectives produce conflicting evaluations. The Decision Engine arbitrates based on your calibrated weights.
          </p>
        </div>
      </div>

      {/* Disagreement Contrast Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        {featured.map((agent, idx) => {
          const Icon = getAgentIcon(agent.iconName)
          const isHighest = idx === 0
          const isLowest = idx === 1

          const badgeText = isHighest
            ? 'Highest Advocate'
            : isLowest
            ? 'Most Critical'
            : 'Balanced Review'

          const badgeClass = isHighest
            ? 'bg-emerald-50 text-emerald-800 border-emerald-200'
            : isLowest
            ? 'bg-amber-50 text-amber-800 border-amber-200'
            : 'bg-indigo-50 text-indigo-700 border-indigo-200'

          return (
            <div
              key={agent.id || agent.name}
              className="bg-slate-50/70 border border-slate-200 rounded-2xl p-5 flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-slate-700">
                      <Icon className="w-4 h-4" />
                    </div>
                    <span className="text-sm font-bold text-slate-900 truncate">
                      {agent.name}
                    </span>
                  </div>
                  <span className="font-mono text-sm font-bold text-slate-800">
                    {agent.score}
                  </span>
                </div>

                <div className="mb-3">
                  <span
                    className={`inline-block px-2.5 py-0.5 rounded-full text-xs font-semibold border ${badgeClass}`}
                  >
                    {badgeText}
                  </span>
                </div>

                <p className="text-xs text-slate-600 leading-relaxed font-normal">
                  {agent.conclusion || agent.specialization}
                </p>
              </div>
            </div>
          )
        })}
      </div>

      {/* Arbitration Notice */}
      <div className="p-4 rounded-xl bg-slate-50 border border-slate-200/80 flex items-start gap-3">
        <AlertCircle className="w-4 h-4 text-slate-400 mt-0.5 flex-shrink-0" />
        <p className="text-xs text-slate-600 leading-relaxed">
          <strong className="text-slate-800">How tension is resolved:</strong> If you prioritized {topAgent?.name}&apos;s factor (assigning it higher weight), its score has greater influence in the composite verdict, balancing {bottomAgent?.name}&apos;s trade-off cautions.
        </p>
      </div>
    </div>
  )
}
