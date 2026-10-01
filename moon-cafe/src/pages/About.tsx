import { Block, Hero } from '../components/Blocks'
import { usePage, useReveal } from '../components/hooks'
export default function About() {
  usePage('About Moon Cafe', 'The story, philosophy, coffee and space behind Moon Cafe.'); const r = useReveal()
  return (<div ref={r}><Hero title="More Than Coffee." sub="Moon Cafe is a place to slow down, meet good people, and stay a little longer." tone={1} />
    <Block sub="Our Story" title="Born after midnight." text="Moon Cafe started as late-night conversations between friends who couldn't find a quiet place to keep talking. So we built one." tone={0} />
    <Block flip sub="Our Philosophy" title="Unhurried by design." text="No rush, no turnover. Every cup is made to be finished slowly, and every table is meant to be kept." tone={2} />
    <Block sub="Our Coffee" title="Small lots, careful roasts." text="Single-origin beans from Indian estates, roasted in small batches and pulled the way they deserve." tone={3} />
    <Block flip sub="Our Space" title="Warm light, deep corners." text="Dark wood, soft amber lamps and window seats made for long evenings." tone={4} /></div>)
}
