import React from 'react'
import ProgressSteps from '../components/ProgressSteps'
import DecisionForm from '../components/DecisionForm'

/**
 * Step 1 of the Decision Wizard: Define your decision.
 */
export default function CreatePage() {
  return (
    <div className="flex-1 w-full py-10 sm:py-14 px-4 sm:px-6 lg:px-8">
      <div className="max-w-[900px] mx-auto">
        {/* Progress Indicator */}
        <ProgressSteps currentStep={1} />

        {/* Heading & Subtitle */}
        <div className="text-center max-w-2xl mx-auto mb-10">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-3">
            What are you deciding?
          </h1>
          <p className="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
            Tell us what you&apos;re trying to decide. We&apos;ll bring the right AI perspectives into the discussion.
          </p>
        </div>

        {/* Decision Input Form */}
        <DecisionForm />
      </div>
    </div>
  )
}
