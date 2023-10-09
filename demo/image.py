import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

import mayaa


class ImageViewer(mayaa.MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.container = mayaa.MayaaStackVertical(self)
        self.container.set_as_core()
        self.upper = mayaa.MayaaStackHorizontal(self.container)
        self.upper.set_background_color(mayaa.MayaaColors.DARKBLUE)
        self.upper.set_width_as_display()
        self.upper.set_height_as_remaining_area()
        self.lower = mayaa.MayaaStackHorizontal(self.container)
        self.lower.set_background_color(mayaa.MayaaColors.BLACKBLUE)
        self.lower.set_width_as_display()
        self.lower.set_fixed_height(100)
        self.container.add_element(self.upper)
        self.container.add_element(self.lower)

        self.container.compute_elements_surfaces()
        self.container.compute_elements_positions()

    def render(self):
        ...


class ImageApp(mayaa.MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Image in Mayaa")
        self.set_rendering_flags(mayaa.pg.RESIZABLE)
        self.set_display_size(400, 400)
        self.image_viewer = ImageViewer(self, "imageview", self.scene_manager)
        self.scene_manager.set_init_scene("imageview")


app = ImageApp()
app.run()
