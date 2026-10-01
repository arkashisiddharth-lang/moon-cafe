# Moon Cafe
Multi-page café demo: React 18, TypeScript, Vite, React Router, GSAP + ScrollTrigger.

    npm install
    npm run dev      # http://localhost:5173
    npm run build    # type-check + production build

Routes: `/`, `/menu`, `/about`, `/experience`, `/gallery`, `/reviews`, `/contact`.
Imagery is generated from CSS/SVG (`components/Art.tsx`) — swap `<Art/>` for `<img>` tags to use real photos.
Animations respect `prefers-reduced-motion`.
