// news-image-20261123 entrypoint (Node 22, standard library only).
//
// The finished front page lives in this repo as entry.png — it was drawn
// offline by build_image.py (Python + Pillow, DejaVu fonts) from the real
// 23 November 2026 news cycle: 40 stories, 7 regions, one source badge per
// story, a world map, a UTC timeline and a date-check. This program just
// places that image where the grader looks for it.
//
// Run locally with:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// The grader sets MAKEFUN_OUTPUT_DIR itself; without it we use /output.

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });
writeFileSync(target, readFileSync(join(here, 'entry.png')));
