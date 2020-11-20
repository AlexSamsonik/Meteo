"""There is CityConfig module. Use it you can load city config file and get object."""

from yaml import load, YAMLObject, FullLoader


class CityConfig(YAMLObject):
    """Provide object from city config file."""
    yaml_tag = u'!CityConfig'

    def __init__(self, city_name):
        self.city_name = city_name


def get_city_config() -> CityConfig:
    """Provide instance of CityConfig class."""
    with open("config/city_config.yaml") as file:
        return load(file, Loader=FullLoader)
