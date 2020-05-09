import pyqrcode


def qr_link(link):
    qr = pyqrcode.create(link, "L")
    # png = qr.png_as_base64_str(scale=6)
    qr.png("documents/qr_post_link.png", scale=6)
    file = open("documents/qr_post_link.png", "rb")
    return file
