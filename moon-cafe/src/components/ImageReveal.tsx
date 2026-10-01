import { useLayoutEffect, useRef } from "react";
import { gsap, prefersReducedMotion, viewDelay } from "../lib/gsap";

type Props = {
  src: string;
  alt: string;
  width: number;
  height: number;
  /** CSS aspect-ratio, e.g. "4 / 5". Defaults to width / height. */
  ratio?: string;
  className?: string;
  /** Parallax amount in percent (max 6). 0 disables it. */
  parallax?: number;
  delay?: number;
  eager?: boolean;
  reveal?: boolean;
  sources?: { media: string; srcSet: string }[];
};

/** Image with a masked reveal, a settling zoom and optional scroll parallax. */
export default function ImageReveal({ src, alt, width, height, ratio, className = "", parallax = 0, delay = 0, eager = false, reveal = true, sources }: Props) {
  const wrap = useRef<HTMLDivElement>(null);
  const amount = Math.min(Math.max(parallax, 0), 6);

  useLayoutEffect(() => {
    const el = wrap.current;
    if (!el || prefersReducedMotion()) return;
    const img = el.querySelector("img");
    const ctx = gsap.context(() => {
      if (reveal) {
        const st = { trigger: el, start: "top 90%", once: true };
        const d = delay + viewDelay(el);
        gsap.fromTo(el, { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 1.1, ease: "power4.inOut", delay: d, scrollTrigger: st, clearProps: "clipPath" });
        if (img) gsap.from(img, { scale: 1.3, duration: 1.6, ease: "power3.out", delay: d, scrollTrigger: st });
      }
      if (amount > 0 && img) {
        gsap.fromTo(img, { yPercent: -amount }, { yPercent: amount, ease: "none", scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: true } });
      }
    }, el);
    return () => ctx.revert();
  }, [reveal, delay, amount]);

  return (
    <div ref={wrap} className={`imgr ${amount ? "imgr--parallax" : ""} ${className}`.trim()} style={{ aspectRatio: ratio ?? `${width} / ${height}` }}>
      <picture>
        {sources?.map((s) => <source key={s.media} media={s.media} srcSet={s.srcSet} />)}
        <img src={src} alt={alt} width={width} height={height} loading={eager ? "eager" : "lazy"} decoding="async" />
      </picture>
    </div>
  );
}
