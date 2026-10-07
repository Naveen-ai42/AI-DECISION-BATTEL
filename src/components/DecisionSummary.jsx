import React from 'react'
import {
  Laptop,
  Briefcase,
  GraduationCap,
  Landmark,
  Plane,
  ShoppingBag,
  MoreHorizontal,
  HelpCircle
} from 'lucide-react'

const CATEGORY_MAP = {
  electronics: { label: 'Electronics', icon: Laptop },
  career: { label: 'Career', icon: Briefcase },
  education: { label: 'Education', icon: GraduationCap },
  finance: { label: 'Finance', icon: Landmark },
  travel: { label: 'Travel', icon: Plane },
  shopping: { label: 'Shopping', icon: ShoppingBag },
  other: { label: 'Other', icon: MoreHorizontal },
}

/**
 * Summary card displaying the decision context defined in Step 1.
 */
export default function DecisionSummary({ decision }) {
  const catKey = (decision?.category || 'electronics').toLowerCase()
  const catInfo = CATEGORY_MAP[catKey] || { label: decision?.category || 'General', icon: HelpCircle }
  const CategoryIcon = catInfo.icon

  const displayText =
    decision?.description?.trim() ||
    'General decision evaluation context.'

  return (
    <div className="bg-white border border-slate-200/90 rounded-2xl p-5 sm:p-6 shadow-xs mb-8">
      <div className="flex items-center justify-between gap-3 mb-2.5">
        <span className="text-xs font-bold tracking-wider uppercase text-slate-400">
          Your Decision
        </span>
        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-indigo-50 border border-indigo-100/80 text-indigo-700 text-xs font-semibold">
          <CategoryIcon className="w-3.5 h-3.5" />
          <span>{catInfo.label}</span>
        </div>
      </div>

      <p className="text-base sm:text-lg font-semibold text-slate-900 leading-snug">
        &ldquo;{displayText}&rdquo;
      </p>

      {/* Optional Metadata Chips if provided */}
      {(decision?.budget || decision?.location || decision?.deadline) && (
        <div className="flex flex-wrap items-center gap-2 mt-3 pt-3 border-t border-slate-100 text-xs text-slate-500">
          {decision.budget && (
            <span className="bg-slate-100 px-2.5 py-0.5 rounded-md font-medium text-slate-700">
              Budget: ₹{decision.budget}
            </span>
          )}
          {decision.location && (
            <span className="bg-slate-100 px-2.5 py-0.5 rounded-md font-medium text-slate-700">
              Location: {decision.location}
            </span>
          )}
          {decision.deadline && (
            <span className="bg-slate-100 px-2.5 py-0.5 rounded-md font-medium text-slate-700">
              Deadline: {decision.deadline}
            </span>
          )}
        </div>
      )}
    </div>
  )
}
