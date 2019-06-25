# -*- coding:utf-8 -*-

import bimpy
from glob import glob
from multiprocessing import Process, Queue

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf
from Modules.preprocess import preprocess


class file_broswer:
    file_list = []
    q = Queue()

    def __init__(self):
        self.refresh_file_list()

    def refresh_file_list(self):
        self.file_list = glob('pictures\*.*')

    def startprocess(self):
        self.pp = preprocess()
        self.pp.update_file_list(self.file_list)

        p = Process(target=self.preprocess, args=(self.pp, self.q))
        p.start()

    def preprocess(self, p=None, q=None):
        for i in p.process():
            q.put(i)


class file_brewswer_ui:
    fb = file_broswer()
    preidx = -1
    selected = bimpy.Int(-1)

    im = None
    process = (0, len(fb.file_list))

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
        if bimpy.button(LANG.file_brewswer_ui_refresh) == True:
            self.fb.refresh_file_list()

        bimpy.same_line()
        if bimpy.button(LANG.about) == True:
            bimpy.open_popup(LANG.about)

        # call render about ui
        # print(dir(windows_info['about_ui']))
        windows_info['about_ui']['self'].about()

        for idx, f_name in enumerate(self.fb.file_list):
            # print(self.selected.value)
            if bimpy.selectable(f_name.split('\\')[-1], self.selected.value == idx):
                self.selected.value = idx

                if self.selected.value != -1 and self.selected.value != self.preidx:
                    self.preidx = self.selected.value
                    windows_info['image_shower_ui']['self'].update_pic(f_name)
                    windows_info['meta_info_ui']['self'].update_meta_info(f_name)

        # progress bar
        if not self.fb.q.empty():
            self.process = self.fb.q.get()
            self.process = (self.process[0] + 1, self.process[1])

        sz = bimpy.get_window_size()
        bimpy.set_cursor_pos(bimpy.Vec2(conf.margin, sz.y - conf.margin * 2))
        bimpy.push_item_width(sz.x - conf.margin * 2)

        process = self.process
        bimpy.progress_bar(process[0] / float(process[1]),
                           bimpy.Vec2(0.0, 0.0),
                           "{}/{}".format(process[0], process[1]))
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
