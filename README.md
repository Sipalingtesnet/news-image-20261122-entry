# news-image-20261122

The world in one picture — Sunday 22 November 2026.

[![Bounty](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![Rank](https://make.fun/badge/news-image-20261122/Sipalingtesnet/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![Reward](https://make.fun/badge/news-image-20261122/Sipalingtesnet/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122)

A deterministic PIL generator that draws a 1024x1024 newspaper front page summing up the world news of Sunday 22 November 2026: NATO standing by Poland, the COP31 dawn deal in Antalya, the Baltic ship drone strike, Gulf tanker tensions, and a ticker of the day's other headlines. Every story is drawn with a short headline, a plain-word summary, and a simple symbolic illustration made only of PIL shapes — no photos, no randomness, no network.

`draw_news.py` regenerates `entry.png` byte-identically every run, and `main.py` copies that image to the output directory, verifying its sha256.

## Run it

```bash
python3 main.py
```

Writes the entry image to `$MAKEFUN_OUTPUT_DIR` (or `/output/entry.png`) and prints the sha256.

Entered on [make.fun](https://make.fun/?ref=p7s7492b&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards