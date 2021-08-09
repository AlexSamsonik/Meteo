"""There is module which create image's file with detailed information about the weather for specific city."""
from argparse import ArgumentParser

from general.weather import Weather

if __name__ == '__main__':
    parser = ArgumentParser('Parameters for getting weather in specific city.')
    parser.add_argument('-c', '--city', help='Name of city', required=True)
    args = parser.parse_args()

    Weather(args.city).save_weathers_image()
