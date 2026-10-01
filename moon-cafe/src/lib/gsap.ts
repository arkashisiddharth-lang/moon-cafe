import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ScrollToPlugin } from "gsap/ScrollToPlugin";

gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);
ScrollTrigger.config({ ignoreMobileResize: true });

export { gsap, ScrollTrigger };

export const prefersReducedMotion = (): boolean =>
  typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/**
 * Extra delay applied to animations that start inside the first viewport.
 * The page transition raises this while the moon wipe is still uncovering the page.
 */
export const entry = { delay: 0.1 };

export const viewDelay = (el: Element): number => {
  const r = el.getBoundingClientRect();
  return r.top < window.innerHeight * 0.92 ? entry.delay : 0;
};
