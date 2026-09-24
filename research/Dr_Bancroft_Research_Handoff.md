# Dr. Bancroft — Research Handoff (evidence base, no synthesis)

Date: 2026-09-24. This run collected evidence only. It contains no angles, personas, headlines or strategy.

## Files
| File | Contents |
|---|---|
| `Dr_Bancroft_Master_Research_Corpus.xlsx` | 1,350 unique sources, one per row (Sources sheet), plus a Counts sheet |
| `Dr_Bancroft_Master_Source_Index.docx` | Every source URL grouped by source type, with a short description |
| `Dr_Bancroft_VOC_Extracts.xlsx` | 2,784 consumer quotes / observations |
| `Dr_Bancroft_Research_Handoff.md` | This file |

## 1. Unique sources
- **Total: 1,350 unique URLs** after normalising and deduplicating (www/old/en Reddit variants, trailing slashes).
- 240 were carried over from Source Corpus v3. v3 had 242 entries; 2 were Reddit URL variants that collapsed to the same thread. The v3 document recorded URLs only, so these rows have domain/type inferred and no notes.
- 1,110 are new this run. 25 further rows that were duplicates across research streams were dropped.

## 2. Source counts by type
| Type | Count |
|---|---|
| Reddit threads | 455 |
| Academic papers | 235 |
| Retail review pages / review feeds | 164 |
| Competitor PDPs (includes v3 rows of unknown subtype) | 130 |
| Forums / blogs / independent reviews | 105 |
| Patents | 89 |
| Trade publications | 72 |
| Market research | 36 |
| Competitor marketing (ad case studies, campaigns) | 30 |
| Regulatory / standards / legal | 19 (+ further regulatory pages typed as "other"/"trade") |
| Other | 14 |
| Video | 1 |

New sources by research stream: academic-consumer 95, market 95, misc (regulatory + adjacent Reddit) 94, academic-skin 91, patents 91, Reddit men's grooming/ads 88, Reddit scent/tallow 84, retail mass brands 84, retail premium/natural 83, competitor marketing 82, Reddit skin/dryness 82, forums/blogs 74, Reddit zero-waste/value 67.

## 3. VOC observations
**2,784 rows**, all from real consumer text (Reddit, retail reviews, forums, blog comments).
- By category: product experience 1,009 · pain point 778 · objection 402 · expectation 186 · comparison 167 · buying trigger 147 · desire 95
- By sentiment: negative 1,061 · positive 987 · neutral 477 · mixed 259
- By origin: retail mass-brand reviews 630 · retail premium/natural 459 · Reddit men/ads 420 · Reddit skin 400 · Reddit value/zero-waste 272 · forums/blogs 266 · Reddit scent/tallow 234 · Reddit misc 105 · competitor blog 2
- All quotes are 40 words or fewer. The Reddit quotes were checked by script against the fetched text, verbatim after whitespace normalisation. Every VOC row links to a source row in the corpus.

## 4. Research areas covered
- **Skin experience:** dryness, tightness, eczema/psoriasis, fragrance-free needs, and soap vs syndet (CeraVe, Cetaphil, Dove, Vanicream).
- **Men's grooming:** body odor, feeling or smelling clean, gym/BJJ hygiene (Defense, pine tar, tea tree).
- **Dr Squatch advertising reactions:** celebrity and AI ads, "synthetic detergent" claims, masculinity messaging, ad fatigue, and quality complaints after the Unilever sale.
- **Scent:** longevity, scent fade, overpowering or artificial scent, essential oils, tallow and animal-fat objections, vegan concerns, and "natural" skepticism.
- **Practical and value:** hard water and soap film, mushy bars, bar life, dishes and savers, travel, plastic-free packaging, subscriptions, gifting, doubts about farmers-market/Etsy soap, goat milk soap, and price per bar.
- **Retail reviews:** Dial, Irish Spring, Ivory, Zest, Coast, Lever 2000, Old Spice, Every Man Jack, Dove Men+Care, Dove Beauty Bar, CeraVe, Cetaphil, SheaMoisture, Olay, Yardley, Basis and Vanicream. Premium/natural: Dr Squatch, Duke Cannon, Dr Bronner's, Grandpa's, Bend, Beekman 1802, Rocky Mountain, Primally Pure, Buff City, Pacha, Chagrin Valley, Moon Valley, Fatworks and Dionis.
- **Competitor marketing:** product pages, guarantees, FAQs, mission pages, Dr Squatch agency and awards case studies, the Duke Cannon x Jeep campaign, and Old Spice.
- **Academic:** soap vs syndets, pH, TEWL, surfactant–protein binding, hard water and eczema (SWET), essential-oil contact allergy, oxidised limonene/linalool, pine and coal tar, triclosan and handwashing, bar-soap contamination; sensory perception, natural-product bias, greenwashing, willingness to pay for sustainable packaging, men's grooming, and packaging.
- **Patents and formulation:** wear rate, mush, cracking, lather, fragrance bloom, skin feel, deposition and syndet/combars. Notes record which attributes and test methods each patent describes.
- **Market:** Circana, NIQ, Mintel, Euromonitor, McKinsey (via secondary coverage), trade press, and Unilever/P&G/Colgate results and the Dr Squatch deal.
- **Regulatory:** FDA soap/cosmetic definitions and MoCRA, EU allergen labelling (2023/1545), IFRA, FTC Made in USA and Green Guides, organic, vegan and cruelty-free certifications, EU EmpCo, UK ASA/CMA, and the Dr Squatch and Honest Co class actions.

