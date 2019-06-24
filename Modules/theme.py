import bimpy

"""
// Setup style
ImGuiStyle& style = ImGui::GetStyle();
style.Colors[ImGuiCol_Text] = ImVec4(0.31f, 0.25f, 0.24f, 1.00f);
style.Colors[ImGuiCol_WindowBg] = ImVec4(0.94f, 0.94f, 0.94f, 1.00f);
style.Colors[ImGuiCol_MenuBarBg] = ImVec4(0.74f, 0.74f, 0.94f, 1.00f);
style.Colors[ImGuiCol_ChildWindowBg] = ImVec4(0.68f, 0.68f, 0.68f, 0.00f);
style.Colors[ImGuiCol_Border] = ImVec4(0.50f, 0.50f, 0.50f, 0.60f);
style.Colors[ImGuiCol_BorderShadow] = ImVec4(0.00f, 0.00f, 0.00f, 0.00f);
style.Colors[ImGuiCol_FrameBg] = ImVec4(0.62f, 0.70f, 0.72f, 0.56f);
style.Colors[ImGuiCol_FrameBgHovered] = ImVec4(0.95f, 0.33f, 0.14f, 0.47f);
style.Colors[ImGuiCol_FrameBgActive] = ImVec4(0.97f, 0.31f, 0.13f, 0.81f);
style.Colors[ImGuiCol_TitleBg] = ImVec4(0.42f, 0.75f, 1.00f, 0.53f);
style.Colors[ImGuiCol_TitleBgCollapsed] = ImVec4(0.40f, 0.65f, 0.80f, 0.20f);
style.Colors[ImGuiCol_ScrollbarBg] = ImVec4(0.40f, 0.62f, 0.80f, 0.15f);
style.Colors[ImGuiCol_ScrollbarGrab] = ImVec4(0.39f, 0.64f, 0.80f, 0.30f);
style.Colors[ImGuiCol_ScrollbarGrabHovered] = ImVec4(0.28f, 0.67f, 0.80f, 0.59f);
style.Colors[ImGuiCol_ScrollbarGrabActive] = ImVec4(0.25f, 0.48f, 0.53f, 0.67f);
style.Colors[ImGuiCol_ComboBg] = ImVec4(0.89f, 0.98f, 1.00f, 0.99f);
style.Colors[ImGuiCol_CheckMark] = ImVec4(0.48f, 0.47f, 0.47f, 0.71f);
style.Colors[ImGuiCol_SliderGrabActive] = ImVec4(0.31f, 0.47f, 0.99f, 1.00f);
style.Colors[ImGuiCol_Button] = ImVec4(1.00f, 0.79f, 0.18f, 0.78f);
style.Colors[ImGuiCol_ButtonHovered] = ImVec4(0.42f, 0.82f, 1.00f, 0.81f);
style.Colors[ImGuiCol_ButtonActive] = ImVec4(0.72f, 1.00f, 1.00f, 0.86f);
style.Colors[ImGuiCol_Header] = ImVec4(0.65f, 0.78f, 0.84f, 0.80f);
style.Colors[ImGuiCol_HeaderHovered] = ImVec4(0.75f, 0.88f, 0.94f, 0.80f);
style.Colors[ImGuiCol_HeaderActive] = ImVec4(0.55f, 0.68f, 0.74f, 0.80f);//ImVec4(0.46f, 0.84f, 0.90f, 1.00f);
style.Colors[ImGuiCol_ResizeGrip] = ImVec4(0.60f, 0.60f, 0.80f, 0.30f);
style.Colors[ImGuiCol_ResizeGripHovered] = ImVec4(1.00f, 1.00f, 1.00f, 0.60f);
style.Colors[ImGuiCol_ResizeGripActive] = ImVec4(1.00f, 1.00f, 1.00f, 0.90f);
style.Colors[ImGuiCol_CloseButton] = ImVec4(0.41f, 0.75f, 0.98f, 0.50f);
style.Colors[ImGuiCol_CloseButtonHovered] = ImVec4(1.00f, 0.47f, 0.41f, 0.60f);
style.Colors[ImGuiCol_CloseButtonActive] = ImVec4(1.00f, 0.16f, 0.00f, 1.00f);
style.Colors[ImGuiCol_TextSelectedBg] = ImVec4(1.00f, 0.99f, 0.54f, 0.43f);
style.Colors[ImGuiCol_TooltipBg] = ImVec4(0.82f, 0.92f, 1.00f, 0.90f);
style.Alpha = 1.0f;
style.WindowFillAlphaDefault = 1.0f;
style.FrameRounding = 4;
style.IndentSpacing = 12.0f;
"""


