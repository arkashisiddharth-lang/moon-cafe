import { Hero } from '../components/Blocks'
import { usePage, useReveal } from '../components/hooks'
import { reviews } from '../data'
export default function Reviews() {
  usePage('Moon Cafe Reviews', 'What guests say about Moon Cafe.'); const r = useReveal()
  return (<div ref={r}><Hero title="Kind words" sub="From guests who stayed longer than planned." tone={0} />
    <div className="wrap rlist">{reviews.map(([q, n]) => <blockquote key={n} data-r><div className="stars" aria-label="5 out of 5 stars">★★★★★</div>“{q}”<cite>— {n}</cite></blockquote>)}</div></div>)
}
