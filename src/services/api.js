/**
 * Decision Arena Backend API Service Layer
 * Connects React frontend to the FastAPI backend running on http://127.0.0.1:8001
 */

const API_BASE_URL = 'http://127.0.0.1:8001';

/**
 * Tests connection with the backend health check endpoint.
 * GET /api/health
 * @returns {Promise<Object>} Backend health status
 */
export async function checkHealth() {
  console.log('Checking backend:', `${API_BASE_URL}/api/health`);

  try {
    const response = await fetch(`${API_BASE_URL}/api/health`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Health check failed with status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Decision Arena API error in checkHealth:', error);
    throw error;
  }
}

/**
 * Submits the decision object to the FastAPI backend for multi-agent analysis and scoring.
 * POST /api/analysis
 * @param {Object} decision - The user's decision context and priorities
 * @returns {Promise<Object>} Analysis response containing agents and decisionEngine synthesis
 */
export async function startDecisionAnalysis(decision) {
  // Format priorities dynamically with guaranteed numbers
  const p = decision?.priorities || {};
  const formattedPriorities = {};
  Object.keys(p).forEach((key) => {
    formattedPriorities[key] = Number(p[key] ?? 20);
  });

  const payload = {
    description: decision?.description || '',
    category: decision?.category || 'electronics',
    subcategory: decision?.subcategory || '',
    topN: Number(decision?.topN || 5),
    budget: String(decision?.budget || ''),
    location: String(decision?.location || ''),
    deadline: String(decision?.deadline || ''),
    additionalRequirements: String(decision?.additionalRequirements || ''),
    requirements: Array.isArray(decision?.requirements) ? decision.requirements : [],
    dealBreakers: Array.isArray(decision?.dealBreakers) ? decision.dealBreakers : [],
    priorities: formattedPriorities,
    riskTolerance: decision?.riskTolerance || 'balanced',
    decisionStyle: decision?.decisionStyle || 'best-overall',
  };

  try {
    const response = await fetch(`${API_BASE_URL}/api/analysis`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      let errorDetail = `Analysis failed with status code ${response.status}`;
      try {
        const errorJson = await response.json();
        if (errorJson?.detail) {
          errorDetail = typeof errorJson.detail === 'string'
            ? errorJson.detail
            : JSON.stringify(errorJson.detail);
        }
      } catch {
        // Fall back to status text
      }
      const err = new Error(errorDetail);
      err.status = response.status;
      throw err;
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Decision Arena API error:', error);
    // Annotate connection failure for friendly UI error handling
    if (error.name === 'TypeError' || error.message.includes('fetch')) {
      error.isConnectionError = true;
    }
    throw error;
  }
}

/**
 * Placeholder helper for future individual agent queries
 */
export async function getAgentResults(decisionId) {
  return [];
}

/**
 * Placeholder helper for future final decision queries
 */
export async function getFinalDecision(decisionId) {
  return null;
}
