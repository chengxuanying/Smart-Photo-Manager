# -*- coding:utf-8 -*-

import bimpy
from glob import glob
from PIL import Image

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf


class meta_info:

    def __init__(self):
        pass



class meta_info_ui:


    def render(self, ctx, windows_info):
        # calculate autoly
        pos = bimpy.Vec2(windows_info['file_brewswer_ui']['x'] +
                         windows_info['file_brewswer_ui']['w'] + conf.margin,
                         windows_info['image_shower_ui']['y'] +
                         windows_info['image_shower_ui']['h'] + conf.margin)

        size = bimpy.Vec2(ctx.width() - pos.x - conf.margin,
                          conf.meta_info_height)

        bimpy.set_next_window_pos(pos, bimpy.Condition.Always)
        bimpy.set_next_window_size(size, bimpy.Condition.Always)

        bimpy.begin("", bimpy.Bool(True),
                    bimpy.WindowFlags.NoCollapse |
                    bimpy.WindowFlags.NoMove |
                    bimpy.WindowFlags.NoResize |
                    bimpy.WindowFlags.NoTitleBar |
                    bimpy.WindowFlags.NoScrollbar)

        ###########UI###########

        bimpy.text('1')
        bimpy.same_line(size.x / 3)
        bimpy.text('2')
        bimpy.same_line(size.x / 3 * 2)
        bimpy.text('3')


        bimpy.text('1')
        bimpy.same_line(size.x / 3)
        bimpy.text('2')
        bimpy.same_line(size.x / 3 * 2)
        bimpy.text('3')


        bimpy.text('1')
        bimpy.same_line(size.x / 3)
        bimpy.text('2')
        bimpy.same_line(size.x / 3 * 2)
        bimpy.text('3')
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