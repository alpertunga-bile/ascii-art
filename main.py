from ascii_art import get_ascii_art, save
from common import ASCII

if __name__ == "__main__":
    image_path = "shiba-inu.webp"
    canvas_size = (6000, 6000)

    result = get_ascii_art(
        image_path,
        ascii_solution=ASCII.FLOAT,
        gamma=1.0,
    )

    save("float_gamma_1", result, canvas_size)

    result = get_ascii_art(
        image_path,
        ascii_solution=ASCII.FLOAT,
        gamma=2.2,
    )

    save("float_gamma_2-2", result, canvas_size)

    result = get_ascii_art(image_path, ascii_solution=ASCII.INDEX, gamma=2.2)

    save("index_gamma_2-2", result, canvas_size)

    result = get_ascii_art(image_path, ascii_solution=ASCII.INDEX, gamma=1.0)

    save("index_gamma_1", result, canvas_size)
