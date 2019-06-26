import bimpy

from Modules.i18n import LANG_EN as LANG
from Modules.conf import conf
from Modules.image_shower import image_shower
from PIL import Image


class retrival():
    pic2label = {}
    label2pic = {}

    i_s = image_shower()
    thumbnail_cache = {}

    def build_pic2label(self, yolo_res: dict):
        for k, v in yolo_res.items():
            self.pic2label[k] = v['labels']

    def build_label2pic(self):
        for k, v in self.pic2label.items():
            for label in v:
                self.label2pic.setdefault(label, [])
                self.label2pic[label].append(k)

        # delete same photo
        for k, v in self.label2pic.items():
            self.label2pic[k] = list(set(v))

    def build_cache(self):
        # cache thumbnail
        for k, v in self.pic2label.items():

            # if not cache
            if k not in self.thumbnail_cache:
                img = Image.open(k)
                img = self.i_s.resize(img, 50, 50)
                self.thumbnail_cache[k] = bimpy.Image(img)

    def get_thumbnail(self, file):
        if file not in self.thumbnail_cache:
            img = Image.open(file)
            img = self.i_s.resize(img, 445, 400)
            self.thumbnail_cache[file] = bimpy.Image(img)

        return self.thumbnail_cache[file]


if __name__ == '__main__':
    import pickle

    with open('../yolo_res', 'rb') as f:
        yolo_res = pickle.load(f)

    r = retrival()
    r.build_pic2label(yolo_res)
    r.build_label2pic()
    print(r.pic2label)
    print(r.label2pic)


class retrival_ui():
    select_label = ''
    r = retrival()
    init = True
    first_init = False

    def render(self, ctx, windows_info):
        t = {
            'self': self,
        }

        if not self.init:
            self.init = True
            self.first_init = True

            self.r.build_pic2label(windows_info['file_brewswer_ui']['self'].fb.pp.yolo_res)
            self.r.build_label2pic()
            # self.r.build_cache()

            print(self.r.pic2label)
            print(self.r.label2pic)
            # print('init')

        return t

    def retrival(self):

        ###########UI###########
        size = bimpy.Vec2(500, 750)
        bimpy.set_next_window_size(size,
                                   bimpy.Condition.Once)

        if bimpy.begin_popup_modal('{}: {}'.format(LANG.retrieve, self.select_label)) \
                and self.select_label != '' and self.first_init:

            for idx, file in enumerate(self.r.label2pic[self.select_label.lower()]):
                if idx != 0:
                    bimpy.separator()

                img = self.r.get_thumbnail(file)
                bimpy.text(file)
                bimpy.image(img)

            bimpy.separator()

            if bimpy.button(LANG.retrieve_close):
                bimpy.clode_current_popup()
            bimpy.end_popup()
        ########################

        t = {
            'x': bimpy.get_window_pos().x,
            'y': bimpy.get_window_pos().y,
            'w': bimpy.get_window_size().x,
            'h': bimpy.get_window_size().y,
            'self': self,
        }

        return t
