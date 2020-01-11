from base64 import b64encode
from PIL import Image


def pic2str(image, script, function_name):
    pic = open(image, 'rb')
    content = '{} = {}\n'.format(function_name, b64encode(pic.read()))
    pic.close()

    with open(script, 'a') as f:
        f.write(content)


def pic2ico(input, output):
    image = Image.open(input)
    image.save(output)


if __name__ == '__main__':
    pic2str('pic/Icon.png', 'icon.py', 'icon')
    pic2ico('pic/Icon.png', 'pic/Icon.ico')