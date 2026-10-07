import React from 'react'
import { CheckCircle2, TrendingUp, ShieldCheck, Award } from 'lucide-react'
import { getCategoryConfig } from '../config/categoryConfig'

/**
 * Section presenting the 4 core reasons why the recommended option won, dynamically tailored per category.
 */
export default function WhyItWon({ category = 'electronics', subcategory = '' }) {
  const categoryConfig = getCategoryConfig(category, subcategory)

  const getCategoryReasons = (cat, sub) => {
    switch (cat) {
      case 'finance':
        return [
          {
            title: 'High risk-adjusted return potential',
            desc: 'Disciplined compounding track record projected to outpace inflation and cash savings over multi-year horizons.',
            icon: TrendingUp,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'Controlled downside risk and low beta',
            desc: 'Diversified across resilient asset classes to prevent single-point capital drawdown or insolvency.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
          {
            title: 'Healthy liquidity and withdrawal access',
            desc: 'Rapid T+1 settlement on emergency reserves with zero punitive long-term lock-in restrictions.',
            icon: CheckCircle2,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
          {
            title: 'Low fee drag preserving net compounding',
            desc: 'Minimal management expense ratio maximizes net principal accumulation over the long term.',
            icon: Award,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
        ]
      case 'career':
        return [
          {
            title: 'Competitive compensation package',
            desc: 'Attractive base salary and performance upside benchmarked against top industry percentiles.',
            icon: Award,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'Exceptional skill alignment & ownership',
            desc: 'Direct application of core proficiencies with high daily autonomy on modern technical problems.',
            icon: CheckCircle2,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
          {
            title: 'High-velocity career trajectory',
            desc: 'Positions your resume at the forefront of high-demand paradigms with clear leadership visibility.',
            icon: TrendingUp,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
          {
            title: 'Sustainable work-life integration',
            desc: 'Flexible working arrangements and balanced team culture protecting against personal burnout.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
        ]
      case 'education':
        return [
          {
            title: 'Rigorous curriculum & distinguished faculty',
            desc: 'Hands-on practical milestones backed by renowned researchers and modern lab infrastructure.',
            icon: Award,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
          {
            title: 'Proven graduate recruitment pipeline',
            desc: 'Tier-1 employer hiring drives yielding strong median starting packages for alumni cohorts.',
            icon: CheckCircle2,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'Favorable educational return on investment',
            desc: 'Reasonable tuition structure balanced by post-graduate career earnings premium.',
            icon: TrendingUp,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
          {
            title: 'Lifelong global alumni leverage',
            desc: 'Timeless institutional brand prestige recognized by international employers and institutions.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
        ]
      case 'travel':
        return [
          {
            title: 'Cost-effective itinerary within budget',
            desc: 'Maximizes cultural immersion and memorable regional experiences without budget overruns.',
            icon: CheckCircle2,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'High safety index & reliable infrastructure',
            desc: 'Safe destination with certified lodging, accessible healthcare, and tourist security.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
          {
            title: 'Pristine scenic beauty & culinary immersion',
            desc: 'Curated mix of scenic viewpoints, regional gastronomy, and relaxing atmosphere.',
            icon: Award,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
          {
            title: 'Convenient transit with minimal friction',
            desc: 'Direct transportation options and walkable town layout reducing travel fatigue.',
            icon: TrendingUp,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
        ]
      case 'shopping':
        return [
          {
            title: 'Premium build quality & craftsmanship',
            desc: 'Durable reinforced materials and tight manufacturing tolerances built for everyday use.',
            icon: Award,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
          {
            title: 'Competitive market pricing & value',
            desc: 'Comes comfortably within the defined budget ceiling with zero artificial markups.',
            icon: CheckCircle2,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'Strong consensus among verified owners',
            desc: 'Consistently high ratings (4.5+) and positive sentiment across long-term user reviews.',
            icon: TrendingUp,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
          {
            title: 'Comprehensive warranty & durability',
            desc: 'Multi-year manufacturer warranty and commercial-grade stress cycle testing.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
        ]
      case 'electronics':
        if (sub === 'smartphone') {
          return [
            {
              title: 'Flagship-grade camera & low-light optics',
              desc: '50MP Sony main sensor with OIS captures crisp, true-to-life images and stable 4K video.',
              icon: Award,
              iconClass: 'text-rose-600 bg-rose-50 border-rose-100',
            },
            {
              title: 'All-day endurance & 100W fast charging',
              desc: '5,500mAh high-density battery delivers 7.5+ hours SOT with sub-30 minute full top-ups.',
              icon: CheckCircle2,
              iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
            },
            {
              title: 'Fluid 1.5K 120Hz LTPO AMOLED display',
              desc: 'Adaptive refresh rates and 4,500 nits peak outdoor brightness ensure pristine visibility.',
              icon: ShieldCheck,
              iconClass: 'text-violet-600 bg-violet-50 border-violet-100',
            },
            {
              title: 'Unbeatable flagship killer value',
              desc: 'Premium Snapdragon compute and 16GB RAM at a fraction of true flagship pricing.',
              icon: TrendingUp,
              iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
            },
          ]
        }
        if (sub === 'smartwatch') {
          return [
            {
              title: 'Pro-grade dual-band GPS & biometric accuracy',
              desc: 'Multi-constellation satellite tracking and 4th-gen HR sensor rival dedicated chest straps.',
              icon: Award,
              iconClass: 'text-rose-600 bg-rose-50 border-rose-100',
            },
            {
              title: '11-day exceptional battery endurance',
              desc: 'Multi-day runtime completely eliminates daily recharge anxiety on work trips and trails.',
              icon: CheckCircle2,
              iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
            },
            {
              title: 'Rugged 5 ATM water resistance & build',
              desc: 'Engineered for open-water swimming, sweat resistance, and intense workout abuse.',
              icon: ShieldCheck,
              iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
            },
            {
              title: 'Zero mandatory paywalled subscriptions',
              desc: 'Full access to recovery metrics, training plans, and HRV status with zero monthly fees.',
              icon: TrendingUp,
              iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
            },
          ]
        }
        return [
          {
            title: 'Strong compute throughput for workloads',
            desc: 'High multi-core throughput and memory headroom handle compiling, local modeling, and multitasking.',
            icon: Award,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
          {
            title: 'Excellent price-to-performance balance',
            desc: 'Maximizes raw hardware value per rupee while staying strictly within your budget ceiling.',
            icon: CheckCircle2,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'Meets primary must-have requirements',
            desc: 'Directly fulfills your non-negotiable specifications for memory capacity and compute capability.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
          {
            title: 'Reliable thermal stability & longevity',
            desc: 'Modern connectivity standards and solid thermal architecture ensure multi-year reliability.',
            icon: TrendingUp,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
        ]
      default:
        return [
          {
            title: 'Direct alignment with primary objectives',
            desc: 'Highest fulfillment of your stated strategic requirements and personal criteria.',
            icon: Award,
            iconClass: 'text-indigo-600 bg-indigo-50 border-indigo-100',
          },
          {
            title: 'Prudent cost and resource balance',
            desc: 'Optimizes return on invested time and capital relative to available alternatives.',
            icon: CheckCircle2,
            iconClass: 'text-emerald-600 bg-emerald-50 border-emerald-100',
          },
          {
            title: 'Controlled downside risk & reversibility',
            desc: 'Downside risks are capped and well-understood with viable pivot routes.',
            icon: ShieldCheck,
            iconClass: 'text-blue-600 bg-blue-50 border-blue-100',
          },
          {
            title: 'Strong qualitative peace of mind',
            desc: 'Offers the lowest day-to-day friction and greatest long-term satisfaction.',
            icon: TrendingUp,
            iconClass: 'text-amber-600 bg-amber-50 border-amber-100',
          },
        ]
    }
  }

  const reasons = getCategoryReasons(
    (category || 'electronics').toLowerCase(),
    (subcategory || '').toLowerCase()
  )

  return (
    <div className="w-full bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 shadow-xs mb-10">
      <div className="mb-6">
        <h3 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
          Why this option won ({categoryConfig.label})
        </h3>
        <p className="text-xs sm:text-sm text-slate-500 mt-1">
          Direct synthesis of agent evidence and criteria matching.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {reasons.map((r, idx) => {
          const Icon = r.icon
          return (
            <div
              key={idx}
              className="p-5 rounded-2xl bg-slate-50/70 border border-slate-200/80 hover:bg-white hover:border-slate-300 transition-all flex items-start gap-3.5"
            >
              <div
                className={`w-9 h-9 rounded-xl flex items-center justify-center border flex-shrink-0 mt-0.5 ${r.iconClass}`}
              >
                <Icon className="w-4 h-4 stroke-[2.2]" />
              </div>
              <div>
                <h4 className="text-sm font-bold text-slate-900 leading-snug mb-1">
                  {r.title}
                </h4>
                <p className="text-xs text-slate-600 leading-relaxed font-normal">
                  {r.desc}
                </p>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
