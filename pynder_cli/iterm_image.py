import base64
import requests

url = 'https://d1ra4hr810e003.cloudfront.net/visual/accountlogo/33FADB9E-122E-4E42-9ADB3DC3A1ADB49B/small-8681C87B-5C48-4377-8F5F5BA08EB73744.png'  # noqa


def display_image(url):
    img = get_raw_image(url)
    display_raw_img_iterm(img)


def get_raw_image(url):
    r = requests.get(url, stream=True)
    r.raw.decode_content = True
    blah = r.raw.read()
    return blah

def get_iterm_text_for_image(img):
    b64filename = base64.b64encode("image.jpeg")
    b64img = base64.b64encode(img)
    return "\033]1337;File=name={};size=40; inline=1:{}^G\a\n".format(
        b64filename, b64img)


def get_raw_imgs_for_urls(urls):
    images = [get_raw_image(img) for img in urls]
    return images


def table_of_images(raw_images):
    from prettytable import PrettyTable
    t = PrettyTable([1, 2, 3, 4, 5])
    t.add_row([get_iterm_text_for_image(img) for img in raw_images])


def display_raw_img_iterm(img, filename="image.jpeg"):
    b64filename = base64.b64encode(filename)
    b64img = base64.b64encode(img)
    print("\033]1337;File=name={};inline=1:{}^G\a\n".format(
        b64filename, b64img))
