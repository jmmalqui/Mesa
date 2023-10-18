import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

import mayaa
import MayaaTransform
import datetime
from calendar import monthrange


MONTHS = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
DAYWIDTH = 50
DAYHEIGHT = 30


class Colors:
    MONTH_CARD_BACKGROUND = "#395B64"
    BACKGROUND = "#2C3333"
    BORDER = "#E7F6F2"
    TEXT = "#FFFFFF"
    DAYSTRIP_COLOR = "#51557E"


class TitleBar(mayaa.MayaaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(25)
        self.set_background_color(Colors.BACKGROUND)

        self.app_name = mayaa.MayaaTextLabel(self)
        self.app_name.set_height_as_parent()
        self.app_name.set_fixed_width(200)
        self.app_name.center_text()
        self.app_name.set_text("Calendar")
        self.app_name.set_font_name("meiryoui")
        self.app_name.set_font_size(18)
        self.app_name.set_text_color(Colors.TEXT)
        self.app_name.set_background_color(Colors.BACKGROUND)
        self.separator = mayaa.MayaaStackHorizontal(self)
        self.separator.set_height_as_parent()
        self.separator.set_width_as_remaining_area()
        self.separator.set_background_color(Colors.BACKGROUND)
        self.date = mayaa.MayaaTextLabel(self)
        self.date.set_height_as_parent()
        self.date.set_fixed_width(150)
        self.date.center_text()
        self.date.set_text(f"{self.get_date()}")
        self.date.set_font_name("meiryoui")
        self.date.set_font_size(18)

        self.date.set_text_color(Colors.TEXT)

        self.date.set_background_color(Colors.BACKGROUND)
        self.add_element(self.app_name)
        self.add_element(self.separator)
        self.add_element(self.date)

    def get_date(self):
        return datetime.datetime.today().strftime("%Y-%m-%d")

    def update(self):
        ...


class Day(mayaa.MayaaTextLabel):
    def __init__(self, parent, list, i, today) -> None:
        super().__init__(parent)
        self.list = list.copy()
        self.today = today
        self.set_fixed_width(DAYWIDTH)
        self.set_fixed_height(DAYHEIGHT)
        self.i = i
        if self.list[i] != "x":
            self.set_text(self.list[i])
        else:
            self.set_text(" ")
        self.set_text_color("black")
        self.set_font_name("meiryoui")
        self.set_font_size(12)
        self.center_text()

        if self.list[i] == str(self.today):
            self.set_background_color("lightgreen")
        elif i % 2 == 0:
            self.set_background_color(Colors.BORDER)
        else:
            self.set_background_color(Colors.BORDER)

    def update(self):
        if self.is_container_hovered():
            self.set_background_color("white")
            self.set_text_color("black")
        else:
            if self.list[self.i] == str(self.today):
                self.set_background_color("lightgreen")
            elif self.i % 2 == 0:
                self.set_background_color(Colors.BORDER)
            else:
                self.set_background_color(Colors.BORDER)
        return super().update()


class DayStripList(mayaa.MayaaStackHorizontal):
    def __init__(self, parent, list) -> None:
        super().__init__(parent)
        self.set_background_color(Colors.DAYSTRIP_COLOR)
        self.set_fixed_height(DAYHEIGHT)
        self.set_fixed_width(7 * DAYWIDTH)
        self.list = list.copy()
        self.today = self.get_date_data().day

        for i in range(7):
            daylabel = Day(self, list, i, self.today)

            self.add_element(daylabel)

    def get_date_data(self):
        date = datetime.datetime.today()
        return date


class DayStrip(mayaa.MayaaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_background_color(Colors.DAYSTRIP_COLOR)
        self.set_fixed_height(DAYHEIGHT)
        self.set_fixed_width(7 * DAYWIDTH)
        self.day_list = ["Sun", "Mon", "Thu", "Wed", "Tue", "Fri", "Sat"]
        for i in range(7):
            daylabel = mayaa.MayaaTextLabel(self)
            daylabel.set_fixed_width(DAYWIDTH)
            daylabel.set_fixed_height(DAYHEIGHT)
            daylabel.set_text(self.day_list[i])
            daylabel.set_text_color(Colors.BORDER)
            daylabel.set_font_name("meiryoui")
            daylabel.set_font_size(12)
            daylabel.center_text()
            daylabel.set_background_color(Colors.DAYSTRIP_COLOR)

            self.add_element(daylabel)


class DayShower(mayaa.MayaaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(6 * DAYHEIGHT)
        self.set_fixed_width(7 * DAYWIDTH)
        self.set_background_color(Colors.BACKGROUND)
        self.set_rounded_borders(8)
        self.day_strip = DayStrip(self)
        self.date = self.get_date_data()
        self.calendar_data = monthrange(self.date.year, self.date.month)
        self.strip_lists = self.get_strips(self.calendar_data)
        self.strip1 = DayStripList(self, self.strip_lists[0])
        self.strip2 = DayStripList(self, self.strip_lists[1])
        self.strip3 = DayStripList(self, self.strip_lists[2])
        self.strip4 = DayStripList(self, self.strip_lists[3])
        self.strip5 = DayStripList(self, self.strip_lists[4])
        self.strip5 = DayStripList(self, self.strip_lists[5])
        self.add_element(self.day_strip)
        self.add_element(self.strip1)
        self.add_element(self.strip2)
        self.add_element(self.strip3)
        self.add_element(self.strip4)
        self.add_element(self.strip5)

    def get_strips(self, data):
        begin_day = data[0]
        num_days = data[1]
        result = []
        count = 1
        for j in range(6):
            list = []
            begin_day_mod_7 = begin_day % 7
            for i in range(7):
                if j == 0:
                    if i < begin_day_mod_7:
                        list.append("x")
                    else:
                        list.append(str(count))
                        count += 1
                else:
                    if count <= num_days:
                        list.append(str(count))
                        count += 1
                    else:
                        list.append("x")
            result.append(list.copy())
        return result

    def get_date_data(self):
        date = datetime.datetime.today()
        return date


class DayShowerSingle(mayaa.MayaaSingleContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color(Colors.BACKGROUND)
        self.dayshower = DayShower(self)
        self.add_element(self.dayshower)
        self.center_element()


class Card(mayaa.MayaaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(500)
        self.set_fixed_width(500)
        self.set_background_color(Colors.BACKGROUND)
        self.set_rounded_borders(15)

        self.date = self.get_date_data()

        self.image = mayaa.MayaaImage(self)
        self.image.set_fixed_height(250)
        self.image.set_width_as_parent()
        self.image.set_image("demo\\images\\march.jpeg")
        self.image.center_element()
        self.image.set_background_color(Colors.BORDER)

        self.current_month = mayaa.MayaaTextLabel(self)
        self.current_month.set_width_as_parent()
        self.current_month.set_fixed_height(40)
        self.current_month.set_font_name("meiryoui")
        self.current_month.set_font_size(18)
        self.current_month.set_background_color(Colors.BACKGROUND)
        self.current_month.set_text_color(Colors.TEXT)
        self.current_month.center_text()
        self.current_month.set_text(f"{MONTHS[self.date.month]} - {self.date.year}")
        self.current_month.set_bold()
        self.days_shower = DayShowerSingle(self)

        self.add_element(self.image)
        self.add_element(self.current_month)
        self.add_element(self.days_shower)
        self.workspace = self.parent.workspace
        self.clicked = False
        self.anim = mayaa.Animation()
        self.animwidth = mayaa.AnimVal(self.anim, 800)
        self.animheight = mayaa.AnimVal(self.anim, 500)

    def late_init(self):
        self.image.resize_match_parent_width()
        return super().late_init()

    def get_date_data(self):
        date = datetime.datetime.today()
        return date

    def update(self):
        self.anim.update()
        for event in self.scene.manager.get_events():
            if event.type == mayaa.pg.MOUSEBUTTONDOWN and self.is_container_hovered():
                self.clicked = not self.clicked
                self.scene.informer.inform(
                    "card has been clicked", mayaa.InfoTagLevels.ALERT
                )

                if self.clicked:
                    self.animheight.move_to(
                        mayaa.pg.display.get_window_size()[1] - 20,
                        75,
                        mayaa.MayaaAnimationCurves.EASE_OUT_ELASTIC,
                    )
                    self.animwidth.move_to(
                        mayaa.pg.display.get_window_size()[1] - 20,
                        60,
                        mayaa.MayaaAnimationCurves.EASE_OUT_EXPO,
                    )
                else:
                    self.animheight.move_to(
                        500, 30, mayaa.MayaaAnimationCurves.EASE_OUT_ELASTIC
                    )

                    self.animwidth.move_to(
                        800, 30, mayaa.MayaaAnimationCurves.EASE_OUT_SINE
                    )
        if self.animwidth.is_moving():
            self.image.set_fixed_height(self.animheight.value // 2)
            self.image.resize_match_parent_width()
            self.set_fixed_height(self.animheight.value)
            self.set_fixed_width(self.animheight.value)
            self.workspace.card_shower.set_fixed_width(self.animwidth.value)
            self.workspace.remake_rendering_tree_from_here()


class CardShower(mayaa.MayaaSingleContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_height_as_parent()
        self.set_fixed_width(800)
        self.set_background_color(Colors.MONTH_CARD_BACKGROUND)
        self.center_element()
        self.set_rounded_borders(15)
        self.workspace = self.parent
        self.card = Card(self)

        self.add_element(self.card)


class CardDescriptor(mayaa.MayaaSingleContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_height_as_parent()
        self.set_width_as_remaining_area()
        self.set_background_color(Colors.BACKGROUND)
        self.workspace = self.parent
        self.textbox = mayaa.TextBox(self)
        self.textbox.set_fixed_height(40)
        self.textbox.set_width_as_parent()
        self.textbox.set_background_color("black")
        self.textbox.set_font_name("meiryoui")
        self.textbox.set_font_size(20)

        self.textbox.set_text_color("white")

        self.center_element_horizontal()
        self.add_element(self.textbox)

    def inf(self):
        self.scene.informer.inform("button press")


class Workspace(mayaa.MayaaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_height_as_remaining_area()
        self.set_width_as_parent()
        self.set_background_color(Colors.BACKGROUND)
        self.card_shower = CardShower(self)
        self.descriptor = CardDescriptor(self)
        self.add_element(self.descriptor)


class MainScene(mayaa.MayaaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color(mayaa.MayaaColors.BLACKBLUE)
        self.container = mayaa.MayaaStackVertical(self)
        self.container.set_as_core()
        self.container.set_background_color(mayaa.MayaaColors.ALICEWHITE)

        self.title_bar = TitleBar(self.container)
        self.workspace = Workspace(self.container)
        self.container.add_element(self.title_bar)
        self.container.add_element(self.workspace)

        self.container.remake_rendering_tree_from_here()


class CalendarApp(mayaa.MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Calendar")
        self.set_rendering_flags(mayaa.pg.RESIZABLE)
        self.set_display_size(800, 500)
        self.set_background_color(mayaa.MayaaColors.ALICEWHITE)
        self.set_clock(60)
        self.main_scene = MainScene(self, "mainscene", self.scene_manager)
        self.scene_manager.set_init_scene("mainscene")


app = CalendarApp()
app.run()
