import type { NextConfig } from "next";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

const projectRoot = resolve(dirname(fileURLToPath(import.meta.url)));

const nextConfig: NextConfig = {
  turbopack: {
    root: projectRoot,
  },
  // Vercel already brotli/gzip-encodes HTML/JS/CSS; keep explicit for Node deploys.
  compress: true,
  poweredByHeader: false,
  compiler: {
    removeConsole: process.env.NODE_ENV === "production",
  },
  experimental: {
    optimizePackageImports: ["lucide-react", "framer-motion", "lenis", "gsap"],
  },
  images: {
    formats: ["image/avif", "image/webp"],
    minimumCacheTTL: 60 * 60 * 24 * 365,
    deviceSizes: [640, 750, 828, 1080, 1200, 1600],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
  async headers() {
    const longCache = [
      {
        key: "Cache-Control",
        value: "public, max-age=31536000, immutable",
      },
    ];
    return [
      {
        source: "/Projects/:path*",
        headers: longCache,
      },
      {
        source: "/:path*.webp",
        headers: longCache,
      },
      {
        source: "/:path*.avif",
        headers: longCache,
      },
      {
        source: "/:path*.png",
        headers: longCache,
      },
      {
        source: "/:path*.jpg",
        headers: longCache,
      },
      {
        source: "/:path*.jpeg",
        headers: longCache,
      },
      {
        source: "/:path*.svg",
        headers: longCache,
      },
    ];
  },
};

export default nextConfig;
