# -*- coding:utf-8 -*-

import bimpy
from PIL import Image
import numpy as np
import time

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf


class image_shower:
    def resize(self, image_pil, width, height):
        '''
        Resize PIL image keeping ratio and using white background.
        '''
        width = int(width)
        height = int(height)

        ratio_w = width / image_pil.width
        ratio_h = height / image_pil.height
        if ratio_w < ratio_h:
            # It must be fixed by width
            resize_width = width
            resize_height = round(ratio_w * image_pil.height)
        else:
            # Fixed by height
            resize_width = round(ratio_h * image_pil.width)
            resize_height = height
        image_resize = image_pil.resize((resize_width, resize_height), Image.ANTIALIAS)

        background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
        offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
        background.paste(image_resize, offset)
        return background.convert('RGB')


class image_shower_ui:
    i_s = image_shower()
    im = None

    def render(self, ctx, windows_info):
        # calculate autoly
        pos = bimpy.Vec2(windows_info['file_brewswer_ui']['x'] +
                         windows_info['file_brewswer_ui']['w'] + conf.margin,
                         conf.margin)

        self.size = bimpy.Vec2(ctx.width() - pos.x - conf.margin,
                               ctx.height() - 3 * conf.margin - conf.meta_info_height)

        bimpy.set_next_window_pos(pos, bimpy.Condition.Always)
        bimpy.set_next_window_size(self.size, bimpy.Condition.Always)

        bimpy.begin(LANG.image_shower_ui_title, bimpy.Bool(True),
                    bimpy.WindowFlags.NoCollapse |
                    bimpy.WindowFlags.NoMove |
                    bimpy.WindowFlags.NoResize)

        ###########UI###########

        if self.im is not None:
            bimpy.image(self.im)
        ########################

        t = {
            'x': bimpy.get_window_pos().x,
            'y': bimpy.get_window_pos().y,
            'w': bimpy.get_window_size().x,
            'h': bimpy.get_window_size().y,
            'self': self,
        }

        bimpy.end()

        return t

    def update_pic(self, im):
        # resize and update pic by message
        im = self.i_s.resize(im, self.size.x, self.size.y - 43)
        self.im = bimpy.Image(im)