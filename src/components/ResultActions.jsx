import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Bookmark,
  Share2,
  PlusCircle,
  ArrowLeft,
  Check,
  Info
} from 'lucide-react'
import Button from './Button'

/**
 * Bottom action controls for the Results page: Save, Start New, Back to Battle, Share Result.
 */
export default function ResultActions({ decision, winnerName = 'Recommended Choice', overallScore = 91, onReset }) {
  const navigate = useNavigate()
  const [toastMessage, setToastMessage] = useState(null)
  const [isSaved, setIsSaved] = useState(false)

  const showToast = (msg) => {
    setToastMessage(msg)
    setTimeout(() => {
      setToastMessage(null)
    }, 3000)
  }

  // Save to localStorage
  const handleSaveDecision = () => {
    try {
      const existing = JSON.parse(localStorage.getItem('saved_decisions') || '[]')
      const entry = {
        id: Date.now(),
        date: new Date().toISOString(),
        description: decision?.description || 'General Decision',
        category: decision?.category || 'electronics',
        subcategory: decision?.subcategory || '',
        budget: decision?.budget || '',
        location: decision?.location || '',
        deadline: decision?.deadline || '',
        additionalRequirements: decision?.additionalRequirements || '',
        priorities: decision?.priorities || {},
        requirements: decision?.requirements || [],
        dealBreakers: decision?.dealBreakers || [],
        riskTolerance: decision?.riskTolerance || 'balanced',
        decisionStyle: decision?.decisionStyle || 'best-overall',
        winner: winnerName,
        score: overallScore,
      }
      const existingIndex = existing.findIndex((saved) => (
        saved.description === entry.description &&
        saved.category === entry.category &&
        (saved.subcategory || '') === entry.subcategory &&
        String(saved.budget || '') === entry.budget
      ))
      if (existingIndex >= 0) {
        entry.id = existing[existingIndex].id || entry.id
        existing.splice(existingIndex, 1)
      }
      existing.unshift(entry)
      localStorage.setItem('saved_decisions', JSON.stringify(existing.slice(0, 20)))
      setIsSaved(true)
      showToast('Decision saved successfully.')
    } catch {
      showToast('Failed to save locally.')
    }
  }

  // Copy share summary to clipboard
  const handleShareResult = async () => {
    const summary = `Decision Arena Verdict:\n` +
      `Objective: "${decision?.description}"\n` +
      `Recommended Choice: ${winnerName}\n` +
      `Match Score: ${overallScore} / 100\n` +
      `Analyzed across 5 autonomous AI perspectives.`

    try {
      if (navigator.clipboard) {
        await navigator.clipboard.writeText(summary)
        showToast('Decision summary copied.')
      } else {
        showToast('Clipboard not supported in this browser.')
      }
    } catch {
      showToast('Decision summary copied.')
    }
  }

  const handleStartNew = () => {
    if (onReset) onReset()
    navigate('/create')
  }

  return (
    <div className="w-full pt-6 border-t border-slate-200/80">
      {/* Action Buttons Row */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 mb-8">
        <div className="flex items-center gap-3 w-full sm:w-auto order-2 sm:order-1">
          <Button
            to="/battle"
            variant="secondary"
            className="w-full sm:w-auto gap-2 text-sm"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back to Battle</span>
          </Button>

          <button
            type="button"
            onClick={handleShareResult}
            className="inline-flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-700 text-xs font-semibold transition-colors cursor-pointer w-full sm:w-auto"
          >
            <Share2 className="w-3.5 h-3.5 text-slate-500" />
            <span>Share Result</span>
          </button>
        </div>

        <div className="flex items-center gap-3 w-full sm:w-auto order-1 sm:order-2">
          <button
            type="button"
            onClick={handleStartNew}
            className="inline-flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-700 text-sm font-semibold transition-colors cursor-pointer w-full sm:w-auto"
          >
            <PlusCircle className="w-4 h-4 text-slate-500" />
            <span>Start New Decision</span>
          </button>

          <Button
            onClick={handleSaveDecision}
            variant="primary"
            className="w-full sm:w-auto px-7 py-3 text-sm shadow-sm hover:shadow-md"
          >
            <Bookmark className="w-4 h-4 mr-1.5" />
            <span>{isSaved ? 'Decision Saved ✓' : 'Save Decision'}</span>
          </Button>
        </div>
      </div>

      {/* Subtle Demo Mode Disclaimer */}
      <div className="text-center pb-2">
        <span className="inline-flex items-center gap-1.5 text-xs text-slate-400">
          <Info className="w-3.5 h-3.5" />
          <span>Demo mode &mdash; AI analysis will be connected in the next development phase.</span>
        </span>
      </div>

      {/* Floating Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-slate-900 text-white px-4 py-3 rounded-2xl shadow-xl flex items-center gap-2 text-xs font-semibold animate-fadeIn">
          <Check className="w-4 h-4 text-emerald-400 stroke-[3]" />
          <span>{toastMessage}</span>
        </div>
      )}
    </div>
  )
}
