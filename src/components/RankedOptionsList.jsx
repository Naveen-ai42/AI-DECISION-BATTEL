import React, { useState } from 'react'
import {
  Award,
  ChevronDown,
  ChevronUp,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  Sparkles,
  Info,
  Layers,
  Tag,
  TrendingUp,
  Eye,
  EyeOff,
} from 'lucide-react'

/**
 * Ranked Options List Component
 * Renders multiple ranked candidate options with rank badges, score badges,
 * requirements checks, deal-breaker audits, and interactive expandable detail panels.
 * 
 * Supports dynamic candidate counts and configurable Top-N presentation with
 * a "View all ranked options" toggle for inspecting the full candidate pool.
 */
export default function RankedOptionsList({
  rankings = [],
  candidateCount = 0,
  topN = 5,
  dataSource = 'demo',
  category = 'electronics',
  subcategory = '',
}) {
  // By default expand Rank #1, and allow toggling any option
  const [expandedId, setExpandedId] = useState(rankings[0]?.id || '')
  // Toggle to show all ranked options beyond top-N
  const [showAllRanked, setShowAllRanked] = useState(false)

  if (!rankings || rankings.length === 0) {
    return null
  }

  const effectiveTopN = Math.max(1, topN || 5)
  const totalCount = candidateCount || rankings.length
  const displayedRankings = showAllRanked ? rankings : rankings.slice(0, effectiveTopN)
  const hasMoreOptions = rankings.length > effectiveTopN

  const toggleExpand = (id) => {
    setExpandedId((prev) => (prev === id ? '' : id))
  }

  return (
    <div className="w-full mb-12">
      {/* Section Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
        <div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-bold uppercase tracking-wider mb-2">
            <Layers className="w-3.5 h-3.5" />
            <span>Multi-Option Evaluation</span>
          </div>
          <h3 className="text-2xl font-bold text-slate-900 tracking-tight">
            Top Ranked Recommendations
          </h3>
          <div className="flex flex-wrap items-center gap-2 mt-1 text-xs text-slate-500">
            <span>
              Evaluated <strong className="text-slate-800">{totalCount} candidate {totalCount === 1 ? 'option' : 'options'}</strong>
            </span>
            <span>•</span>
            <span>
              Showing {showAllRanked ? `all ${rankings.length}` : `Top ${Math.min(effectiveTopN, rankings.length)}`}
            </span>
            <span>•</span>
            <span className="capitalize">Source: {dataSource}</span>
          </div>
        </div>

        {/* Demo Data Disclaimer Badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-xl bg-amber-50 border border-amber-200/80 text-amber-900 text-xs font-medium self-start sm:self-auto shadow-2xs">
          <Info className="w-4 h-4 text-amber-600 shrink-0" />
          <span>Demo Analysis / Sample Benchmark Data</span>
        </div>
      </div>

      {/* Ranked Cards List */}
      <div className="space-y-4">
        {displayedRankings.map((opt) => {
          const isRank1 = opt.rank === 1
          const isRank2 = opt.rank === 2
          const isRank3 = opt.rank === 3
          const isExpanded = expandedId === opt.id

          // Rank badge styling
          let rankBadgeBg = 'bg-slate-100 text-slate-700 border-slate-200'
          let medalEmoji = `#${opt.rank}`
          if (isRank1) {
            rankBadgeBg = 'bg-amber-100 text-amber-900 border-amber-300 font-bold'
            medalEmoji = '🥇 #1'
          } else if (isRank2) {
            rankBadgeBg = 'bg-slate-200 text-slate-800 border-slate-300 font-bold'
            medalEmoji = '🥈 #2'
          } else if (isRank3) {
            rankBadgeBg = 'bg-amber-50 text-amber-800 border-amber-200 font-bold'
            medalEmoji = '🥉 #3'
          }

          const passedCount = opt.requirementsPassed?.length || 0
          const missedCount = opt.requirementsMissed?.length || 0
          const dbTriggeredCount = opt.dealBreakersTriggered?.length || 0

          return (
            <div
              key={opt.id}
              className={`w-full rounded-2xl border transition-all duration-200 overflow-hidden ${
                isRank1
                  ? 'bg-gradient-to-r from-indigo-50/40 via-white to-emerald-50/30 border-indigo-200 shadow-sm'
                  : 'bg-white border-slate-200/90 hover:border-slate-300 shadow-2xs'
              }`}
            >
              {/* Card Summary Header (Clickable) */}
              <div
                onClick={() => toggleExpand(opt.id)}
                className="p-4 sm:p-5 flex flex-col md:flex-row md:items-center justify-between gap-4 cursor-pointer select-none"
              >
                {/* Left: Rank + Name + Price + Description */}
                <div className="flex items-start sm:items-center gap-3.5 flex-1 min-w-0">
                  {/* Rank Badge */}
                  <div
                    className={`shrink-0 w-12 h-12 rounded-xl flex items-center justify-center border text-sm ${rankBadgeBg}`}
                  >
                    <span>{medalEmoji}</span>
                  </div>

                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-2 mb-1">
                      <h4 className="text-lg font-bold text-slate-900 truncate">
                        {opt.name}
                      </h4>
                      {isRank1 && (
                        <span className="px-2 py-0.5 rounded-full bg-emerald-600 text-white text-[11px] font-bold uppercase tracking-wider">
                          Best Overall
                        </span>
                      )}
                      {opt.price && (
                        <span className="px-2 py-0.5 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">
                          {opt.price}
                        </span>
                      )}
                    </div>

                    {opt.description && (
                      <p className="text-xs sm:text-sm text-slate-500 line-clamp-1">
                        {opt.description}
                      </p>
                    )}
                  </div>
                </div>

                {/* Right: Requirements Audit Tags + Score Pill + Accordion Toggle */}
                <div className="flex items-center justify-between md:justify-end gap-3 shrink-0 pt-2 md:pt-0 border-t md:border-t-0 border-slate-100">
                  {/* Requirement Audit Status Badges */}
                  <div className="hidden sm:flex items-center gap-2 text-xs">
                    <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 font-medium border border-emerald-100">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                      <span>{passedCount} passed</span>
                    </span>

                    {missedCount > 0 && (
                      <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-rose-50 text-rose-700 font-medium border border-rose-100">
                        <XCircle className="w-3.5 h-3.5 text-rose-600" />
                        <span>{missedCount} missed</span>
                      </span>
                    )}

                    {dbTriggeredCount > 0 && (
                      <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-amber-50 text-amber-800 font-medium border border-amber-200">
                        <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                        <span>{dbTriggeredCount} deal-breaker</span>
                      </span>
                    )}
                  </div>

                  {/* Score Pill */}
                  <div className="flex items-center gap-2">
                    <div
                      className={`px-3 py-1.5 rounded-xl flex items-center gap-1.5 border font-bold text-sm ${
                        opt.score >= 90
                          ? 'bg-emerald-50 text-emerald-700 border-emerald-200'
                          : opt.score >= 85
                          ? 'bg-indigo-50 text-indigo-700 border-indigo-200'
                          : 'bg-slate-100 text-slate-700 border-slate-200'
                      }`}
                    >
                      <Sparkles className="w-3.5 h-3.5" />
                      <span>{opt.score.toFixed(1)}</span>
                    </div>

                    <button
                      type="button"
                      className="p-1.5 rounded-lg text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
                      aria-label={isExpanded ? 'Collapse' : 'Expand'}
                    >
                      {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                    </button>
                  </div>
                </div>
              </div>

              {/* Expandable Option Detail View */}
              {isExpanded && (
                <div className="px-5 pb-5 pt-2 border-t border-slate-100/90 bg-slate-50/50">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
                    {/* Left: Factor Score Breakdown */}
                    <div>
                      <h5 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-1.5">
                        <TrendingUp className="w-3.5 h-3.5 text-indigo-600" />
                        <span>Agent Factor Evaluations</span>
                      </h5>

                      <div className="space-y-2">
                        {opt.factorScores &&
                          Object.entries(opt.factorScores).map(([factorKey, score]) => (
                            <div key={factorKey} className="flex items-center justify-between gap-3 text-xs">
                              <span className="font-medium text-slate-700 capitalize">
                                {factorKey.replace(/([A-Z])/g, ' $1')}
                              </span>
                              <div className="flex items-center gap-2 min-w-[130px]">
                                <div className="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
                                  <div
                                    className={`h-full rounded-full ${
                                      score >= 90
                                        ? 'bg-emerald-500'
                                        : score >= 85
                                        ? 'bg-indigo-500'
                                        : 'bg-slate-400'
                                    }`}
                                    style={{ width: `${Math.min(100, Math.max(0, score))}%` }}
                                  />
                                </div>
                                <span className="font-semibold text-slate-900 w-8 text-right">
                                  {Math.round(score)}
                                </span>
                              </div>
                            </div>
                          ))}
                      </div>

                      {/* Raw unpenalized vs Final penalized */}
                      {opt.rawScore && opt.rawScore !== opt.score && (
                        <div className="mt-4 pt-3 border-t border-slate-200 text-xs text-slate-500 flex justify-between">
                          <span>Raw weighted score:</span>
                          <span className="font-medium text-slate-700">{opt.rawScore.toFixed(1)}</span>
                        </div>
                      )}
                    </div>

                    {/* Right: Strengths & Concerns */}
                    <div className="space-y-4">
                      {/* Strengths */}
                      {opt.strengths && opt.strengths.length > 0 && (
                        <div>
                          <h5 className="text-xs font-bold uppercase tracking-wider text-emerald-700 mb-2 flex items-center gap-1.5">
                            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                            <span>Key Strengths</span>
                          </h5>
                          <ul className="space-y-1.5 text-xs text-slate-600">
                            {opt.strengths.map((str, idx) => (
                              <li key={idx} className="flex items-start gap-1.5">
                                <span className="text-emerald-500 font-bold shrink-0">•</span>
                                <span>{str}</span>
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {/* Concerns */}
                      {opt.concerns && opt.concerns.length > 0 && (
                        <div>
                          <h5 className="text-xs font-bold uppercase tracking-wider text-amber-700 mb-2 flex items-center gap-1.5">
                            <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                            <span>Trade-offs & Considerations</span>
                          </h5>
                          <ul className="space-y-1.5 text-xs text-slate-600">
                            {opt.concerns.map((con, idx) => (
                              <li key={idx} className="flex items-start gap-1.5">
                                <span className="text-amber-500 font-bold shrink-0">•</span>
                                <span>{con}</span>
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {/* Deal Breakers if any */}
                      {opt.dealBreakersTriggered && opt.dealBreakersTriggered.length > 0 && (
                        <div className="p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-xs text-rose-800">
                          <span className="font-bold block mb-1">Triggered Negative Constraint:</span>
                          <ul className="list-disc list-inside space-y-0.5">
                            {opt.dealBreakersTriggered.map((db, idx) => (
                              <li key={idx}>{db}</li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </div>

      {/* "View all ranked options" Toggle Button */}
      {hasMoreOptions && (
        <div className="mt-5 text-center">
          <button
            type="button"
            onClick={() => setShowAllRanked((prev) => !prev)}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white border border-slate-200 hover:border-indigo-300 hover:bg-indigo-50/40 text-slate-700 hover:text-indigo-700 text-sm font-semibold transition-all shadow-2xs"
          >
            {showAllRanked ? (
              <>
                <EyeOff className="w-4 h-4 text-indigo-600" />
                <span>Show Top {effectiveTopN} Only</span>
              </>
            ) : (
              <>
                <Eye className="w-4 h-4 text-indigo-600" />
                <span>
                  View all {rankings.length} ranked options ({rankings.length - effectiveTopN} more)
                </span>
              </>
            )}
          </button>
        </div>
      )}
    </div>
  )
}
