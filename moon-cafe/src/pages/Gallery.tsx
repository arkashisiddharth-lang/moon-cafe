import Art from '../components/Art'
import { Hero } from '../components/Blocks'
import { usePage, useReveal } from '../components/hooks'
const shots: [number, string, string][] = [[0,'3/4','tall'],[1,'4/3',''],[2,'1/1',''],[3,'16/9','wide'],[4,'4/5',''],[1,'1/1',''],[0,'3/2','wide'],[3,'3/4','']]
export default function Gallery() {
  usePage('Moon Cafe Gallery', 'A look inside Moon Cafe: coffee, desserts, light and late-night corners.'); const r = useReveal()
  return (<div ref={r}><Hero title="Gallery" sub="Light, steam and slow evenings." tone={4} />
    <div className="wrap masonry">{shots.map(([t, ra, c], i) => <figure key={i} className={'mz ' + c} data-mask><div className="zoom"><Art tone={t} ratio={ra} label={`Moon Cafe photo ${i + 1}`} /></div></figure>)}</div></div>)
}
