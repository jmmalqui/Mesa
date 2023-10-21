import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))
from mayaa import *


class MyOwnText(MayaaTextBox):
    def __init__(self, parent, color) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.set_font_size(24)
        self.set_text_color("black")
        self.set_background_color(color)
        self.set_rounded_borders(15)
        self.border("red", 2)
        self.set_font_name("meiryoui")
        self.parent.add_element(self)


class Mytext(MayaaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.set_font_size(24)
        self.set_text_color("white")
        self.set_background_color("black")
        self.set_rounded_borders(15)
        self.set_text(text)
        self.border("red", 2)
        self.set_font_name("meiryoui")
        self.parent.add_element(self)


class Scene(MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.container = MayaaStackVertical(self)
        self.container.set_as_core()
        self.container.cover_parent_surface()
        self.container.set_background_color("gray")

        self.mytextcontainer = MayaaStackVertical(self.container)
        self.mytextcontainer.cover_parent_surface()
        self.text = MyOwnText(self.mytextcontainer, "red")
        self.text2 = MyOwnText(self.mytextcontainer, "yellow")
        self.text3 = MyOwnText(self.mytextcontainer, "gray")
        self.text4 = MyOwnText(self.mytextcontainer, "green")
        self.text5 = MyOwnText(self.mytextcontainer, "pink")

        self.label = Mytext(self.mytextcontainer, "colas colas")

        self.container.add_element(self.mytextcontainer)
        self.container.build()

        self.dog = pg.image.load("demo\\images\\january.png").convert_alpha()
        self.dog = pg.transform.scale_by(self.dog, 0.2)

        

    def update(self):
        if self.text.get_input().buffer != "":
            self.label.set_text(str(self.text.get_input().buffer))
        return super().update()

    def render(self):
        self.surface.blit(self.dog, [0, 0])
        return super().render()


class MyMayaaApp(MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Text Input")
        self.set_rendering_flags(pg.RESIZABLE)
        self.set_display_size(600, 600)
        self.set_background_color("black")
        self.set_clock(60)

        self.appscene = Scene(self, "scene", self.scene_manager)
        self.scene_manager.set_init_scene("scene")


app = MyMayaaApp()
app.run()
