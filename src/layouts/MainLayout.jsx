import React from 'react'
import Navbar from '../components/Navbar'
import Footer from '../components/Footer'

/**
 * Main application layout wrapper featuring sticky Navbar and minimal Footer.
 */
export default function MainLayout({ children }) {
  return (
    <div className="min-h-screen flex flex-col bg-[#fafbfc] text-slate-900 selection:bg-indigo-100 selection:text-indigo-900">
      <Navbar />
      <main className="flex-1 flex flex-col">
        {children}
      </main>
      <Footer />
    </div>
  )
}
