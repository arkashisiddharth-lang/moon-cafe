import { useLayoutEffect, useRef, type ElementType, type ReactNode } from "react";
import { gsap, prefersReducedMotion, viewDelay } from "../lib/gsap";

type Props = {
  children: ReactNode;
  as?: "div" | "p" | "ul" | "section" | "figure" | "blockquote" | "li";
  className?: string;
  /** Animate each direct child in sequence instead of the element itself. */
  stagger?: boolean;
  y?: number;
  delay?: number;
};

/** Scroll-triggered fade and rise for supporting content. */
export default function Reveal({ children, as = "div", className = "", stagger = false, y = 28, delay = 0 }: Props) {
  const ref = useRef<HTMLElement>(null);
  const Tag = as as ElementType;

  useLayoutEffect(() => {
    const el = ref.current;
    if (!el || prefersReducedMotion()) return;
    const ctx = gsap.context(() => {
      const targets = stagger ? Array.from(el.children) : el;
      gsap.from(targets, {
        opacity: 0,
        y,
        duration: 0.9,
        ease: "power3.out",
        stagger: stagger ? 0.1 : 0,
        delay: delay + viewDelay(el),
        scrollTrigger: { trigger: el, start: "top 88%", once: true },
      });
    }, el);
    return () => ctx.revert();
  }, [stagger, y, delay]);

  return (
    <Tag ref={ref} className={className}>
      {children}
    </Tag>
  );
}
