import React from 'react'
import { Check } from 'lucide-react'

/**
 * Visual Progress Indicator for the 5-step Decision Arena flow.
 * Steps: 01 Define, 02 Requirements, 03 Priorities, 04 AI Battle, 05 Result
 */
export default function ProgressSteps({ currentStep = 1 }) {
  const steps = [
    { number: '01', title: 'Define', id: 1 },
    { number: '02', title: 'Requirements', id: 2 },
    { number: '03', title: 'Priorities', id: 3 },
    { number: '04', title: 'AI Battle', id: 4 },
    { number: '05', title: 'Result', id: 5 },
  ]

  return (
    <div className="w-full max-w-3xl mx-auto mb-10 px-2 sm:px-4">
      {/* Step items container */}
      <div className="flex items-center justify-between relative">
        {/* Continuous connector line behind circles */}
        <div className="absolute top-4 left-6 right-6 h-0.5 bg-slate-200 -z-0 hidden sm:block" />

        {steps.map((step, idx) => {
          const isActive = step.id === currentStep
          const isCompleted = step.id < currentStep
          const isUpcoming = step.id > currentStep

          return (
            <div
              key={step.id}
              className="flex flex-col items-center relative z-10 text-center flex-1"
            >
              <div
                className={`w-8 h-8 sm:w-9 sm:h-9 rounded-full flex items-center justify-center text-xs font-bold transition-all duration-200 ${
                  isActive
                    ? 'bg-indigo-600 text-white shadow-md shadow-indigo-500/25 ring-4 ring-indigo-50 scale-105'
                    : isCompleted
                    ? 'bg-emerald-600 text-white'
                    : 'bg-white border-2 border-slate-200 text-slate-400'
                }`}
              >
                {isCompleted ? (
                  <Check className="w-4 h-4 stroke-[3]" />
                ) : (
                  <span>{step.number}</span>
                )}
              </div>

              <span
                className={`mt-2 text-xs font-medium tracking-tight transition-colors hidden sm:block ${
                  isActive
                    ? 'text-indigo-600 font-bold'
                    : isCompleted
                    ? 'text-slate-700'
                    : 'text-slate-400'
                }`}
              >
                {step.title}
              </span>
            </div>
          )
        })}
      </div>

      {/* Mobile Current Step Label */}
      <div className="mt-3 text-center sm:hidden">
        <span className="text-xs font-semibold text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100">
          Step {steps[currentStep - 1]?.number}: {steps[currentStep - 1]?.title}
        </span>
      </div>
    </div>
  )
}
