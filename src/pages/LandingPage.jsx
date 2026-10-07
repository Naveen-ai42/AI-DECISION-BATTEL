import React from 'react'
import Hero from '../components/Hero'
import AgentNetwork from '../components/AgentNetwork'
import HowItWorks from '../components/HowItWorks'
import FeatureSection from '../components/FeatureSection'
import ExampleDecision from '../components/ExampleDecision'
import FinalCTA from '../components/FinalCTA'

/**
 * Complete Decision Arena Landing Page assembly.
 */
export default function LandingPage() {
  return (
    <div className="flex flex-col w-full">
      <Hero />
      <AgentNetwork />
      <HowItWorks />
      <FeatureSection />
      <ExampleDecision />
      <FinalCTA />
    </div>
  )
}
