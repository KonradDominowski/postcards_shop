from os.path import join, isfile

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim
from os import listdir

geolocator = Nominatim(user_agent="geoapiExercises")


def clean_coordinates(image_path: str):
    coordinates = get_coordinates(image_path)

    if not coordinates:
        return None

    cleaned_coordinates = dict()

    long = coordinates['GPSLongitude']
    lat = coordinates['GPSLatitude']
    cleaned_coordinates['longitude_ref'] = coordinates['GPSLongitudeRef']
    cleaned_coordinates['latitude_ref'] = coordinates['GPSLatitudeRef']

    cleaned_coordinates['longitude'] = str(round(long[0] + float(long[1]) / 60 + float(long[2]) / 3600, 6))
    cleaned_coordinates['latitude'] = str(round(lat[0] + float(lat[1]) / 60 + float(lat[2]) / 3600, 6))

    return cleaned_coordinates


def get_coordinates(image_path: str):
    image = Image.open(image_path)
    exif_data = image._getexif()
    decoded_info = {}

    for tagID, tagVALUE in exif_data.items():
        decoded_tag = TAGS.get(tagID, tagID)
        decoded_info[decoded_tag] = tagVALUE

    gps_info = {}

    try:
        for k in decoded_info['GPSInfo'].keys():
            decode = GPSTAGS.get(k, k)
            gps_info[decode] = decoded_info['GPSInfo'][k]

    except KeyError:
        return None  # No geolocation data

    return gps_info


def get_exact_info(coordinates):
    if not coordinates:
        return

    location = geolocator.reverse(f"{coordinates['latitude']}, {coordinates['longitude']}")

    for key, value in location.raw['address'].items():
        print(f"{key}: {value}")
