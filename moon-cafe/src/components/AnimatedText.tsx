import { useLayoutEffect, useRef, type ElementType } from "react";
import { gsap, prefersReducedMotion, viewDelay } from "../lib/gsap";

type Props = {
  text: string;
  as?: "h1" | "h2" | "h3" | "h4" | "p" | "div";
  className?: string;
  by?: "words" | "chars";
  delay?: number;
  stagger?: number;
  /** Wait for the element to scroll into view (default). Set false to play on mount. */
  scroll?: boolean;
};

/**
 * Masked text reveal. Use "\n" in `text` for hard line breaks.
 * The real text is exposed through aria-label; the split spans are hidden from assistive tech.
 */
export default function AnimatedText({ text, as = "h2", className = "", by = "words", delay = 0, stagger, scroll = true }: Props) {
  const ref = useRef<HTMLElement>(null);
  const Tag = as as ElementType;
  const lines = text.split("\n");

  useLayoutEffect(() => {
    const el = ref.current;
    if (!el || prefersReducedMotion()) return;
    const ctx = gsap.context(() => {
      const items = el.querySelectorAll(".at-i");
      const vars: gsap.TweenVars = {
        yPercent: 118,
        duration: 1,
        ease: "power4.out",
        stagger: stagger ?? (by === "chars" ? 0.045 : 0.07),
        delay: delay + viewDelay(el),
      };
      if (scroll) vars.scrollTrigger = { trigger: el, start: "top 90%", once: true };
      gsap.from(items, vars);
    }, el);
    return () => ctx.revert();
  }, [text, by, delay, stagger, scroll]);

  return (
    <Tag ref={ref} className={`at ${className}`.trim()} aria-label={text.replace(/\n/g, " ")}>
      {lines.map((line, li) => (
        <span className="at-l" aria-hidden="true" key={li}>
          {line.split(" ").map((word, wi) => (
            <span className="at-word" key={wi}>
              {by === "chars" ? (
                Array.from(word).map((ch, ci) => (
                  <span className="at-w" key={ci}>
                    <span className="at-i">{ch}</span>
                  </span>
                ))
              ) : (
                <span className="at-w">
                  <span className="at-i">{word}</span>
                </span>
              )}
              {" "}
            </span>
          ))}
        </span>
      ))}
    </Tag>
  );
}
