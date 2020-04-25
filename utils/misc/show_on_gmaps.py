URL = "http://maps.google.com/maps?q={lat},{lon}"


def show(lat, lon):
    return URL.format(**locals())
