# -*- coding:utf-8 -*-

from multiprocessing import freeze_support
import pickle

if __name__ == "__main__":
    freeze_support()
    from Modules.gui import GUI
    from Modules.file_broswer import file_brewswer_ui
    from Modules.image_shower import image_shower_ui
    from Modules.meta_info import meta_info_ui
    from Modules.about import about_ui


    gui = GUI()
    gui.init()

    gui.render_list.append(about_ui())
    gui.render_list.append(file_brewswer_ui())
    gui.render_list.append(image_shower_ui())
    gui.render_list.append(meta_info_ui())


    # load
    try:
        with open('yolo_res', 'rb') as f:
            gui.render_list[1].fb.pp.yolo_res = pickle.load(f)
    except:
        pass

    gui.render_list[1].fb.startprocess()

    gui.render()




