import React, { useState } from 'react'
import { DecisionContext, initialDecisionState } from './decisionState'

const HISTORY_STORAGE_KEY = 'decision_history'

function getStoredHistory() {
  try {
    const saved = localStorage.getItem(HISTORY_STORAGE_KEY)
    return saved ? JSON.parse(saved) : []
  } catch {
    return []
  }
}

export function DecisionProvider({ children }) {
  const [decision, setDecision] = useState(() => {
    try {
      const saved = sessionStorage.getItem('current_decision')
      return saved ? { ...initialDecisionState, ...JSON.parse(saved) } : initialDecisionState
    } catch {
      return initialDecisionState
    }
  })

  const [history, setHistory] = useState(getStoredHistory)

  const syncHistory = (nextHistory) => {
    setHistory(nextHistory)
    try {
      localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(nextHistory))
    } catch {
      // Ignore local storage errors
    }
  }

  const updateDecision = (updates) => {
    setDecision((prev) => {
      const updated = { ...prev, ...updates }
      try {
        sessionStorage.setItem('current_decision', JSON.stringify(updated))
      } catch {
        // Ignore session storage errors
      }
      return updated
    })
  }

  const saveCurrentDecisionToHistory = (entryOverride) => {
    const entry = entryOverride || {
      id: Date.now(),
      description: decision.description,
      category: decision.category,
      subcategory: decision.subcategory,
      budget: decision.budget,
      createdAt: new Date().toISOString(),
    }

    const nextHistory = [entry, ...history.filter((item) => item.description !== entry.description || item.category !== entry.category)].slice(0, 8)
    syncHistory(nextHistory)
  }

  const clearHistory = () => syncHistory([])

  const resetDecision = () => {
    setDecision(initialDecisionState)
    try {
      sessionStorage.removeItem('current_decision')
    } catch {
      // Ignore
    }
  }

  return (
    <DecisionContext.Provider value={{
      decision,
      history,
      updateDecision,
      resetDecision,
      saveCurrentDecisionToHistory,
      clearHistory,
    }}>
      {children}
    </DecisionContext.Provider>
  )
}
