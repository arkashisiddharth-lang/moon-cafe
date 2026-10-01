import type { ReactNode } from "react";
import TLink from "./TLink";

type Props = {
  children: ReactNode;
  to?: string;
  href?: string;
  onClick?: () => void;
  type?: "button" | "submit";
  variant?: "solid" | "ghost" | "gold";
  arrow?: boolean;
  disabled?: boolean;
  className?: string;
};

const Arrow = () => (
  <svg className="btn__arrow" width="18" height="12" viewBox="0 0 18 12" fill="none" aria-hidden="true">
    <path d="M1 6h15M11 1l5 5-5 5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

export default function Button({ children, to, href, onClick, type = "button", variant = "solid", arrow = true, disabled, className = "" }: Props) {
  const cls = `btn btn--${variant} ${className}`.trim();
  const inner = (
    <>
      <span className="btn__fill" aria-hidden="true" />
      <span className="btn__label">{children}</span>
      {arrow && <Arrow />}
    </>
  );
  if (to) return <TLink to={to} className={cls}>{inner}</TLink>;
  if (href) return <a href={href} className={cls} target="_blank" rel="noreferrer">{inner}</a>;
  return (
    <button type={type} className={cls} onClick={onClick} disabled={disabled}>
      {inner}
    </button>
  );
}
