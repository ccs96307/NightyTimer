import base64


def pic2str(file, function_name):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(function_name, base64.b64encode(pic.read()))
    pic.close()

    with open('icon.py', 'a') as f:
        f.write(content)


if __name__ == '__main__':
    pic2str('pic/Icon.png', 'icon')