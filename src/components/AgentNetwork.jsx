import React from 'react'
import {
  Zap,
  Tag,
  BatteryCharging,
  Sparkles,
  TrendingUp,
  Cpu,
  CheckCircle2,
  HelpCircle,
  ArrowDown
} from 'lucide-react'

/**
 * Clean AI System Diagram showing:
 * 5 AI Agents -> Your Decision -> Decision Engine -> Final Recommendation
 */
export default function AgentNetwork() {
  const agents = [
    { name: 'Core Fit', icon: Zap, color: 'text-indigo-600', bg: 'bg-indigo-50', border: 'border-indigo-200' },
    { name: 'Value & ROI', icon: Tag, color: 'text-emerald-600', bg: 'bg-emerald-50', border: 'border-emerald-200' },
    { name: 'Risk & Endurance', icon: BatteryCharging, color: 'text-blue-600', bg: 'bg-blue-50', border: 'border-blue-200' },
    { name: 'Experience', icon: Sparkles, color: 'text-violet-600', bg: 'bg-violet-50', border: 'border-violet-200' },
    { name: 'Future Growth', icon: TrendingUp, color: 'text-amber-600', bg: 'bg-amber-50', border: 'border-amber-200' },
  ]

  return (
    <div className="w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
      <div className="bg-white/70 backdrop-blur-sm border border-slate-200/90 rounded-3xl p-6 sm:p-10 shadow-sm relative overflow-hidden">
        {/* Subtle decorative background gradient circles */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-indigo-50/50 rounded-full blur-3xl pointer-events-none -z-10" />

        <div className="text-center mb-8">
          <span className="text-xs font-semibold tracking-wider uppercase text-slate-400">
            System Architecture
          </span>
          <h2 className="text-lg sm:text-xl font-semibold text-slate-800 mt-1">
            Autonomous Multi-Agent Consensus Flow
          </h2>
        </div>

        {/* 1. AGENTS LAYER */}
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 sm:gap-4 max-w-4xl mx-auto mb-6">
          {agents.map((agent) => {
            const Icon = agent.icon
            return (
              <div
                key={agent.name}
                className="bg-white border border-slate-200 rounded-2xl p-3 sm:p-4 text-center shadow-xs hover:border-slate-300 hover:shadow-sm transition-all duration-200 flex flex-col items-center group"
              >
                <div
                  className={`w-9 h-9 sm:w-10 sm:h-10 rounded-xl ${agent.bg} ${agent.color} flex items-center justify-center mb-2 transition-transform duration-200 group-hover:scale-105`}
                >
                  <Icon className="w-4 h-4 sm:w-5 sm:h-5" />
                </div>
                <div className="text-xs sm:text-sm font-semibold text-slate-800">
                  {agent.name}
                </div>
                <span className="text-[11px] text-slate-400 mt-0.5">Specialist</span>
              </div>
            )
          })}
        </div>

        {/* Subtle Convergence SVG (Desktop) */}
        <div className="hidden sm:block w-full max-w-3xl mx-auto h-12 mb-2">
          <svg className="w-full h-full" viewBox="0 0 600 48" fill="none">
            {/* Connecting lines towards center */}
            <path d="M 60 4 Q 180 30 300 44" stroke="#CBD5E1" strokeWidth="1.5" strokeDasharray="4 4" className="animate-dash-flow" />
            <path d="M 180 4 Q 240 24 300 44" stroke="#CBD5E1" strokeWidth="1.5" strokeDasharray="4 4" className="animate-dash-flow" />
            <path d="M 300 4 L 300 44" stroke="#818CF8" strokeWidth="2" strokeDasharray="4 4" className="animate-dash-flow" />
            <path d="M 420 4 Q 360 24 300 44" stroke="#CBD5E1" strokeWidth="1.5" strokeDasharray="4 4" className="animate-dash-flow" />
            <path d="M 540 4 Q 420 30 300 44" stroke="#CBD5E1" strokeWidth="1.5" strokeDasharray="4 4" className="animate-dash-flow" />
          </svg>
        </div>

        {/* Mobile Connector Arrow */}
        <div className="flex sm:hidden justify-center my-3 text-slate-400">
          <ArrowDown className="w-4 h-4" />
        </div>

        {/* 2. CENTER NODE: "Your Decision" */}
        <div className="flex justify-center mb-6">
          <div className="relative group">
            <div className="w-full sm:w-80 bg-white border-2 border-indigo-500/40 rounded-2xl p-4 sm:p-5 text-center shadow-md animate-pulse-subtle">
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 text-[11px] font-semibold mb-2">
                <HelpCircle className="w-3 h-3 text-indigo-600" />
                <span>Central Focal Point</span>
              </div>
              <h3 className="text-base sm:text-lg font-bold text-slate-900">
                Your Decision
              </h3>
              <p className="text-xs text-slate-500 mt-1">
                Unified arena evaluating all perspectives
              </p>
            </div>
          </div>
        </div>

        {/* Vertical Flow to Decision Engine */}
        <div className="flex justify-center my-2 text-indigo-400">
          <ArrowDown className="w-5 h-5 animate-bounce" />
        </div>

        {/* 3. DECISION ENGINE NODE */}
        <div className="flex justify-center mb-6">
          <div className="w-full sm:w-72 bg-slate-900 text-white rounded-2xl p-4 text-center shadow-sm flex items-center justify-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-indigo-500/20 text-indigo-400 flex items-center justify-center border border-indigo-400/30">
              <Cpu className="w-5 h-5" />
            </div>
            <div className="text-left">
              <div className="text-xs uppercase font-medium text-indigo-300 tracking-wider">
                Processing
              </div>
              <div className="text-sm font-semibold text-white">
                Decision Engine
              </div>
            </div>
          </div>
        </div>

        {/* Vertical Flow to Recommendation */}
        <div className="flex justify-center my-2 text-slate-400">
          <ArrowDown className="w-5 h-5" />
        </div>

        {/* 4. FINAL RECOMMENDATION NODE */}
        <div className="flex justify-center">
          <div className="w-full sm:w-80 bg-emerald-50/70 border border-emerald-200 rounded-2xl p-4 sm:p-5 text-center shadow-xs">
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100/80 text-emerald-800 text-[11px] font-semibold mb-1.5">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
              <span>Consensus Outcome</span>
            </div>
            <div className="text-base sm:text-lg font-bold text-slate-900">
              Final Recommendation
            </div>
            <p className="text-xs text-slate-600 mt-1">
              Transparent, weighted verdict with full rationale
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
