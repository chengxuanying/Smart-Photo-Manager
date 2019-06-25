# -*- coding:utf-8 -*-

import bimpy
from glob import glob


from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf


class file_broswer:
    file_list = []

    def __init__(self):
        pass

    def refresh_file_list(self):
        self.file_list = glob('pictures\*.*')


class file_brewswer_ui:
    fb = file_broswer()
    preidx = -1
    selected = bimpy.Int(-1)

    im = None

    def render(self, ctx, windows_info):
        pos = bimpy.Vec2(conf.margin, conf.margin)
        size_min = bimpy.Vec2(conf.min_file_browser_width,
                              ctx.height() - 2 * conf.margin)
        size_max = bimpy.Vec2(conf.max_file_browser_width,
                              ctx.height() - 2 * conf.margin)

        bimpy.set_next_window_pos(pos, bimpy.Condition.Once)
        bimpy.set_next_window_size_constraints(size_min, size_max)

        bimpy.begin(LANG.file_brewswer_ui_title, bimpy.Bool(True),
                    bimpy.WindowFlags.NoCollapse |
                    bimpy.WindowFlags.NoMove)

        ###########UI###########

        self.fb.refresh_file_list()

        for idx, f_name in enumerate(self.fb.file_list):
            # print(self.selected.value)
            if bimpy.selectable(f_name.split('\\')[-1], self.selected.value == idx):
                self.selected.value = idx

                if self.selected.value != -1 and self.selected.value != self.preidx:
                    self.preidx = self.selected.value
                    windows_info['image_shower_ui']['self'].update_pic(f_name)
                    windows_info['meta_info_ui']['self'].update_meta_info(f_name)



        ########################

        t = {
            'x': bimpy.get_window_pos().x,
            'y': bimpy.get_window_pos().y,
            'w': bimpy.get_window_size().x,
            'h': bimpy.get_window_size().y,
            'self' : self,
        }

        bimpy.end()

        return t
