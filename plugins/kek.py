from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from plugins.utils import *

class main:
	level = 1
	keywords = ['кек','kek']
	def execute(self,msg):
		if 'photo' in msg['attachments'][0]:
			ret = msg['attachments'][0]['photo']['sizes']
			num = 0
			for size in ret:
				if size['width'] > num:
					num = size['width']
					url = size['url']
			ret = requests.get(url).content

			outimgs = []
			
			image_obj = Image.open(BytesIO(ret))
			imgByteArr = BytesIO()
			image2 = image_obj.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
			image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj.paste(image2,(int(image_obj.size[0]/2),0))
			image_obj.save(imgByteArr,format='PNG')
			outimgs.append(imgByteArr.getvalue())
		
			imgByteArr = BytesIO()
			image_obj = Image.open(BytesIO(ret))
			image2 = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
			image2 = image2.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
			image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj.paste(image2,(int(image_obj.size[0]/2),0))
			image_obj.save(imgByteArr,format='PNG')
			outimgs.append(imgByteArr.getvalue())

			apisay('Готово!',msg['toho'],photo=outimgs)
		else:
			apisay('Картинку забыл сунуть',msg['toho'])
		image_obj.close()
		image2.close()