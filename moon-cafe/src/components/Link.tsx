import type { MouseEvent, ReactNode } from 'react'
import { Link as RL, NavLink, useNavigate, useLocation } from 'react-router-dom'
import { gsap, reduced } from './hooks'
/** Runs the cover animation, then navigates. App reveals the new page. */
export function useGo() {
  const nav = useNavigate(); const { pathname } = useLocation()
  return (to: string) => {
    if (to === pathname) return window.scrollTo({ top: 0, behavior: 'smooth' })
    const o = document.querySelector('.curtain')
    if (!o || reduced()) return nav(to)
    gsap.set(o, { clipPath: 'inset(100% 0 0 0)', display: 'block' })
    gsap.to(o, { clipPath: 'inset(0% 0 0 0)', duration: .45, ease: 'power3.inOut', onComplete: () => nav(to) })
  }
}
type P = { to: string; children: ReactNode; className?: string; nav?: boolean; onClick?: () => void }
export default function TLink({ to, children, className, nav, onClick }: P) {
  const go = useGo(); const C: any = nav ? NavLink : RL
  return <C to={to} className={className} end={nav ? to === '/' : undefined} onClick={(e: MouseEvent) => { e.preventDefault(); onClick?.(); go(to) }}>{children}</C>
}
export const Btn = ({ to, children, ghost }: { to: string; children: ReactNode; ghost?: boolean }) =>
  <TLink to={to} className={'btn' + (ghost ? ' ghost' : '')}><span>{children}</span><b aria-hidden>→</b></TLink>
