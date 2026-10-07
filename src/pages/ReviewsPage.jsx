import { useState } from 'react'
import { Link } from 'react-router-dom'
import { ArrowRight, MessageSquareText, Star, Trash2 } from 'lucide-react'
import Button from '../components/Button'
import { readSavedReviews, writeSavedReviews } from '../utils/userReviews'

export default function ReviewsPage() {
  const [reviews, setReviews] = useState(readSavedReviews)
  const [notice, setNotice] = useState('')

  const removeReview = (reviewId) => {
    const updated = reviews.filter((review) => review.id !== reviewId)
    try {
      writeSavedReviews(updated)
      setReviews(updated)
      setNotice('Review deleted.')
    } catch {
      setNotice('This browser could not update saved reviews.')
    }
  }

  const clearReviews = () => {
    try {
      writeSavedReviews([])
      setReviews([])
      setNotice('All saved reviews were deleted.')
    } catch {
      setNotice('This browser could not update saved reviews.')
    }
  }

  return (
    <div className="flex-1 w-full py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-8">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-amber-700">Saved here</p>
            <h1 className="mt-2 text-3xl sm:text-4xl font-bold text-slate-900">Your Reviews</h1>
            <p className="mt-2 text-sm text-slate-500">Saved in this browser only. Reviews are self-reported and not independently verified.</p>
          </div>

          {reviews.length > 0 && (
            <button
              type="button"
              onClick={clearReviews}
              className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 hover:border-red-200 hover:text-red-600 transition-colors"
            >
              <Trash2 className="w-4 h-4" />
              Clear reviews
            </button>
          )}
        </div>

        {reviews.length === 0 ? (
          <div className="rounded-3xl border border-dashed border-slate-300 bg-white p-8 text-center shadow-xs">
            <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-amber-50 text-amber-700">
              <MessageSquareText className="h-8 w-8" />
            </div>
            <h2 className="mt-5 text-2xl font-bold text-slate-900">No saved reviews yet</h2>
            <p className="mt-3 text-sm text-slate-500 max-w-md mx-auto">
              Share an owner review from a decision results page. Your saved reviews will appear here.
            </p>
            <div className="mt-6 flex justify-center">
              <Button to="/results" variant="primary" className="justify-center">
                Go to results
                <ArrowRight className="w-4 h-4 ml-1.5" />
              </Button>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            {reviews.map((review) => (
              <article key={review.id} className="rounded-2xl border border-slate-200 bg-white p-5 shadow-xs">
                <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
                  <div className="min-w-0">
                    <p className="text-xs font-semibold uppercase tracking-[0.16em] text-slate-500">{review.optionName}</p>
                    <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1">
                      <h2 className="text-lg font-semibold text-slate-900">{review.reviewerName}</h2>
                      <span className="text-xs text-slate-500">
                        {new Date(review.createdAt).toLocaleDateString(undefined, { dateStyle: 'medium' })} · Owner-reported
                      </span>
                    </div>
                    <div className="mt-2 flex items-center gap-0.5 text-amber-500" aria-label={`${review.rating} out of 5 stars`}>
                      {[1, 2, 3, 4, 5].map((star) => (
                        <Star key={star} className={`w-4 h-4 ${star <= review.rating ? 'fill-current' : 'text-slate-200'}`} />
                      ))}
                    </div>
                    <p className="mt-3 text-sm leading-relaxed text-slate-700">{review.reviewText}</p>
                  </div>

                  <button
                    type="button"
                    onClick={() => removeReview(review.id)}
                    aria-label={`Delete review for ${review.optionName}`}
                    title="Delete review"
                    className="inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-slate-200 text-slate-500 hover:border-red-200 hover:bg-red-50 hover:text-red-600 transition-colors"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </article>
            ))}
          </div>
        )}

        <div className="mt-8 flex items-center justify-between">
          <Link to="/" className="text-sm font-medium text-indigo-600 hover:text-indigo-500">Back to home</Link>
          <span role="status" aria-live="polite" className="text-xs text-slate-500">{notice}</span>
        </div>
      </div>
    </div>
  )
}
