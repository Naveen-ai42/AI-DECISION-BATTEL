import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Sparkles, ArrowRight, AlertCircle } from 'lucide-react'
import CategorySelector from './CategorySelector'
import AdditionalContext from './AdditionalContext'
import Button from './Button'
import { useDecision } from '../hooks/useDecision'
import { getCategoryConfig, getDefaultPrioritiesForCategory } from '../config/categoryConfig'

export default function DecisionForm() {
  const navigate = useNavigate()
  const { decision, updateDecision } = useDecision()

  const [description, setDescription] = useState(decision.description || '')
  const [category, setCategory] = useState(decision.category || 'electronics')
  const [subcategory, setSubcategory] = useState(decision.subcategory || 'laptop')
  const [extraContext, setExtraContext] = useState({
    budget: decision.budget || '',
    location: decision.location || '',
    deadline: decision.deadline || '',
    additionalRequirements: decision.additionalRequirements || '',
  })
  const [touched, setTouched] = useState(false)

  // Dynamically load category & subcategory configuration
  const currentCategoryConfig = getCategoryConfig(category, subcategory)

  const handleDescriptionChange = (e) => {
    const val = e.target.value
    if (val.length <= 500) {
      setDescription(val)
      if (!touched) setTouched(true)

      // Intelligent subcategory auto-detection for electronics if user types keywords
      if (category === 'electronics') {
        const lower = val.toLowerCase()
        if (lower.includes('watch') || lower.includes('smartwatch')) {
          setSubcategory('smartwatch')
        } else if (lower.includes('phone') || lower.includes('mobile') || lower.includes('smartphone')) {
          setSubcategory('smartphone')
        }
      }
    }
  }

  const handleCategorySelect = (newCategory) => {
    setCategory(newCategory)
    const conf = getCategoryConfig(newCategory)
    const newSub = conf.subcategories?.length ? conf.subcategories[0].id : ''
    setSubcategory(newSub)

    // Update priorities to match new category & subcategory factors
    const defaultP = getDefaultPrioritiesForCategory(newCategory, newSub)
    updateDecision({
      category: newCategory,
      subcategory: newSub,
      priorities: defaultP,
    })
  }

  const handleSubcategorySelect = (newSubcategory) => {
    setSubcategory(newSubcategory)
    const defaultP = getDefaultPrioritiesForCategory(category, newSubcategory)
    updateDecision({
      category,
      subcategory: newSubcategory,
      priorities: defaultP,
    })
  }

  const handleContextChange = (field, value) => {
    setExtraContext((prev) => ({
      ...prev,
      [field]: value,
    }))
  }

  const handleApplyExample = (example) => {
    const exCat = example.category || category
    const exSub = example.subcategory || (exCat === 'electronics' ? 'laptop' : '')
    setDescription(example.description)
    setCategory(exCat)
    setSubcategory(exSub)
    if (example.budget !== undefined) {
      setExtraContext((prev) => ({ ...prev, budget: example.budget }))
    }
    const defaultP = getDefaultPrioritiesForCategory(exCat, exSub)
    updateDecision({
      category: exCat,
      subcategory: exSub,
      priorities: defaultP,
    })
    setTouched(true)
  }

  // Validation rules
  const trimmedLength = description.trim().length
  const isEmpty = trimmedLength === 0
  const isTooShort = trimmedLength > 0 && trimmedLength < 10
  const isValid = trimmedLength >= 10

  const getValidationMessage = () => {
    if (!touched) return null
    if (isEmpty) return "Tell us what you're deciding before continuing."
    if (isTooShort) return "Please provide a little more detail."
    return null
  }

  const validationMessage = getValidationMessage()

  const handleContinue = (e) => {
    e.preventDefault()
    setTouched(true)

    if (!isValid) return

    // Ensure priorities match current category & subcategory
    const defaultP = getDefaultPrioritiesForCategory(category, subcategory)
    const existingPriorities = decision.priorities || {}
    const hasCategoryKeys = currentCategoryConfig.factors.every((f) => existingPriorities[f.key] !== undefined)
    const finalPriorities = hasCategoryKeys ? existingPriorities : defaultP

    const payload = {
      description: description.trim(),
      category,
      subcategory,
      budget: extraContext.budget,
      location: extraContext.location,
      deadline: extraContext.deadline,
      additionalRequirements: extraContext.additionalRequirements,
      priorities: finalPriorities,
    }

    updateDecision(payload)
    navigate('/requirements', { state: { decision: payload } })
  }

  return (
    <form onSubmit={handleContinue} className="space-y-8">
      {/* 1. CATEGORY SELECTOR (Choose what type of decision first) */}
      <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-7 shadow-xs">
        <CategorySelector
          selectedCategory={category}
          onSelectCategory={handleCategorySelect}
          selectedSubcategory={subcategory}
          onSelectSubcategory={handleSubcategorySelect}
        />
      </div>

      {/* 2. DECISION DESCRIPTION */}
      <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-7 shadow-xs">
        <div className="flex items-center justify-between mb-2">
          <label
            htmlFor="decision-description"
            className="block text-sm font-semibold text-slate-900"
          >
            Describe your decision ({currentCategoryConfig.label})
          </label>
          <span
            className={`text-xs font-mono font-medium ${
              description.length >= 480
                ? 'text-amber-600 font-bold'
                : 'text-slate-400'
            }`}
          >
            {description.length} / 500
          </span>
        </div>

        <div className="relative">
          <textarea
            id="decision-description"
            rows={4}
            value={description}
            onChange={handleDescriptionChange}
            onBlur={() => setTouched(true)}
            placeholder={currentCategoryConfig.placeholder}
            className={`block w-full p-4 text-base text-slate-900 bg-slate-50/50 rounded-xl border transition-all duration-200 outline-none resize-none placeholder:text-slate-400 ${
              validationMessage
                ? 'border-rose-300 focus:border-rose-500 focus:ring-2 focus:ring-rose-500/20'
                : 'border-slate-200 focus:border-indigo-600 focus:bg-white focus:ring-4 focus:ring-indigo-500/10 focus:shadow-sm'
            }`}
          />
        </div>

        {/* Validation message */}
        {validationMessage && (
          <div className="flex items-center gap-1.5 text-xs text-rose-600 font-medium mt-2.5 animate-fadeIn">
            <AlertCircle className="w-3.5 h-3.5 flex-shrink-0" />
            <span>{validationMessage}</span>
          </div>
        )}

        {/* DYNAMIC CATEGORY EXAMPLES */}
        <div className="mt-6 pt-5 border-t border-slate-100">
          <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3">
            <Sparkles className="w-3.5 h-3.5 text-indigo-500" />
            <span>{currentCategoryConfig.label} Examples</span>
          </div>

          <div className="flex flex-wrap gap-2">
            {currentCategoryConfig.examples.map((ex) => {
              const Icon = currentCategoryConfig.icon
              return (
                <button
                  key={ex.label}
                  type="button"
                  onClick={() => handleApplyExample(ex)}
                  className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-medium bg-slate-50 text-slate-700 border border-slate-200 hover:border-indigo-300 hover:bg-indigo-50/60 hover:text-indigo-700 transition-all cursor-pointer shadow-2xs text-left"
                >
                  <Icon className="w-3.5 h-3.5 text-slate-500 flex-shrink-0" />
                  <span>{ex.label}</span>
                </button>
              )
            })}
          </div>
        </div>
      </div>

      {/* 3. OPTIONAL CONTEXT */}
      <AdditionalContext
        values={extraContext}
        onChange={handleContextChange}
      />

      {/* 4. BOTTOM ACTION */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4">
        <p className="text-xs text-slate-400 text-center sm:text-left">
          {isValid
            ? '✓ Ready to define requirements'
            : 'Enter at least 10 characters to continue'}
        </p>

        <Button
          type="submit"
          variant="primary"
          disabled={!isValid}
          className="w-full sm:w-auto px-8 py-3.5 text-base shadow-sm hover:shadow-md"
        >
          <span>Continue</span>
          <ArrowRight className="w-4 h-4 ml-2" />
        </Button>
      </div>
    </form>
  )
}
