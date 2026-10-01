"""Render a Happy brutalist avatar tile as a crisp square plugin icon.

Usage: python3 render.py <tile-name> <tint> <background> <out.png> [size] [ink-scale]
"""
import sys
from PIL import Image, ImageFilter

SRC = "/Users/kirilldubovitskiy/Developer/happy-desktop/packages/happy-desktop-ui/src/assets/brutalist"


def crisp_alpha(tile: str, size: int, bold: int = 0) -> Image.Image:
    alpha = Image.open(f"{SRC}/{tile}.png").convert("RGBA").split()[3]
    # Interpolate the 100px contour at 4x the target, threshold it to a hard edge,
    # then downsample so the edge is antialiased instead of blurry.
    big = alpha.resize((size * 4, size * 4), Image.BICUBIC).filter(ImageFilter.GaussianBlur(3))
    big = big.point(lambda v: 255 if v >= 128 else 0)
    if bold:
        # Thicken thin strokes so the mark survives composer-icon sizes.
        big = big.filter(ImageFilter.MaxFilter(bold * 2 + 1))
    return big.resize((size, size), Image.LANCZOS)


def render(tile: str, tint: str, background: str, out: str, size: int = 512, ink: float = 0.62, bold: int = 0):
    canvas = Image.new("RGBA", (size, size), background)
    inner = round(size * ink)
    alpha = crisp_alpha(tile, inner, bold)
    layer = Image.new("RGBA", (inner, inner), tint)
    offset = (size - inner) // 2
    canvas.paste(layer, (offset, offset), alpha)
    canvas.convert("RGB").save(out, optimize=True)


if __name__ == "__main__":
    tile, tint, background, out = sys.argv[1:5]
    size = int(sys.argv[5]) if len(sys.argv) > 5 else 512
    ink = float(sys.argv[6]) if len(sys.argv) > 6 else 0.62
    bold = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    render(tile, tint, background, out, size, ink, bold)
