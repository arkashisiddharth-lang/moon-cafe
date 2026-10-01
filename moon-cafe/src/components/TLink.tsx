import type { AnchorHTMLAttributes, MouseEvent, ReactNode } from "react";
import { useTransition } from "../context/Transition";

type Props = Omit<AnchorHTMLAttributes<HTMLAnchorElement>, "href"> & { to: string; children: ReactNode };

/** An internal link that plays the GSAP page transition. Modified clicks (new tab etc.) behave normally. */
export default function TLink({ to, onClick, children, ...rest }: Props) {
  const { go } = useTransition();
  const handle = (e: MouseEvent<HTMLAnchorElement>) => {
    onClick?.(e);
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    go(to);
  };
  return (
    <a href={to} onClick={handle} {...rest}>
      {children}
    </a>
  );
}
