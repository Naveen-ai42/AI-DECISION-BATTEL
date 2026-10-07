import { createContext } from 'react'
import { getDefaultPrioritiesForCategory } from '../config/categoryConfig'

export const initialDecisionState = {
  description: '',
  category: 'electronics',
  subcategory: 'laptop',
  budget: '',
  location: '',
  deadline: '',
  additionalRequirements: '',
  requirements: [],
  dealBreakers: [],
  priorities: getDefaultPrioritiesForCategory('electronics', 'laptop'),
  riskTolerance: 'balanced',
  decisionStyle: 'best-overall',
}

export const DecisionContext = createContext(null)
