#!/usr/bin/env python3
"""Compose an untouched source photo and a generated illustration into an exact 3:4 diptych."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageColor, ImageOps


def fit_contain(image: Image.Image, size: tuple[int, int], background: str) -> Image.Image:
    canvas = Image.new("RGB", size, ImageColor.getrgb(background))
    contained = ImageOps.contain(image.convert("RGB"), size, Image.Resampling.LANCZOS)
    x = (size[0] - contained.width) // 2
    y = (size[1] - contained.height) // 2
    canvas.paste(contained, (x, y))
    return canvas


def fit_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(
        image.convert("RGB"), size, Image.Resampling.LANCZOS, centering=(0.5, 0.5)
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create an exact 3:4 poster with equal photo and illustration panels."
    )
    parser.add_argument("photo", type=Path)
    parser.add_argument("illustration", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, default=1800)
    parser.add_argument("--background", default="#F4EFE4")
    parser.add_argument(
        "--photo-mode",
        choices=("contain", "cover"),
        default="contain",
        help="Contain preserves the whole photo; cover minimally crops it.",
    )
    args = parser.parse_args()

    if args.width <= 0 or args.width % 3:
        raise SystemExit("--width must be a positive multiple of 3")

    height = args.width * 4 // 3
    half_height = height // 2
    panel_size = (args.width, half_height)

    with Image.open(args.photo) as photo_src, Image.open(args.illustration) as art_src:
        if args.photo_mode == "contain":
            top = fit_contain(photo_src, panel_size, args.background)
        else:
            top = fit_cover(photo_src, panel_size)
        bottom = fit_cover(art_src, panel_size)

    poster = Image.new("RGB", (args.width, height), ImageColor.getrgb(args.background))
    poster.paste(top, (0, 0))
    poster.paste(bottom, (0, half_height))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    poster.save(args.output, format="PNG", optimize=True)

    if poster.width * 4 != poster.height * 3 or half_height * 2 != poster.height:
        raise RuntimeError("Output invariant failed")


if __name__ == "__main__":
    main()
