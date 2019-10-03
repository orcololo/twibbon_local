from PIL import Image
import string
import random
import glob


def filebrowser():
    return [f for f in glob.glob("trait/*.jpeg")]


def Crop(test_image):
    original = Image.open(test_image)
    if original.size[-1] > 1270:
        width, height = original.size  # Get dimensions
        left = width / 100
        top = height / 100
        right = 4 * width / 4
        bottom = 4 * height / 4
        cropped = original.crop((left, top, right, bottom))
        print(cropped.size)
        name = f'/tmp/{random_name()}_cropped.png'
        cropped.save(name)
        return name, original.size
    else:
        width, height = original.size  # Get dimensions
        left = width / 6
        top = height / 6
        right = 3 * width / 4
        bottom = 3 * height / 4
        cropped = original.crop((left, top, right, bottom))
        print(cropped.size)
        name = f'/tmp/{random_name()}_cropped.png'
        cropped.save(name)
        return name, cropped.size


def random_name():
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for i in range(16))


def Merge2Images(watermark_file, pic_file):
    photo = Image.open(pic_file)
    watermark = Image.open(watermark_file)
    photo.paste(watermark, (0, 0), watermark)
    photo.save(f'final/{random_name()}_final.png')


def Resize(size, file):
    im = Image.open(file)
    im.thumbnail(size)
    name = f'/tmp/{random_name()}_resized.png'
    im.save(name)
    return name


def TraitImage(watermark_file, pic_file):
    c_name, size = Crop(f'{pic_file}')
    r_name = Resize(size, 'watermark.png')
    Merge2Images(r_name, c_name)


# TraitImage('watermark.png','2.jpeg')
def TraitAll():
    x = filebrowser()
    c = 0
    for i in x:
        TraitImage('watermark.png', i)
        c += 1
    print(f'{c} images done.')


if __name__ == '__main__':
    TraitAll()
