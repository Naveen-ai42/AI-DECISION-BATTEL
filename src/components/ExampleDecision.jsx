import React, { useState } from 'react'
import {
  Laptop,
  Landmark,
  Briefcase,
  Zap,
  Tag,
  BatteryCharging,
  Sparkles,
  TrendingUp,
  ShieldAlert,
  Coins,
  ArrowUpRight,
  DollarSign,
  CheckCircle2,
  Award,
  AlertCircle
} from 'lucide-react'

const SHOWCASE_DATA = {
  electronics: {
    category: 'Electronics',
    icon: Laptop,
    prompt: '“Choose a laptop under ₹55,000 for coding, AI/ML projects and entertainment.”',
    agents: [
      { name: 'Performance', score: 92, icon: Zap, color: 'text-indigo-600', bg: 'bg-indigo-50', bar: 'bg-indigo-600' },
      { name: 'Value', score: 86, icon: Tag, color: 'text-emerald-600', bg: 'bg-emerald-50', bar: 'bg-emerald-500' },
      { name: 'Battery', score: 81, icon: BatteryCharging, color: 'text-blue-600', bg: 'bg-blue-50', bar: 'bg-blue-500' },
      { name: 'Experience', score: 90, icon: Sparkles, color: 'text-violet-600', bg: 'bg-violet-50', bar: 'bg-violet-500' },
    ],
    winner: 'ASUS TUF Gaming A15',
    score: 87,
    summary: 'High compute throughput and display clarity with verified coding and ML performance.',
  },
  finance: {
    category: 'Finance',
    icon: Landmark,
    prompt: '“Choose the best investment option for ₹2 lakh with moderate risk and growth.”',
    agents: [
      { name: 'Return', score: 89, icon: TrendingUp, color: 'text-emerald-600', bg: 'bg-emerald-50', bar: 'bg-emerald-600' },
      { name: 'Risk', score: 84, icon: ShieldAlert, color: 'text-rose-600', bg: 'bg-rose-50', bar: 'bg-rose-500' },
      { name: 'Liquidity', score: 86, icon: Coins, color: 'text-blue-600', bg: 'bg-blue-50', bar: 'bg-blue-500' },
      { name: 'Growth', score: 91, icon: ArrowUpRight, color: 'text-amber-600', bg: 'bg-amber-50', bar: 'bg-amber-500' },
    ],
    winner: 'Diversified Index & Flexi-Cap Allocation',
    score: 87,
    summary: 'High compounding upside with defensive downside buffers and zero lock-in drag.',
  },
  career: {
    category: 'Career',
    icon: Briefcase,
    prompt: '“Which career path should I choose after BTech Data Science?”',
    agents: [
      { name: 'Compensation', score: 88, icon: DollarSign, color: 'text-emerald-600', bg: 'bg-emerald-50', bar: 'bg-emerald-600' },
      { name: 'Skill-Fit', score: 93, icon: CheckCircle2, color: 'text-indigo-600', bg: 'bg-indigo-50', bar: 'bg-indigo-600' },
      { name: 'Growth', score: 90, icon: TrendingUp, color: 'text-amber-600', bg: 'bg-amber-50', bar: 'bg-amber-500' },
      { name: 'Work-Life', score: 82, icon: Sparkles, color: 'text-blue-600', bg: 'bg-blue-50', bar: 'bg-blue-500' },
    ],
    winner: 'Senior Applied Data Scientist Track',
    score: 89,
    summary: 'Direct application of technical proficiencies with accelerated career runway.',
  },
}

/**
 * Example decision demonstration card showing simulated multi-agent breakdown across categories.
 */
