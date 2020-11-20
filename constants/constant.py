"""There is Constant module. Use it you can load constant file and get object."""
from typing import Dict

from yaml import load, YAMLObject, FullLoader


class Constant(YAMLObject):
    """Provide object from constant file."""
    yaml_tag = u'!Constant'

    def __init__(self, url, user_agent: Dict[str, str], coordinate: Dict[str, Dict[str, str]]):
        self.url = url
        self.user_agent = user_agent
        self.coordinate = coordinate


def get_constants() -> Constant:
    """Provide instance of Constant class."""
    with open("constants/constant.yaml") as file:
        return load(file, Loader=FullLoader)
