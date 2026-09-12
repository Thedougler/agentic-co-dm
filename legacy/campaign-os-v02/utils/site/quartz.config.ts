import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Campaign OS — player site (Quartz 4)
 *
 * Contract: sys/runbooks/publish.md
 *
 * This config is layer 1 of the three-layer publish defense: the `filters`
 * array below is set to Plugin.ExplicitPublish() (NOT the default
 * RemoveDrafts()) so only pages with `publish: true` in frontmatter are
 * built at all. `ignorePatterns` is a belt-and-suspenders second net in
 * case this config is ever pointed directly at vault content instead of at
 * scripts/build_site.sh's stripped staging copy — see that script for
 * layers 2 (section strip) and 3 (leak check).
 *
 * TODO before a real deploy: set `baseUrl` to the real GitHub Pages (or
 * other host) domain — RSS/sitemap generation depend on it. Left as a
 * placeholder here because bootstrap step 10 doesn't know the campaign's
 * eventual public URL yet.
 *
 * See https://quartz.jzhao.xyz/configuration for upstream Quartz docs.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Campaign OS — Player Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "changeme.github.io/campaign-os",
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      // Structural denylist (sys/runbooks/publish.md § The layered defense):
      // belt-and-suspenders only — build_site.sh's staging copy already
      // excludes all of this before Quartz ever runs.
      "prep",
      "prep/**",
      "docs",
      "docs/**",
      // docs/external (vendored CC-BY reference material) is already
      // covered by "docs"/"docs/**" above — named explicitly anyway so an
      // auditor greps to a hit instead of tracing the glob.
      "docs/external",
      "docs/external/**",
      "scripts",
      "scripts/**",
      ".claude",
      ".claude/**",
      "**/audio/**",
      "**/transcript*.md",
      "**/state-changes.md",
      "sys/secrets.md",
      "**/sys/secrets.md",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    // L3 primitive (sys/runbooks/publish.md): default-deny, opt-in only.
    filters: [Plugin.ExplicitPublish()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
