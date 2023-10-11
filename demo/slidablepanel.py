import math
import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

import mayaa


class SliderDemo(mayaa.MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("black")
        self.container = mayaa.MayaaStackVertical(self)
        self.container.set_as_core()
        self.container.border("white", 5)
        self.container.set_background_color("lightblue")

        self.header = mayaa.MayaaStackHorizontal(self.container)
        self.header.set_width_as_parent()
        self.header.set_fixed_height(40)
        self.header.border("white", 5)
        self.header.set_color_as_parent()
        self.container.add_element(self.header)
        mayaa.Mayaa
        self.workspace = mayaa.MayaaStackHorizontal(self.container)
        self.workspace.set_width_as_parent()
        self.workspace.set_height_as_remaining_area()
        self.workspace.set_background_color("#55efc4")
        self.workspace.border("white", 5)

        self.left_menu = mayaa.MayaaStackVertical(self.workspace)
        self.left_menu.set_height_as_parent()
        self.left_menu.set_fixed_width(100)
        self.left_menu.set_background_color("red")
        self.left_menu.border("white", 5)

        self.double_panel = mayaa.MayaaSlidablePanelHorizontal(self.workspace)
        self.double_panel.set_width_as_remaining_area()
        self.double_panel.set_height_as_remaining_area()
        self.double_panel.set_background_color("#55efc4")
        self.double_panel.border("white", 5)

        self.left_panel = mayaa.MayaaSlidablePanel(self.double_panel)
        self.left_panel.set_background_color("#a29bfe")
        self.double_panel.add_element(self.left_panel)

        self.right_panel = mayaa.MayaaSlidablePanel(self.double_panel)
        self.right_panel.set_background_color("yellow")
        self.double_panel.add_element(self.right_panel)

        self.workspace.add_element(self.left_menu)
        self.workspace.add_element(self.double_panel)
        self.container.add_element(self.workspace)

        self.container.compute_elements_surfaces()
        self.container.compute_elements_positions()
        self.tick = 0

        self.anim = mayaa.Animation()

    def update(self):
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
        self.slider_demo = SliderDemo(self, "sliderdemo", self.scene_manager)
        self.scene_manager.set_init_scene("sliderdemo")

    def render(self):
        ...


app = ImageApp()
app.run()
