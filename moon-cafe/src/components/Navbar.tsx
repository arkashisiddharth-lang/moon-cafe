import { useEffect, useRef, useState } from 'react'
import TLink, { Btn } from './Link'
import { links } from '../data'
import { gsap, reduced } from './hooks'
export default function Navbar() {
  const [open, setOpen] = useState(false); const [solid, setSolid] = useState(false); const m = useRef<HTMLDivElement>(null)
  useEffect(() => { const f = () => setSolid(scrollY > 40); f(); addEventListener('scroll', f, { passive: true }); return () => removeEventListener('scroll', f) }, [])
  useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    if (!m.current || reduced()) return
    const ctx = gsap.context(() => { if (open) gsap.fromTo('.mnav a', { y: 40, opacity: 0 }, { y: 0, opacity: 1, stagger: .06, duration: .6, ease: 'power3.out', delay: .15 }) }, m)
    return () => ctx.revert()
  }, [open])
  return (<header className={'nav' + (solid ? ' solid' : '')}>
    <TLink to="/" className="logo" onClick={() => setOpen(false)}>MOON CAFE</TLink>
    <nav className="dnav" aria-label="Main">{links.map(([n, p]) => <TLink key={p} to={p} nav className="ul">{n}</TLink>)}</nav>
    <div className="dcta"><Btn to="/contact">Reserve</Btn></div>
    <button className={'burger' + (open ? ' on' : '')} aria-label={open ? 'Close menu' : 'Open menu'} aria-expanded={open} onClick={() => setOpen(!open)}><span /><span /></button>
    <div ref={m} className={'mnav' + (open ? ' open' : '')} aria-hidden={!open}>{links.map(([n, p]) => <TLink key={p} to={p} nav onClick={() => setOpen(false)}>{n}</TLink>)}</div>
  </header>)
}
