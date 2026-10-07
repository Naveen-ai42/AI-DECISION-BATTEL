import React from 'react'
import { Scale } from 'lucide-react'
import { Link, useLocation } from 'react-router-dom'

/**
 * Minimal clean footer with brand statement and essential links.
 */
export default function Footer() {
  const location = useLocation()

  const handleScroll = (e, targetId) => {
    if (location.pathname !== '/') {
      return
    }
    e.preventDefault()
    const element = document.getElementById(targetId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <footer className="w-full bg-white border-t border-slate-200/80 py-12">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-slate-100">
          {/* Brand info */}
          <div className="flex flex-col items-center md:items-start text-center md:text-left">
            <Link
              to="/"
              className="flex items-center gap-2 text-slate-900 font-bold text-lg mb-1"
            >
              <div className="w-7 h-7 rounded-lg bg-indigo-600 text-white flex items-center justify-center">
                <Scale className="w-4 h-4" />
              </div>
              <span>Decision Arena</span>
            </Link>
            <p className="text-sm text-slate-500 font-normal">
              AI-powered decision support.
            </p>
          </div>

          {/* Nav links */}
          <div className="flex flex-wrap items-center justify-center gap-6 sm:gap-8 text-sm font-medium text-slate-600">
            <a
              href="#how-it-works"
              onClick={(e) => handleScroll(e, 'how-it-works')}
              className="hover:text-indigo-600 transition-colors"
            >
              How It Works
            </a>
            <a
              href="#features"
              onClick={(e) => handleScroll(e, 'features')}
              className="hover:text-indigo-600 transition-colors"
            >
              Features
            </a>
            <button
              type="button"
              onClick={() => alert('Privacy Policy: Decision Arena does not sell or share your personal data.')}
              className="hover:text-indigo-600 transition-colors cursor-pointer"
            >
              Privacy
            </button>
            <a
              href="mailto:contact@decisionarena.ai"
              className="hover:text-indigo-600 transition-colors"
            >
              Contact
            </a>
          </div>
        </div>

        {/* Bottom copyright */}
        <div className="pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400 text-center sm:text-left">
          <p>&copy; {new Date().getFullYear()} Decision Arena. All rights reserved.</p>
          <p>Transparent Multi-Agent Decision Engine.</p>
        </div>
      </div>
    </footer>
  )
}