## 5. Where evidence is thin
- **Amazon, Walmart, Trustpilot, Etsy, BBB, YouTube and TikTok are absent or nearly absent.** All blocked automated access (bot protection, CAPTCHA, or login walls). This is the biggest gap. Bring in these reviews only through licensed exports or manually saved pages.
- **Etsy and artisan soap reviews:** covered only indirectly, via Reddit and small brands' own review widgets.
- **Reddit:** r/youtube, r/advertising, r/Colognes, r/keratosispilaris, r/Hidradenitis, r/tallow, r/tretinoin, r/Dermatology, r/Sensitiveskin, r/HomeImprovement, r/AskWomen and r/FemaleFashionAdvice returned nothing, because archive searches timed out. BuyItForLife has only 2 new threads, and Duke Cannon has little Reddit material of its own.
- **Market figures:** no hard Circana or Kantar bar-soap or tallow sales figures, and no Statista summary.
- **Academic evidence on some sensory topics is limited:** lather/foam as a cleaning cue, wet-skin feel, and bar shape, weight and grip. Some willingness-to-pay and "natural" bias papers come from food categories, not cosmetics.
- **No directly inspected Prop 65 source.** Hard-water VOC is modest, and men's-gift threads are thin.
- **Competitor pages:** Dr Squatch's own ingredient page and its "vs body wash" page returned 404. The Meta Ad Library was not accessed.

## 6. Inaccessible or paywalled sources
- About 110 corpus rows are marked in "What was inspected" as abstract-only, paywalled or teaser-only.
- **All 186 new academic papers were read as title and abstract only**, via the PubMed E-utilities and Crossref APIs. No full texts were read.
- **Paywalled market reports:** 14 rows (Mintel store pages, Euromonitor, Cosmetics Business, Adweek) record only the visible teaser or table of contents.
- **Blocked entirely, and so not recorded as sources:**
  - Retail and review sites: amazon.com reviews, walmart.com reviews, cvs.com, walgreens.com, trustpilot.com, etsy.com, bbb.org complaint pages, influenster.com.
  - Forums and social: youtube.com, soapmakingforum.com, mumsnet.com, quora.com, basenotes.net, fragrantica.com, theshaveden.com, houzz.com.
  - Brand sites: lush.com, manscaped.com, crate61.com.
  - Press and trade: happi.com, forbes.com, businessoffashion.com.
  - Other: web.archive.org, several eur-lex, ecfr, nsf and asa.org.uk pages.

## 7. Methodology
- **Starting point:** read Corpus v3 (242 URLs) and used its URLs as the dedupe list.
- **Research streams:** 13 parallel streams, plus 3 re-runs of Reddit streams that failed the first time. Each followed a shared instruction set: record only pages actually opened; label abstract-only, paywalled or snippet-only pages; never invent quotes, counts or URLs; follow leads by snowballing.
- **Access routes:**
  - Reddit: the Arctic Shift archive API. One source row per thread; the post plus up to 100 comments were read.
  - Retail: Target's public reviews API, and brand-site review feeds (Bazaarvoice, Yotpo, Okendo, Judge.me, Loox, Stamped, PowerReviews).
  - Academic: PubMed E-utilities and Crossref.
  - Other pages: fetched directly.
- **Evidence labels:** evidence type separates consumer anecdote, aggregate reviews, controlled experiment, review paper, observational study, company claim, market survey, patent disclosure and regulatory guidance.

## 8. Limitations — read before synthesis
1. **Retail VOC was selected and tagged by script.** The 1,089 retail review quotes were chosen by keyword filters (about 3–7 sentences per product, deliberately including 1–3 star reviews). Themes and categories come from keywords, and sentiment largely from star rating, so tags are approximate. They were spot-checked, not fully hand-reviewed. The mix of low and high stars is deliberate and does not reflect the real rating distribution.
2. **Some retail source URLs point to review-data feeds.** 150 VOC rows and their source rows use a Bazaarvoice API URL rather than a product page. Brand-site feeds may also include reviews copied in from retailers.
3. **Academic evidence types are machine-assigned.** In the academic-consumer stream they came from keyword rules; most default to "observational study". Skin-science rows use PubMed publication-type labels. Notes are title plus conclusion sentences.
4. **Reddit is skewed to recent posts.** The archive search returns newest first, so most threads are from 2025–2026. Some r/Soap posts may be brand seeding and are flagged in their notes.
5. **Patents describe what manufacturers measure, not proof of product claims.** Competitor pages are company claims, not independent evidence. Reddit and reviews are anecdotes, not scientific evidence.
6. **Some pages were read only in part.** Market and trade pages were often read through topic-matched passages rather than end to end. Threads with more than 100 comments were only partly read.
7. **Carried-over v3 rows have minimal metadata.** The 240 v3 rows have no notes or quotes, because v3 recorded URLs only.
8. **The patents stream was stopped early,** at 91 sources, when all research was paused.
