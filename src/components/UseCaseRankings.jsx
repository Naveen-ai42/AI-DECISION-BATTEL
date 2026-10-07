import { useState } from 'react'
import {
  BatteryCharging,
  Camera,
  Laptop,
  Monitor,
  ShieldAlert,
  ShieldCheck,
  Tag,
  Target,
  Wrench,
  Zap,
} from 'lucide-react'

const USE_CASES = {
  smartphone: [
    { id: 'camera', label: 'Camera', factor: 'camera', icon: Camera },
    { id: 'gaming', label: 'Gaming', factor: 'performance', icon: Zap },
    { id: 'battery', label: 'Battery', factor: 'battery', icon: BatteryCharging },
    { id: 'value', label: 'Value', factor: 'value', icon: Tag },
    { id: 'build', label: 'Build', factor: 'build', icon: Laptop },
  ],
  laptop: [
    { id: 'performance', label: 'Performance', factor: 'performance', icon: Zap },
    { id: 'battery', label: 'Battery', factor: 'battery', icon: BatteryCharging },
    { id: 'display', label: 'Display', factor: 'display', icon: Monitor },
    { id: 'upgradeability', label: 'Upgradeability', factor: 'upgradeability', icon: Wrench },
    { id: 'value', label: 'Value', factor: 'value', icon: Tag },
  ],
}

const FACTOR_ICONS = {
  safety: ShieldCheck,
  risk: ShieldAlert,
  durability: ShieldCheck,
  stability: ShieldCheck,
  healthFitness: Zap,
  soundQuality: Camera,
  noiseCancellation: ShieldCheck,
  camera: Camera,
  performance: Zap,
  battery: BatteryCharging,
  display: Monitor,
  upgradeability: Wrench,
  value: Tag,
  price: Tag,
}

function getFactorScore(item, factor) {
  return Number(item.factorScores?.[factor] ?? item.attributes?.[factor] ?? 0)
}

export default function UseCaseRankings({
  rankings = [],
  productType = 'generic',
  factorDefinitions = [],
  itemLabel = 'Option',
}) {
  const useCases = USE_CASES[productType] || factorDefinitions.map((factor) => ({
    id: factor.key,
    label: factor.name || factor.key,
    factor: factor.key,
    icon: FACTOR_ICONS[factor.key] || Target,
  }))
  const productLabel = productType === 'laptop'
    ? 'Laptop'
    : productType === 'smartphone'
      ? 'Phone'
      : itemLabel
  const sectionTitle = productType === 'generic'
    ? `${productLabel} options ranked by factor`
    : `${productLabel} leaders by use case`
  const [activeUseCaseId, setActiveUseCaseId] = useState(useCases[0]?.id || '')
  const activeUseCase = useCases.find((useCase) => useCase.id === activeUseCaseId) || useCases[0]

  if (rankings.length === 0 || !activeUseCase) return null

  const sortedItems = [...rankings].sort((first, second) => (
    getFactorScore(second, activeUseCase.factor) - getFactorScore(first, activeUseCase.factor) ||
    Number(second.score || 0) - Number(first.score || 0)
  ))
  const leader = sortedItems[0]

  return (
    <section className="w-full bg-white border border-slate-200/90 rounded-2xl p-5 sm:p-7 shadow-xs mb-10" aria-labelledby="use-case-rankings-title">
      <div className="mb-5">
        <p className="text-xs font-bold uppercase tracking-wider text-indigo-700 mb-2">{productLabel} comparison</p>
        <h3 id="use-case-rankings-title" className="text-xl sm:text-2xl font-bold text-slate-900">
          {sectionTitle}
        </h3>
      </div>

      <div role="tablist" aria-label={`Rank ${productLabel.toLowerCase()} options by factor`} className="flex gap-2 overflow-x-auto pb-3">
        {useCases.map((useCase) => {
          const Icon = useCase.icon
          const isActive = useCase.id === activeUseCaseId
          return (
            <button
              key={useCase.id}
              type="button"
              role="tab"
              aria-selected={isActive}
              onClick={() => setActiveUseCaseId(useCase.id)}
              className={`inline-flex shrink-0 items-center gap-2 rounded-lg border px-3.5 py-2 text-sm font-semibold transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 ${
                isActive
                  ? 'border-indigo-600 bg-indigo-600 text-white'
                  : 'border-slate-200 bg-white text-slate-700 hover:bg-slate-50'
              }`}
            >
              <Icon className="w-4 h-4" />
              {useCase.label}
            </button>
          )
        })}
      </div>

      <div role="tabpanel" className="border-t border-slate-200 pt-4">
        <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-2 mb-4">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">Top {activeUseCase.label} pick</p>
            <h4 className="text-lg font-bold text-slate-900 mt-1">{leader.name}</h4>
          </div>
          <div className="text-sm text-slate-600">
            {Math.round(getFactorScore(leader, activeUseCase.factor))} / 100 in {activeUseCase.label.toLowerCase()}
            {leader.price ? ` · ${leader.price}` : ''}
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full min-w-[560px] text-left text-sm">
            <thead>
              <tr className="border-y border-slate-200 bg-slate-50 text-xs font-bold uppercase text-slate-500">
                <th className="px-3 py-2.5">Factor rank</th>
                <th className="px-3 py-2.5">{productLabel}</th>
                <th className="px-3 py-2.5">{activeUseCase.label}</th>
                <th className="px-3 py-2.5">Overall</th>
                <th className="px-3 py-2.5">Price</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {sortedItems.map((item, index) => (
                <tr key={item.id} className={index === 0 ? 'bg-emerald-50/60' : 'hover:bg-slate-50/70'}>
                  <td className="px-3 py-2.5 font-semibold text-slate-600">#{index + 1}</td>
                  <td className="px-3 py-2.5 font-semibold text-slate-900">{item.name}</td>
                  <td className="px-3 py-2.5 font-bold text-slate-800">{Math.round(getFactorScore(item, activeUseCase.factor))}</td>
                  <td className="px-3 py-2.5 text-slate-600">{Number(item.score || 0).toFixed(1)}</td>
                  <td className="px-3 py-2.5 text-slate-600">{item.price || 'Not listed'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  )
}