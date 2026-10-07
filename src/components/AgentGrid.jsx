import React from 'react'
import AgentCard from './AgentCard'

/**
 * Responsive grid displaying all 5 autonomous agent cards.
 * Desktop: 5 columns
 * Tablet: 2 columns
 * Mobile: 1 column
 */
export default function AgentGrid({ agents, onInspect, canInspect }) {
  return (
    <div className="w-full mb-10">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        {agents.map((agent) => (
          <AgentCard
            key={agent.id}
            agent={agent}
            onInspect={onInspect}
            canInspect={canInspect}
          />
        ))}
      </div>
    </div>
  )
}
