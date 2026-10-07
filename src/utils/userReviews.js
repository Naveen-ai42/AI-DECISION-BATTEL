export const USER_REVIEWS_KEY = 'decision_arena_product_reviews'

export function readSavedReviews() {
  try {
    const parsed = JSON.parse(localStorage.getItem(USER_REVIEWS_KEY) || '[]')
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

export function writeSavedReviews(reviews) {
  localStorage.setItem(USER_REVIEWS_KEY, JSON.stringify(reviews))
}
