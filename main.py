"""There is module which image's file with detailed information about the weather in Grodno City."""
from configuration.config import get_config
from api.meteo_pl import create_params, get_image_by_bytes

if __name__ == '__main__':
    GRODNO = "grodno"
    with open(f"{GRODNO}.png", "wb") as file:
        coordinate = get_config().coordinate.get(GRODNO)  # Get coordinate for specific City.
        params = create_params(coordinate)  # Create params for request.
        bytes_image = get_image_by_bytes(params)  # Send request and get image by bytes.
        file.write(bytes_image)  # Write image to file "image.png"
