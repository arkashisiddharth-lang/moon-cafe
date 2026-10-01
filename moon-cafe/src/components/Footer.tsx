import TLink from './Link'
import { links } from '../data'
import { gsap, reduced } from './hooks'
export default function Footer() {
  return (<footer className="foot"><div className="wrap fgrid">
    <div><h3 className="logo">MOON CAFE</h3><p>Coffee. Conversations. Midnight Vibes.</p></div>
    <div><h4>Navigate</h4>{links.map(([n, p]) => <TLink key={p} to={p} className="ul">{n}</TLink>)}</div>
    <div><h4>Visit</h4><p>21 Crescent Street<br />Mumbai, India</p><p>Mon–Fri 8 AM – 11 PM<br />Sat–Sun 8 AM – 12 AM</p></div>
    <div><h4>Say hello</h4><p>+91 98765 43210<br />hello@mooncafe.demo</p>
      <a className="ul" href="https://instagram.com" target="_blank" rel="noreferrer">Instagram</a>
      <a className="ul" href="https://facebook.com" target="_blank" rel="noreferrer">Facebook</a>
      <a className="ul" href="https://maps.google.com/?q=Mumbai" target="_blank" rel="noreferrer">Google Maps</a></div>
  </div><div className="wrap fbar"><span>© 2026 Moon Cafe — demo project</span>
    <button className="ul" onClick={() => reduced() ? window.scrollTo(0, 0) : gsap.to(window, { scrollTo: 0, duration: 1, ease: 'power3.inOut' })}>Back to top ↑</button></div></footer>)
}
