'use client'

import {
  ProjectPattern,
  toneForSlug
} from '@/components/brand/patterns/ProjectPattern'
import { brandMotion, brandType } from '@/lib/brand-system'
import { projects } from '@/data/projects'
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
 * /projects case-study band — original pattern + product frame + scroll reveal.
 */
export function ProjectsPortfolioGrid () {
  const listRef = useRef<HTMLOListElement | null>(null)

  useGSAP(
    () => {
      if (!listRef.current) return
      const mm = gsap.matchMedia()

      mm.add('(prefers-reduced-motion: reduce)', () => {
        listRef.current
          ?.querySelectorAll('[data-case-media], [data-case-copy]')
          .forEach(el => {
            gsap.set(el, { clearProps: 'all', opacity: 1, y: 0, clipPath: 'none' })
          })
      })

      mm.add('(prefers-reduced-motion: no-preference)', () => {
        listRef.current!.querySelectorAll('[data-case-row]').forEach(row => {
          const media = row.querySelector('[data-case-media]')
          const copy = row.querySelectorAll('[data-case-copy]')
          if (media) {
            gsap.fromTo(
              media,
              { clipPath: 'inset(10% 6% 10% 6%)', opacity: 0.6, y: 24 },
              {
                clipPath: 'inset(0% 0% 0% 0%)',
                opacity: 1,
                y: 0,
                duration: brandMotion.durationSlow,
                ease: 'power3.out',
                scrollTrigger: { trigger: row, start: 'top 80%', once: true }
              }
            )
          }
          if (copy.length) {
            gsap.fromTo(
              copy,
              { opacity: 0, y: 18 },
              {
                opacity: 1,
                y: 0,
                duration: brandMotion.duration,
                stagger: brandMotion.stagger,
                ease: 'power3.out',
                scrollTrigger: { trigger: row, start: 'top 82%', once: true }
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
    <ol ref={listRef} className='space-y-0'>
      {projects.map((project, i) => {
        const short = project.title.split('—')[0].trim()
        const image = project.images?.[0] ?? project.image
        const reverse = i % 2 === 1
        const tone = toneForSlug(project.slug)

        return (
          <li
            key={project.slug}
            data-case-row
            className='border-b border-heading/10'
          >
            <Link
              href={`/projects/${project.slug}`}
              className={cn(
                'group mx-auto grid w-full max-w-[1280px] lg:grid-cols-2',
                reverse && 'lg:[&>*:first-child]:order-2'
              )}
            >
              <div
                data-case-media
                className='relative aspect-[16/10] overflow-hidden lg:aspect-auto lg:min-h-[380px]'
              >
                <ProjectPattern
                  tone={tone}
                  className='absolute inset-0 h-full w-full'
                />
                <div className='absolute inset-5 overflow-hidden border border-heading/10 bg-background shadow-[0_20px_50px_-24px_rgba(18,26,40,0.4)] md:inset-8'>
                  <Image
                    src={encodeSrc(image)}
                    alt={project.imageAlt ?? short}
                    fill
                    sizes='(max-width: 1024px) 100vw, 50vw'
                    className='object-cover object-top transition-transform duration-700 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.03]'
                    unoptimized={isSvg(image)}
                  />
                  <div
                    className='pointer-events-none absolute inset-0 bg-gradient-to-t from-heading/20 via-transparent to-transparent'
                    aria-hidden
                  />
                </div>
                <span className='absolute left-5 top-5 z-10 border border-white/25 bg-black px-2.5 py-1.5 font-mono text-xs font-semibold tracking-wide text-white md:left-8 md:top-8'>
                  Case {String(i + 1).padStart(2, '0')}
                </span>
              </div>

              <div className='relative flex flex-col justify-center overflow-hidden px-6 py-8 sm:px-8 md:px-10 md:py-12 lg:px-12'>
                <span
                  className='pointer-events-none absolute -right-[0.05em] -top-[0.18em] font-display text-[7.5rem] font-bold leading-none tracking-[-0.08em] text-heading/[0.03]'
                  aria-hidden
                >
                  {String(i + 1).padStart(2, '0')}
                </span>

                <p
                  data-case-copy
                  className='font-mono text-xs tracking-wide text-highlight'
                >
                  {project.role}
                </p>
                <h2
                  data-case-copy
                  className={cn(
                    'mt-3',
                    brandType.title,
                    'transition-colors group-hover:text-highlight'
                  )}
                >
                  {short}
                </h2>
                <p
                  data-case-copy
                  className='mt-4 max-w-[46ch] text-sm leading-relaxed text-body'
                >
                  {project.problem}
                </p>
                <p
                  data-case-copy
                  className='mt-3 max-w-[46ch] text-sm leading-relaxed text-body/80'
                >
                  {project.impact[0] ?? project.summary}
                </p>

                <p
                  data-case-copy
                  className='mt-6 font-mono text-xs tracking-wide text-heading/[0.35]'
                >
                  {project.stack.slice(0, 5).join(' · ')}
                </p>

                <span
                  data-case-copy
                  className='mt-7 inline-flex items-center gap-2 text-sm font-semibold text-heading'
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
    </ol>
  )
}
