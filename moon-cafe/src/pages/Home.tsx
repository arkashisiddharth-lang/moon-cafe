import { useLayoutEffect, useRef } from 'react'
import { Btn } from '../components/Link'
import Art from '../components/Art'
import { gsap, reduced, usePage, useReveal } from '../components/hooks'
import { menu, reviews } from '../data'
export default function Home() {
  usePage('Moon Cafe — Coffee. Conversations. Midnight Vibes.', 'Moon Cafe is a late-night Mumbai café for slow coffee, good company and midnight vibes.')
  const root = useReveal(); const hero = useRef<HTMLElement>(null)
  useLayoutEffect(() => {
    if (reduced()) return
    const ctx = gsap.context(() => {
      const t = gsap.timeline({ defaults: { ease: 'power3.out' } })
      t.from('.hero h1 span', { yPercent: 115, duration: 1, stagger: .12 }).from('.hero .lead', { y: 20, opacity: 0, duration: .7 }, '-=.5')
        .from('.hero .btns > *', { y: 20, opacity: 0, stagger: .1, duration: .6 }, '-=.4')
      gsap.fromTo('.hero .art', { scale: 1.15 }, { scale: 1, duration: 2.2, ease: 'power2.out' })
      gsap.to('.hero .hbg', { yPercent: 8, ease: 'none', scrollTrigger: { trigger: '.hero', scrub: true, start: 'top top', end: 'bottom top' } })
    }, hero)
    return () => ctx.revert()
  }, [])
  return (<div ref={root}>
    <section className="hero" ref={hero}><div className="hbg"><Art tone={2} ratio="auto" /></div><div className="wrap hin">
      <h1><em className="ln"><span>MOON</span></em><em className="ln"><span>CAFE</span></em></h1>
      <p className="lead">Coffee. Conversations. Midnight Vibes.</p>
      <div className="btns"><Btn to="/menu">Explore Menu</Btn><Btn to="/contact" ghost>Reserve a Table</Btn></div></div></section>
    <section className="wrap sec intro"><p className="big" data-split>A slow-lit corner of Mumbai where the espresso is strong and the evenings are longer.</p></section>
    <section className="wrap sec"><div className="shead"><h2 data-split>On the menu tonight</h2><Btn to="/menu" ghost>View Menu</Btn></div>
      <div className="grid3">{[menu[0], menu[3], menu[12]].map(i => <article className="card" key={i.name} data-r><Art tone={i.tone} ratio="4/5" /><h3>{i.name}</h3><p>{i.desc}</p><span className="price">₹{i.price}</span></article>)}</div></section>
    <section className="block wrap"><div className="bimg" data-mask><Art tone={1} /></div><div className="btxt"><h2 data-split>More than coffee.</h2><p data-r>Moon Cafe is a place to slow down, meet good people, and stay a little longer.</p><Btn to="/about" ghost>Discover More</Btn></div></section>
    <section className="block wrap flip"><div className="bimg" data-mask><Art tone={3} /></div><div className="btxt"><h2 data-split>From first brew to last call.</h2><p data-r>Mornings of quiet focus, afternoons of long conversations, evenings that glow.</p><Btn to="/experience" ghost>Explore</Btn></div></section>
    <section className="wrap sec"><div className="shead"><h2 data-split>Moments</h2><Btn to="/gallery" ghost>See Gallery</Btn></div>
      <div className="grid3">{[0, 4, 2].map(t => <div key={t} data-mask><Art tone={t} ratio="1/1" /></div>)}</div></section>
    <section className="wrap sec quote"><blockquote data-r>“{reviews[1][0]}”<cite>— {reviews[1][1]}</cite></blockquote><Btn to="/reviews" ghost>Read Reviews</Btn></section>
    <section className="wrap sec loc"><div><h2 data-split>Find us</h2><p data-r>21 Crescent Street, Mumbai · Open until 11 PM, midnight on weekends.</p></div><Btn to="/contact" ghost>Get Directions</Btn></section>
    <section className="cta"><h2 data-split>Save a table under the moon.</h2><Btn to="/contact">Reserve a Table</Btn></section></div>)
}