export default function ExampleDecision() {
  const [activeTab, setActiveTab] = useState('electronics')
  const activeData = SHOWCASE_DATA[activeTab]

  return (
    <section className="py-20 sm:py-28 bg-white border-y border-slate-200/70">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider mb-3">
            <span className="w-2 h-2 rounded-full bg-indigo-500" />
            General AI Decision Platform
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight">
            See the battle before you make the choice.
          </h2>
          <p className="text-sm sm:text-base text-slate-500 mt-2 font-normal">
            Autonomous AI agents dynamically adapt their expertise and factors to your specific decision domain.
          </p>
        </div>

        {/* Category Showcase Tabs */}
        <div className="flex items-center justify-center gap-2 mb-8">
          {Object.entries(SHOWCASE_DATA).map(([key, data]) => {
            const Icon = data.icon
            const isSelected = activeTab === key
            return (
              <button
                key={key}
                type="button"
                onClick={() => setActiveTab(key)}
                className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
                  isSelected
                    ? 'bg-indigo-600 text-white shadow-xs'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200/80 hover:text-slate-900'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span>{data.category}</span>
              </button>
            )
          })}
        </div>

        {/* Demonstration Container */}
        <div className="bg-slate-50/80 border border-slate-200 rounded-3xl p-6 sm:p-10 shadow-xs relative">
          {/* Explicit Example Badges */}
          <div className="flex flex-wrap items-center justify-between gap-3 pb-6 border-b border-slate-200/80 mb-6">
            <span className="px-3 py-1 rounded-md bg-indigo-600 text-white text-xs font-semibold uppercase tracking-wide">
              {activeData.category} Showcase
            </span>
            <div className="flex items-center gap-1.5 text-xs text-slate-500">
              <AlertCircle className="w-3.5 h-3.5 text-slate-400" />
              <span>Simulated multi-agent deliberative outcome.</span>
            </div>
          </div>

          {/* User's Decision Query */}
          <div className="mb-8 bg-white border border-slate-200 rounded-2xl p-5 shadow-2xs">
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                Decision Prompt ({activeData.category})
              </span>
              <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-slate-100 text-slate-600">
                {activeData.category}
              </span>
            </div>
            <p className="text-base sm:text-lg font-medium text-slate-900">
              {activeData.prompt}
            </p>
          </div>

          {/* 4 Agent Score Badges */}
          <div className="mb-8">
            <div className="text-xs font-semibold uppercase tracking-wider text-slate-500 mb-3">
              {activeData.category} AI Agent Evaluations
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
              {activeData.agents.map((agent) => {
                const Icon = agent.icon
                return (
                  <div
                    key={agent.name}
                    className="bg-white border border-slate-200 rounded-2xl p-4 shadow-2xs flex flex-col justify-between"
                  >
                    <div className="flex items-center justify-between mb-3">
                      <div className={`w-8 h-8 rounded-lg ${agent.bg} ${agent.color} flex items-center justify-center`}>
                        <Icon className="w-4 h-4" />
                      </div>
                      <span className="text-xl font-bold text-slate-900 font-mono">
                        {agent.score}
                      </span>
                    </div>
                    <div>
                      <div className="text-xs font-medium text-slate-700">
                        {agent.name} Agent
                      </div>
                      <div className="w-full bg-slate-100 rounded-full h-1.5 mt-2 overflow-hidden">
                        <div
                          className={`h-full rounded-full ${agent.bar}`}
                          style={{ width: `${agent.score}%` }}
                        />
                      </div>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>

          {/* Recommended Winner Card */}
          <div className="bg-white border-2 border-emerald-500/30 rounded-2xl p-6 sm:p-7 shadow-xs">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-3">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center">
                  <Award className="w-5 h-5" />
                </div>
                <div>
                  <div className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold mb-0.5">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>Recommended</span>
                  </div>
                  <h3 className="text-xl font-bold text-slate-900">
                    {activeData.winner}
                  </h3>
                </div>
              </div>

              {/* Overall Score */}
              <div className="flex items-baseline gap-1 bg-slate-50 border border-slate-200 px-4 py-2 rounded-xl self-start sm:self-auto">
                <span className="text-2xl font-extrabold text-slate-900 font-mono">
                  {activeData.score}
                </span>
                <span className="text-sm font-medium text-slate-400">
                  / 100
                </span>
              </div>
            </div>

            <p className="text-sm text-slate-600 mt-2 font-normal leading-relaxed">
              {activeData.summary}
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}
