/**
 * Centralized Decision Configuration System (src/config/decisionConfig.js)
 * 
 * Provides unified category and subcategory definitions, evaluation factors,
 * specialized autonomous agent definitions, candidate option types,
 * common must-have requirements, and common deal-breakers across all domains.
 */

import {
  CATEGORIES_CONFIG,
  getCategoryConfig,
  getDefaultPrioritiesForCategory,
  CATEGORY_LIST,
} from './categoryConfig'

export {
  CATEGORIES_CONFIG,
  getCategoryConfig,
  getDefaultPrioritiesForCategory,
  CATEGORY_LIST,
}

/**
 * Returns specialized agents for a given decision category and subcategory.
 */
export function getAgentsForDecision(category, subcategory) {
  const config = getCategoryConfig(category, subcategory)
  return config.agents || []
}

/**
 * Returns dynamic evaluation factors for a decision category and subcategory.
 */
export function getFactorsForDecision(category, subcategory) {
  const config = getCategoryConfig(category, subcategory)
  return config.factors || []
}

/**
 * Reusable Option schema helper
 */
export function createCandidateOptionModel({
  id,
  name,
  category,
  subcategory,
  attributes = {},
  price = '',
  description = '',
  strengths = [],
  concerns = [],
}) {
  return {
    id,
    name,
    category,
    subcategory,
    attributes,
    price,
    description,
    strengths,
    concerns,
  }
}
