import { useContext } from 'react'
import { DecisionContext, initialDecisionState } from '../context/decisionState'

export function useDecision() {
  const context = useContext(DecisionContext)
  if (!context) {
    return {
      decision: initialDecisionState,
      history: [],
      updateDecision: () => {},
      resetDecision: () => {},
      saveCurrentDecisionToHistory: () => {},
      clearHistory: () => {},
    }
  }
  return context
}
