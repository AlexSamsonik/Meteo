"""There are functions for request https://www.meteo.pl/ ."""
from datetime import datetime
from typing import Dict

from requests import get

from configuration.config import get_config


def get_image_by_bytes(params: Dict[str, str]):
    """Sends a GET request.

    :param params: Optional arguments that 'request' takes.
    :return:
    """
    return get(get_config().url, params=params).content


def create_params(coordinate: Dict[str, str]) -> Dict[str, str]:
    """Create params for get request.

    Next attribute will create:
        ntype: does not have documentation what exactly mean :). Value always will be equals '0u'.\n
        fdate: date when you want to know weather forecast e.g. 2020111500 mean than star at 00:00 15 November, 2020.
        Value always generate automatically and equals now.\n
        col: x-coordinate in meteo.pl system e.g. 297.\n
        row: y-coordinate in meteo.pl system e.g 360.\n
        lang: language equals pl.\n

    :param coordinate: coordinate for specific City in meteo.pl systems.
        For example: coordinates do not equals to real coordinate, so you must know 'col' and 'row' in meteo.pl system.
    """
    return {
        "ntype": "0u",
        "fdate": f"{datetime.now().strftime('%Y%m%d')}00",
        "col": coordinate.get("col"),
        "row": coordinate.get("row"),
        "lang": "pl"
    }
