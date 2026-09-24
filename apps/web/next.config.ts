import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: ["@repo/ui", "@repo/ai"],
  experimental: {
    typedRoutes: true,
  },
};

export default nextConfig;
