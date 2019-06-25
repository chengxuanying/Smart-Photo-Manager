# -*- coding:utf-8 -*-

import bimpy
from PIL import Image
from geopy.geocoders import Nominatim
from multiprocessing import Process

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf
from Modules.exif_reader import exif_reader


class meta_info:

    def __init__(self):
        pass


class meta_info_ui:
    mi = meta_info()
    er = exif_reader()
    meta_info = None

    geolocator = Nominatim(user_agent="specify_your_app_name_here")

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

        if self.meta_info is not None:
            ####LINE1####
            self.meta_info.setdefault('ImageWidth', '')
            self.meta_info.setdefault('ImageLength', '')
            bimpy.text('{}:{}x{}'.format(LANG.meta_size,
                                         self.meta_info['ImageWidth'],
                                         self.meta_info['ImageLength']))
            bimpy.same_line(size.x / 3)

            self.meta_info.setdefault('DateTimeOriginal', '')
            bimpy.text('{}:{}'.format(LANG.meta_date,
                                      self.meta_info['DateTimeOriginal']))
            bimpy.same_line(size.x / 3 * 2)

            self.meta_info.setdefault('Make', '')
            self.meta_info.setdefault('Model', '')
            bimpy.text('{}:{} {}'.format(LANG.meta_device,
                                         self.meta_info['Make'],
                                         self.meta_info['Model']))

            ####LINE2####
            self.meta_info.setdefault('FocalLength', '')
            bimpy.text('{}:{}'.format(LANG.meta_focal_length,
                                      self.meta_info['FocalLength']))
            bimpy.same_line(size.x / 3)

            self.meta_info.setdefault('ExposureTime', '')
            # truncate too high number
            try:
                x, y = self.meta_info['ExposureTime']
                self.meta_info['ExposureTime'] = (x % 1000, y % 1000)
            except:
                pass

            bimpy.text('{}:{}'.format(LANG.meta_exposure_time,
                                      self.meta_info['ExposureTime']))
            bimpy.same_line(size.x / 3 * 2)

            self.meta_info.setdefault('ISOSpeedRatings', '')
            bimpy.text('{}:{}'.format(LANG.meta_ISO_speed_ratings,
                                      self.meta_info['ISOSpeedRatings']))

            ####LINE3####
            bimpy.text('{}:({},{})'.format(LANG.meta_GPS,
                                           round(self.lat, 1),
                                           round(self.lon, 1)))
            bimpy.same_line(size.x / 3)

            bimpy.text('{}:{}'.format(LANG.meta_location,
                                      self.location))
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

    def update_meta_info(self, f_name):
        self.meta_info = self.er.get_exif_data(Image.open(f_name))

        self.location = LANG.meta_cant_find
        self.lat = 0.
        self.lon = 0.

        self.lat, self.lon = self.er.get_lat_lon(self.meta_info)
        if self.lat != None:
            pass
            # self.location = self.geolocator.reverse("{}, {}".format(self.lat, self.lon))
        else:
            self.lat = 0.
            self.lon = 0.

        # Process(target=self.get_online_info(), args=()).start()


    def get_online_info(self):
        self.lat, self.lon = self.er.get_lat_lon(self.meta_info)
        if self.lat != None:
            self.location = self.geolocator.reverse("{}, {}".format(self.lat, self.lon))
        else:
            self.lat = 0.
            self.lon = 0.
        # print(self.location)







