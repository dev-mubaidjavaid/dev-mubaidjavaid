/**
 * Rasterize Figma SVG exports (embedded PNG) → WebP for production.
 * Usage (from repo root, after placing SVGs under public/Projects):
 *   node scripts/optimize-project-images.mjs
 * Then remap paths:
 *   node scripts/remap-project-images.mjs
 */
import sharp from 'sharp'
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const projectsRoot = path.join(root, 'public', 'Projects')

function walk (dir, out = []) {
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name)
    if (ent.isDirectory()) walk(p, out)
    else if (ent.name.toLowerCase().endsWith('.svg')) out.push(p)
  }
  return out
}

const files = walk(projectsRoot)
let ok = 0
let fail = 0
let saved = 0

for (const src of files) {
  const dir = path.dirname(src)
  const base = path.basename(src, '.svg').replace(/\s+/g, '-')
  const out = path.join(dir, `${base}.webp`)
  const before = fs.statSync(src).size
  try {
    await sharp(src, { density: 144, limitInputPixels: false })
      .resize({ width: 1600, withoutEnlargement: true })
      .webp({ quality: 72, effort: 4 })
      .toFile(out)
    saved += Math.max(0, before - fs.statSync(out).size)
    ok++
  } catch (e) {
    fail++
    console.error('FAIL', src, e.message)
  }
}

console.log({ ok, fail, savedMB: Math.round(saved / 1024 / 1024) })
