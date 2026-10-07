import React, { useState } from 'react'
import { ChevronDown, ChevronUp, MapPin, Calendar, FileText } from 'lucide-react'

/**
 * Collapsible section for optional contextual details:
 * Budget, Location, Deadline, Additional Requirements.
 */
export default function AdditionalContext({
  values,
  onChange,
}) {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="w-full border border-slate-200/90 rounded-2xl bg-white overflow-hidden transition-all duration-200">
      {/* Header toggle */}
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-5 py-4 flex items-center justify-between text-left hover:bg-slate-50/70 transition-colors cursor-pointer group"
        aria-expanded={isOpen}
      >
        <div className="flex items-center gap-2">
          <span className="text-sm font-semibold text-slate-800 group-hover:text-indigo-600 transition-colors">
            {isOpen ? '− Hide optional context' : '+ Add more context'}
          </span>
          <span className="text-xs text-slate-400 font-normal">
            (Budget, Location, Deadline)
          </span>
        </div>
        <div className="text-slate-400 group-hover:text-indigo-600 transition-colors">
          {isOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
        </div>
      </button>

      {/* Collapsible Content */}
      {isOpen && (
        <div className="px-5 pb-6 pt-2 border-t border-slate-100 space-y-4 bg-slate-50/40">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {/* Budget with ₹ prefix */}
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                Budget (Optional)
              </label>
              <div className="relative rounded-xl shadow-2xs">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500 font-medium text-sm">
                  ₹
                </div>
                <input
                  type="number"
                  name="budget"
                  value={values.budget || ''}
                  onChange={(e) => onChange('budget', e.target.value)}
                  placeholder="55,000"
                  className="block w-full pl-8 pr-3 py-2.5 text-sm bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-600 outline-none transition-all placeholder:text-slate-400"
                />
              </div>
            </div>

            {/* Location */}
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                Location (Optional)
              </label>
              <div className="relative rounded-xl shadow-2xs">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
                  <MapPin className="w-3.5 h-3.5" />
                </div>
                <input
                  type="text"
                  name="location"
                  value={values.location || ''}
                  onChange={(e) => onChange('location', e.target.value)}
                  placeholder="e.g. Bangalore, India"
                  className="block w-full pl-8 pr-3 py-2.5 text-sm bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-600 outline-none transition-all placeholder:text-slate-400"
                />
              </div>
            </div>

            {/* Deadline */}
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                Target Deadline (Optional)
              </label>
              <div className="relative rounded-xl shadow-2xs">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
                  <Calendar className="w-3.5 h-3.5" />
                </div>
                <input
                  type="date"
                  name="deadline"
                  value={values.deadline || ''}
                  onChange={(e) => onChange('deadline', e.target.value)}
                  className="block w-full pl-8 pr-3 py-2.5 text-sm bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-600 outline-none transition-all text-slate-700"
                />
              </div>
            </div>
          </div>

          {/* Additional Requirements */}
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5">
              Additional Requirements or Constraints (Optional)
            </label>
            <div className="relative rounded-xl shadow-2xs">
              <textarea
                name="additionalRequirements"
                rows={2}
                value={values.additionalRequirements || ''}
                onChange={(e) => onChange('additionalRequirements', e.target.value)}
                placeholder="Specific preferences, non-negotiable features, brand constraints, etc."
                className="block w-full p-3 text-sm bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-600 outline-none transition-all placeholder:text-slate-400 resize-none"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
