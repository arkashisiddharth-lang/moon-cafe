import { useEffect, useLayoutEffect, useRef, useState } from 'react'
import Art from '../components/Art'
import { Hero } from '../components/Blocks'
import { gsap, reduced, usePage, useReveal } from '../components/hooks'
import { cats, menu } from '../data'
export default function Menu() {
  usePage('Moon Cafe Menu — Coffee, Desserts & More', 'Browse the Moon Cafe menu: espresso, cold drinks, tea, fresh bakery and desserts.')
  const root = useReveal(); const [cat, setCat] = useState<typeof cats[number]>('Coffee'); const list = useRef<HTMLDivElement>(null)
  useLayoutEffect(() => { if (reduced()) return; const c = gsap.context(() => { gsap.from('.mi', { y: 30, opacity: 0, stagger: .07, duration: .55, ease: 'power2.out' }) }, list); return () => c.revert() }, [cat])
  const pick = (c: typeof cats[number]) => {
    if (c === cat) return
    if (reduced()) return setCat(c)
    gsap.to(list.current!.querySelectorAll('.mi'), { y: -16, opacity: 0, stagger: .04, duration: .25, onComplete: () => setCat(c) })
  }
  useEffect(() => () => { gsap.killTweensOf('.mi') }, [])
  return (<div ref={root}><Hero title="The Menu" sub="Made fresh, served slowly." tone={3} />
    <div className="wrap tabs" role="tablist">{cats.map(c => <button key={c} role="tab" aria-selected={c === cat} className={'tab' + (c === cat ? ' on' : '')} onClick={() => pick(c)}>{c}</button>)}</div>
    <div className="wrap mlist" ref={list}>{menu.filter(i => i.cat === cat).map(i => <article className="mi card" key={i.name}><Art tone={i.tone} ratio="1/1" /><div><h3>{i.name}</h3><p>{i.desc}</p></div><span className="price">₹{i.price}</span></article>)}</div></div>)
}
