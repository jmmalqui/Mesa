import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

from mayaa import *
import json

TOKEN = "FT4MkyazfJIcVKnnbbik84jZOzgXgicHoWRS6HiUCyL0uacfRAhAO2ri "


class ImageWithText(MayaaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)


class CenteredInheritTextLabel(MayaaTextLabel):
    def __init__(self, parent, text, height, fontsize, color) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(height)
        self.set_font_size(fontsize)
        self.set_font_name("meiryoui")
        self.set_text(f"{text}")
        self.set_color_as_parent()
        self.set_text_color(color)


class ProductShowerGadget(MayaaStackHorizontal):
    def __init__(self, parent, path, brand, name) -> None:
        super().__init__(parent)
        self.set_fixed_width(300)
        self.set_fixed_height(100)
        self.set_background_color("white")
        self.set_rounded_borders(20)
        self.separator = MayaaStackHorizontal(self)
        self.separator.set_height_as_parent()
        self.separator.set_fixed_width(10)
        self.separator.set_background_color("white")
        self.product_image = MayaaImage(self)
        self.product_image.set_color_as_parent()
        self.product_image.set_fixed_width(100)
        self.product_image.set_fixed_height(100)
        self.product_image.set_image(path)
        self.product_image.resize_image([80, 80])
        self.product_image.center_element()
        self.product_image.set_rounded_borders(40)
        self.description_area = MayaaStackVertical(self)
        self.description_area.set_color_as_parent()
        self.description_area.set_width_as_remaining_area()
        self.description_area.set_height_as_parent()

        self.separator2 = MayaaStackHorizontal(self.description_area)
        self.separator2.set_fixed_height(5)
        self.separator2.set_width_as_parent()
        self.separator2.set_color_as_parent()

        self.brand_name = MayaaTextLabel(self.description_area)
        self.brand_name.set_width_as_parent()
        self.brand_name.set_fixed_height(30)
        self.brand_name.set_font_size(20)
        self.brand_name.set_color_as_parent()
        self.brand_name.set_font_name("meiryoui")
        self.brand_name.set_text(f"{brand}")
        self.brand_name.set_text_color("black")
        self.brand_name.center_text_vertical()

        self.product_name = MayaaTextLabel(self.description_area)
        self.product_name.set_width_as_parent()
        self.product_name.set_fixed_height(12)
        self.product_name.set_font_size(12)
        self.product_name.set_color_as_parent()
        self.product_name.set_font_name("meiryoui")
        self.product_name.set_text(f"{name}")
        self.product_name.set_text_color("black")
        self.product_name.center_text_vertical()

        self.see_more_button = MayaaButtonText(self.description_area)
        self.see_more_button.set_width_as_parent()
        self.see_more_button.set_fixed_height(50)

        self.description_area.add_element(self.separator2)
        self.description_area.add_element(self.brand_name)
        self.description_area.add_element(self.product_name)
        self.description_area.add_element(self.see_more_button)
        self.add_element(self.separator)
        self.add_element(self.product_image)
        self.add_element(self.description_area)

    def update(self):
        for event in self.scene.manager.get_events():
            if (
                event.type == pg.MOUSEBUTTONDOWN
                and self.see_more_button.is_container_hovered()
            ):
                self.scene.core.entry_scene.tick = 0
                self.scene.core.entry_scene.app_title.set_font_size(20)
                self.scene.manager.go_to("entry_scene")


class ProductShowerGadgetContainer(MayaaSingleContainer):
    def __init__(self, parent, path, brand, name) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(150)
        self.set_background_color("lightgray")
        self.gadget = ProductShowerGadget(self, path, brand, name)
        self.center_element()
        self.add_element(self.gadget)


class Header(MayaaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(50)
        self.set_width_as_parent()
        self.set_background_color("white")
        self.image = MayaaImage(self)
        self.image.set_background_color("white")
        self.image.set_fixed_height(50)
        self.image.set_fixed_width(50)
        self.image.center_element()
        self.image.set_image("demo\\res\\slidericon.jpeg")
        self.image.resize_image([30, 30])
        self.app_title = MayaaTextLabel(self)
        self.app_title.set_fixed_height(50)
        self.app_title.set_width_as_remaining_area()
        self.app_title.center_text()
        self.app_title.set_text("Renteck")
        self.app_title.set_font_name("meiryoui")
        self.app_title.set_font_size(25)
        self.app_title.set_text_color("black")
        self.app_title.set_background_color("white")
        self.app_title.set_bold()
        self.add_element(self.image)
        self.add_element(self.app_title)


class ProductShower(MayaaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_height_as_remaining_area()
        self.set_width_as_display()
        self.set_background_color("pink")
        with open("demo\\data.json") as f:
            self.product_list = json.load(f)

        for s in self.product_list["products"]:
            self.product = ProductShowerGadgetContainer(
                self, s["path"], s["brand"], s["name"]
            )
            self.add_element(self.product)


class Footer(MayaaSingleContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(80)
        self.set_background_color("gray")
        self.buttons_container = MayaaStackHorizontal(self)
        self.buttons_container.set_fixed_width(180)
        self.buttons_container.set_height_as_parent()
        self.buttons_container.set_background_color("white")
        self.center_element()
        self.add_element(self.buttons_container)


class ProductShowScene(MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MayaaStackVertical(self)
        self.container.set_as_core()
        self.container.set_background_color("white")

        self.header = Header(self.container)
        self.shower = ProductShower(self.container)
        self.footer = Footer(self.container)
        self.container.add_element(self.header)
        self.container.add_element(self.shower)
        self.container.add_element(self.footer)
        self.container.remake_rendering_tree_from_here()


class EntryScene(MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MayaaSingleContainer(self)
        self.container.set_as_core()
        self.container.set_background_color("white")

        self.app_title = MayaaTextLabel(self.container)

        self.app_title.set_fixed_height(100)
        self.app_title.set_fixed_width(300)
        self.app_title.center_text()
        self.app_title.set_text("RenTeck")
        self.app_title.set_font_name("meiryoui")
        self.app_title.set_font_size(25)
        self.app_title.set_text_color("black")
        self.app_title.set_background_color("white")
        self.container.add_element(self.app_title)
        self.container.center_element()
        self.container.remake_rendering_tree_from_here()
        self.tick = 0
        self.anim = Animation()
        self.extend = AnimVal(self.anim, 0)

    def update(self):
        self.anim.update()
        self.tick += 1
        if self.tick == 30:
            self.extend.move_to(100, 15, MayaaAnimationCurves.EASE_OUT_EXPO)
        self.app_title.set_fixed_height(100 + self.extend.value)
        self.app_title.set_fixed_width(300 + self.extend.value)
        self.app_title.set_font_size(25 + int(self.extend.value // 2.7))
        self.container.remake_rendering_tree_from_here()
        if self.tick == 60:
            self.manager.go_to("productshow")


class Renteck(MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Renteck")
        self.set_rendering_flags(pg.SRCALPHA, pg.SCALED)
        self.set_display_size(360, 600)

        self.set_background_color("black")
        self.set_clock(60)
        self.entry_scene = EntryScene(self, "entry_scene", self.scene_manager)
        self.product_show = ProductShowScene(self, "productshow", self.scene_manager)
        self.scene_manager.set_init_scene("entry_scene")


app = Renteck()
app.run()
