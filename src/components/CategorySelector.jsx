import { Check } from 'lucide-react'
import { CATEGORY_LIST, getCategoryConfig } from '../config/categoryConfig'

/**
 * Category selector with visual active states, responsive layout,
 * and dynamic subcategory chips when supported (e.g., Electronics -> Laptop, Smartphone, Smartwatch).
 */
export default function CategorySelector({
  selectedCategory,
  onSelectCategory,
  selectedSubcategory,
  onSelectSubcategory,
}) {
  const currentConfig = getCategoryConfig(selectedCategory, selectedSubcategory)
  const subcategories = currentConfig.subcategories || []

  return (
    <div className="w-full space-y-4">
      <div>
        <div className="flex items-center justify-between mb-3">
          <label className="block text-sm font-semibold text-slate-800">
            What type of decision is this?
          </label>
          <span className="text-xs text-slate-400 font-normal">
            Select one category
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2 sm:gap-2.5">
          {CATEGORY_LIST.map((cat) => {
            const Icon = cat.icon
            const isSelected = selectedCategory.toLowerCase() === cat.id

            return (
              <button
                type="button"
                key={cat.id}
                onClick={() => onSelectCategory(cat.id)}
                className={`flex flex-col items-center justify-center p-3 rounded-xl border text-center transition-all duration-150 cursor-pointer relative ${
                  isSelected
                    ? 'border-indigo-600 bg-indigo-50/70 text-indigo-700 ring-2 ring-indigo-500/20 shadow-xs font-semibold'
                    : 'border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:bg-slate-50'
                }`}
              >
                {isSelected && (
                  <span className="absolute top-1.5 right-1.5 w-4 h-4 rounded-full bg-indigo-600 text-white flex items-center justify-center">
                    <Check className="w-2.5 h-2.5 stroke-[3]" />
                  </span>
                )}
                <div
                  className={`w-8 h-8 rounded-lg flex items-center justify-center mb-1.5 transition-colors ${
                    isSelected
                      ? 'bg-indigo-600 text-white'
                      : 'bg-slate-100 text-slate-500'
                  }`}
                >
                  <Icon className="w-4 h-4" />
                </div>
                <span className="text-xs">{cat.label}</span>
              </button>
            )
          })}
        </div>
      </div>

      {/* Dynamic Subcategory Chips if active category has subcategories */}
      {subcategories.length > 0 && onSelectSubcategory && (
        <div className="pt-3 border-t border-slate-100">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">
              Subcategory
            </span>
            <span className="text-xs text-slate-400">
              Specializes agents & factors
            </span>
          </div>

          <div className="flex flex-wrap gap-2">
            {subcategories.map((sub) => {
              const SubIcon = sub.icon
              const isSubSelected =
                (selectedSubcategory || subcategories[0].id).toLowerCase() === sub.id

              return (
                <button
                  type="button"
                  key={sub.id}
                  onClick={() => onSelectSubcategory(sub.id)}
                  className={`inline-flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-medium border transition-all cursor-pointer ${
                    isSubSelected
                      ? 'border-indigo-600 bg-indigo-600 text-white shadow-xs font-semibold'
                      : 'border-slate-200 bg-slate-50/80 text-slate-700 hover:bg-slate-100 hover:border-slate-300'
                  }`}
                >
                  <SubIcon
                    className={`w-3.5 h-3.5 ${
                      isSubSelected ? 'text-white' : 'text-slate-500'
                    }`}
                  />
                  <span>{sub.label}</span>
                </button>
              )
            })}
          </div>
        </div>
      )}
    </div>
  )
}
