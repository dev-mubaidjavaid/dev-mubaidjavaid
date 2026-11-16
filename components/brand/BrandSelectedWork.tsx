'use client'

import {
  ProjectPattern,
  toneForSlug
} from '@/components/brand/patterns/ProjectPattern'
import { BrandSection } from '@/components/brand/system/BrandSection'
import { useGsapReveal } from '@/components/motion/useGsapReveal'
import { brandMotion, brandType } from '@/lib/brand-system'
import { selectedWorkProjects } from '@/lib/homepage-media'
import { cn } from '@/lib/utils'
import { useGSAP } from '@gsap/react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { ArrowUpRight } from 'lucide-react'
import Image from 'next/image'
import Link from 'next/link'
import { useRef } from 'react'

gsap.registerPlugin(ScrollTrigger, useGSAP)

function encodeSrc (src: string) {
  return encodeURI(src)
}

function isSvg (src: string) {
  return /\.svg($|\?)/i.test(src)
}

/**
 * Portfolio band — original pattern frames + product visuals + scroll choreography.
 * Purpose: spatial continuity + explanation (marketing showcase). Animate skill lane.
 */
export function BrandSelectedWork () {
  const featured = selectedWorkProjects()
  const headerRef = useRef<HTMLDivElement | null>(null)
  const listRef = useRef<HTMLUListElement | null>(null)

  useGsapReveal(headerRef, { y: brandMotion.revealY, stagger: 0.08, start: 'top 82%' })

  useGSAP(
    () => {
      if (!listRef.current) return
      const mm = gsap.matchMedia()

      mm.add('(prefers-reduced-motion: reduce)', () => {
        listRef.current
          ?.querySelectorAll('[data-work-media], [data-work-copy]')
          .forEach(el => {
            gsap.set(el, { clearProps: 'all', opacity: 1, y: 0, clipPath: 'none' })
          })
      })

      mm.add('(prefers-reduced-motion: no-preference)', () => {
        const rows = listRef.current!.querySelectorAll('[data-work-row]')
        rows.forEach(row => {
          const media = row.querySelector('[data-work-media]')
          const copy = row.querySelectorAll('[data-work-copy]')
          if (media) {
            gsap.fromTo(
              media,
              { clipPath: 'inset(12% 8% 12% 8%)', opacity: 0.55, y: 28 },
              {
                clipPath: 'inset(0% 0% 0% 0%)',
                opacity: 1,
                y: 0,
                duration: brandMotion.durationSlow,
                ease: 'power3.out',
                scrollTrigger: {
                  trigger: row,
                  start: 'top 78%',
                  once: true
                }
              }
            )
          }
          if (copy.length) {
            gsap.fromTo(
              copy,
              { opacity: 0, y: 22 },
              {
                opacity: 1,
                y: 0,
                duration: brandMotion.duration,
                stagger: brandMotion.stagger,
                ease: 'power3.out',
                scrollTrigger: {
                  trigger: row,
                  start: 'top 80%',
                  once: true
                }
              }
            )
          }
        })
      })

      return () => mm.revert()
    },
    { scope: listRef }
  )

  return (
    <BrandSection
      id='work'
      layout='band'
      className='relative min-h-0 overflow-hidden bg-[hsl(214_28%_98%)]'
    >
      <div
        className='pointer-events-none absolute inset-0 opacity-[0.45]'
        aria-hidden
        style={{
          backgroundImage:
            'radial-gradient(circle, hsl(211 45% 35% / 0.07) 0.7px, transparent 0.8px)',
          backgroundSize: '22px 22px'
        }}
      />

      <div
        ref={headerRef}
        data-reveal
        className='relative mx-auto flex w-full max-w-[1280px] flex-col gap-6 px-6 pb-10 pt-16 sm:px-8 md:flex-row md:items-end md:justify-between md:px-10 md:pb-14 md:pt-20 lg:px-12'
      >
        <div className='max-w-xl'>
          <p className='font-mono text-xs tracking-wide text-highlight'>
            Portfolio · Selected work
          </p>
          <h2 className={cn('mt-4', brandType.title)}>
            Products you can
            <br />
            <span className='text-highlight'>inspect.</span>
          </h2>
          <p className='mt-5 max-w-[46ch] text-sm leading-relaxed text-body md:text-base'>
            Featured case studies with real product frames — problem, stack, and
            the architecture decisions behind each build.
          </p>
        </div>
        <Link
          href='/projects'
          className='cta-primary group inline-flex shrink-0'
        >
          View all work
          <ArrowUpRight
            size={15}
            className='transition-transform group-hover:-translate-y-0.5 group-hover:translate-x-0.5'
            aria-hidden
          />
        </Link>
      </div>

      <ul ref={listRef} className='relative border-t border-heading/10'>
        {featured.map((project, i) => {
          const short = project.title.split('—')[0].trim()
          const img = project.images?.[0] ?? project.image
          const reverse = i % 2 === 1
          const tone = toneForSlug(project.slug)
          const category =
            project.stack.includes('Firebase') && project.slug.includes('pos')
              ? 'SaaS · Point of sale'
              : project.slug.includes('naaz')
                ? 'Commerce · D2C'
                : project.slug.includes('apex')
                  ? 'Fintech · Platform'
                  : project.slug.includes('hsms')
                    ? 'SaaS · Operations'
                    : project.role

          return (
            <li
              key={project.slug}
              data-work-row
              className='border-b border-heading/10'
            >
              <Link
                href={`/projects/${project.slug}`}
                className={cn(
                  'group mx-auto grid w-full max-w-[1280px] lg:grid-cols-12',
                  reverse && 'lg:[&>*:first-child]:order-2'
                )}
              >
                <div
                  data-work-media
                  className='relative min-h-[42vh] overflow-hidden lg:col-span-7 lg:min-h-[min(58vh,520px)]'
                >
                  <ProjectPattern
                    tone={tone}
                    className='absolute inset-0 h-full w-full'
                  />
                  <div className='absolute inset-6 overflow-hidden border border-heading/10 bg-background shadow-[0_24px_60px_-28px_rgba(18,26,40,0.45)] md:inset-10'>
                    <Image
                      src={encodeSrc(img)}
                      alt={project.imageAlt ?? short}
                      fill
                      sizes='(max-width: 1024px) 100vw, 58vw'
                      className='object-cover object-top transition-transform duration-700 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.03]'
                      unoptimized={isSvg(img)}
                      priority={i === 0}
                    />
                    <div
                      className='pointer-events-none absolute inset-0 bg-gradient-to-t from-heading/20 via-transparent to-transparent'
                      aria-hidden
                    />
                  </div>
                  <span className='absolute left-6 top-6 z-10 border border-white/25 bg-black px-2.5 py-1.5 font-mono text-xs font-semibold tracking-wide text-white md:left-10 md:top-10'>
                    {String(i + 1).padStart(2, '0')} /{' '}
                    {String(featured.length).padStart(2, '0')}
                  </span>
                </div>

                <div className='relative flex flex-col justify-center overflow-hidden px-6 py-10 sm:px-8 md:px-10 lg:col-span-5 lg:px-12 lg:py-16'>
                  <span
                    className='pointer-events-none absolute -right-[0.04em] -top-[0.12em] font-display text-[6.5rem] font-bold leading-none tracking-[-0.08em] text-heading/[0.035]'
                    aria-hidden
                  >
                    {String(i + 1).padStart(2, '0')}
                  </span>

                  <p
                    data-work-copy
                    className='font-mono text-xs tracking-wide text-highlight'
                  >
                    {category}
                  </p>
                  <h3
                    data-work-copy
                    className={cn(
                      'mt-3',
                      brandType.title,
                      'text-[clamp(1.75rem,3vw,2.5rem)] transition-colors duration-300 group-hover:text-highlight'
                    )}
                  >
                    {short}
                  </h3>
                  <p
                    data-work-copy
                    className='mt-4 max-w-[42ch] text-sm leading-relaxed text-body md:text-base'
                  >
                    {project.problem}
                  </p>
                  <p
                    data-work-copy
                    className='mt-6 font-mono text-xs tracking-wide text-heading/40'
                  >
                    {project.stack.slice(0, 5).join(' · ')}
                  </p>
                  <span
                    data-work-copy
                    className='mt-8 inline-flex items-center gap-2 text-sm font-semibold text-heading'
                  >
                    Open case study
                    <ArrowUpRight
                      size={15}
                      className='transition-transform duration-300 group-hover:-translate-y-0.5 group-hover:translate-x-0.5'
                      aria-hidden
                    />
                  </span>
                </div>
              </Link>
            </li>
          )
        })}
      </ul>
    </BrandSection>
  )
}
