import { Award, Sparkles, CheckCircle2 } from 'lucide-react'
import ScoreIndicator from './ScoreIndicator'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Large premium recommendation card featuring the winning option and dynamic score ring.
 */
export default function WinnerCard({ winnerName, overallScore = 91, category = 'electronics', subcategory = '' }) {
  const categoryConfig = getCategoryConfig(category, subcategory)
  const finalWinner = winnerName || categoryConfig.defaultRecommendation

  return (
    <div className="w-full bg-gradient-to-br from-indigo-50/70 via-white to-emerald-50/50 border-2 border-indigo-200/90 rounded-3xl p-6 sm:p-10 shadow-sm mb-10 relative overflow-hidden">
      {/* Decorative ambient background blur */}
      <div className="absolute top-0 right-0 w-80 h-80 bg-indigo-100/40 rounded-full blur-3xl pointer-events-none -z-0" />

      <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-8">
        {/* Left: Recommendation Details */}
        <div className="max-w-xl">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-600 text-white text-xs font-bold uppercase tracking-wider mb-3 shadow-xs">
            <Award className="w-3.5 h-3.5" />
            <span>Recommended Choice</span>
          </div>

          <h2 className="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-2">
            {finalWinner}
          </h2>

          <p className="text-sm sm:text-base text-slate-600 leading-relaxed mb-4">
            Highest overall synthesis based on your requirements, negative constraints, and calibrated priority weights.
          </p>

          <div className="flex flex-wrap items-center gap-2 text-xs">
            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-emerald-100/90 text-emerald-800 font-semibold">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
              <span>Overall Match</span>
            </span>
            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-700 font-semibold shadow-2xs">
              <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
              <span>Strong Match</span>
            </span>
          </div>
        </div>

        {/* Right: Circular Score Indicator */}
        <div className="bg-white/90 border border-slate-200/90 rounded-2xl p-6 shadow-xs flex flex-col items-center justify-center self-center md:self-auto min-w-[210px] text-center">
          <ScoreIndicator score={overallScore} size={116} strokeWidth={9} />

          <div className="mt-3 text-center">
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block">
              Synthesized Score
            </span>
            <span className="text-xs font-semibold text-emerald-700 mt-0.5 block">
              {overallScore >= 90 ? 'Consensus Winner' : 'Top Viable Match'}
            </span>
          </div>
        </div>
      </div>
    </div>
  )
}