def set_yellow():
    style = bimpy.get_style()

    # style.set_color(bimpy.Colors.Text, bimpy.Vec4(0.31, 0.25, 0.24, 1.00))
    # style.set_color(bimpy.Colors.WindowBg, bimpy.Vec4(0.94, 0.94, 0.94, 1.00))
    #
    # style.set_color(bimpy.Colors.ChildWindowBg, bimpy.Vec4(0.00, 0.00, 0.00, 0.00))
    # style.set_color(bimpy.Colors.Border, bimpy.Vec4(0.00, 0.00, 0.00, 0.39))
    # style.set_color(bimpy.Colors.BorderShadow, bimpy.Vec4(1.00, 1.00, 1.00, 0.10))
    # style.set_color(bimpy.Colors.FrameBg, bimpy.Vec4(1.00, 1.00, 1.00, 1.00))
    # style.set_color(bimpy.Colors.FrameBgHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.40))
    # style.set_color(bimpy.Colors.FrameBgActive, bimpy.Vec4(0.26, 0.59, 0.98, 0.67))
    # style.set_color(bimpy.Colors.TitleBg, bimpy.Vec4(0.96, 0.96, 0.96, 1.00))
    # style.set_color(bimpy.Colors.TitleBgCollapsed, bimpy.Vec4(1.00, 1.00, 1.00, 0.51))
    # style.set_color(bimpy.Colors.TitleBgActive, bimpy.Vec4(0.82, 0.82, 0.82, 1.00))
    # style.set_color(bimpy.Colors.MenuBarBg, bimpy.Vec4(0.86, 0.86, 0.86, 1.00))
    # style.set_color(bimpy.Colors.ScrollbarBg, bimpy.Vec4(0.98, 0.98, 0.98, 0.53))
    # style.set_color(bimpy.Colors.ScrollbarGrab, bimpy.Vec4(0.69, 0.69, 0.69, 0.80))
    # style.set_color(bimpy.Colors.ScrollbarGrabHovered, bimpy.Vec4(0.49, 0.49, 0.49, 0.80))
    # style.set_color(bimpy.Colors.ScrollbarGrabActive, bimpy.Vec4(0.49, 0.49, 0.49, 1.00))
    # # style.set_color(bimpy.Colors.ComboBg, bimpy.Vec4(0.86, 0.86, 0.86, 0.99))
    # style.set_color(bimpy.Colors.CheckMark, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    # style.set_color(bimpy.Colors.SliderGrab, bimpy.Vec4(0.26, 0.59, 0.98, 0.78))
    # style.set_color(bimpy.Colors.SliderGrabActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(bimpy.Colors.Button, bimpy.Vec4(1.00, 0.79, 0.18, 0.78))
    style.set_color(bimpy.Colors.ButtonHovered, bimpy.Vec4(0.42, 0.82, 1.00, 0.81))
    style.set_color(bimpy.Colors.ButtonActive, bimpy.Vec4(0.72, 1.00, 1.00, 0.86))

    style.set_color(bimpy.Colors.Header, bimpy.Vec4(0.65, 0.78, 0.84, 0.80))
    style.set_color(bimpy.Colors.HeaderHovered, bimpy.Vec4(0.75, 0.88, 0.94, 0.80))
    style.set_color(bimpy.Colors.HeaderActive, bimpy.Vec4(0.55, 0.68, 0.74, 0.80))

    # style.set_color(bimpy.Colors.Column, bimpy.Vec4(0.39, 0.39, 0.39, 1.00))
    # style.set_color(bimpy.Colors.ColumnHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.78))
    # style.set_color(bimpy.Colors.ColumnActive, bimpy.Vec4(0.26, 0.59, 0.98, 1.00))
    # style.set_color(bimpy.Colors.ResizeGrip, bimpy.Vec4(0.50, 0.50, 0.50, 1.00))
    # style.set_color(bimpy.Colors.ResizeGripHovered, bimpy.Vec4(0.26, 0.59, 0.98, 0.67))
    # style.set_color(bimpy.Colors.ResizeGripActive, bimpy.Vec4(0.26, 0.59, 0.98, 0.95))
    # # style.set_color(bimpy.Colors.CloseButton, bimpy.Vec4(0.59, 0.59, 0.59, 0.50))
    # # style.set_color(bimpy.Colors.CloseButtonHovered, bimpy.Vec4(0.98, 0.39, 0.36, 1.00))
    # # style.set_color(bimpy.Colors.CloseButtonActive, bimpy.Vec4(0.98, 0.39, 0.36, 1.00))
    # style.set_color(bimpy.Colors.PlotLines, bimpy.Vec4(0.39, 0.39, 0.39, 1.00))
    # style.set_color(bimpy.Colors.PlotLinesHovered, bimpy.Vec4(1.00, 0.43, 0.35, 1.00))
    # style.set_color(bimpy.Colors.PlotHistogram, bimpy.Vec4(0.90, 0.70, 0.00, 1.00))
    # style.set_color(bimpy.Colors.PlotHistogramHovered, bimpy.Vec4(1.00, 0.60, 0.00, 1.00))
    # style.set_color(bimpy.Colors.TextSelectedBg, bimpy.Vec4(0.26, 0.59, 0.98, 0.35))
    # style.set_color(bimpy.Colors.PopupBg, bimpy.Vec4(1.00, 1.00, 1.00, 0.94))
    # style.set_color(bimpy.Colors.ModalWindowDarkening, bimpy.Vec4(0.20, 0.20, 0.20, 0.35))

    style.alpha = 1.0
    style.indent_spacing = 12.0

    bimpy.set_style(style)
