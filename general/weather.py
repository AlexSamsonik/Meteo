"""Module which provide function to working with Weather class."""

from datetime import date

from api.meteo_pl import create_params, get_image_by_bytes
from constants.constant import get_constants


class Weather:

    def __init__(self, city_name: str):
        """Initialization Weather class.

        :param city_name: Name of city.
        """
        self.city_name = city_name
        self.weathers_file_name = f"{self.city_name}_{str(date.today())}"

    def save_weathers_image(self):
        """Function which save weather's image for specific city."""
        with open(f"{self.weathers_file_name}.png", "wb") as file:
            coordinate = get_constants().coordinate.get(self.city_name)  # Get coordinate for specific <city_name>.
            params = create_params(coordinate)  # Create params for request.
            bytes_image = get_image_by_bytes(params)  # Send request and get image by bytes.
            file.write(bytes_image)  # Write image to file "<weathers_file_name>.png"
