import React, { useState } from 'react'
import { ChevronDown, ChevronUp, FileText, CheckCircle2, AlertTriangle } from 'lucide-react'

/**
 * Expandable detailed analysis panel exposing factors, evidence, scores, and conclusions without chain-of-thought.
 */
export default function DetailedAnalysis({ agents = [] }) {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl overflow-hidden shadow-xs mb-10 transition-all">
      {/* Header Toggle */}
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full p-6 sm:p-7 flex items-center justify-between text-left hover:bg-slate-50/70 transition-colors cursor-pointer group"
        aria-expanded={isOpen}
      >
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-50 border border-indigo-100 text-indigo-600 flex items-center justify-center">
            <FileText className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-lg sm:text-xl font-bold text-slate-900 group-hover:text-indigo-600 transition-colors">
              {isOpen ? 'Detailed Agent Evidence & Findings' : 'Show detailed analysis'}
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Inspect factors considered, scores, strengths, and concerns per specialist.
            </p>
          </div>
        </div>

        <div className="p-2 rounded-xl bg-slate-100 group-hover:bg-indigo-50 text-slate-500 group-hover:text-indigo-600 transition-colors">
          {isOpen ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
        </div>
      </button>

      {/* Expanded Accordion Body */}
      {isOpen && (
        <div className="p-6 sm:p-8 border-t border-slate-100 bg-slate-50/40 space-y-5">
          {agents.map((agent) => (
            <div
              key={agent.id}
              className="bg-white border border-slate-200 rounded-2xl p-5 shadow-2xs"
            >
              <div className="flex items-center justify-between mb-2.5 pb-2.5 border-b border-slate-100">
                <div>
                  <h4 className="text-sm font-bold text-slate-900">
                    {agent.name}
                  </h4>
                  <span className="text-[11px] text-slate-400">
                    Scope: {agent.evaluated}
                  </span>
                </div>
                <div className="font-mono text-sm font-bold text-slate-900 bg-slate-50 border border-slate-200 px-2.5 py-1 rounded-lg">
                  {agent.score} / 100
                </div>
              </div>

              {/* Factors Considered & Evidence */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 my-3 text-xs">
                <div>
                  <span className="font-semibold text-emerald-800 uppercase tracking-wider block mb-1.5 flex items-center gap-1">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                    <span>Validated Factors</span>
                  </span>
                  <ul className="space-y-1 text-slate-600">
                    {agent.strengths?.map((s, i) => (
                      <li key={i} className="flex items-start gap-1.5">
                        <span className="text-emerald-500 font-bold">&bull;</span>
                        <span>{s}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div>
                  <span className="font-semibold text-amber-800 uppercase tracking-wider block mb-1.5 flex items-center gap-1">
                    <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                    <span>Concerns &amp; Trade-offs</span>
                  </span>
                  <ul className="space-y-1 text-slate-600">
                    {agent.concerns?.map((c, i) => (
                      <li key={i} className="flex items-start gap-1.5">
                        <span className="text-amber-500 font-bold">&bull;</span>
                        <span>{c}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              {/* Conclusion */}
              <div className="mt-3 pt-2.5 border-t border-slate-100 text-xs text-slate-700 italic">
                Conclusion: &ldquo;{agent.conclusion}&rdquo;
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
