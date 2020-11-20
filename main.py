"""There is module which create image's file with detailed information about the weather for specific city."""
from api.meteo_pl import create_params, get_image_by_bytes
from config.city_config import get_city_config
from constants.constant import get_constants

if __name__ == '__main__':
    CITY_NAME = get_city_config().city_name
    with open(f"{CITY_NAME}.png", "wb") as file:
        coordinate = get_constants().coordinate.get(CITY_NAME)  # Get coordinate for specific <city_name>.
        params = create_params(coordinate)  # Create params for request.
        bytes_image = get_image_by_bytes(params)  # Send request and get image by bytes.
        file.write(bytes_image)  # Write image to file "<city_name>.png"
