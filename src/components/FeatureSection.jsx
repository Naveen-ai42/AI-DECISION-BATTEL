import React from 'react'
import {
  Users,
  Sliders,
  BarChart3,
  FileCheck,
  GitCompare,
  History
} from 'lucide-react'

/**
 * FeatureSection featuring a compact, elegant 2-column layout.
 */
export default function FeatureSection() {
  const features = [
    {
      title: 'Multi-Agent Analysis',
      description: 'Different AI agents evaluate different aspects of your decision.',
      icon: Users,
    },
    {
      title: 'Custom Priorities',
      description: 'Tell the system what matters most to you using adjustable weights.',
      icon: Sliders,
    },
    {
      title: 'Transparent Scoring',
      description: 'See exactly how each option performed.',
      icon: BarChart3,
    },
    {
      title: 'Explainable Results',
      description: 'Understand why the final recommendation won.',
      icon: FileCheck,
    },
    {
      title: 'Agent Disagreement',
      description: 'See where different AI perspectives disagree.',
      icon: GitCompare,
    },
    {
      title: 'Decision History',
      description: 'Save and revisit previous decisions.',
      icon: History,
    },
  ]

  return (
    <section id="features" className="py-20 sm:py-28 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      {/* Header */}
      <div className="text-center max-w-2xl mx-auto mb-16">
        <span className="text-xs font-semibold tracking-wider uppercase text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100">
          Capabilities
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold text-slate-900 mt-4 tracking-tight">
          Built for decisions that actually matter.
        </h2>
        <p className="text-base text-slate-600 mt-3 font-normal">
          A methodical decision framework designed for clarity and confidence.
        </p>
      </div>

      {/* 2-Column Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {features.map((feature) => {
          const Icon = feature.icon
          return (
            <div
              key={feature.title}
              className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:border-slate-300 hover:shadow-sm transition-all duration-200 flex items-start gap-4"
            >
              <div className="flex-shrink-0 w-11 h-11 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center border border-indigo-100/80">
                <Icon className="w-5 h-5 stroke-[2]" />
              </div>
              <div>
                <h3 className="text-base font-semibold text-slate-900 mb-1">
                  {feature.title}
                </h3>
                <p className="text-sm text-slate-600 leading-relaxed font-normal">
                  {feature.description}
                </p>
              </div>
            </div>
          )
        })}
      </div>
    </section>
  )
}
