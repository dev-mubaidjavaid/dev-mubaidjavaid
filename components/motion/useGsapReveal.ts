'use client'

import { useGSAP } from '@gsap/react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { RefObject } from 'react'

gsap.registerPlugin(ScrollTrigger, useGSAP)

type RevealOptions = {
  /** y offset to start from, default 36 */
  y?: number
  /** stagger between children, default 0.1 */
  stagger?: number
  /** delay before animation, default 0 */
  delay?: number
  /** Start trigger e.g. 'top 85%', default 'top 82%' */
  start?: string
}

/**
 * Drop-in GSAP ScrollTrigger reveal for any section container.
 * Targets direct children tagged with [data-reveal] or the container itself.
 * Honors prefers-reduced-motion via gsap.matchMedia (gsap-core / gsap-react).
 */
export function useGsapReveal (
  containerRef: RefObject<HTMLElement | null>,
  options: RevealOptions = {}
) {
  const { y = 36, stagger = 0.1, delay = 0, start = 'top 82%' } = options

  useGSAP(
    () => {
      if (!containerRef.current) return

      const mm = gsap.matchMedia()

      mm.add('(prefers-reduced-motion: reduce)', () => {
        const targets = containerRef.current!.querySelectorAll('[data-reveal]')
        const els =
          targets.length > 0
            ? Array.from(targets)
            : [containerRef.current!]
        gsap.set(els, { clearProps: 'all', opacity: 1, y: 0 })
      })

      mm.add('(prefers-reduced-motion: no-preference)', () => {
        const targets = containerRef.current!.querySelectorAll('[data-reveal]')
        const els =
          targets.length > 0
            ? Array.from(targets)
            : [containerRef.current!]

        gsap.fromTo(
          els,
          { opacity: 0, y },
          {
            opacity: 1,
            y: 0,
            duration: 0.7,
            delay,
            stagger,
            ease: 'power3.out',
            scrollTrigger: {
              trigger: containerRef.current!,
              start,
              once: true
            }
          }
        )
      })

      return () => mm.revert()
    },
    { scope: containerRef }
  )
}
