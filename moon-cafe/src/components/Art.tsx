const IMAGES = [
  '/images/hero-night.svg',
  '/images/moon-latte.svg',
  '/images/about-preview.svg',
  '/images/experience-preview.svg',
  '/images/gallery-1.svg',
  '/images/gallery-2.svg',
  '/images/gallery-3.svg',
  '/images/gallery-4.svg',
  '/images/gallery-5.svg',
  '/images/gallery-6.svg',
  '/images/gallery-7.svg',
  '/images/gallery-8.svg',
  '/images/gallery-9.svg',
  '/images/classic-tiramisu.svg',
  '/images/midnight-cold-brew.svg',
];

export default function Art({ tone = 0, ratio = '4/5', label }: { tone?: number; ratio?: string; label?: string }) {
  const src = IMAGES[Math.abs(tone) % IMAGES.length];
  return (
    <div className="art" role="img" aria-label={label || 'Moon Cafe'} style={{ aspectRatio: ratio }}>
      <img src={src} alt="" loading="lazy" decoding="async" />
      <i aria-hidden="true" />
    </div>
  );
}
