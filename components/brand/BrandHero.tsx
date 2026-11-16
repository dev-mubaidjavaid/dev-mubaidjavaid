'use client'

import { TrackedCtaLink } from '@/components/analytics/TrackedCtaLink'
import { MotionRevealIn } from '@/components/brand/system/MotionReveal'
import { heroContent, site } from '@/data/site'
import { ArrowUpRight } from 'lucide-react'

/**
 * Hero — brand-first, one composition: name, positioning, value, CTAs, ink portrait.
 * Skills: frontend-design + emil-design-eng + animate (entrance via MotionRevealIn).
 */
export function BrandHero () {
  return (
    <section
      id='hero'
      data-hero-theme='ink'
      className='relative min-h-[100svh] overflow-hidden bg-ink-deep text-white'
    >
      <div
        className='pointer-events-none absolute inset-0 opacity-[0.35]'
        aria-hidden
        style={{
          backgroundImage:
            'radial-gradient(circle, rgba(255,255,255,0.22) 0.7px, transparent 0.8px)',
          backgroundSize: '22px 22px'
        }}
      />

      <div
        className='pointer-events-none absolute -right-24 top-1/4 h-[55%] w-[50%] rounded-full bg-highlight/20 blur-3xl'
        aria-hidden
      />
      <div
        className='pointer-events-none absolute -left-20 bottom-0 h-[40%] w-[40%] rounded-full bg-primary/40 blur-3xl'
        aria-hidden
      />

      <div className='pointer-events-none absolute inset-y-0 right-0 w-[58%] max-w-2xl overflow-hidden'>
        <picture>
          <source
            media='(min-width: 768px)'
            srcSet='/mubaidjavaid-hero-cutout.webp?v=4'
            type='image/webp'
          />
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src='/mubaidjavaid-hero-cutout-sm.webp?v=4'
            alt={`${site.name}, ${site.role} based in ${site.location}`}
            width={1632}
            height={2610}
            fetchPriority='high'
            decoding='async'
            className='absolute inset-x-0 bottom-0 top-[10%] h-[90%] w-full object-contain object-bottom opacity-[0.38]'
          />
        </picture>
        {/* Soft left + bottom blend into ink so the cutout stays quiet behind copy */}
        <div
          className='absolute inset-0'
          style={{
            background:
              'linear-gradient(90deg, hsl(var(--ink-deep)) 0%, hsl(var(--ink-deep) / 0.72) 34%, hsl(var(--ink-deep) / 0.2) 62%, transparent 100%)'
          }}
        />
        <div
          className='absolute inset-x-0 bottom-0 h-[28%]'
          style={{
            background:
              'linear-gradient(to top, hsl(var(--ink-deep)), transparent)'
          }}
        />
      </div>

      <div className='relative z-10 mx-auto flex min-h-[100svh] max-w-[1180px] flex-col justify-center px-6 pb-24 pt-28 md:px-10 lg:px-12'>
        <MotionRevealIn className='max-w-xl lg:max-w-2xl'>
          <p className='font-mono text-xs tracking-wide text-highlight-on-ink'>
            {site.role} · {site.roleSecondary} · {site.location}
          </p>

          <p className='mt-5 font-display text-[clamp(2.75rem,6.5vw,4.75rem)] font-bold leading-[1.05] tracking-[-0.025em] text-white text-balance'>
            {site.name}
          </p>

          <h1 className='mt-6 max-w-[18ch] font-display text-[clamp(1.35rem,2.8vw,2rem)] font-semibold leading-[1.2] tracking-[-0.02em] text-white/95 text-pretty'>
            {heroContent.line}
          </h1>

          <p className='mt-5 max-w-[42ch] text-base leading-relaxed text-white/65 md:text-lg'>
            {heroContent.paragraph}
          </p>

          <p className='mt-4 inline-flex items-center gap-2 font-mono text-xs tracking-wide text-highlight-on-ink/90'>
            <span
              className='h-1.5 w-1.5 shrink-0 rounded-full bg-highlight-on-ink'
              aria-hidden
            />
            {heroContent.availability}
          </p>

          <ul
            className='mt-6 flex max-w-xl flex-wrap gap-2'
            aria-label='Focus areas'
          >
            {heroContent.skills.map(skill => (
              <li
                key={skill}
                className='border border-white/20 bg-white/[0.06] px-3.5 py-1.5 text-xs font-semibold tracking-tight text-white/90 md:text-sm'
              >
                {skill}
              </li>
            ))}
          </ul>

          <div className='mt-10 flex flex-wrap items-center gap-4'>
            <TrackedCtaLink
              href='/contact'
              event='discuss_project'
              detail='brand_hero'
              className='cta-primary-ink'
            >
              Discuss your project
              <ArrowUpRight className='h-3.5 w-3.5' aria-hidden />
            </TrackedCtaLink>
            <TrackedCtaLink
              href='/projects'
              event='view_work'
              detail='brand_hero'
              className='inline-flex min-h-11 items-center gap-1.5 px-1 text-sm font-semibold text-white/75 transition-colors duration-200 hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/40'
            >
              Explore my work
              <ArrowUpRight className='h-3.5 w-3.5' aria-hidden />
            </TrackedCtaLink>
          </div>
        </MotionRevealIn>
      </div>
    </section>
  )
}
