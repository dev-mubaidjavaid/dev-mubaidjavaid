import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const projectsFile = path.join(root, 'data', 'projects.ts')
let text = fs.readFileSync(projectsFile, 'utf8')

const before = [...text.matchAll(/\/Projects\/[^"']+\.svg/g)].length
text = text.replace(/\/Projects\/[^"']+\.svg/g, (match) => {
  const i = match.lastIndexOf('/')
  const dir = match.slice(0, i + 1)
  const file = match
    .slice(i + 1)
    .replace(/\.svg$/i, '.webp')
    .replace(/\s+/g, '-')
  return dir + file
})
fs.writeFileSync(projectsFile, text)

const refs = [...text.matchAll(/"(\/Projects\/[^"]+)"/g)].map((m) => m[1])
const missing = refs.filter((r) => !fs.existsSync(path.join(root, 'public', r)))
console.log({
  beforeSvg: before,
  refs: refs.length,
  missing: missing.length,
  sampleMissing: missing.slice(0, 8)
})
