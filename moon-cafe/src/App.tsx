import { useLayoutEffect } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import { gsap, reduced, ScrollTrigger } from './components/hooks'
import Home from './pages/Home'; import Menu from './pages/Menu'; import About from './pages/About'; import Experience from './pages/Experience'
import Gallery from './pages/Gallery'; import Reviews from './pages/Reviews'; import Contact from './pages/Contact'
export default function App() {
  const { pathname } = useLocation()
  useLayoutEffect(() => {
    window.scrollTo(0, 0); ScrollTrigger.refresh()
    const o = document.querySelector('.curtain'); if (!o || reduced()) return
    gsap.to(o, { clipPath: 'inset(0 0 100% 0)', duration: .55, ease: 'power3.inOut', delay: .05, onComplete: () => { gsap.set(o, { display: 'none' }) } })
    gsap.fromTo('main', { y: 30, scale: .99 }, { y: 0, scale: 1, duration: .8, ease: 'power3.out' })
  }, [pathname])
  return (<><a className="skip" href="#main">Skip to content</a><Navbar /><main id="main"><Routes>
    <Route path="/" element={<Home />} /><Route path="/menu" element={<Menu />} /><Route path="/about" element={<About />} /><Route path="/experience" element={<Experience />} />
    <Route path="/gallery" element={<Gallery />} /><Route path="/reviews" element={<Reviews />} /><Route path="/contact" element={<Contact />} /><Route path="*" element={<Home />} /></Routes></main><Footer /><div className="curtain" aria-hidden /></>)
}
