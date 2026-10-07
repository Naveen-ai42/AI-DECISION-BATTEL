import React, { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Clock3, ArrowRight, RotateCcw, Trash2 } from 'lucide-react'
import Button from '../components/Button'
import { useDecision } from '../hooks/useDecision'

const HISTORY_KEY = 'saved_decisions'

export default function HistoryPage() {
  const navigate = useNavigate()
  const { updateDecision } = useDecision()
  const [history, setHistory] = useState([])

  useEffect(() => {
    try {
      const saved = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]')
      setHistory(saved)
    } catch {
      setHistory([])
    }
  }, [])

  const clearHistory = () => {
    localStorage.removeItem(HISTORY_KEY)
    setHistory([])
  }

  const handleRestore = (entry) => {
    updateDecision({
      description: entry.description || '',
      category: entry.category || 'electronics',
      subcategory: entry.subcategory || '',
      budget: entry.budget || '',
      location: entry.location || '',
      deadline: entry.deadline || '',
      additionalRequirements: entry.additionalRequirements || '',
      priorities: entry.priorities || {},
      requirements: entry.requirements || [],
      dealBreakers: entry.dealBreakers || [],
      riskTolerance: entry.riskTolerance || 'balanced',
      decisionStyle: entry.decisionStyle || 'best-overall',
    })
    navigate('/create')
  }

  const handleRerun = (entry) => {
    updateDecision({
      description: entry.description || '',
      category: entry.category || 'electronics',
      subcategory: entry.subcategory || '',
      budget: entry.budget || '',
      location: entry.location || '',
      deadline: entry.deadline || '',
      additionalRequirements: entry.additionalRequirements || '',
      priorities: entry.priorities || {},
      requirements: entry.requirements || [],
      dealBreakers: entry.dealBreakers || [],
      riskTolerance: entry.riskTolerance || 'balanced',
      decisionStyle: entry.decisionStyle || 'best-overall',
      analysisResults: null,
    })
    navigate('/battle')
  }

  return (
    <div className="flex-1 w-full py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-8">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-indigo-600">Activity</p>
            <h1 className="mt-2 text-3xl sm:text-4xl font-bold text-slate-900">Decision History</h1>
          </div>

          {history.length > 0 && (
            <button
              type="button"
              onClick={clearHistory}
              className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 hover:border-red-200 hover:text-red-600 transition-colors"
            >
              <Trash2 className="w-4 h-4" />
              Clear history
            </button>
          )}
        </div>

        {history.length === 0 ? (
          <div className="rounded-3xl border border-dashed border-slate-300 bg-white p-8 text-center shadow-xs">
            <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-indigo-50 text-indigo-600">
              <Clock3 className="h-8 w-8" />
            </div>
            <h2 className="mt-5 text-2xl font-bold text-slate-900">No saved decisions yet</h2>
            <p className="mt-3 text-sm text-slate-500 max-w-md mx-auto">
              Your completed decisions will appear here once you save a result.
            </p>
            <div className="mt-6 flex justify-center">
              <Button to="/create" variant="primary" className="justify-center">
                Start a decision
                <ArrowRight className="w-4 h-4 ml-1.5" />
              </Button>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            {history.map((entry) => (
              <div key={entry.id || `${entry.description}-${entry.date}`} className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs">
                <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                  <div>
                    <p className="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">{entry.category || 'electronics'}</p>
                    <h3 className="mt-2 text-xl font-semibold text-slate-900">{entry.description || 'Untitled decision'}</h3>
                    <div className="mt-3 flex flex-wrap gap-2 text-xs text-slate-500">
                      {entry.winner && <span className="rounded-full bg-slate-100 px-2.5 py-1">Winner: {entry.winner}</span>}
                      {entry.score && <span className="rounded-full bg-slate-100 px-2.5 py-1">Score: {entry.score}</span>}
                    </div>
                  </div>

                  <div className="flex flex-col sm:flex-row gap-2 shrink-0">
                    <button
                      type="button"
                      onClick={() => handleRerun(entry)}
                      className="inline-flex items-center justify-center gap-2 rounded-xl bg-indigo-600 px-4 py-2.5 text-sm font-medium text-white hover:bg-indigo-500 transition-colors"
                    >
                      <RotateCcw className="w-4 h-4" />
                      Run again
                    </button>
                    <button
                      type="button"
                      onClick={() => handleRestore(entry)}
                      className="inline-flex items-center justify-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors"
                    >
                      Edit decision
                      <ArrowRight className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        <div className="mt-8 text-center">
          <Link to="/" className="text-sm font-medium text-indigo-600 hover:text-indigo-500">
            Back to home
          </Link>
        </div>
      </div>
    </div>
  )
}
