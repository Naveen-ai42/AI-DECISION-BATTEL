import React, { useState } from 'react'
import { Plus, X, Ban, Sparkles } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Interactive input for adding and removing negative deal-breaker criteria based on category.
 */
export default function DealBreakerInput({ category = 'electronics', subcategory = '', dealBreakers = [], onAdd, onRemove }) {
  const [inputValue, setInputValue] = useState('')
  const categoryConfig = getCategoryConfig(category, subcategory)
  const suggestions = categoryConfig.dealBreakers || []

  const handleAdd = (e) => {
    if (e) e.preventDefault()
    const trimmed = inputValue.trim()
    if (!trimmed) return
    if (!dealBreakers.includes(trimmed)) {
      onAdd(trimmed)
    }
    setInputValue('')
  }

  const handleSuggestionClick = (suggestion) => {
    if (!dealBreakers.includes(suggestion)) {
      onAdd(suggestion)
    }
  }

  return (
    <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-7 shadow-xs">
      <div className="mb-4">
        <div className="flex items-center justify-between">
          <h3 className="text-base sm:text-lg font-bold text-slate-900">
            Any deal-breakers? ({categoryConfig.label})
          </h3>
          <span className="text-xs text-slate-400 font-normal">Optional</span>
        </div>
        <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
          Things you definitely don&apos;t want. Options with these traits will be penalized or filtered.
        </p>
      </div>

      {/* Input row */}
      <form onSubmit={handleAdd} className="flex gap-2.5 mb-4">
        <div className="relative flex-1">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder={`Add a deal-breaker... (e.g. ${suggestions[0] || 'Unacceptable terms'})`}
            className="w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:border-rose-500 focus:bg-white focus:ring-4 focus:ring-rose-500/10 outline-none transition-all placeholder:text-slate-400"
          />
        </div>
        <button
          type="submit"
          disabled={!inputValue.trim()}
          className="inline-flex items-center justify-center px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-900 text-white text-sm font-semibold shadow-xs disabled:opacity-40 disabled:cursor-not-allowed transition-all cursor-pointer"
        >
          <Plus className="w-4 h-4 mr-1" />
          <span>Add</span>
        </button>
      </form>

      {/* Suggestion inspiration pills */}
      {suggestions.length > 0 && (
        <div className="flex flex-wrap items-center gap-1.5 mb-4 text-xs">
          <span className="text-slate-400 font-medium inline-flex items-center gap-1 mr-1">
            <Sparkles className="w-3 h-3 text-rose-500" />
            Common deal-breakers:
          </span>
          {suggestions.map((sug) => {
            const isAdded = dealBreakers.includes(sug)
            return (
              <button
                key={sug}
                type="button"
                onClick={() => handleSuggestionClick(sug)}
                disabled={isAdded}
                className={`px-2.5 py-1 rounded-lg transition-all text-xs font-medium cursor-pointer ${
                  isAdded
                    ? 'bg-slate-100 text-slate-400 border border-slate-200/50 cursor-default'
                    : 'bg-rose-50 hover:bg-rose-100 text-rose-700 border border-rose-100'
                }`}
              >
                + {sug}
              </button>
            )
          })}
        </div>
      )}

      {/* Removable deal-breaker chips */}
      <div className="min-h-[44px] p-3 rounded-xl bg-slate-50/70 border border-slate-200/60 flex flex-wrap gap-2 items-center">
        {dealBreakers.length === 0 ? (
          <span className="text-xs text-slate-400 italic">
            None specified (optional). Add any absolute red flags here.
          </span>
        ) : (
          dealBreakers.map((db) => (
            <div
              key={db}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-rose-50/70 border border-rose-200 text-rose-800 text-xs font-medium shadow-2xs group"
            >
              <Ban className="w-3.5 h-3.5 text-rose-600 flex-shrink-0" />
              <span>{db}</span>
              <button
                type="button"
                onClick={() => onRemove(db)}
                className="ml-1 p-0.5 rounded-md hover:bg-rose-100 text-rose-400 hover:text-rose-700 transition-colors cursor-pointer"
                aria-label={`Remove deal-breaker ${db}`}
              >
                <X className="w-3.5 h-3.5 stroke-[2.5]" />
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  )
}
