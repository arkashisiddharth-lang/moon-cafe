import { useEffect, useLayoutEffect, useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { ScrollToPlugin } from 'gsap/ScrollToPlugin'
gsap.registerPlugin(ScrollTrigger, ScrollToPlugin)
export { gsap, ScrollTrigger }
export const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
export function usePage(title: string, desc: string) {
  useEffect(() => {
    document.title = title
    document.querySelector('meta[name=description]')?.setAttribute('content', desc)
  }, [title, desc])
}
/** Scroll reveals: [data-r] fade/lift, [data-mask] clip-path image reveal, [data-split] staggered words, [data-par] parallax */
export function useReveal() {
  const root = useRef<HTMLDivElement>(null)
  useLayoutEffect(() => {
    if (reduced()) return
    const ctx = gsap.context(() => {
      gsap.utils.toArray<HTMLElement>('[data-split]').forEach(el => {
        el.innerHTML = el.textContent!.split(' ').map(w => `<span class="w"><span>${w}</span></span>`).join(' ')
        gsap.from(el.querySelectorAll('.w > span'), { yPercent: 110, duration: .9, stagger: .06, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 88%' } })
      })
      gsap.utils.toArray<HTMLElement>('[data-r]').forEach(el => gsap.from(el, { y: 30, opacity: 0, duration: .8, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 90%' } }))
      gsap.utils.toArray<HTMLElement>('[data-mask]').forEach(el => gsap.from(el, { clipPath: 'inset(100% 0 0 0)', duration: 1.1, ease: 'power3.inOut', scrollTrigger: { trigger: el, start: 'top 88%' } }))
      gsap.utils.toArray<HTMLElement>('[data-par]').forEach(el => gsap.to(el, { yPercent: -8, ease: 'none', scrollTrigger: { trigger: el, scrub: true } }))
    }, root)
    return () => ctx.revert()
  }, [])
  return root
}
