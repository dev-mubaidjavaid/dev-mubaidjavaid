/**
 * Original geometric patterns for portfolio frames — steel-navy family,
 * one accent per product category. Static SVG; no animation of its own.
 */
export type ProjectPatternTone =
  | 'teal'
  | 'violet'
  | 'rose'
  | 'sky'
  | 'emerald'
  | 'amber'

const TONES: Record<
  ProjectPatternTone,
  { ink: string; mid: string; soft: string }
> = {
  teal: { ink: '#0D9488', mid: '#14B8A6', soft: '#99F6E4' },
  violet: { ink: '#7C3AED', mid: '#8B5CF6', soft: '#DDD6FE' },
  rose: { ink: '#DB2777', mid: '#EC4899', soft: '#FBCFE8' },
  sky: { ink: '#0369A1', mid: '#0EA5E9', soft: '#BAE6FD' },
  emerald: { ink: '#059669', mid: '#10B981', soft: '#A7F3D0' },
  amber: { ink: '#D97706', mid: '#F59E0B', soft: '#FDE68A' }
}

export function toneForSlug (slug: string): ProjectPatternTone {
  if (slug.includes('hsms') || slug.includes('housing')) return 'teal'
  if (slug.includes('quik') || slug.includes('pos')) return 'violet'
  if (slug.includes('naaz') || slug.includes('commerce')) return 'rose'
  if (slug.includes('apex') || slug.includes('fintech')) return 'sky'
  if (slug.includes('surgi')) return 'emerald'
  if (slug.includes('vitalis') || slug.includes('health')) return 'amber'
  return 'sky'
}

export function ProjectPattern ({
  tone = 'sky',
  className
}: {
  tone?: ProjectPatternTone
  className?: string
}) {
  const c = TONES[tone]
  const id = `pp-${tone}`

  return (
    <svg
      className={className}
      viewBox='0 0 400 400'
      preserveAspectRatio='xMidYMid slice'
      aria-hidden
    >
      <defs>
        <pattern
          id={`${id}-grid`}
          width='28'
          height='28'
          patternUnits='userSpaceOnUse'
        >
          <path
            d='M28 0H0V28'
            fill='none'
            stroke={c.ink}
            strokeOpacity='0.12'
            strokeWidth='1'
          />
        </pattern>
        <pattern
          id={`${id}-dots`}
          width='16'
          height='16'
          patternUnits='userSpaceOnUse'
        >
          <circle cx='1.5' cy='1.5' r='1.1' fill={c.mid} fillOpacity='0.35' />
        </pattern>
        <linearGradient id={`${id}-wash`} x1='0' y1='0' x2='1' y2='1'>
          <stop offset='0%' stopColor={c.ink} stopOpacity='0.22' />
          <stop offset='55%' stopColor={c.mid} stopOpacity='0.08' />
          <stop offset='100%' stopColor='#F4F7FA' stopOpacity='0' />
        </linearGradient>
      </defs>
      <rect width='400' height='400' fill={`url(#${id}-grid)`} />
      <rect width='400' height='400' fill={`url(#${id}-dots)`} />
      <rect width='400' height='400' fill={`url(#${id}-wash)`} />
      <path
        d='M0 320 Q120 260 220 300 T400 240 L400 400 L0 400 Z'
        fill={c.ink}
        fillOpacity='0.08'
      />
      <circle cx='320' cy='80' r='56' fill={c.soft} fillOpacity='0.45' />
      <circle
        cx='320'
        cy='80'
        r='56'
        fill='none'
        stroke={c.ink}
        strokeOpacity='0.25'
        strokeWidth='1.5'
      />
      <rect
        x='36'
        y='48'
        width='72'
        height='8'
        rx='2'
        fill={c.ink}
        fillOpacity='0.55'
      />
      <rect
        x='36'
        y='66'
        width='48'
        height='6'
        rx='2'
        fill={c.mid}
        fillOpacity='0.4'
      />
    </svg>
  )
}
