import { useLayoutEffect, useRef, type DependencyList } from "react";
import { gsap, prefersReducedMotion } from "../lib/gsap";

/**
 * Runs `build` inside a gsap.context scoped to the returned ref.
 * Everything created inside (tweens, ScrollTriggers) is reverted on cleanup.
 * Skipped entirely when the visitor prefers reduced motion.
 */
export function useGsapScope<T extends HTMLElement = HTMLDivElement>(
  build: (root: T) => void,
  deps: DependencyList = [],
) {
  const ref = useRef<T>(null);
  useLayoutEffect(() => {
    const root = ref.current;
    if (!root || prefersReducedMotion()) return;
    const ctx = gsap.context(() => build(root), root);
    return () => ctx.revert();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
  return ref;
}
