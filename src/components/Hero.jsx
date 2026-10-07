import React from 'react'
import { ArrowRight, Sparkles } from 'lucide-react'
import Button from './Button'

/**
 * Hero section with clear headline, dual CTAs, and trust statement.
 */
export default function Hero() {
  const scrollToHowItWorks = (e) => {
    e.preventDefault()
    const element = document.getElementById('how-it-works')
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <section className="pt-16 pb-12 sm:pt-24 sm:pb-16 text-center px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto">
      {/* Category pill */}
      <div className="inline-flex items-center gap-2 px-3.5 py-1.5 mb-8 rounded-full bg-indigo-50/80 border border-indigo-100 text-indigo-700 text-xs sm:text-sm font-medium shadow-xs">
        <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
        <span>Multi-Agent Consensus Platform</span>
      </div>

      {/* Large headline */}
      <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-slate-900 leading-[1.15] mb-6">
        Make Better Decisions.{' '}
        <span className="block mt-1 sm:inline">
          Let{' '}
          <span className="bg-gradient-to-r from-indigo-600 via-indigo-700 to-violet-600 bg-clip-text text-transparent underline decoration-indigo-200 decoration-wavy decoration-from-font underline-offset-8">
            AI Debate
          </span>{' '}
          the Options.
        </span>
      </h1>

      {/* Subtitle */}
      <p className="max-w-2xl mx-auto text-lg sm:text-xl text-slate-600 leading-relaxed font-normal mb-10">
        Bring multiple AI experts together, compare their perspectives, and get a transparent recommendation based on what matters most to you.
      </p>

      {/* Primary & Secondary Buttons */}
      <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-10">
        <Button to="/create" variant="primary" className="w-full sm:w-auto px-7 py-3.5 text-base">
          Start a Decision
          <ArrowRight className="w-4 h-4 ml-2" />
        </Button>
        <Button
          onClick={scrollToHowItWorks}
          variant="secondary"
          className="w-full sm:w-auto px-6 py-3.5 text-base"
        >
          See How It Works
        </Button>
      </div>

      {/* Trust statement */}
      <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-3 text-xs sm:text-sm font-medium text-slate-500">
        <span>Multiple perspectives</span>
        <span className="text-slate-300">•</span>
        <span>Weighted analysis</span>
        <span className="text-slate-300">•</span>
        <span>Explainable results</span>
      </div>
    </section>
  )
}
