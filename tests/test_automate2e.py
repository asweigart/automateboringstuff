from __future__ import division, print_function
import pytest



def test_c10_manipulating_images():
    from PIL import ImageColor
    assert ImageColor.getcolor('red', 'RGBA') == (255, 0, 0, 255)
    assert ImageColor.getcolor('RED', 'RGBA') == (255, 0, 0, 255)
    assert ImageColor.getcolor('Black', 'RGBA') == (0, 0, 0, 255)
    assert ImageColor.getcolor('chocolate', 'RGBA') ==   (210, 105, 30, 255)
    assert ImageColor.getcolor('CornflowerBlue', 'RGBA') == (100, 149, 237, 255)


    from PIL import Image
    catIm = Image.open('zophie.png')


    from PIL import Image
    catIm = Image.open('zophie.png')
    assert catIm.size == (816, 1088)
    width, height = catIm.size
    assert width == 816
    assert height == 1088
    assert catIm.filename == 'zophie.png'
    assert catIm.format == 'PNG'
    assert catIm.format_description == 'Portable network graphics'
    catIm.save('_deleteme.jpg') #catIm.save('zophie.jpg')


    from PIL import Image
    im = Image.new('RGBA', (100, 200), 'purple')
    #im.save('purpleImage.png')
    im2 = Image.new('RGBA', (20, 20))
    #im2.save('transparentImage.png')

    from PIL import Image
    catIm = Image.open('zophie.png')
    croppedIm = catIm.crop((335, 345, 565, 560))
    #croppedIm.save('cropped.png')


    from PIL import Image
    catIm = Image.open('zophie.png')
    catCopyIm = catIm.copy()


    faceIm = catIm.crop((335, 345, 565, 560))
    assert faceIm.size == (230, 215)
    catCopyIm.paste(faceIm, (0, 0))
    catCopyIm.paste(faceIm, (400, 500))
    #catCopyIm.save('pasted.png')


    catImWidth, catImHeight = catIm.size
    faceImWidth, faceImHeight = faceIm.size
    catCopyTwo = catIm.copy()
    for left in range(0, catImWidth, faceImWidth):
        for top in range(0, catImHeight, faceImHeight):
            #print(left, top)
            catCopyTwo.paste(faceIm, (left, top))
    #catCopyTwo.save('tiled.png')



    from PIL import Image
    catIm = Image.open('zophie.png')
    width, height = catIm.size
    quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
    #quartersizedIm.save('quartersized.png')
    svelteIm = catIm.resize((width, height + 300))
    #svelteIm.save('svelte.png')


    from PIL import Image
    catIm = Image.open('zophie.png')
    catIm.rotate(90).save('rotated90.png')
    catIm.rotate(180).save('rotated180.png')
    catIm.rotate(270).save('rotated270.png')



    catIm.rotate(6).save('rotated6.png')
    catIm.rotate(6, expand=True).save('rotated6_expanded.png')


    catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')



    from PIL import Image
    im = Image.new('RGBA', (100, 100))
    assert im.getpixel((0, 0)) == (0, 0, 0, 0)
    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210))

    from PIL import ImageColor
    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
    assert im.getpixel((0, 0)) == (210, 210, 210, 255)
    assert im.getpixel((0, 50)) == (169, 169, 169, 255)
    #im.save('putPixel.png')



    """
    import os
    from PIL import Image

    SQUARE_FIT_SIZE = 300
    LOGO_FILENAME = 'catlogo.png'

    logoIm = Image.open(LOGO_FILENAME)
    logoWidth, logoHeight = logoIm.size

    os.makedirs('withLogo', exist_ok=True)
    # Loop over all files in the working directory.
    for filename in os.listdir('.'):
        if not (filename.endswith('.png') or filename.endswith('.jpg')) \
           or filename == LOGO_FILENAME:
            continue # skip non-image files and the logo file itself

        im = Image.open(filename)
        width, height = im.size

        # Check if image needs to be resized.
        if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
            # Calculate new width and height to resize to.
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE

            # Resize the image
            print('Resizing %s...' % (filename))
            im = im.resize((width, height))

        # Add logo.
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        # Save changes.
        im.save(os.path.join('withLogo', filename))
        """



    from PIL import Image, ImageDraw
    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)

    from PIL import Image, ImageDraw
    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)
    draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
    draw.rectangle((20, 30, 60, 60), fill='blue')
    draw.ellipse((120, 30, 160, 60), fill='red')
    draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
       fill='brown')
    for i in range(100, 200, 10):
        draw.line([(i, 0), (200, i - 100)], fill='green')

    #im.save('drawing.png')



    from PIL import ImageFont
    from PIL import Image, ImageDraw, ImageFont
    import os
    im = Image.new('RGBA', (200, 200), 'white')
    draw = ImageDraw.Draw(im)
    draw.text((20, 150), 'Hello', fill='purple')
    fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts'
    arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
    draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
    #im.save('text.png')





if __name__ == '__main__':
    pytest.main()
