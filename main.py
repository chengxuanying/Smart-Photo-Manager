# -*- coding:utf-8 -*-

from Modules.gui import GUI
from Modules.file_broswer import file_broswer, file_brewswer_ui
from Modules.image_shower import image_shower, image_shower_ui
from Modules.meta_info import meta_info, meta_info_ui
from Modules.about import about_ui

if __name__ == "__main__":
    gui = GUI()
    gui.init()

    gui.render_list.append(about_ui())
    gui.render_list.append(file_brewswer_ui())
    gui.render_list.append(image_shower_ui())
    gui.render_list.append(meta_info_ui())

    gui.render()



