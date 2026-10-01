import { useState, type InputHTMLAttributes } from 'react'
import { Hero } from '../components/Blocks'
import { usePage, useReveal } from '../components/hooks'
const F = ({ l, ...p }: { l: string } & InputHTMLAttributes<HTMLInputElement>) => <label className="fld"><input placeholder=" " {...p} /><span>{l}</span></label>
export default function Contact() {
  usePage('Contact Moon Cafe', 'Reserve a table or find Moon Cafe at 21 Crescent Street, Mumbai.'); const r = useReveal(); const [sent, setSent] = useState(false)
  return (<div ref={r}><Hero title="Reserve a table" sub="We'll hold it for fifteen minutes." tone={2} />
    <div className="wrap cgrid"><form onSubmit={e => { e.preventDefault(); setSent(true) }}>
      {sent ? <p className="ok" role="status">Thank you — your request is in. We'll confirm by email shortly.</p> : <>
        <F l="Name" required /><F l="Email" type="email" required /><F l="Phone" type="tel" required />
        <div className="row"><F l="Date" type="date" required /><F l="Time" type="time" required /></div>
        <F l="Guests" type="number" min={1} max={12} defaultValue={2} required /><button className="btn" type="submit"><span>Reserve</span><b aria-hidden>→</b></button></>}</form>
      <aside><h3>Moon Cafe</h3><p>21 Crescent Street<br />Mumbai, India</p><h4>Opening hours</h4><p>Mon–Fri: 8:00 AM – 11:00 PM<br />Sat–Sun: 8:00 AM – 12:00 AM</p><p>+91 98765 43210<br />hello@mooncafe.demo</p>
        <svg className="map" viewBox="0 0 300 200" role="img" aria-label="Stylised map showing Moon Cafe on Crescent Street"><rect width="300" height="200" fill="#1d1816" /><g stroke="#3a312b" strokeWidth="10" fill="none"><path d="M0 60H300M0 140H300M80 0V200M210 0V200" /></g><path d="M0 200Q150 20 300 120" stroke="#c9a76a55" strokeWidth="6" fill="none" /><circle cx="150" cy="100" r="10" fill="#c9a76a" /><circle cx="150" cy="100" r="22" fill="none" stroke="#c9a76a" /><text x="164" y="94" fill="#f3ead9" fontSize="11">Moon Cafe</text></svg></aside></div></div>)
}
