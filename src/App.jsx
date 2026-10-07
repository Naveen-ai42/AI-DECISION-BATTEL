// Decision Arena App Root with Decision Context and Routing
import React, { useEffect } from 'react'
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import { DecisionProvider } from './context/DecisionContext'
import MainLayout from './layouts/MainLayout'
import LandingPage from './pages/LandingPage'
import CreatePage from './pages/CreatePage'
import RequirementsPage from './pages/RequirementsPage'
import BattlePage from './pages/BattlePage'
import ResultsPage from './pages/ResultsPage'
import HistoryPage from './pages/HistoryPage'
import ReviewsPage from './pages/ReviewsPage'
import ProfilePage from './pages/ProfilePage'

function ScrollToTop() {
  const { pathname } = useLocation()

  useEffect(() => {
    window.scrollTo({ top: 0, left: 0, behavior: 'auto' })
    if (document.documentElement) {
      document.documentElement.scrollTop = 0
    }
    if (document.body) {
      document.body.scrollTop = 0
    }
  }, [pathname])

  return null
}

export default function App() {
  return (
    <DecisionProvider>
      <BrowserRouter>
        <ScrollToTop />
        <MainLayout>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/create" element={<CreatePage />} />
            <Route path="/requirements" element={<RequirementsPage />} />
            <Route path="/battle" element={<BattlePage />} />
            <Route path="/results" element={<ResultsPage />} />
            <Route path="/history" element={<HistoryPage />} />
            <Route path="/reviews" element={<ReviewsPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="*" element={<LandingPage />} />
          </Routes>
        </MainLayout>
      </BrowserRouter>
    </DecisionProvider>
  )
}
