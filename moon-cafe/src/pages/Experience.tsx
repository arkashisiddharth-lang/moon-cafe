import { Block, Hero } from '../components/Blocks'
import { usePage, useReveal } from '../components/hooks'
export default function Experience() {
  usePage('Moon Cafe Experience — Slow Down', 'From morning coffee to late-night moments: the Moon Cafe experience.'); const r = useReveal()
  return (<div ref={r}><Hero title="Slow down. Stay a little longer." tone={2} />
    <Block title="Morning Coffee" text="Fresh croissants, first espresso, and a quiet table by the window." tone={1} />
    <Block flip title="Afternoon Conversations" text="Laptops closed, voices low. Long lunches and longer catch-ups." tone={4} />
    <Block title="Evening Vibes" text="Lamps glow, the playlist softens, and the room fills with easy company." tone={3} />
    <Block flip title="Late Night Moments" text="Dessert, one more coffee, and the city quiet outside until midnight." tone={0} /></div>)
}
