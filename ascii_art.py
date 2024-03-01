from common import get_ascii, ASCII
from PIL import Image, ImageDraw, ImageOps
from tqdm import tqdm


def save(filename: str, ascii_art: str, size: tuple[int, int]) -> None:
    write_ascii_as_png(filename + ".png", ascii_art, size)
    write_ascii_to_file(filename + ".txt", ascii_art)


def write_ascii_as_png(filepath: str, ascii_art: str, size: tuple[int, int]) -> None:
    image = Image.new("RGBA", size, "black")
    width, height = size

    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(ascii_art)

    width_location = (width - w) / 2
    height_location = (height - h) / 2

    draw.text((width_location, height_location), ascii_art, fill="white")

    image.save(filepath, "PNG")

    print(f"{filepath} is saved")


def write_ascii_to_file(filepath: str, ascii_art: str) -> None:
    with open(filepath, "w") as file:
        file.write(ascii_art)

    print(f"ASCII art is saved to {filepath}")


def get_ascii_art(
    image_path: str,
    resize: tuple[int, int] = None,
    rotate_angle: float = None,
    flip_vertical: bool = False,
    ascii_solution: ASCII = ASCII.FLOAT,
    gamma: float = 2.2,
) -> str:
    image = Image.open(image_path)
    image = ImageOps.exif_transpose(image)

    if flip_vertical:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    if rotate_angle:
        image = image.rotate(rotate_angle, Image.Resampling.BICUBIC)

    if resize:
        image = image.resize(resize, Image.Resampling.LANCZOS)

    pixels = list(image.getdata())
    width, height = image.size

    result = ""

    for p_index in tqdm(range(0, len(pixels)), desc=f"Converting {image_path}"):
        pixel_values = pixels[p_index]
        total_value = len(pixel_values)

        r_value = float(pixel_values[0]) / 255.0
        g_value = float(pixel_values[1]) / 255.0
        b_value = float(pixel_values[2]) / 255.0

        if total_value == 4:
            a_value = float(pixel_values[3]) / 255.0

        gray_value = (
            0.2126 * (r_value**gamma)
            + 0.7152 * (g_value**gamma)
            + 0.0722 * (b_value**gamma)
        )

        if total_value == 4:
            gray_value *= a_value

        result += get_ascii(gray_value, ascii_solution) * 2

        if p_index % width == 0 and p_index != 0:
            result += "\n"

    image.close()

    return result
