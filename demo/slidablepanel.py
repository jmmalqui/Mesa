import math
import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

import mayaa


class Colors:
    BAR = "#1c263f"
    MENU = "#202336"
    PANEL = "#161b2e"
    SEPARATOR = "#1d2a4a"


class SliderDemo(mayaa.MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("black")
        self.container = mayaa.MayaaStackVertical(self)
        self.container.set_as_core()
        self.container.set_background_color(Colors.PANEL)

        self.header = mayaa.MayaaStackHorizontal(self.container)
        self.header.set_width_as_parent()
        self.header.set_fixed_height(40)
        self.header.set_background_color(Colors.BAR)
        self.fps_counter = mayaa.MayaaTextLabel(self.header)
        self.fps_counter.set_height_as_parent()
        self.fps_counter.set_fixed_width(100)
        self.fps_counter.set_color_as_parent()
        self.fps_counter.set_font_name("Consolas")
        self.fps_counter.set_font_size(20)
        self.fps_counter.set_text_color("white")
        self.fps_counter.set_text(f"FPS: {self.core.clock.get_fps() :.1f}")
        self.header.add_element(self.fps_counter)
        self.container.add_element(self.header)

        self.workspace = mayaa.MayaaStackHorizontal(self.container)
        self.workspace.set_width_as_parent()
        self.workspace.set_height_as_remaining_area()
        self.workspace.set_background_color(Colors.PANEL)

        self.left_menu = mayaa.MayaaStackVertical(self.workspace)
        self.left_menu.set_height_as_parent()
        self.left_menu.set_fixed_width(100)
        self.left_menu.set_background_color(Colors.MENU)

        self.double_panel = mayaa.MayaaSlidablePanelHorizontal(self.workspace)
        self.double_panel.set_width_as_remaining_area()
        self.double_panel.set_height_as_parent()
        self.double_panel.set_background_color(Colors.PANEL)
        self.double_panel.set_slider_color(Colors.SEPARATOR)

        self.left_panel = mayaa.MayaaStackVertical(self.double_panel)
        self.left_panel.set_background_color(Colors.PANEL)
        for i in range(20):
            self.label = mayaa.MayaaTextLabel(self.left_panel)
            self.label.set_fixed_height(20)
            self.label.set_width_as_parent()
            self.label.set_color_as_parent()
            self.label.set_text("My first text label in Mayaa")
            self.label.set_font_name("Consolas")
            self.label.set_font_size(12)
            self.label.set_text_color("white")

            self.left_panel.add_element(self.label)
        self.double_panel.add_element(self.left_panel)

        self.right_panel = mayaa.MayaaSlidablePanelVertical(self.double_panel)
        self.right_panel.set_background_color(Colors.PANEL)
        self.right_panel.set_slider_color(Colors.SEPARATOR)

        self.right_up = mayaa.MayaaSlidablePanelHorizontal(self.right_panel)
        self.right_up.set_background_color(Colors.PANEL)
        self.right_up.set_slider_color(Colors.SEPARATOR)

        self.right_down = mayaa.MayaaSlidablePanel(self.right_panel)
        self.right_down.set_background_color(Colors.PANEL)

        self.l = mayaa.MayaaSlidablePanel(self.right_up)
        self.l.set_background_color(Colors.PANEL)
        self.r = mayaa.MayaaSlidablePanel(self.right_up)
        self.r.set_background_color(Colors.PANEL)

        self.right_up.add_element(self.l)
        self.right_up.add_element(self.r)
        self.right_panel.add_element(self.right_up)
        self.right_panel.add_element(self.right_down)
        self.double_panel.add_element(self.right_panel)

        self.workspace.add_element(self.left_menu)
        self.workspace.add_element(self.double_panel)
        self.container.add_element(self.workspace)

        self.container.remake_rendering_tree_from_here()

        self.tick = 0

        self.anim = mayaa.Animation()

    def update(self):
        for event in self.manager.get_events():
            if event.type == mayaa.pg.MOUSEBUTTONDOWN:
                self.informer.inform(f"{self.double_panel.absolute_position}")
                self.informer.inform(
                    f"{self.double_panel.width, self.double_panel.height, self.double_panel.parent}"
                )
        for label in self.left_panel.elements:
            label.set_text(f"My first label in Mayaa {mayaa.pg.mouse.get_pos()}")
        self.fps_counter.set_text(f"FPS: {self.core.clock.get_fps() :.0f}")
        self.tick += 1
        self.anim.update()

    def render(self):
        ...


class ImageApp(mayaa.MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("SliderPanels")
        self.set_rendering_flags(mayaa.pg.RESIZABLE)
        self.set_display_size(400, 400)
        self.set_background_color("black")
        self.set_clock(600)
        self.slider_demo = SliderDemo(self, "sliderdemo", self.scene_manager)
        self.scene_manager.set_init_scene("sliderdemo")

    def render(self):
        ...


app = ImageApp()
app.run()
