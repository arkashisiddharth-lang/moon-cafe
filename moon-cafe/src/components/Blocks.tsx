import Art from './Art'
export const Hero = ({ title, sub, tone = 0 }: { title: string; sub?: string; tone?: number }) =>
  <section className="phero wrap"><h1 data-split>{title}</h1>{sub && <p data-r className="lead">{sub}</p>}<div className="pimg" data-mask><Art tone={tone} ratio="21/9" /></div></section>
export const Block = ({ title, text, tone, flip, sub }: { title: string; text: string; tone: number; flip?: boolean; sub?: string }) =>
  <section className={'block wrap' + (flip ? ' flip' : '')}>
    <div className="bimg" data-mask><div data-par><Art tone={tone} ratio="4/5" /></div></div>
    <div className="btxt">{sub && <small data-r>{sub}</small>}<h2 data-split>{title}</h2><p data-r>{text}</p></div></section>
