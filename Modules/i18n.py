# -*- coding:utf-8 -*-

class LANG_EN:
    ####global####
    name = 'Smart Picture Manager'

    ####file_brewswer####
    file_brewswer_ui_title = 'Picture Broswer'
    file_brewswer_ui_refresh = 'Refresh'

    ####image_shower####
    image_shower_ui_title = 'Image Displayer'
    click_to_view_more = 'View similar images'
    smart_analyse = 'AI Analyse'
    drag = 'Drag to Resize'
    auto = 'AUTO'

    ####meta_info####
    meta_size = 'Size'
    meta_date = 'Date'
    meta_device = 'Device'

    meta_focal_length = 'FocalLength'
    meta_exposure_time = 'ExposureTime'
    meta_ISO_speed_ratings = 'ISOSpeedRatings'

    meta_GPS = 'GPS'
    meta_location = 'Location'
    meta_cant_find = 'None'


    ###about###
    about = 'About'
    about_close = 'Close'
    about_content = 'The Smart Picture Manager (SPM) embraces the ' \
                    'recent advances of deep learning (DL), and provides ' \
                    'a unified software experience for managing personal photos. \n\n ' \
                    'Features of SMP:\n' \
                    '* Easy-to-use User Interaction\n' \
                    '* AI photo analyser\n' \
                    '* One-key photo semantic match\n' \
                    '\n' \
                    'Besides, this software is an coursework for "Programming Designment Training" and the instructor is Heng, Qi\n' \
                    '\n' \
                    'Author: Chengxuan, Ying\n' \
                    'Last Update: 6.25.2019'

if __name__=='__main__':
    print(LANG_EN().about_content)