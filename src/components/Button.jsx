import React from 'react'
import { Link } from 'react-router-dom'

/**
 * Reusable Button component with clean SaaS styling.
 * Supports rendering as a standard button, react-router Link, or an anchor tag.
 */
export default function Button({
  children,
  onClick,
  to,
  href,
  type = 'button',
  variant = 'primary',
  className = '',
  disabled = false,
  ...props
}) {
  const baseStyles =
    'inline-flex items-center justify-center font-medium rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer'

  const variants = {
    primary:
      'bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm hover:shadow-md hover:shadow-indigo-500/10 focus:ring-indigo-500 px-6 py-3 text-sm sm:text-base font-semibold',
    secondary:
      'bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 hover:border-slate-300 shadow-sm hover:shadow focus:ring-slate-400 px-5 py-2.5 text-sm sm:text-base',
    ghost:
      'text-slate-600 hover:text-slate-900 hover:bg-slate-100/80 px-4 py-2 text-sm',
    outline:
      'border border-indigo-200 text-indigo-600 hover:bg-indigo-50/60 focus:ring-indigo-500 px-5 py-2.5 text-sm font-medium',
  }

  const variantStyles = variants[variant] || variants.primary
  const combinedClasses = `${baseStyles} ${variantStyles} ${className}`

  if (to) {
    return (
      <Link to={to} className={combinedClasses} {...props}>
        {children}
      </Link>
    )
  }

  if (href) {
    return (
      <a href={href} className={combinedClasses} {...props}>
        {children}
      </a>
    )
  }

  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={combinedClasses}
      {...props}
    >
      {children}
    </button>
  )
}
