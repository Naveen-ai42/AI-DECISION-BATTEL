import React from 'react'
import { Target, Users2, Scale } from 'lucide-react'

/**
 * How It Works section featuring 3 clean numbered steps.
 */
export default function HowItWorks() {
  const steps = [
    {
      number: '01',
      title: 'Define',
      description: "Tell Decision Arena what you're trying to decide.",
      icon: Target,
      highlight: 'Set requirements & goals',
    },
    {
      number: '02',
      title: 'Debate',
      description: 'Specialized AI agents analyze your decision from different perspectives.',
      icon: Users2,
      highlight: 'Unbiased multi-agent review',
    },
    {
      number: '03',
      title: 'Decide',
      description: 'A weighted decision engine combines the results and explains the recommendation.',
      icon: Scale,
      highlight: 'Clear, explainable winner',
    },
  ]

  return (
    <section id="how-it-works" className="py-20 sm:py-28 bg-white border-y border-slate-200/70">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="text-xs font-semibold tracking-wider uppercase text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100">
            Process
          </span>
          <h2 className="text-3xl sm:text-4xl font-bold text-slate-900 mt-4 tracking-tight">
            One decision. Multiple perspectives.
          </h2>
          <p className="text-base sm:text-lg text-slate-600 mt-3 font-normal leading-relaxed">
            Decision Arena breaks complex choices into clear, understandable steps.
          </p>
        </div>

        {/* 3 Step Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {steps.map((step) => {
            const Icon = step.icon
            return (
              <div
                key={step.number}
                className="relative bg-slate-50/70 border border-slate-200/80 rounded-2xl p-8 hover:bg-white hover:border-indigo-200 hover:shadow-md transition-all duration-200 group flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-6">
                    <span className="text-3xl font-extrabold text-slate-300 group-hover:text-indigo-600 transition-colors font-mono">
                      {step.number}
                    </span>
                    <div className="w-10 h-10 rounded-xl bg-white border border-slate-200 group-hover:border-indigo-100 group-hover:bg-indigo-50 flex items-center justify-center text-slate-600 group-hover:text-indigo-600 transition-colors shadow-xs">
                      <Icon className="w-5 h-5" />
                    </div>
                  </div>

                  <h3 className="text-xl font-bold text-slate-900 mb-2">
                    {step.title}
                  </h3>
                  <p className="text-sm text-slate-600 leading-relaxed font-normal">
                    {step.description}
                  </p>
                </div>

                <div className="mt-8 pt-4 border-t border-slate-200/60 text-xs font-medium text-slate-500">
                  {step.highlight}
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </section>
  )
}
