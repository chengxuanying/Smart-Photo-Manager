# -*- coding:utf-8 -*-

import bimpy
from PIL import Image
import numpy as np

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf


class image_shower:
    pass


class image_shower_ui:
    im = None

    def render(self, ctx, windows_info):
        # calculate autoly
        pos = bimpy.Vec2(windows_info['file_brewswer_ui']['x'] +
                         windows_info['file_brewswer_ui']['w'] + conf.margin, conf.margin)
        size = bimpy.Vec2(ctx.width() - pos.x - conf.margin, ctx.height() - 2 * conf.margin)

        bimpy.set_next_window_pos(pos, bimpy.Condition.Always)
        bimpy.set_next_window_size(size, bimpy.Condition.Always)

        bimpy.begin(LANG.image_shower_ui_title, bimpy.Bool(True), bimpy.WindowFlags.NoCollapse |
                    bimpy.WindowFlags.NoMove | bimpy.WindowFlags.NoResize)

        ###########UI###########
        if windows_info['file_brewswer_ui']['self'].im is not None:
            bimpy.image(windows_info['file_brewswer_ui']['self'].im)
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
