"""There is Config module. Use it you can load configuration file and get object."""
from typing import Dict

from yaml import load, YAMLObject, FullLoader


class Config(YAMLObject):
    """Provide object from configuration file."""
    yaml_tag = u'!Config'

    def __init__(self, url, user_agent: Dict[str, str], coordinate: Dict[str, Dict[str, str]]):
        self.url = url
        self.user_agent = user_agent
        self.coordinate = coordinate


def get_config() -> Config:
    """Provide instance of Config class."""
    with open("configuration/config.yaml") as cfg_file:
        return load(cfg_file, Loader=FullLoader)
