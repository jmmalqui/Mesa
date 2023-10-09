import math
import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

import mayaa


class ImageViewer(mayaa.MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("black")
        self.container = mayaa.MayaaStackVertical(self)
        self.container.set_as_core()
        self.upper = mayaa.MayaaStackHorizontal(self.container)
        self.upper.set_margin(10)
        self.upper.set_width_as_display()
        self.upper.set_height_as_remaining_area()

        self.right = mayaa.MayaaStackVertical(self.upper)
        self.right.set_height_as_parent()
        self.right.set_fixed_width(100)
        self.right.set_background_color(mayaa.MayaaColors.BLACKBLUE)
        self.left = mayaa.MayaaStackHorizontal(self.upper)
        self.left.set_margin(40)
        self.left.set_height_as_parent()
        self.left.set_width_as_remaining_area()
        self.left.set_background_color(mayaa.MayaaColors.BLACKBLUE)

        self.upper.add_element(self.left)

        self.upper.add_element(self.right)

        self.lower = mayaa.MayaaStackHorizontal(self.container)
        self.lower.set_margin(10)
        self.lower.set_background_color(mayaa.MayaaColors.BLACKBLUE)
        self.lower.set_width_as_display()
        self.lower.set_fixed_height(100)

        self.container.add_element(self.lower)
        self.container.add_element(self.upper)

        self.container.compute_elements_surfaces()
        self.container.compute_elements_positions()
        self.tick = 0

        self.anim = mayaa.Animation()
        self.rigthw = mayaa.AnimVal(self.anim, 100)
        self.goleft = True

    def update(self):
        self.tick += 1
        self.anim.update()

        for event in self.manager.get_events():
            if event.type == mayaa.pg.MOUSEBUTTONDOWN:
                if self.goleft:
                    self.rigthw.move_to(
                        400, 60, mayaa.MayaaAnimationCurves.EASE_IN_OUT_BACK
                    )
                else:
                    self.rigthw.move_to(
                        100, 60, mayaa.MayaaAnimationCurves.EASE_IN_OUT_BACK
                    )
                self.goleft = not self.goleft
        self.right.set_fixed_width(self.rigthw.value)

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
        self.set_background_color("black")
        self.image_viewer = ImageViewer(self, "imageview", self.scene_manager)
        self.scene_manager.set_init_scene("imageview")


app = ImageApp()
app.run()
