# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/errnex/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/errnex/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

The World in One Day — a one-page newspaper front page summing up Monday 23 November 2026: 40 stories across 7 regions, each with its source badge, a world map of where it happened, a UTC timeline of the day as it unfolded, a date-check box, and the Friday market close. The three lead stories are COP31 collapsing in Antalya over fossil fuels, the war at the Strait of Hormuz, and the Russian drone strike on a flat block in Dymer, north of Kyiv. Built with Python + Pillow and real DejaVu fonts; the entry program copies the finished image to `/output/entry.png`. Full source list in [SOURCES.md](SOURCES.md).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Rebuild the image from scratch (regenerates `entry.png` deterministically):

```sh
python3 build_image.py
```

---

Entered on [make.fun](https://make.fun/?ref=h14gtbhq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards
