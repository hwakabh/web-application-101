import qrcode


fname = './vmware_jp.png'
target_url = 'https://www.vmware.com/jp.html'

img = qrcode.make(target_url)
img.save(fname)
