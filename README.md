# LinkedIn B2B SaaS Research

A curated research repository on LinkedIn organic content strategy for B2B SaaS — built as part of a technical assignment for 100Hires.

## What This Is

This repo contains content collected from 10 practitioners who actively use LinkedIn to grow B2B SaaS businesses. The goal was to find high-signal sources — people with real results, not just people who write about marketing.

## Topic

**LinkedIn Organic Content Strategy for B2B SaaS**

## How I Chose the Experts

The biggest risk with this kind of research is ending up with generic, obvious picks. To avoid that, I cross-referenced 5 different "top LinkedIn experts" lists from Google and excluded anyone who appeared on 2 or more of them. What remained were practitioners who actually build in public, share real numbers, and have documented results.

Each person was then verified individually — are they still active, do they have original frameworks, and do their results actually come from LinkedIn content specifically?

## What I Collected

- **LinkedIn posts** — 3 posts per expert, collected manually. LinkedIn blocks scrapers so this was done by hand. Posts were selected based on relevance to B2B SaaS content strategy.
- **YouTube transcripts** — 2 videos per expert, collected using the YouTube Data API v3 to fetch video links and Supadata API to extract transcripts.

## Repo Structure

    research/
    ├── sources.md                  # All 10 experts with links and reasoning
    ├── linkedin-posts/             # 3 LinkedIn posts per expert
    ├── youtube-transcripts/        # 2 video transcripts per expert
    └── other/
        ├── methodology.md          # How experts were selected and content collected
        └── fetch_transcripts.py    # Python script used to collect YouTube transcripts

## Tools Used

- YouTube Data API v3 — to fetch recent video links by channel ID
- Supadata API — to extract clean transcripts from YouTube videos
- Python (requests, os) — to automate transcript collection
- GitHub — to organize and version the research

## Experts Covered

1. Adam Robinson
2. Richard van der Blom
3. Lara Acosta
4. Pierre Herubel
5. Devin Reed
6. Kevin Indig
7. Ross Simmonds
8. Andrei Zinkevich
9. Sam Dunning
10. Daniel Murray
