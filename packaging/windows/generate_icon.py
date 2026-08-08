from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUTPUT = Path(__file__).resolve().parent / "assets" / "rag-finance.ico"
SIZES = (16, 24, 32, 48, 64, 128, 256)
YELLOW = "#FFD400"
BLUE = "#0757B8"


def main() -> None:
    canvas = Image.new("RGBA", (256, 256), YELLOW)
    draw = ImageDraw.Draw(canvas)
    font_path = Path("C:/Windows/Fonts/arialbd.ttf")
    if not font_path.exists():
        font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    font = ImageFont.truetype(str(font_path), 190)
    bounds = draw.textbbox((0, 0), "R", font=font)
    x = (256 - (bounds[2] - bounds[0])) / 2 - bounds[0]
    y = (256 - (bounds[3] - bounds[1])) / 2 - bounds[1] - 5
    draw.text((x, y), "R", font=font, fill=BLUE)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, format="ICO", sizes=[(size, size) for size in SIZES])
    print(f"Generated {OUTPUT} with {len(SIZES)} sizes")


if __name__ == "__main__":
    main()
