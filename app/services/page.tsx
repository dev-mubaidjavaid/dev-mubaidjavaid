import { TrackedCtaLink } from '@/components/analytics/TrackedCtaLink'
import { PageHeroHeader } from '@/components/sections/PageHeroHeader'
import { services } from '@/data/site'
import { brandType } from '@/lib/brand-system'
import { pageMetadata } from '@/lib/seo'
import { cn } from '@/lib/utils'
import {
  ArrowUpRight,
  Boxes,
  Gauge,
  Layers3,
  Workflow,
  type LucideIcon
} from 'lucide-react'
import type { Metadata } from 'next'
import Link from 'next/link'

export const dynamic = 'force-static'
export const revalidate = 86400

export const metadata: Metadata = pageMetadata({
  title: 'Hire Next.js & MERN Developer',
  description:
    'Contract and freelance full-stack development: Next.js, MERN, SaaS MVPs, fintech and healthcare web apps. Based in Multan, open to remote. Discuss your project.',
  path: '/services'
})

const serviceIcons: LucideIcon[] = [Boxes, Layers3, Gauge, Workflow]
const servicePhases = ['Build', 'Operate', 'Domain', 'Modernize'] as const

export default function ServicesPage () {
  return (
    <>
      <PageHeroHeader
        subtitle='Services · Hire Next.js & MERN'
        watermark='HIRE'
        title={
          <>
            What you can hire
            <br />
            <span className='text-highlight'>me to build.</span>
          </>
        }
        description='Specific delivery for founders and companies who need production MERN / Next.js systems — SaaS, fintech, healthcare, and operational platforms. Based in Multan, available remotely.'
      >
        <div className='flex flex-wrap items-center gap-4'>
          <TrackedCtaLink
            href='/contact'
            event='discuss_project'
            detail='services_hero'
            className='cta-primary'
          >
            Discuss your project
            <ArrowUpRight size={15} aria-hidden />
          </TrackedCtaLink>
          <Link
            href='/projects'
            className='inline-flex min-h-11 items-center gap-1.5 text-sm font-semibold text-heading transition-colors hover:text-primary'
          >
            Review case studies
            <ArrowUpRight size={15} aria-hidden />
          </Link>
        </div>
      </PageHeroHeader>

      <section className='relative isolate overflow-hidden bg-background'>
        <div className='mx-auto w-full max-w-[1280px] px-6 py-6 sm:px-8 md:px-10 lg:px-12'>
          <div className='flex items-center gap-4 border-b border-heading/10 pb-5'>
            <p className='font-mono text-xs tracking-wide text-heading/[0.35]'>
              Delivery system
            </p>
            <span className='h-px flex-1 bg-heading/10' aria-hidden />
            <p className='font-mono text-xs tracking-wide text-highlight'>
              Scope → Ship → Handover
            </p>
          </div>
        </div>

        <ul>
          {services.map((service, index) => {
            const Icon = serviceIcons[index] ?? Boxes
            const phase = servicePhases[index] ?? 'Build'
            return (
              <li key={service.title} className='border-b border-heading/10'>
                <article className='mx-auto grid w-full max-w-[1280px] gap-8 px-6 py-12 sm:px-8 md:px-10 md:py-16 lg:grid-cols-[0.85fr_1.15fr] lg:gap-14 lg:px-12'>
                  <div>
                    <div className='flex items-center gap-3'>
                      <span className='flex h-11 w-11 items-center justify-center rounded-full border border-heading/[0.15] text-highlight'>
                        <Icon size={17} strokeWidth={1.55} aria-hidden />
                      </span>
                      <p className='font-mono text-xs tracking-wide text-highlight'>
                        {String(index + 1).padStart(2, '0')} · {phase}
                      </p>
                    </div>
                    <h2 className={cn('mt-6', brandType.title)}>
                      {service.title}
                    </h2>
                    <p className='mt-4 max-w-[42ch] text-sm leading-relaxed text-body md:text-base'>
                      {service.description}
                    </p>
                    <p className='mt-6 max-w-[40ch] border-l-2 border-highlight pl-4 text-sm text-heading/70'>
                      <span className='font-semibold text-heading'>Who: </span>
                      {service.who}
                    </p>
                    <p className='mt-3 max-w-[40ch] text-sm text-body'>
                      <span className='font-semibold text-heading'>
                        Problem:{' '}
                      </span>
                      {service.problem}
                    </p>
                    <ul
                      className='mt-5 flex flex-wrap gap-2'
                      aria-label={`Technologies for ${service.title}`}
                    >
                      {service.tech.map(t => (
                        <li
                          key={t}
                          className='border border-heading/15 px-2.5 py-1 font-mono text-xs text-heading/70'
                        >
                          {t}
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div className='border-t border-heading/10 pt-6 lg:border-l lg:border-t-0 lg:pl-10 lg:pt-0'>
                    <p className='font-mono text-xs tracking-wide text-heading/[0.35]'>
                      What ships
                    </p>
                    <ul className='mt-4 divide-y divide-heading/10 border-y border-heading/10'>
                      {service.deliverables.map((item, deliverableIndex) => (
                        <li
                          key={item}
                          className='grid grid-cols-[2.25rem_1fr] gap-3 py-4 text-sm leading-relaxed text-heading'
                        >
                          <span className='font-mono text-xs text-highlight'>
                            {String(deliverableIndex + 1).padStart(2, '0')}
                          </span>
                          {item}
                        </li>
                      ))}
                    </ul>
                  </div>
                </article>
              </li>
            )
          })}
        </ul>

        <section
          id='how-i-work'
          className='mx-auto w-full max-w-[1280px] border-t border-heading/10 px-6 py-14 sm:px-8 md:px-10 md:py-20 lg:px-12'
        >
          <p className='font-mono text-xs tracking-wide text-highlight'>
            How I work
          </p>
          <h2 className={cn('mt-4 max-w-[18ch]', brandType.title)}>
            Remote-ready process from Multan.
          </h2>
          <p className='mt-4 max-w-[52ch] text-sm leading-relaxed text-body md:text-base'>
            Built for founders and CTOs who want staging URLs, written scope, and
            honest timelines — not vanity always-online claims.
          </p>
          <ol className='mt-10 grid gap-6 md:grid-cols-2 lg:grid-cols-4'>
            {[
              {
                t: 'Scope',
                d: 'One primary workflow, constraints, and definition of done before heavy build.'
              },
              {
                t: 'Staging',
                d: 'Clickable staging early. Decisions happen against a running product.'
              },
              {
                t: 'Async rhythm',
                d: 'PKT timezone with scheduled overlap. Weekly written updates with what changed / blocked.'
              },
              {
                t: 'Handover',
                d: 'Readable architecture, env docs, and a path your team can extend.'
              }
            ].map((item, i) => (
              <li key={item.t} className='border-t border-heading/10 pt-4'>
                <span className='font-mono text-xs text-highlight'>
                  {String(i + 1).padStart(2, '0')}
                </span>
                <p className='mt-2 font-display text-lg font-semibold text-heading'>
                  {item.t}
                </p>
                <p className='mt-2 text-sm leading-relaxed text-body'>{item.d}</p>
              </li>
            ))}
          </ol>
          <div className='mt-10 flex flex-wrap gap-3'>
            <Link
              href='/projects/quikpos-saas-point-of-sale'
              className='text-sm font-semibold text-heading underline-offset-4 hover:underline'
            >
              QuikPOS proof →
            </Link>
            <Link
              href='/projects/vitalis-health-healthcare-platform'
              className='text-sm font-semibold text-heading underline-offset-4 hover:underline'
            >
              Vitalis proof →
            </Link>
            <Link
              href='/blog/remote-engineer-pakistan-timezone-git-staging'
              className='text-sm font-semibold text-heading underline-offset-4 hover:underline'
            >
              Remote working notes →
            </Link>
          </div>
        </section>

        <div className='mx-auto flex w-full max-w-[1280px] flex-col gap-5 px-6 py-12 sm:flex-row sm:items-center sm:justify-between sm:px-8 md:px-10 lg:px-12'>
          <div>
            <p className='font-mono text-xs tracking-wide text-heading/[0.35]'>
              Good fit / not a fit
            </p>
            <p className='mt-3 max-w-[48ch] text-sm leading-relaxed text-body'>
              Best for founders and teams who want production systems with clear
              ownership. Not ideal for speculative UI-only experiments without a
              delivery path.
            </p>
          </div>
          <div className='flex flex-wrap gap-3'>
            <Link
              href='/projects'
              className='inline-flex border border-border px-5 py-2.5 text-sm font-medium text-heading transition-colors hover:border-heading'
            >
              Review case studies
            </Link>
            <TrackedCtaLink
              href='/contact'
              event='discuss_project'
              detail='services_footer'
              className='group inline-flex items-center gap-2 bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary-hover'
            >
              Discuss your project
              <ArrowUpRight
                size={15}
                className='transition-transform group-hover:-translate-y-0.5 group-hover:translate-x-0.5'
                aria-hidden
              />
            </TrackedCtaLink>
          </div>
        </div>
      </section>
    </>
  )
}
