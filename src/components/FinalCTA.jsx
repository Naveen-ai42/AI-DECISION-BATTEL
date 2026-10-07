import React from 'react'
import { ArrowRight, Sparkles } from 'lucide-react'
import Button from './Button'

/**
 * Clean, high-impact final call-to-action section.
 */
export default function FinalCTA() {
  return (
    <section className="py-20 sm:py-28 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto">
      <div className="bg-gradient-to-br from-indigo-50/70 via-white to-violet-50/70 border border-indigo-100/80 rounded-3xl p-8 sm:p-14 text-center shadow-xs relative overflow-hidden">
        {/* Subtle decorative glow */}
        <div className="absolute top-0 right-1/4 w-64 h-64 bg-indigo-200/20 rounded-full blur-2xl pointer-events-none" />

        <div className="relative z-10 max-w-2xl mx-auto">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white border border-indigo-100 text-indigo-700 text-xs font-semibold shadow-2xs mb-6">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Ready to Decide?</span>
          </div>

          <h2 className="text-3xl sm:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
            Your next decision deserves more than one opinion.
          </h2>

          <p className="text-base sm:text-lg text-slate-600 mb-8 font-normal leading-relaxed">
            Let AI analyze the options. You make the final call.
          </p>

          <div className="flex justify-center">
            <Button
              to="/create"
              variant="primary"
              className="px-8 py-3.5 text-base sm:text-lg shadow-md hover:shadow-lg"
            >
              Start Your First Decision
              <ArrowRight className="w-5 h-5 ml-2" />
            </Button>
          </div>
        </div>
      </div>
    </section>
  )
}
