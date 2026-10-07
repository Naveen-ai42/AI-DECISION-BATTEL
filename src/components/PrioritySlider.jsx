import React from 'react'
import { RotateCcw } from 'lucide-react'
import PriorityDistribution from './PriorityDistribution'
import SmartInsight from './SmartInsight'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Priority setting section with category-aware factors and proportional 100% normalization sliders.
 */
export default function PrioritySlider({ category = 'electronics', subcategory = '', priorities, onChange, onReset }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const factors = categoryConfig.factors

  const handleSliderChange = (changedKey, rawNewVal) => {
    const newVal = Math.min(100, Math.max(0, parseInt(rawNewVal, 10) || 0))
    const keys = factors.map((f) => f.key)
    const otherKeys = keys.filter((k) => k !== changedKey)

    if (newVal === 100) {
      const updated = { ...priorities, [changedKey]: 100 }
      otherKeys.forEach((k) => {
        updated[k] = 0
      })
      onChange(updated)
      return
    }

    const remainingBudget = 100 - newVal
    const currentOtherSum = otherKeys.reduce(
      (sum, k) => sum + (priorities[k] ?? 20),
      0
    )

    const nextPriorities = { ...priorities, [changedKey]: newVal }

    if (currentOtherSum > 0) {
      // Proportional redistribution among remaining factors
      otherKeys.forEach((k) => {
        const ratio = (priorities[k] ?? 20) / currentOtherSum
        nextPriorities[k] = Math.round(ratio * remainingBudget)
      })

      // Fix rounding errors so total strictly sums to 100
      let currentTotal =
        newVal + otherKeys.reduce((sum, k) => sum + nextPriorities[k], 0)
      let diff = 100 - currentTotal

      if (diff !== 0) {
        // Adjust the other key with the highest value to absorb the rounding diff
        const candidateKey = otherKeys.reduce((best, k) =>
          nextPriorities[k] > nextPriorities[best] ? k : best
        , otherKeys[0])

        nextPriorities[candidateKey] = Math.max(
          0,
          nextPriorities[candidateKey] + diff
        )
      }
    } else {
      // If other keys were all zero, distribute remaining budget equally
      const base = Math.floor(remainingBudget / otherKeys.length)
      const remainder = remainingBudget % otherKeys.length
      otherKeys.forEach((k, idx) => {
        nextPriorities[k] = base + (idx < remainder ? 1 : 0)
      })
    }

    onChange(nextPriorities)
  }

  return (
    <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-7 shadow-xs space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <h3 className="text-base sm:text-lg font-bold text-slate-900">
            What matters most to you? ({categoryConfig.label})
          </h3>
          <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
            Calibrate the relative importance of each factor. Total must equal 100%.
          </p>
        </div>

        {/* Reset Button */}
        <button
          type="button"
          onClick={onReset}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 hover:border-slate-300 bg-slate-50 hover:bg-slate-100 text-slate-600 text-xs font-semibold transition-all cursor-pointer self-start sm:self-auto"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>Reset to Balanced</span>
        </button>
      </div>

      {/* 5 Dynamic Sliders */}
      <div className="space-y-5 pt-2">
        {factors.map((factor) => {
          const Icon = factor.icon
          const val = priorities[factor.key] ?? 20

          return (
            <div
              key={factor.key}
              className="p-3.5 rounded-xl bg-slate-50/60 border border-slate-200/70 hover:border-slate-300 transition-colors"
            >
              <div className="flex items-center justify-between mb-1.5">
                <div className="flex items-center gap-2">
                  <div className={`w-6 h-6 rounded-md bg-white border border-slate-200/80 ${factor.color} flex items-center justify-center`}>
                    <Icon className="w-3.5 h-3.5" />
                  </div>
                  <div>
                    <span className="text-sm font-bold text-slate-900">
                      {factor.name}
                    </span>
                    <span className="text-xs text-slate-400 hidden sm:inline ml-2 font-normal">
                      &mdash; {factor.desc}
                    </span>
                  </div>
                </div>

                <div className="font-mono text-sm font-bold text-slate-900 bg-white border border-slate-200 px-2.5 py-0.5 rounded-md min-w-[50px] text-center shadow-2xs">
                  {val}%
                </div>
              </div>

              {/* Slider Input */}
              <div className="pt-1">
                <input
                  type="range"
                  min="0"
                  max="100"
                  step="1"
                  value={val}
                  onChange={(e) => handleSliderChange(factor.key, e.target.value)}
                  className={`w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer ${factor.accent || 'accent-indigo-600'}`}
                  aria-label={`${factor.name} weight percentage`}
                />
              </div>
            </div>
          )
        })}
      </div>

      {/* Distribution visual bar */}
      <PriorityDistribution category={category} subcategory={subcategory} priorities={priorities} />

      {/* Smart insight preview */}
      <SmartInsight category={category} subcategory={subcategory} priorities={priorities} />
    </div>
  )
}
