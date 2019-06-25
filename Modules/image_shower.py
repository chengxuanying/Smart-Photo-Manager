# -*- coding:utf-8 -*-

import bimpy
from PIL import Image
import numpy as np
import cv2
import cvlib as cv
from cvlib.object_detection import populate_class_labels
import threading
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
    raw_im = None
    im = None
    labels = None

    now_im =None

    scale = bimpy.Float(100.0)
    last_scale = 100.0

    auto = bimpy.Bool(False)

    def render(self, ctx, windows_info):
        # calculate autoly
        self.pos = bimpy.Vec2(windows_info['file_brewswer_ui']['x'] +
                              windows_info['file_brewswer_ui']['w'] + conf.margin,
                              conf.margin)

        self.size = bimpy.Vec2(ctx.width() - self.pos.x - conf.margin,
                               ctx.height() - 3 * conf.margin - conf.meta_info_height)

        bimpy.set_next_window_pos(self.pos, bimpy.Condition.Always)
        bimpy.set_next_window_size(self.size, bimpy.Condition.Always)

        bimpy.begin(LANG.image_shower_ui_title, bimpy.Bool(True),
                    bimpy.WindowFlags.NoCollapse |
                    bimpy.WindowFlags.NoMove |
                    bimpy.WindowFlags.NoResize |
                    bimpy.WindowFlags.HorizontalScrollbar)

        ###########UI###########

        if self.im is not None:
            bimpy.set_cursor_pos(bimpy.Vec2(0.0, conf.margin * 3))
            bimpy.image(self.im)

            # if image is loaded
            if self.labels is not None:
                for i, label in enumerate(self.labels):
                    color = self.COLORS[self.classes.index(label)]

                    # print((self.bbox[i][0], self.bbox[i][1] - 10))

                    # show on the left bottom of the picture
                    bimpy.set_cursor_pos(bimpy.Vec2(self.bbox[i][0] + 10
                                                    , self.bbox[i][3] + 10))

                    # set style
                    bimpy.push_id_int(i)

                    if conf.show_yolo_confience:
                        bimpy.button(label + ' ' +
                                     str(format(self.confidence[i] * 100, '.2f')) + '%')
                    else:
                        bimpy.button(label)

                    if bimpy.is_item_hovered(i):
                        s = "{} ({})\n{}"

                        label = label[0].upper() + label[1:]

                        s = s.format(label,
                                     str(format(self.confidence[i] * 100, '.2f')) + '%',
                                     LANG.click_to_view_more)

                        bimpy.set_tooltip(s)

                    if bimpy.is_item_active():
                        print(22)
                    bimpy.pop_id()

            # bimpy.set_cursor_pos(bimpy.Vec2(conf.margin, self.size.y - conf.margin * 2))
            bimpy.set_cursor_pos(bimpy.Vec2(conf.margin, conf.margin * 1.5))
            if bimpy.button(LANG.smart_analyse) == True:
                self.object_detection()

            bimpy.same_line()
            bimpy.checkbox(LANG.auto, self.auto)

            ### Resize ###
            bimpy.same_line()
            bimpy.push_item_width(150)
            bimpy.drag_float(LANG.drag, self.scale,
                             1.0, 10, 1000)
            bimpy.pop_item_width()

            if abs(self.last_scale - self.scale.value) > 4.:
                xx = self.size.x * self.scale.value / 100.
                yy = (self.size.y - 45 - 40) * self.scale.value / 100.

                im = self.i_s.resize(self.raw_im,
                                     xx,
                                     yy)
                self.now_im = im
                self.set_im(im)

                # set to save computation
                self.last_scale = self.scale.value


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

    def update_pic(self, f_name):
        # init
        self.scale = bimpy.Float(100.0)
        self.last_scale = 100.0

        # resize and update pic by message
        im = Image.open(f_name)
        self.raw_im = im

        im = self.i_s.resize(im, self.size.x, self.size.y - 45 - 40)
        self.now_im = im
        self.set_im(im)

        # reset
        self.labels = None

        if self.auto.value == True:
            self.object_detection()

    def object_detection(self):
        img = np.asarray(self.now_im)

        self.bbox, self.labels, self.confidence = cv.detect_common_objects(img)

        self.COLORS = np.random.uniform(0, 255, size=(80, 3))
        self.classes = populate_class_labels()

        for i, label in enumerate(self.labels):
            color = self.COLORS[self.classes.index(label)]
            if True:
                label += ' ' + str(format(self.confidence[i] * 100, '.2f')) + '%'

            cv2.rectangle(img,
                          (self.bbox[i][0], self.bbox[i][1]),
                          (self.bbox[i][2], self.bbox[i][3]), color, 2)

            # cv2.putText(img, label,
            #             (self.bbox[i][0], self.bbox[i][1] - 10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        self.set_im(img)

    def set_im(self, im):
        self.im = bimpy.Image(im)
