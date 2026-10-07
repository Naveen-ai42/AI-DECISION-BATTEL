import React, { useState } from 'react'
import { Plus, X, CheckCircle2, Sparkles } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Interactive input for adding and removing category-aware must-have requirements.
 */
export default function RequirementInput({ category = 'electronics', subcategory = '', requirements = [], onAdd, onRemove }) {
  const [inputValue, setInputValue] = useState('')
  const categoryConfig = getCategoryConfig(category, subcategory)
  const suggestions = categoryConfig.requirements || []

  const handleAdd = (e) => {
    if (e) e.preventDefault()
    const trimmed = inputValue.trim()
    if (!trimmed) return
    if (!requirements.includes(trimmed)) {
      onAdd(trimmed)
    }
    setInputValue('')
  }

  const handleSuggestionClick = (suggestion) => {
    if (!requirements.includes(suggestion)) {
      onAdd(suggestion)
    }
  }

  return (
    <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-7 shadow-xs">
      <div className="mb-4">
        <h3 className="text-base sm:text-lg font-bold text-slate-900">
          What are your must-haves? ({categoryConfig.label})
        </h3>
        <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
          Specify non-negotiable features or specifications you need.
        </p>
      </div>

      {/* Input row */}
      <form onSubmit={handleAdd} className="flex gap-2.5 mb-4">
        <div className="relative flex-1">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder={`Add a requirement... (e.g. ${suggestions[0] || 'High quality'})`}
            className="w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:border-indigo-600 focus:bg-white focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all placeholder:text-slate-400"
          />
        </div>
        <button
          type="submit"
          disabled={!inputValue.trim()}
          className="inline-flex items-center justify-center px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold shadow-xs disabled:opacity-40 disabled:cursor-not-allowed transition-all cursor-pointer"
        >
          <Plus className="w-4 h-4 mr-1" />
          <span>Add</span>
        </button>
      </form>

      {/* Suggestion inspiration pills */}
      {suggestions.length > 0 && (
        <div className="flex flex-wrap items-center gap-1.5 mb-4 text-xs">
          <span className="text-slate-400 font-medium inline-flex items-center gap-1 mr-1">
            <Sparkles className="w-3 h-3 text-indigo-500" />
            Ideas:
          </span>
          {suggestions.map((sug) => {
            const isAdded = requirements.includes(sug)
            return (
              <button
                key={sug}
                type="button"
                onClick={() => handleSuggestionClick(sug)}
                disabled={isAdded}
                className={`px-2.5 py-1 rounded-lg transition-all text-xs font-medium cursor-pointer ${
                  isAdded
                    ? 'bg-slate-100 text-slate-400 border border-slate-200/50 cursor-default'
                    : 'bg-indigo-50/60 hover:bg-indigo-100 text-indigo-700 border border-indigo-100'
                }`}
              >
                + {sug}
              </button>
            )
          })}
        </div>
      )}

      {/* Removable chips container */}
      <div className="min-h-[44px] p-3 rounded-xl bg-slate-50/70 border border-slate-200/60 flex flex-wrap gap-2 items-center">
        {requirements.length === 0 ? (
          <span className="text-xs text-slate-400 italic">
            No requirements added yet. Type above or click an idea to add.
          </span>
        ) : (
          requirements.map((req) => (
            <div
              key={req}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-slate-800 text-xs font-medium shadow-2xs group"
            >
              <CheckCircle2 className="w-3.5 h-3.5 text-indigo-600 flex-shrink-0" />
              <span>{req}</span>
              <button
                type="button"
                onClick={() => onRemove(req)}
                className="ml-1 p-0.5 rounded-md hover:bg-slate-100 text-slate-400 hover:text-rose-600 transition-colors cursor-pointer"
                aria-label={`Remove requirement ${req}`}
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
