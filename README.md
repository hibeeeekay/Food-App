# Sweet Flavour Magazzino — Website

A premium, self-contained catering website for **Sweet Flavour Magazzino** (Ipaja · Ayobo · Lagos).

---

## The files

| File | What it is |
|---|---|
| **`index.html`** | 🎯 **The website.** One single file, images included. Double-click to open, or upload anywhere. |
| `site/_template.html` | The readable source (with image placeholders). Edit here for big changes. |
| `site/build.py` | Rebuilds `index.html` from the template + images: `python3 site/build.py` |
| `web/` | Web-optimised images (used by the build) |
| `assets/` | Full-resolution originals — great for Instagram, flyers, WhatsApp catalogues |
| `sweet-flavour-proposal.html` | The feature proposal you approved |

> You only ever need to share **`index.html`**. Everything — every photo, every style, every script — lives inside it.

---

## What's built in

**Ordering**
- **Order basket** — customers tap *Add to Order* on any menu item; it builds a list and sends **one tidy WhatsApp message** to you. The basket survives a page refresh.
- **Booking form** — name, phone, service, occasion, date, guest count, delivery area, budget, notes → opens WhatsApp pre-written.
- **Popup-blocked fallback** — if WhatsApp can't open, the full order text appears in a box the customer can copy and send manually. No order is ever lost.
- **One-tap Call** — `+234 803 576 7902`
- **Floating WhatsApp button** — always visible, gently pulsing.

**Content**
- Hero · services (4) · filterable menu (8 items) · occasion packages (3 tiers) · booking form · testimonials · delivery areas · FAQ (6) · footer
- No prices shown anywhere — everything is *"Request a Quote"*, as you chose.

**Technical**
- Mobile-first, works on weak Nigerian networks, ~1.2 MB total including all images
- Local SEO: page title, meta description, keywords, and **structured data** (FoodEstablishment schema) so Google understands your services and location
- Scroll animations, gold-on-black luxury styling, and a subtle film-grain texture

---
