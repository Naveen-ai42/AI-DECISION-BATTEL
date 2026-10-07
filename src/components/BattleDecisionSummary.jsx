import React, { useState } from 'react'
import {
  FileText,
  X,
  CheckCircle2,
  Ban,
  Sliders,
  DollarSign,
  Tag,
  ShieldCheck,
  Compass
} from 'lucide-react'
import { getCategoryConfig, getDefaultPrioritiesForCategory } from '../config/categoryConfig'

/**
 * Compact summary card of the user's decision with interactive modal for requirements inspection.
 */
export default function BattleDecisionSummary({ decision }) {
  const [isModalOpen, setIsModalOpen] = useState(false)

  const {
    description = '',
    category = 'electronics',
    subcategory = '',
    budget = '',
    decisionStyle = 'best-overall',
    riskTolerance = 'balanced',
    requirements = [],
    dealBreakers = [],
  } = decision || {}

  const priorities = decision?.priorities || getDefaultPrioritiesForCategory(category, subcategory)

  const formatStyle = (style) => {
    switch (style) {
      case 'best-value': return 'Best Value'
      case 'best-performance': return 'Best Performance'
      case 'best-long-term': return 'Best Long-term'
      default: return 'Best Overall'
    }
  }

  return (
    <>
      <div className="w-full bg-white border border-slate-200/90 rounded-2xl p-5 sm:p-6 shadow-xs mb-8">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-3">
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Your Decision
            </span>
          </div>

          <button
            type="button"
            onClick={() => setIsModalOpen(true)}
            className="inline-flex items-center gap-1.5 text-xs font-semibold text-indigo-600 hover:text-indigo-700 bg-indigo-50/70 hover:bg-indigo-100/70 px-3 py-1.5 rounded-lg border border-indigo-100 transition-colors cursor-pointer self-start sm:self-auto"
          >
            <FileText className="w-3.5 h-3.5" />
            <span>View requirements</span>
          </button>
        </div>

        {/* Decision Text */}
        <p className="text-base sm:text-lg font-semibold text-slate-900 leading-snug mb-4">
          &ldquo;{description}&rdquo;
        </p>

        {/* Badges Row */}
        <div className="flex flex-wrap items-center gap-2 pt-3 border-t border-slate-100 text-xs">
          {/* Category */}
          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-slate-100 text-slate-700 font-medium capitalize">
            <Tag className="w-3 h-3 text-slate-500" />
            <span>{category}</span>
          </span>

          {/* Budget */}
          {budget && (
            <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-slate-100 text-slate-700 font-medium">
              <span>Budget: ₹{budget}</span>
            </span>
          )}

          {/* Decision style */}
          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-slate-100 text-slate-700 font-medium">
            <Compass className="w-3 h-3 text-slate-500" />
            <span>Style: {formatStyle(decisionStyle)}</span>
          </span>

          {/* Risk tolerance */}
          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-slate-100 text-slate-700 font-medium capitalize">
            <ShieldCheck className="w-3 h-3 text-slate-500" />
            <span>Risk: {riskTolerance}</span>
          </span>
        </div>
      </div>

      {/* Requirements Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-fadeIn">
          <div className="bg-white rounded-3xl border border-slate-200 max-w-lg w-full p-6 sm:p-7 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            {/* Modal Header */}
            <div className="flex items-center justify-between pb-4 border-b border-slate-100 mb-5">
              <div>
                <h3 className="text-lg font-bold text-slate-900">
                  Decision Specifications
                </h3>
                <p className="text-xs text-slate-500">
                  Input constraints passed to AI agents
                </p>
              </div>
              <button
                type="button"
                onClick={() => setIsModalOpen(false)}
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors cursor-pointer"
                aria-label="Close modal"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Must-Haves */}
            <div className="mb-5">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-2">
                Must-Have Requirements ({requirements.length})
              </span>
              {requirements.length === 0 ? (
                <p className="text-xs text-slate-400 italic">No specific must-haves set.</p>
              ) : (
                <div className="flex flex-wrap gap-1.5">
                  {requirements.map((req) => (
                    <span
                      key={req}
                      className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-indigo-50 border border-indigo-100 text-indigo-800 text-xs font-medium"
                    >
                      <CheckCircle2 className="w-3 h-3 text-indigo-600 flex-shrink-0" />
                      {req}
                    </span>
                  ))}
                </div>
              )}
            </div>

            {/* Deal-Breakers */}
            <div className="mb-5">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-2">
                Deal-Breakers ({dealBreakers.length})
              </span>
              {dealBreakers.length === 0 ? (
                <p className="text-xs text-slate-400 italic">None specified.</p>
              ) : (
                <div className="flex flex-wrap gap-1.5">
                  {dealBreakers.map((db) => (
                    <span
                      key={db}
                      className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-rose-50 border border-rose-200 text-rose-800 text-xs font-medium"
                    >
                      <Ban className="w-3 h-3 text-rose-600 flex-shrink-0" />
                      {db}
                    </span>
                  ))}
                </div>
              )}
            </div>

            {/* Priorities */}
            <div className="mb-6">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-2.5">
                Priority Calibration
              </span>
              <div className="grid grid-cols-2 gap-2 text-xs">
                {getCategoryConfig(category, subcategory).factors.map((factor) => (
                  <div key={factor.key} className="p-2.5 rounded-lg bg-slate-50 border border-slate-100 flex justify-between">
                    <span className="text-slate-600 truncate">{factor.name}:</span>
                    <span className="font-mono font-bold text-slate-900 ml-1">
                      {priorities[factor.key] ?? 20}%
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Close Button */}
            <button
              type="button"
              onClick={() => setIsModalOpen(false)}
              className="w-full py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-sm font-semibold transition-colors cursor-pointer"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </>
  )
}
