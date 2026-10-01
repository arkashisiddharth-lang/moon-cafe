import { createContext, useCallback, useContext, useLayoutEffect, useRef, type ReactNode } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { entry, gsap, prefersReducedMotion, ScrollTrigger } from "../lib/gsap";

type TransitionApi = { go: (to: string) => void };

const TransitionContext = createContext<TransitionApi>({ go: () => undefined });

export const useTransition = () => useContext(TransitionContext);

const COVER_FROM = "circle(0% at 50% 100%)";
const COVER_TO = "circle(150% at 50% 100%)";
const UNCOVER_TO = "circle(0% at 50% 0%)";

/**
 * Page transitions.
 * Leaving: a charcoal "moon" rises from the bottom edge and covers the page while the old page lifts away.
 * Arriving: the circle closes toward the top while the new page settles in.
 */
export function TransitionProvider({ children }: { children: ReactNode }) {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const overlay = useRef<HTMLDivElement>(null);
  const mark = useRef<HTMLDivElement>(null);
  const covering = useRef(false);
  const busy = useRef(false);
  const firstRun = useRef(true);
  const pathRef = useRef(pathname);
  pathRef.current = pathname;

  const go = useCallback(
    (to: string) => {
      const target = to.split("#")[0] || "/";
      if (busy.current) return;
      if (target === pathRef.current) {
        gsap.to(window, { scrollTo: 0, duration: 0.8, ease: "power3.inOut" });
        return;
      }
      const el = overlay.current;
      if (prefersReducedMotion() || !el) {
        navigate(to);
        return;
      }
      busy.current = true;
      covering.current = true;
      entry.delay = 0.55;

      const page = document.querySelector("[data-page]");
      const tl = gsap.timeline({
        onComplete: () => {
          window.scrollTo(0, 0);
          navigate(to);
        },
      });
      tl.set(el, { autoAlpha: 1 }, 0);
      tl.fromTo(el, { clipPath: COVER_FROM }, { clipPath: COVER_TO, duration: 0.65, ease: "power3.inOut" }, 0);
      if (page) tl.to(page, { opacity: 0.25, y: -30, duration: 0.65, ease: "power2.in" }, 0);
      if (mark.current) tl.fromTo(mark.current, { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out" }, 0.3);
    },
    [navigate],
  );

  useLayoutEffect(() => {
    const el = overlay.current;
    const page = document.querySelector("[data-page]");

    const finish = () => {
      if (el) gsap.set(el, { autoAlpha: 0 });
      covering.current = false;
      busy.current = false;
      entry.delay = 0.1;
      ScrollTrigger.refresh();
    };

    if (firstRun.current) {
      firstRun.current = false;
      if (prefersReducedMotion() || !el) return;
      // Opening moment: the wipe reveals the site once.
      covering.current = true;
      entry.delay = 0.55;
      gsap.set(el, { autoAlpha: 1, clipPath: COVER_TO });
      const tl = gsap.timeline({ delay: 0.35, onComplete: finish });
      if (mark.current) {
        tl.fromTo(mark.current, { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }, 0);
        tl.to(mark.current, { opacity: 0, duration: 0.25 }, 0.55);
      }
      tl.to(el, { clipPath: UNCOVER_TO, duration: 0.8, ease: "power3.inOut" }, 0.6);
      return;
    }

    if (!covering.current) {
      // Browser back / forward or a programmatic navigation: a quick fade is enough.
      window.scrollTo(0, 0);
      if (page && !prefersReducedMotion()) {
        gsap.fromTo(page, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out", clearProps: "transform,opacity" });
      }
      requestAnimationFrame(() => ScrollTrigger.refresh());
      return;
    }

    if (!el) return finish();
    const tl = gsap.timeline({ delay: 0.08, onComplete: finish });
    if (mark.current) tl.to(mark.current, { opacity: 0, duration: 0.25 }, 0);
    tl.to(el, { clipPath: UNCOVER_TO, duration: 0.7, ease: "power3.inOut" }, 0);
    if (page) {
      tl.fromTo(page, { y: 50, opacity: 0.4 }, { y: 0, opacity: 1, duration: 0.9, ease: "power3.out", clearProps: "transform,opacity" }, 0.05);
    }
  }, [pathname]);

  return (
    <TransitionContext.Provider value={{ go }}>
      {children}
      <div ref={overlay} className="t-overlay" aria-hidden="true">
        <div ref={mark} className="t-mark">
          <span className="t-mark__moon" />
          <span className="t-mark__name">Moon Cafe</span>
        </div>
      </div>
    </TransitionContext.Provider>
  );
}
