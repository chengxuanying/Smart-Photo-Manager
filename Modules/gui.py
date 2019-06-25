# -*- coding:utf-8 -*-

import bimpy
import time
import os

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf

class GUI:
    render_list = []
    ctx = None

    def init(self):
        # new instance

        ctx = bimpy.Context()

        # init
        ctx.init(conf.width, conf.height, LANG.name)

        # load font and theme
        # set_yellow()
        bimpy.add_font_from_file_ttf(conf.font, conf.font_size)
        bimpy.themes.set_light_theme()

        self.ctx = ctx


    def render(self):
        windows_info = {}

        while(not self.ctx.should_close()):
            # os.system('cls')

            with self.ctx:

                for i in self.render_list:
                    windows_info[i.__class__.__name__] = i.render(self.ctx, windows_info)
                # print(windows_info)

                self.ctx.render()


                time.sleep(0.02)
