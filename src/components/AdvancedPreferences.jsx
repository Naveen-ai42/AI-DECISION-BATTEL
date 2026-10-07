import React, { useState } from 'react'
import { ChevronDown, ChevronUp, Sliders, ShieldCheck, Compass } from 'lucide-react'

const RISK_OPTIONS = [
  { id: 'low', label: 'Low', desc: 'Conservative, proven options' },
  { id: 'balanced', label: 'Balanced', desc: 'Equal upside and stability' },
  { id: 'high', label: 'High', desc: 'Maximum performance or specs' },
]

const STYLE_OPTIONS = [
  { id: 'best-overall', label: 'Best overall', desc: 'Highest comprehensive score' },
  { id: 'best-value', label: 'Best value', desc: 'Maximum bang for your rupee' },
  { id: 'best-performance', label: 'Best performance', desc: 'Top tier raw capabilities' },
  { id: 'best-long-term', label: 'Best long-term choice', desc: 'Durability & multi-year value' },
]

/**
 * Collapsible section for Risk Tolerance and Decision Style.
 */
export default function AdvancedPreferences({
  riskTolerance = 'balanced',
  decisionStyle = 'best-overall',
  onChange,
}) {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="border border-slate-200/90 rounded-2xl bg-white overflow-hidden transition-all duration-200">
      {/* Header toggle */}
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-5 py-4 flex items-center justify-between text-left hover:bg-slate-50/70 transition-colors cursor-pointer group"
        aria-expanded={isOpen}
      >
        <div className="flex items-center gap-2">
          <Sliders className="w-4 h-4 text-slate-500 group-hover:text-indigo-600 transition-colors" />
          <span className="text-sm font-semibold text-slate-800 group-hover:text-indigo-600 transition-colors">
            Advanced preferences
          </span>
          <span className="text-xs text-slate-400 font-normal">
            (Risk tolerance, Decision style)
          </span>
        </div>
        <div className="text-slate-400 group-hover:text-indigo-600 transition-colors">
          {isOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
        </div>
      </button>

      {/* Content */}
      {isOpen && (
        <div className="px-5 pb-6 pt-2 border-t border-slate-100 space-y-6 bg-slate-50/40">
          {/* Risk Tolerance */}
          <div>
            <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-700 uppercase tracking-wider mb-2.5">
              <ShieldCheck className="w-3.5 h-3.5 text-indigo-600" />
              <span>Risk Tolerance</span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
              {RISK_OPTIONS.map((opt) => {
                const isSelected = riskTolerance === opt.id
                return (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => onChange('riskTolerance', opt.id)}
                    className={`p-3 rounded-xl border text-left transition-all cursor-pointer ${
                      isSelected
                        ? 'border-indigo-600 bg-indigo-50/70 text-indigo-900 ring-2 ring-indigo-500/20 shadow-xs'
                        : 'border-slate-200 bg-white text-slate-700 hover:border-slate-300'
                    }`}
                  >
                    <div className="text-sm font-bold">{opt.label}</div>
                    <div className="text-xs text-slate-500 mt-0.5">{opt.desc}</div>
                  </button>
                )
              })}
            </div>
          </div>

          {/* Decision Style */}
          <div>
            <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-700 uppercase tracking-wider mb-2.5">
              <Compass className="w-3.5 h-3.5 text-indigo-600" />
              <span>Decision Style</span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {STYLE_OPTIONS.map((style) => {
                const isSelected = decisionStyle === style.id
                return (
                  <button
                    key={style.id}
                    type="button"
                    onClick={() => onChange('decisionStyle', style.id)}
                    className={`p-3 rounded-xl border text-left transition-all cursor-pointer ${
                      isSelected
                        ? 'border-indigo-600 bg-indigo-50/70 text-indigo-900 ring-2 ring-indigo-500/20 shadow-xs'
                        : 'border-slate-200 bg-white text-slate-700 hover:border-slate-300'
                    }`}
                  >
                    <div className="text-sm font-bold">{style.label}</div>
                    <div className="text-xs text-slate-500 mt-0.5">{style.desc}</div>
                  </button>
                )
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
