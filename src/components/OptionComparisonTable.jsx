import React from 'react'
import { Table, Sparkles, Award } from 'lucide-react'

/**
 * OptionComparisonTable Component
 * Generates dynamic side-by-side factor comparison matrix for all candidate options.
 */
export default function OptionComparisonTable({ comparison, rankings = [] }) {
  if (!comparison || !comparison.factors || !comparison.options || comparison.options.length === 0) {
    return null
  }

  const { factors, options } = comparison

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 shadow-xs mb-10 overflow-hidden">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
        <div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-bold uppercase tracking-wider mb-2">
            <Table className="w-3.5 h-3.5" />
            <span>Comparative Matrix</span>
          </div>
          <h3 className="text-2xl font-bold text-slate-900 tracking-tight">
            Side-by-Side Factor Comparison
          </h3>
          <p className="text-sm text-slate-500 mt-0.5">
            Compare agent evaluation scores across all evaluated options.
          </p>
        </div>
      </div>

      {/* Responsive Table Container */}
      <div className="overflow-x-auto -mx-6 sm:-mx-8 px-6 sm:px-8">
        <table className="w-full text-left border-collapse min-w-[620px]">
          <thead>
            <tr className="border-b border-slate-200 bg-slate-50/80">
              <th className="py-3.5 px-4 text-xs font-bold uppercase tracking-wider text-slate-500 rounded-l-xl">
                Evaluation Factor
              </th>
              {options.map((opt, idx) => {
                const isWinner = opt.rank === 1
                return (
                  <th
                    key={opt.id || idx}
                    className={`py-3.5 px-4 text-xs font-bold text-slate-900 ${
                      isWinner
                        ? 'bg-indigo-50/70 border-x border-indigo-200 text-indigo-950 font-extrabold'
                        : ''
                    } ${idx === options.length - 1 ? 'rounded-r-xl' : ''}`}
                  >
                    <div className="flex flex-col">
                      <div className="flex items-center gap-1">
                        {isWinner && <Award className="w-3.5 h-3.5 text-amber-500 shrink-0" />}
                        <span className="truncate max-w-[150px]">{opt.name}</span>
                      </div>
                      <span className="text-[11px] font-normal text-slate-500">
                        {opt.badge || `Rank #${opt.rank}`}
                      </span>
                    </div>
                  </th>
                )
              })}
            </tr>
          </thead>

          <tbody className="divide-y divide-slate-100 text-sm">
            {/* Factor Score Rows */}
            {factors.map((factor) => (
              <tr key={factor.key} className="hover:bg-slate-50/50 transition-colors">
                <td className="py-3 px-4 font-medium text-slate-700 whitespace-nowrap">
                  {factor.name}
                </td>
                {options.map((opt) => {
                  const isWinner = opt.rank === 1
                  const score = opt[factor.key] ?? opt.factorScores?.[factor.key] ?? 85

                  let scoreColor = 'text-slate-700'
                  if (score >= 90) scoreColor = 'text-emerald-700 font-bold'
                  else if (score >= 85) scoreColor = 'text-indigo-700 font-semibold'
                  else if (score < 80) scoreColor = 'text-slate-500'

                  return (
                    <td
                      key={opt.id}
                      className={`py-3 px-4 ${
                        isWinner ? 'bg-indigo-50/30 border-x border-indigo-100' : ''
                      }`}
                    >
                      <span className={`inline-block ${scoreColor}`}>
                        {Math.round(score)}
                      </span>
                    </td>
                  )
                })}
              </tr>
            ))}

            {/* Overall Weighted Score Summary Row */}
            <tr className="border-t-2 border-slate-200 bg-slate-50 font-bold">
              <td className="py-4 px-4 text-sm font-extrabold text-slate-900">
                Overall Synthesized Score
              </td>
              {options.map((opt) => {
                const isWinner = opt.rank === 1
                return (
                  <td
                    key={opt.id}
                    className={`py-4 px-4 ${
                      isWinner
                        ? 'bg-indigo-100/60 border-x border-indigo-200 text-indigo-900 font-extrabold'
                        : 'text-slate-900'
                    }`}
                  >
                    <div className="flex items-center gap-1.5">
                      {isWinner && <Sparkles className="w-3.5 h-3.5 text-indigo-600" />}
                      <span className="text-base font-extrabold">
                        {typeof opt.score === 'number' ? opt.score.toFixed(1) : opt.score}
                      </span>
                    </div>
                  </td>
                )
              })}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  )
}
