import qrcode
img = qrcode.make('https://rapidimages.atlassian.net/wiki/home')
type(img)
img.save('test.png')