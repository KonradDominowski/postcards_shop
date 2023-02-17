from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")


def clean_coordinates(image_path: str):
    """
    Convert coordinates from minutes and seconds system into decimals.

    :param image_path:
    :return: Dictionary with cleaned coordinates.
    """
    coordinates = get_coordinates(image_path)

    if not coordinates:
        return None

    cleaned_coordinates = dict()

    long = coordinates['GPSLongitude']
    lat = coordinates['GPSLatitude']

    print(lat)
    print(long)

    cleaned_coordinates['latitude'] = str(round(lat[0] + float(lat[1]) / 60 + float(lat[2]) / 3600, 6))
    cleaned_coordinates['longitude'] = str(round(long[0] + float(long[1]) / 60 + float(long[2]) / 3600, 6))

    if coordinates['GPSLatitudeRef'] == 'S':
        cleaned_coordinates['latitude'] = f"-{cleaned_coordinates['latitude']}"

    if coordinates['GPSLongitudeRef'] == 'W':
        cleaned_coordinates['longitude'] = f"-{cleaned_coordinates['longitude']}"

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


def get_exact_info(latitude, longitude):
    if not latitude or not longitude:
        return

    location = geolocator.reverse(f"{latitude}, {longitude}")

    return location.raw['address']
