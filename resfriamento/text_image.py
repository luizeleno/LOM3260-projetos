import numpy as np
from PIL import Image, ImageDraw, ImageFont

class InitialCondition:
    
    def __init__(self):
        pass
        
    def gera_texto(self, text='COOL', W=101, H=101, fontsize=24):
        '''
            Generates an WxH array with the string `text`
            printed at a certain position and with a certain fontsize.
        '''

        backcolor = 0
        textcolor = 1

        font = ImageFont.truetype("FreeSerif.ttf", fontsize, encoding="unic")
        img = Image.new('L', (W, H), color=backcolor)

        d = ImageDraw.Draw(img)
        d.text((10, H//2 - 10), text, fill=textcolor, font=font)
        # TODO: centralize text in array

        return np.array(img)[::-1, :]

    def gera_forma(self, forma='quadrado'):
    
        if forma == 'quadrado':
            # TODO: implementar !
            pass
        elif formar=='elipse':
            pass
            
    
