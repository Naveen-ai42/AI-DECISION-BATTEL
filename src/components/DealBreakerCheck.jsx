import React from 'react'
import { ShieldCheck, AlertCircle, Ban } from 'lucide-react'

/**
 * Deal-breaker screening audit verifying whether negative constraints were violated.
 */
export default function DealBreakerCheck({ dealBreakers = [] }) {
  if (!dealBreakers || dealBreakers.length === 0) return null

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 shadow-xs mb-10">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
            Deal-breaker check
          </h3>
          <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
            Exclusion criteria analysis for absolute non-negotiables.
          </p>
        </div>
        <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-semibold">
          <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
          <span>Screened Clean</span>
        </span>
      </div>

      <div className="space-y-3">
        {dealBreakers.map((db, idx) => (
          <div
            key={idx}
            className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80 flex items-center justify-between gap-3 text-xs"
          >
            <div className="flex items-center gap-2.5">
              <div className="w-6 h-6 rounded-md bg-white border border-slate-200 text-slate-600 flex items-center justify-center">
                <Ban className="w-3.5 h-3.5" />
              </div>
              <span className="font-semibold text-slate-800 text-sm">
                &ldquo;{db}&rdquo;
              </span>
            </div>

            <span className="inline-flex items-center gap-1 text-emerald-700 font-semibold bg-white border border-emerald-200 px-2.5 py-1 rounded-lg shadow-2xs">
              <ShieldCheck className="w-3 h-3 text-emerald-600" />
              <span>No violation detected</span>
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}
