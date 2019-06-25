import bimpy
from Modules.i18n import LANG_EN as LANG


class about_ui:

    def render(self, ctx, windows_info):

        # if bimpy.begin_popup_modal('about'):
        #     if bimpy.button('123'):
        #         bimpy.clode_current_popup()
        #     bimpy.end_popup()
        t = {
            'self': self,
        }

        return t

    def about(self):
        size = bimpy.Vec2(450, 400)
        bimpy.set_next_window_size(size,
                                   bimpy.Condition.Once)

        if bimpy.begin_popup_modal(LANG.about):
            bimpy.text_wrapped(LANG.about_content)
            bimpy.separator()

            if bimpy.button(LANG.about_close):
                bimpy.clode_current_popup()
            bimpy.end_popup()
