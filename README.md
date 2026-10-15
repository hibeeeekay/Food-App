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

## Editing your content

All your text lives in **`site/_template.html`** — search for these words and change them:

- **Opening hours** — appears twice, search `7am – 9pm`
- **Testimonials** — search `Chioma A.` (swap in real reviews when you have them)
- **Prices / packages** — search `The Intimate`, `The Signature`, `The Royal`
- **Delivery areas** — search `Alagbado`
- **Phone numbers** — search `2348024589080` (WhatsApp) and `2348035767902` (call)

After editing, rebuild:
```bash
python3 site/build.py
```

**Or** just edit `index.html` directly — it's plain HTML, and any text you can see on the page you can find and change. No rebuild needed.

---

## Putting it online

**Easiest (free, 2 minutes):**
1. Go to [netlify.com/drop](https://app.netlify.com/drop)
2. Drag **`index.html`** onto the page
3. You get a live link instantly — share it on WhatsApp, Instagram bio, Facebook

**Custom domain** (e.g. `sweetflavourmagazino.com`): buy from a Nigerian registrar (~₦10–15k/year), then point it at Netlify. I can walk you through it.

---

## Still to come (when you're ready)

- [ ] **Your real photos** — send them and I'll swap them in properly (crop, colour-grade, optimise)
- [ ] **Instagram / Facebook / email links** — currently placeholders in the footer, just send me the handles and email address
- [ ] **Real customer reviews** — replace the three sample testimonials
- [ ] **Price list** — if you change your mind and want *"from ₦—"* prices shown
- [ ] **More menu items** — the gallery is built to keep growing

---

**Sweet Flavour Magazzino** · Ipaja – Ayobo, Lagos, Nigeria
WhatsApp **+234 802 458 9080** · Call **+234 803 576 7902**
