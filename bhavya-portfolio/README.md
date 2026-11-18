# Bhavya Sharma: portfolio and four demo projects

## Live links (Claude-hosted pages)

| Page | Link |
|---|---|
| Portfolio | https://claude.ai/artifact/73ssx4wYmtkY8zXPVr4xDn |
| Mettle Strength Club (gym demo) | https://claude.ai/artifact/3oue5CCFioWZMHKvE2PW9s |
| Fringe Hair Studio (booking demo) | https://claude.ai/artifact/ERUT3vy2m5NwzQ7sfqzAmq |
| Dabara Coffee House (café demo) | https://claude.ai/artifact/H35uoNJntNNtEisLWQa5ze |
| Hookloop Social Studio (social and motion showcase) | https://claude.ai/artifact/MwSKVmupab5pkS8MBVythX |

All five links are **private until you share them**. Signed-out visitors see "Sign in to view this page".
- Open each link and use the page's Share menu to make it viewable by anyone with the link.
- Do this for all five pages: the portfolio links to the four demos, and each demo links back to the portfolio.

## What's in this folder

- `sites/` – standalone copies of the five pages. Each folder has a complete `index.html` plus its images or videos. They work on any static host.
  - To publish on your own domain, upload the `sites` folder to Netlify, Vercel, Cloudflare Pages or GitHub Pages.
  - Then update the links between pages (see below).
- `source/` – the editable source:
  - `src/<site>/index.html` – the page source.
  - `tools/build.py` – inlines the fonts and writes the publishable page.
  - `tools/make_portfolio.py` – generates the portfolio from the project data.
  - `campaign-graphics-and-motion/` – the HTML sources for every Hookloop graphic and animation.
  - `tests/` – the Playwright scripts used to test the flows.
- `CERTIFICATES.md` – the verified free-certificate shortlist and what you need to do.

## Moving the pages to your own hosting

1. Choose the new URLs.
2. Update the links:
   - project links: the `URL` dictionary in `source/tools/make_portfolio.py`;
   - the "Designed and built by" link on each demo: `PORTFOLIO_URL` in `source/tools/config.json`.
3. Install the build tools:
   - `npm install` in a `fontpkgs/` folder, using `source/tools/font-packages.json` as its `package.json`;
   - `pip install fonttools brotli`.
4. Run `python3 source/tools/make_portfolio.py`, then `python3 source/tools/build.py`. The paths at the top of the scripts point to the original build machine, so edit them to your folders first.

## Please check

- **ClearTrade.** The case study describes only what is visible on cleartrade.in. Your role is written as "Design and development. ClearTrade is my own product". Adjust it if you worked with others.
- **Demo labels.** The four demos are labelled as independent concept demos with fictional brands. All their forms, bookings and orders are simulated and say so on screen.

## Fonts

Every typeface is used under the SIL Open Font License 1.1:
- portfolio: Mona Sans;
- Mettle: Big Shoulders Display, Instrument Sans;
- Dabara: Shrikhand, Bricolage Grotesque;
- Fringe: Gloock, Albert Sans;
- Hookloop: Anybody, Hanken Grotesk, Azeret Mono;
- graphics: Young Serif, Newsreader, Bagel Fat One, Mukta.

All illustrations, graphics and motion were made for these projects. No stock images were used.
