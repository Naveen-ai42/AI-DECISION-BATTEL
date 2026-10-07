import React, { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Scale, Menu, X, ArrowRight, Home, History, MessageSquareText, User } from 'lucide-react'
import Button from './Button'

/**
 * Sticky Navbar that adapts contextually:
 * - On Landing Page (/): Shows "How It Works", "Features", and "Start a Decision" button.
 * - In Decision Studio (/create, /requirements, etc.): Shows "Home", "History", "Profile".
 */
export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const location = useLocation()
  const isLandingPage = location.pathname === '/'

  const handleNavClick = (e, targetId) => {
    setMobileMenuOpen(false)
    if (!isLandingPage) {
      return
    }
    e.preventDefault()
    const element = document.getElementById(targetId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <header className="sticky top-0 z-50 w-full border-b border-slate-200/80 bg-white/90 backdrop-blur-md transition-all">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand Logo */}
        <Link
          to="/"
          className="flex items-center gap-2.5 text-slate-900 hover:opacity-90 transition-opacity focus:outline-none focus:ring-2 focus:ring-indigo-500 rounded-lg"
          aria-label="Decision Arena Home"
        >
          <div className="flex items-center justify-center w-9 h-9 rounded-xl bg-indigo-600 text-white shadow-sm shadow-indigo-500/20">
            <Scale className="w-5 h-5 stroke-[2.2]" />
          </div>
          <span className="font-bold text-lg tracking-tight text-slate-900">
            Decision Arena
          </span>
        </Link>

        {/* Desktop Navigation Links */}
        <nav className="hidden md:flex items-center gap-7 text-sm font-medium text-slate-600">
          {isLandingPage ? (
            <>
              <a
                href="#how-it-works"
                onClick={(e) => handleNavClick(e, 'how-it-works')}
                className="hover:text-indigo-600 transition-colors"
              >
                How It Works
              </a>
              <a
                href="#features"
                onClick={(e) => handleNavClick(e, 'features')}
                className="hover:text-indigo-600 transition-colors"
              >
                Features
              </a>
            </>
          ) : (
            <>
              <Link
                to="/"
                className="flex items-center gap-1.5 hover:text-indigo-600 transition-colors"
              >
                <Home className="w-4 h-4" />
                <span>Home</span>
              </Link>
              <Link
                to="/history"
                className="flex items-center gap-1.5 hover:text-indigo-600 transition-colors"
              >
                <History className="w-4 h-4" />
                <span>History</span>
              </Link>
              <Link
                to="/reviews"
                className="flex items-center gap-1.5 hover:text-indigo-600 transition-colors"
              >
                <MessageSquareText className="w-4 h-4" />
                <span>Reviews</span>
              </Link>
              <Link
                to="/profile"
                className="flex items-center gap-1.5 hover:text-indigo-600 transition-colors"
              >
                <div className="w-6 h-6 rounded-full bg-slate-100 border border-slate-200 flex items-center justify-center text-slate-600">
                  <User className="w-3.5 h-3.5" />
                </div>
                <span>Profile</span>
              </Link>
            </>
          )}
        </nav>

        {/* Desktop CTA on Landing Page */}
        {isLandingPage && (
          <div className="hidden md:flex items-center gap-4">
            <Button to="/create" variant="primary" className="py-2.5 px-4.5 text-sm">
              Start a Decision
              <ArrowRight className="w-4 h-4 ml-1.5" />
            </Button>
          </div>
        )}

        {/* Mobile Hamburger Button */}
        <div className="flex md:hidden items-center">
          <button
            type="button"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="p-2 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            aria-label={mobileMenuOpen ? 'Close Menu' : 'Open Menu'}
            aria-expanded={mobileMenuOpen}
          >
            {mobileMenuOpen ? (
              <X className="w-6 h-6" />
            ) : (
              <Menu className="w-6 h-6" />
            )}
          </button>
        </div>
      </div>

      {/* Mobile Dropdown Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden border-b border-slate-200 bg-white px-4 pt-3 pb-5 space-y-3 shadow-lg">
          <nav className="flex flex-col space-y-2">
            {isLandingPage ? (
              <>
                <a
                  href="#how-it-works"
                  onClick={(e) => handleNavClick(e, 'how-it-works')}
                  className="px-3 py-2 rounded-lg text-base font-medium text-slate-700 hover:text-indigo-600 hover:bg-slate-50 transition-colors"
                >
                  How It Works
                </a>
                <a
                  href="#features"
                  onClick={(e) => handleNavClick(e, 'features')}
                  className="px-3 py-2 rounded-lg text-base font-medium text-slate-700 hover:text-indigo-600 hover:bg-slate-50 transition-colors"
                >
                  Features
                </a>
                <div className="pt-2">
                  <Button
                    to="/create"
                    onClick={() => setMobileMenuOpen(false)}
                    variant="primary"
                    className="w-full justify-center py-3 text-sm"
                  >
                    Start a Decision
                    <ArrowRight className="w-4 h-4 ml-1.5" />
                  </Button>
                </div>
              </>
            ) : (
              <>
                <Link
                  to="/"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 px-3 py-2 rounded-lg text-base font-medium text-slate-700 hover:text-indigo-600 hover:bg-slate-50 transition-colors"
                >
                  <Home className="w-4 h-4" />
                  <span>Home</span>
                </Link>
                <Link
                  to="/history"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 px-3 py-2 rounded-lg text-base font-medium text-slate-700 hover:text-indigo-600 hover:bg-slate-50 transition-colors"
                >
                  <History className="w-4 h-4" />
                  <span>History</span>
                </Link>
                <Link
                  to="/reviews"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 px-3 py-2 rounded-lg text-base font-medium text-slate-700 hover:text-indigo-600 hover:bg-slate-50 transition-colors"
                >
                  <MessageSquareText className="w-4 h-4" />
                  <span>Reviews</span>
                </Link>
                <Link
                  to="/profile"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 px-3 py-2 rounded-lg text-base font-medium text-slate-700 hover:text-indigo-600 hover:bg-slate-50 transition-colors"
                >
                  <User className="w-4 h-4" />
                  <span>Profile</span>
                </Link>
              </>
            )}
          </nav>
        </div>
      )}
    </header>
  )
}
