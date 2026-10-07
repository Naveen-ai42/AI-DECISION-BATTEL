import React, { useEffect, useState } from 'react'
import { UserCircle2, Sparkles, LayoutGrid, ArrowRight } from 'lucide-react'
import { Link } from 'react-router-dom'
import Button from '../components/Button'
import { useDecision } from '../hooks/useDecision'

export default function ProfilePage() {
  const { decision } = useDecision()
  const [savedCount, setSavedCount] = useState(0)

  useEffect(() => {
    try {
      const saved = JSON.parse(localStorage.getItem('saved_decisions') || '[]')
      setSavedCount(saved.length)
    } catch {
      setSavedCount(0)
    }
  }, [])

  return (
    <div className="flex-1 w-full py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <div className="rounded-[28px] border border-slate-200 bg-white p-6 sm:p-8 shadow-xs">
          <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
            <div className="flex items-center gap-4">
              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-indigo-50 text-indigo-600">
                <UserCircle2 className="h-8 w-8" />
              </div>
              <div>
                <p className="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500">Profile</p>
                <h1 className="mt-1 text-3xl font-bold text-slate-900">Guest workspace</h1>
              </div>
            </div>

            <div className="rounded-full border border-emerald-200 bg-emerald-50 px-3 py-1.5 text-sm font-medium text-emerald-700">
              Session active
            </div>
          </div>

          <div className="mt-8 grid gap-5 md:grid-cols-3">
            <div className="rounded-2xl bg-slate-50 p-5 border border-slate-200">
              <div className="flex items-center gap-3 text-slate-700">
                <Sparkles className="h-5 w-5 text-indigo-600" />
                <span className="text-sm font-semibold">Current plan</span>
              </div>
              <p className="mt-4 text-2xl font-bold text-slate-900">Free</p>
              <p className="mt-2 text-sm text-slate-500">Guest access to the decision studio.</p>
            </div>

            <div className="rounded-2xl bg-slate-50 p-5 border border-slate-200">
              <div className="flex items-center gap-3 text-slate-700">
                <LayoutGrid className="h-5 w-5 text-indigo-600" />
                <span className="text-sm font-semibold">Saved decisions</span>
              </div>
              <p className="mt-4 text-2xl font-bold text-slate-900">{savedCount}</p>
              <p className="mt-2 text-sm text-slate-500">Stored in this browser.</p>
            </div>

            <div className="rounded-2xl bg-slate-50 p-5 border border-slate-200">
              <div className="flex items-center gap-3 text-slate-700">
                <ArrowRight className="h-5 w-5 text-indigo-600" />
                <span className="text-sm font-semibold">Current focus</span>
              </div>
              <p className="mt-4 text-2xl font-bold text-slate-900">{decision.category || 'Electronics'}</p>
              <p className="mt-2 text-sm text-slate-500">{decision.subcategory || 'laptop'} category</p>
            </div>
          </div>

          <div className="mt-8 rounded-2xl border border-slate-200 bg-slate-50 p-5">
            <h2 className="text-lg font-semibold text-slate-900">Session summary</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-600">
              <li>• Current description: {decision.description || 'Not started yet'}</li>
              <li>• Budget: {decision.budget || 'Not set'}</li>
              <li>• Requirement count: {decision.requirements?.length || 0}</li>
              <li>• Deal breakers: {decision.dealBreakers?.length || 0}</li>
            </ul>
          </div>

          <div className="mt-8 flex flex-col sm:flex-row gap-3">
            <Button to="/create" variant="primary" className="justify-center">
              Continue decision
              <ArrowRight className="w-4 h-4 ml-1.5" />
            </Button>
            <Link to="/history" className="inline-flex items-center justify-center rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-slate-700 hover:border-slate-300 transition-colors">
              View history
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
