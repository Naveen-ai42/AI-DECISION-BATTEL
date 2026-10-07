import { useState } from 'react'
import { MessageSquareText, Send, Star } from 'lucide-react'
import { readSavedReviews, writeSavedReviews } from '../utils/userReviews'

function getOptionId(option, index) {
  return String(option.id || option.name || index)
}

export default function ProductReviews({ rankings = [], winnerName = '' }) {
  const initialOption = rankings.find((option) => option.name === winnerName) || rankings[0]
  const [reviews, setReviews] = useState(readSavedReviews)
  const [selectedOptionId, setSelectedOptionId] = useState(
    initialOption ? getOptionId(initialOption, 0) : ''
  )
  const [rating, setRating] = useState(0)
  const [hoveredRating, setHoveredRating] = useState(0)
  const [reviewerName, setReviewerName] = useState('')
  const [reviewText, setReviewText] = useState('')
  const [hasUsedOption, setHasUsedOption] = useState(false)
  const [notice, setNotice] = useState('')

  const selectedOption = rankings.find((option, index) => (
    getOptionId(option, index) === selectedOptionId
  )) || initialOption
  const selectedOptionIndex = rankings.indexOf(selectedOption)
  const selectedId = selectedOption ? getOptionId(selectedOption, selectedOptionIndex) : ''
  const visibleReviews = reviews.filter((review) => review.optionId === selectedId)
  const averageRating = visibleReviews.length
    ? visibleReviews.reduce((total, review) => total + review.rating, 0) / visibleReviews.length
    : 0

  const handleSubmit = (event) => {
    event.preventDefault()
    if (!selectedOption || rating < 1 || !hasUsedOption || !reviewText.trim()) return

    const review = {
      id: `${Date.now()}-${Math.random().toString(36).slice(2)}`,
      optionId: selectedId,
      optionName: selectedOption.name,
      reviewerName: reviewerName.trim() || 'Guest owner',
      rating,
      reviewText: reviewText.trim(),
      createdAt: new Date().toISOString(),
    }
    const updatedReviews = [review, ...reviews].slice(0, 100)

    try {
      writeSavedReviews(updatedReviews)
      setReviews(updatedReviews)
      setRating(0)
      setReviewerName('')
      setReviewText('')
      setHasUsedOption(false)
      setNotice('Your review was saved on this device.')
    } catch {
      setNotice('This browser could not save the review.')
    }
  }

  if (!selectedOption) return null

  return (
    <section className="w-full bg-white border border-slate-200/90 rounded-2xl p-5 sm:p-7 shadow-xs mb-10" aria-labelledby="product-reviews-title">
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4 mb-6">
        <div>
          <div className="inline-flex items-center gap-2 text-amber-700 text-xs font-bold uppercase tracking-wider mb-2">
            <MessageSquareText className="w-4 h-4" />
            Owner reviews
          </div>
          <h3 id="product-reviews-title" className="text-xl sm:text-2xl font-bold text-slate-900">
            Advice from people who have used it
          </h3>
          <p className="text-sm text-slate-500 mt-1">
            Reviews are self-reported and saved only in this browser. They are not independently verified or shared with other users.
          </p>
        </div>
        <label className="w-full sm:w-64 text-sm font-semibold text-slate-700">
          Choose an option
          <select
            value={selectedOptionId}
            onChange={(event) => setSelectedOptionId(event.target.value)}
            className="mt-1.5 w-full rounded-lg border border-slate-300 bg-white px-3 py-2.5 text-sm font-normal text-slate-800 focus:border-amber-500 focus:outline-none focus:ring-2 focus:ring-amber-100"
          >
            {rankings.map((option, index) => (
              <option key={getOptionId(option, index)} value={getOptionId(option, index)}>
                {option.name}
              </option>
            ))}
          </select>
        </label>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-[minmax(0,1fr)_minmax(280px,0.9fr)] gap-7">
        <div>
          <div className="flex items-center gap-3 pb-4 border-b border-slate-100">
            <span className="text-3xl font-bold text-slate-900">
              {visibleReviews.length ? averageRating.toFixed(1) : '--'}
            </span>
            <div>
              <div className="flex items-center gap-0.5 text-amber-500" aria-label={visibleReviews.length ? `${averageRating.toFixed(1)} out of 5 stars` : 'No ratings yet'}>
                {[1, 2, 3, 4, 5].map((star) => (
                  <Star key={star} className={`w-4 h-4 ${star <= Math.round(averageRating) ? 'fill-current' : 'text-slate-200'}`} />
                ))}
              </div>
              <p className="text-xs text-slate-500 mt-1">
                {visibleReviews.length} {visibleReviews.length === 1 ? 'review' : 'reviews'} saved here
              </p>
            </div>
          </div>

          {visibleReviews.length ? (
            <div className="divide-y divide-slate-100">
              {visibleReviews.map((review) => (
                <article key={review.id} className="py-4">
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="text-sm font-semibold text-slate-900">{review.reviewerName}</p>
                      <p className="text-xs text-slate-500 mt-0.5">
                        {new Date(review.createdAt).toLocaleDateString()} · Owner-reported
                      </p>
                    </div>
                    <div className="flex items-center gap-0.5 text-amber-500" aria-label={`${review.rating} out of 5 stars`}>
                      {[1, 2, 3, 4, 5].map((star) => (
                        <Star key={star} className={`w-3.5 h-3.5 ${star <= review.rating ? 'fill-current' : 'text-slate-200'}`} />
                      ))}
                    </div>
                  </div>
                  <p className="text-sm text-slate-700 leading-relaxed mt-2">{review.reviewText}</p>
                </article>
              ))}
            </div>
          ) : (
            <p className="py-5 text-sm text-slate-500">
              No owner reviews for {selectedOption.name} have been saved in this browser yet.
            </p>
          )}
        </div>

        <form onSubmit={handleSubmit} className="border-t lg:border-t-0 lg:border-l border-slate-200 pt-6 lg:pt-0 lg:pl-7">
          <h4 className="text-base font-bold text-slate-900">Share your experience</h4>
          <p className="text-xs text-slate-500 mt-1 mb-4">A short, specific review helps someone compare their options.</p>

          <fieldset>
            <legend className="text-sm font-semibold text-slate-700">Your rating</legend>
            <div className="flex items-center gap-1 mt-2" onMouseLeave={() => setHoveredRating(0)}>
              {[1, 2, 3, 4, 5].map((star) => {
                const active = star <= (hoveredRating || rating)
                return (
                  <button
                    key={star}
                    type="button"
                    aria-label={`${star} ${star === 1 ? 'star' : 'stars'}`}
                    aria-pressed={rating === star}
                    onMouseEnter={() => setHoveredRating(star)}
                    onFocus={() => setHoveredRating(star)}
                    onBlur={() => setHoveredRating(0)}
                    onClick={() => setRating(star)}
                    className="p-1 text-amber-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-amber-500 rounded"
                  >
                    <Star className={`w-6 h-6 ${active ? 'fill-current' : 'text-slate-300'}`} />
                  </button>
                )
              })}
            </div>
          </fieldset>

          <label className="block text-sm font-semibold text-slate-700 mt-4">
            Review
            <textarea
              value={reviewText}
              onChange={(event) => setReviewText(event.target.value)}
              maxLength={800}
              required
              rows={4}
              placeholder="What worked well? What should another buyer know?"
              className="mt-1.5 w-full resize-y rounded-lg border border-slate-300 px-3 py-2.5 text-sm font-normal text-slate-800 placeholder:text-slate-400 focus:border-amber-500 focus:outline-none focus:ring-2 focus:ring-amber-100"
            />
          </label>

          <label className="block text-sm font-semibold text-slate-700 mt-3">
            Display name <span className="font-normal text-slate-400">(optional)</span>
            <input
              value={reviewerName}
              onChange={(event) => setReviewerName(event.target.value)}
              maxLength={40}
              placeholder="Guest owner"
              className="mt-1.5 w-full rounded-lg border border-slate-300 px-3 py-2.5 text-sm font-normal text-slate-800 placeholder:text-slate-400 focus:border-amber-500 focus:outline-none focus:ring-2 focus:ring-amber-100"
            />
          </label>

          <label className="flex items-start gap-2.5 mt-4 text-sm text-slate-700">
            <input
              type="checkbox"
              checked={hasUsedOption}
              onChange={(event) => setHasUsedOption(event.target.checked)}
              required
              className="mt-0.5 h-4 w-4 rounded border-slate-300 accent-amber-600"
            />
            <span>I have personally used this option.</span>
          </label>

          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mt-4">
            <button
              type="submit"
              disabled={!rating || !hasUsedOption || !reviewText.trim()}
              className="inline-flex items-center justify-center gap-2 rounded-lg bg-slate-900 px-4 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-slate-700 disabled:cursor-not-allowed disabled:bg-slate-300"
            >
              <Send className="w-4 h-4" />
              Save review
            </button>
            <span role="status" aria-live="polite" className="text-xs text-slate-500">{notice}</span>
          </div>
        </form>
      </div>
    </section>
  )
}
