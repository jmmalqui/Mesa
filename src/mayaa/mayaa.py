import math
import random
from typing import Dict, Union
import pygame as pg
from enum import Enum


def ease_in_sine(x):
    return 1 - math.cos((x * math.pi) / 2)


def ease_out_sine(x):
    return math.sin((x * math.pi) / 2)


def ease_in_out_sine(x):
    return -1 * (math.cos(math.pi * x) - 1) / 2


def ease_in_quad(x):
    return x * x


def ease_out_quad(x):
    return 1 - (1 - x) * (1 - x)


def ease_in_out_quad(x):
    if x < 0.5:
        return 2 * x * x
    else:
        return 1 - math.pow(-2 * x + 2, 2) / 2


def ease_in_cubic(x):
    return x * x * x


def ease_out_cubic(x):
    return 1 - math.pow(1 - x, 3)


def ease_in_out_cubic(x):
    if x < 0.5:
        return 4 * x * x * x
    else:
        return 1 - math.pow(-2 * x + 2, 3) / 2


def ease_in_quart(x):
    return x * x * x * x


def ease_out_quart(x):
    return 1 - math.pow(1 - x, 4)


def ease_in_out_quart(x):
    if x < 0.5:
        return 8 * x * x * x * x
    else:
        return 1 - math.pow(-2 * x + 2, 4) / 2


def ease_in_quint(x):
    return x * x * x * x * x


def ease_out_quint(x):
    return 1 - math.pow(1 - x, 5)


def ease_in_out_quint(x):
    if x < 0.5:
        return 16 * x * x * x * x * x
    else:
        return 1 - math.pow(-2 * x + 2, 5) / 2


def ease_in_expo(x):
    return 0 if x == 0 else math.pow(2, 10 * x - 10)


def ease_out_expo(x):
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)


def ease_in_out_expo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x < 0.5:
        return math.pow(2, 20 * x - 10) / 2
    else:
        return (2 - math.pow(2, -20 * x + 10)) / 2


def ease_in_circ(x):
    return 1 - math.sqrt(1 - math.pow(x, 2))


def ease_out_circ(x):
    return math.sqrt(1 - math.pow(x - 1, 2))


def ease_in_out_circ(x):
    if x < 0.5:
        return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2
    else:
        return (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2


def ease_in_back(x):
    c1 = 1.70158
    c2 = c1 + 1
    return c2 * x * x * x - c1 * x * x


def ease_out_back(x):
    c1 = 1.70158
    c2 = c1 + 1
    return 1 + c2 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)


def ease_in_out_back(x):
    c1 = 1.70158
    c2 = c1 * 1.525

    return (
        (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2
        if x < 0.5
        else (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2
    )


def ease_in_elastic(x):
    c1 = (2 * math.pi) / 3
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return math.pow(2, 10 * x - 10) * math.sin((x * 10 - 0.75) * c1)


def ease_out_elastic(x):
    c1 = (2 * math.pi) / 3
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c1) + 1


class MayaaColors:
    ALICEWHITE = [194, 206, 210]
    BLACKBLUE = [0, 14, 20]
    DARKBLUE = [0, 61, 92]


class MayaaDefaultGUI:
    DEFAULT_APP_HEIGHT = 600
    DEFAULT_APP_WIDTH = 360
    DEFAULT_APP_BACKGROUND_COLOR = MayaaColors.BLACKBLUE
    DEFAULT_CONTAINER_BACKGROUND_COLOR = MayaaColors.DARKBLUE
    DEFAULT_SCENE_BACKGROUND_COLOR = MayaaColors.DARKBLUE
    DEFAULT_FONT_SIZE = 16
    DEFAULT_TEXT_INPUT_SIZE = 16
    DEFAULT_FONT_TYPE = "consolas"
    DEFAULT_TEXT_COLOR = MayaaColors.ALICEWHITE
    DEFAULT_TEXT_HOVER_COLOR = MayaaColors.DARKBLUE
    HEADER_FONT_SIZE = 20
    SECONDARY_FONT_SIZE = 12


class MayaaRenderFlag(Enum):
    DISPLAY_HEIGHT_REMAIN = 0
    DISPLAY_HEIGHT_WINDOW = 1
    DISPLAY_HEIGHT_PARENT = 2
    DISPLAY_HEIGHT_PANEL = 3
    DISPLAY_WIDTH_REMAIN = 4
    DISPLAY_WIDTH_WINDOW = 5
    DISPLAY_WIDTH_PARENT = 6
    DISPLAY_WIDTH_PANEL = 7

    CORE_CONTAINER = 8
    SLIDABLE_CONTAINER = 9


class MayaaCoreFlag(Enum):
    NOT_DECLARED_ON_INIT = 0
    NON_TICK_BUSY_CLOCK = 1
    TICK_BUSY_CLOCK = 2


class MayaaAnimationCurves:
    EASE_IN_SINE = ease_in_sine
    EASE_OUT_SINE = ease_out_sine
    EASE_IN_OUT_SINE = ease_in_out_sine
    EASE_IN_QUAD = ease_in_quad
    EASE_OUT_QUAD = ease_out_quad
    EASE_IN_OUT_QUAD = ease_in_out_quad
    EASE_IN_CUBIC = ease_in_cubic
    EASE_OUT_CUBIC = ease_out_cubic
    EASE_IN_OUT_CUBIC = ease_in_out_cubic
    EASE_IN_QUART = ease_in_quart
    EASE_OUT_QUART = ease_out_quart
    EASE_IN_OUT_QUART = ease_in_out_quart
    EASE_IN_QUINT = ease_in_quint
    EASE_OUT_QUINT = ease_out_quint
    EASE_IN_OUT_QUINT = ease_in_out_quint
    EASE_IN_OUT_QUINT = ease_in_expo
    EASE_OUT_EXPO = ease_out_expo
    EASE_IN_OUT_EXPO = ease_in_out_expo
    EASE_IN_CIRC = ease_in_circ
    EASE_OUT_CIRC = ease_out_circ
    EASE_IN_OUT_CIRC = ease_in_out_circ
    EASE_IN_BACK = ease_in_back
    EASE_OUT_BACK = ease_out_back
    EASE_IN_OUT_BACK = ease_in_out_back
    EASE_IN_ELASTIC = ease_in_elastic
    EASE_OUT_ELASTIC = ease_out_elastic


class Animation:
    def __init__(self) -> None:
        self.val_list: list[AnimVal] = []

    def update(self):
        for value in self.val_list:
            value.update()


class AnimVal:
    def __init__(self, handler, value) -> None:
        handler.val_list.append(self)
        self.value = value
        self.start_value = value
        self.tick = 0
        self.begin_movement = False
        self.next_target_value = None
        self.anim_duration = 0
        self.value_diff = None
        self.animation_curve = None

    def is_moving(self):
        """Checks if the animation value has not reached its endpoints."""
        return self.begin_movement

    def perform(self):
        if self.next_target_value == None:
            return
        if self.tick == self.anim_duration:
            self.begin_movement = False
        if self.animation_curve:
            anim_pos = self.animation_curve(self.tick / self.anim_duration)
            self.value = self.start_value + anim_pos * self.value_diff
        else:
            self.value = -1

    def move_to(self, target_value, duration, curve):
        self.tick = 0
        self.begin_movement = True
        self.start_value = self.value
        self.next_target_value = target_value
        self.anim_duration = duration
        self.animation_curve = curve
        self.value_diff = target_value - self.value

    def update(self):
        if self.begin_movement:
            self.tick += 1
        self.perform()


class MayaaSceneManager:
    def __init__(self, core) -> None:
        self.core: MayaaCore = core
        self.scenes: Dict["str", MayaaScene] = {}
        self.current_scene_name = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.current_scene: Union[
            MayaaScene, MayaaCoreFlag
        ] = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.events = []

    def set_init_scene(self, scene_name):
        self.current_scene_name = scene_name

    def get_events(self):
        return self.events

    def pump_event(self, event):
        if event:
            self.events.append(event)
        else:
            self.events.clear()

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def update_scene_sizes(self):
        for scene in self.scenes.values():
            scene.resize()

    def update_scene_ids(self):
        self.current_scene = self.scenes[self.current_scene_name]

    def go_to(self, scene_name):
        self.current_scene_name = scene_name

    def resize_current_surface(self):
        if self.current_scene != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.current_scene.surface = pg.Surface(pg.display.get_window_size())
            self.current_scene.container.set_size_as_display()
            self.current_scene.container.set_position_as_core()
            self.current_scene.container.compute_elements_surfaces()
            self.current_scene.container.compute_elements_positions()

    def update(self):
        self.update_scene_ids()
        self.current_scene.__coreupdate__()

    def render(self):
        self.current_scene.__corerender__()


class MayaaScene:
    def __init__(self, core, scene_name, manager) -> None:
        self.core: MayaaCore = core
        self.name = scene_name
        self.position = pg.Vector2([0, 0])
        self.manager: MayaaSceneManager = manager
        self.manager.add_scene(self)
        self.container: _MayaaContainer = None
        self.modals = []  # Fancy word for pop up windows
        self.informer = self.core.info_tag
        self.surface = pg.Surface(self.core.display.get_size())
        self.is_active = False
        self.background_color = MayaaDefaultGUI.DEFAULT_SCENE_BACKGROUND_COLOR

    def set_background_color(self, color):
        self.background_color = color

    def resize(self):
        # why did I make this method
        self.surface = pg.Surface(self.core.display.get_size())

    def update(self):
        # do your update stuff here
        ...

    def update_container(self):
        self.container.__coreupdate__()

    def __coreupdate__(self):
        self.update()
        self.update_container()

    def blit_into_core(self):
        self.core.display.blit(self.surface, self.position)

    def fill_color(self):
        self.surface.fill(self.background_color)

    def render_container(self):
        self.container.__corerender__()

    def render_modals(self):
        # modals here modals there
        ...

    def render(self):
        # do your render stuff here  YES I KNOW DOCSTRINGS EXIST
        ...

    def __corerender__(self):
        self.fill_color()
        self.render_container()
        self.render_modals()
        self.render()
        self.blit_into_core()


class MayaaComponent:
    def __init__(self) -> None:
        pass


class _MayaaContainer:
    def __init__(self, parent) -> None:
        if isinstance(parent, MayaaScene) or isinstance(parent, _MayaaContainer):
            self.type_flag = MayaaRenderFlag.CORE_CONTAINER
            self.parent = parent
            self.parent.container = self
            self.elements = []
            self.width = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.height = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.width_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.height_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.margin = 0
            self.surface = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.position = pg.Vector2(0, 0)
            if isinstance(parent, MayaaScene):
                self.scene = parent
            if isinstance(parent, _MayaaContainer):
                self.scene = parent.scene
                self.absolute_position = self.parent.absolute_position + self.position
            else:
                self.absolute_position = pg.Vector2(0, 0)
            self.rect = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.background_color = MayaaDefaultGUI.DEFAULT_CONTAINER_BACKGROUND_COLOR
            self.original_color = self.background_color.copy()
            self.font = pg.font.SysFont(
                MayaaDefaultGUI.DEFAULT_FONT_TYPE, MayaaDefaultGUI.DEFAULT_FONT_SIZE
            )
            self.is_hovered = False
            self.borders = [
                [False, None, None],
                [False, None, None],
                [False, None, None],
                [False, None, None],
            ]

    def set_margin(self, margin):
        self.margin = margin

    def set_color_as_parent(self):
        self.background_color = self.parent.background_color
        self.original_color = self.background_color

    def set_background_color(self, color):
        self.background_color = color
        self.original_color = self.background_color

    def get_absolute_position(self):
        return self.parent.absolute_position + self.position

    def is_container_hovered(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

    def populate_rects(self):
        ...

    def compute_elements_positions(self):
        for element in self.elements:
            element.compute_elements_positions()
            element.populate_rects()

    def _compute_elements_surfaces_handle_width_case(self, element):
        if element.width_flag == MayaaRenderFlag.DISPLAY_WIDTH_WINDOW:
            return pg.display.get_window_size()[0]
        if element.width_flag == MayaaRenderFlag.DISPLAY_WIDTH_PARENT:
            return element.parent.width
        if element.width_flag == MayaaRenderFlag.DISPLAY_WIDTH_REMAIN:
            accum_width = 0
            for other_element in self.elements:
                if other_element == element:
                    continue
                else:
                    if (
                        other_element.width == MayaaCoreFlag.NOT_DECLARED_ON_INIT
                        or other_element.width_flag
                        == MayaaRenderFlag.DISPLAY_WIDTH_REMAIN
                    ):
                        raise ValueError(
                            "Could not build surface. No enough information was given [TWO LAYOUTS WITH NO DEFINED WIDTH]"
                        )
                    accum_width += other_element.width
            return element.parent.width - accum_width
        return element.width

    def _compute_elements_surfaces_handle_height_case(self, element):
        if element.height_flag == MayaaRenderFlag.DISPLAY_HEIGHT_WINDOW:
            return pg.display.get_window_size()[1]
        if element.height_flag == MayaaRenderFlag.DISPLAY_HEIGHT_PARENT:
            return element.parent.height
        if element.height_flag == MayaaRenderFlag.DISPLAY_HEIGHT_REMAIN:
            accum_height = 0
            for other_element in self.elements:
                if other_element == element:
                    continue
                else:
                    if (
                        other_element.height == MayaaCoreFlag.NOT_DECLARED_ON_INIT
                        or other_element.height_flag
                        == MayaaRenderFlag.DISPLAY_HEIGHT_REMAIN
                    ):
                        raise ValueError(
                            "Could not build surface. No enough information was given [TWO LAYOUTS WITH NO DEFINED HEIGHT]"
                        )
                    accum_height += other_element.height
            return element.parent.height - accum_height
        return element.height

    def compute_elements_surfaces(self):
        self.rect = pg.Rect(self.absolute_position, self.surface.get_size())
        for element in self.elements:
            element.height = self._compute_elements_surfaces_handle_height_case(element)
            element.width = self._compute_elements_surfaces_handle_width_case(element)

            element.surface = pg.Surface(
                [
                    element.width - 2 * element.margin,
                    element.height - 2 * element.margin,
                ]
            )
            if isinstance(element, _MayaaContainer):
                element.compute_elements_surfaces()

    def set_as_core(self):
        self.position = pg.Vector2(0, 0)
        self.absolute_position = pg.Vector2(0, 0)
        self.width = pg.display.get_window_size()[0]
        self.height = pg.display.get_window_size()[1]
        self.surface = pg.Surface([self.width, self.height])
        self.rect = pg.Rect(self.absolute_position, pg.display.get_window_size())

    def set_position_as_core(self):
        self.position = pg.Vector2(0, 0)
        self.absolute_position = pg.Vector2(0, 0)

    def borderless(self):
        self.borders = [
            [False, None, None],
            [False, None, None],
            [False, None, None],
            [False, None, None],
        ]

    def border(self, color, thick):
        self.border_left(color, thick)
        self.border_right(color, thick)
        self.border_up(color, thick)
        self.border_down(color, thick)

    def border_left(self, color, thick):
        self.borders[0][0] = True
        self.borders[0][1] = thick
        self.borders[0][2] = color

    def border_right(self, color, thick):
        self.borders[1][0] = True
        self.borders[1][1] = thick
        self.borders[1][2] = color

    def border_up(self, color, thick):
        self.borders[2][0] = True
        self.borders[2][1] = thick
        self.borders[2][2] = color

    def border_down(self, color, thick):
        self.borders[3][0] = True
        self.borders[3][1] = thick
        self.borders[3][2] = color

    def set_size_as_display(self):
        self.width = pg.display.get_window_size()[0]
        self.height = pg.display.get_window_size()[1]
        self.surface = pg.Surface([self.width, self.height])

    def set_height_as_display(self):
        self.height_flag = MayaaRenderFlag.DISPLAY_HEIGHT_WINDOW

    def set_width_as_display(self):
        self.width_flag = MayaaRenderFlag.DISPLAY_WIDTH_WINDOW

    def set_height_as_remaining_area(self):
        self.height_flag = MayaaRenderFlag.DISPLAY_HEIGHT_REMAIN

    def set_width_as_remaining_area(self):
        self.width_flag = MayaaRenderFlag.DISPLAY_WIDTH_REMAIN

    def set_height_as_parent(self):
        self.height_flag = MayaaRenderFlag.DISPLAY_HEIGHT_PARENT

    def set_width_as_parent(self):
        self.width_flag = MayaaRenderFlag.DISPLAY_WIDTH_PARENT

    def set_fixed_width(self, value):
        self.width = value

    def set_fixed_height(self, value):
        self.height = value

    def add_element(self, element):
        if isinstance(element, (MayaaComponent, _MayaaContainer)):
            self.elements.append(element)
        else:
            raise ValueError(
                "Classes that are not Component or Containers cannot be added to a Container parent"
            )

    def update(self):
        ...

    def inherit_update(self):
        ...

    def __coreupdate__(self):
        self.update()
        self.inherit_update()
        for element in self.elements:
            element.__coreupdate__()

    def render(self):
        ...

    def __corerender__(self):
        self.surface.fill(self.background_color)

        self.render_borders()
        self.render()

        for element in self.elements:
            element.__corerender__()
        self.parent.surface.blit(self.surface, self.position)

    def render_borders(self):
        for index, border in enumerate(self.borders):
            if border[0] == False:
                continue
            else:
                if index == 0:
                    pg.draw.rect(
                        self.surface,
                        border[2],
                        pg.Rect(0, 0, border[1], self.surface.get_height()),
                    )
                if index == 1:
                    pg.draw.rect(
                        self.surface,
                        border[2],
                        pg.Rect(
                            self.surface.get_width() - border[1],
                            0,
                            self.surface.get_width() - border[1],
                            self.surface.get_height(),
                        ),
                    )
                if index == 2:
                    pg.draw.rect(
                        self.surface,
                        border[2],
                        pg.Rect(0, 0, self.surface.get_width(), border[1]),
                    )
                if index == 3:
                    pg.draw.rect(
                        self.surface,
                        border[2],
                        pg.Rect(
                            0,
                            self.surface.get_height() - border[1],
                            self.surface.get_width(),
                            border[1],
                        ),
                    )


class MayaaStackVertical(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def compute_elements_positions(self):
        accum = pg.Vector2(0, 0)

        for element in self.elements:
            element.position.x = accum.x + element.margin
            element.position.y = accum.y + element.margin
            element.absolute_position.x = (
                self.absolute_position.x + accum.x + element.margin
            )
            element.absolute_position.y = (
                self.absolute_position.y + accum.y + element.margin
            )
            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )
            accum.y += element.height

        return super().compute_elements_positions()


class MayaaStackHorizontal(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def compute_elements_positions(self):
        accum = pg.Vector2(0, 0)
        for element in self.elements:
            element.position.x = accum.x + element.margin
            element.position.y = accum.y + element.margin
            element.absolute_position.x = (
                self.absolute_position.x + accum.x + element.margin
            )
            element.absolute_position.y = (
                self.absolute_position.y + accum.y + element.margin
            )
            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )
            accum.x += element.width
        return super().compute_elements_positions()


class MayaaSlidablePanel(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.type_flag = MayaaRenderFlag.SLIDABLE_CONTAINER
        self.width_flag = MayaaRenderFlag.DISPLAY_WIDTH_PANEL
        self.height_flag = MayaaRenderFlag.DISPLAY_HEIGHT_PANEL


class MayaaSlidablePanelHorizontal(MayaaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.type_flag = MayaaRenderFlag.SLIDABLE_CONTAINER
        self.perform_late_init = True
        self.rect_list = []
        self.rect_width = 10
        self.handle_get = False
        self.mouse_handle = pg.Vector2(pg.mouse.get_pos())
        self.separator = MayaaCoreFlag.NOT_DECLARED_ON_INIT

    def populate_rects(self):
        self.rect_list.clear()
        if len(self.elements) > 1:
            for index, element in enumerate(self.elements[:-1]):
                rectx = element.absolute_position.x + element.width - self.rect_width
                recty = element.absolute_position.y
                rectw = self.rect_width
                recth = element.height

                nextrectx = self.elements[index + 1].absolute_position.x
                nextrecty = self.elements[index + 1].absolute_position.y
                nextrectw = self.rect_width
                nextrecth = self.elements[index + 1].height
                self.rect_list.append(pg.Rect(rectx, recty, rectw, recth))
                self.rect_list.append(
                    pg.Rect(nextrectx, nextrecty, nextrectw, nextrecth)
                )

    def inherit_update(self):
        if self.perform_late_init:
            self.populate_rects()
            self.perform_late_init = False
        self.rect_get = False
        rel = [0, 0]
        if self.handle_get:
            rel = pg.Vector2(pg.mouse.get_pos()) - self.mouse_handle
        # self.scene.informer.inform(f"{rel}")
        for index, rect in enumerate(self.rect_list):
            if rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed(3)[0]:
                if self.rect_get == False:
                    self.mouse_handle = pg.mouse.get_pos()
                self.handle_get = True
                self.rect_get = True

                if index % 2 == 1:
                    width = self.elements[index * 2 - 1].width

                    self.elements[index * 2 - 1].set_fixed_width(width - rel[0])
                    self.populate_rects()
                if index % 2 == 0:
                    width = self.elements[index * 2].width

                    self.elements[index * 2].set_fixed_width(width + rel[0])
                    self.populate_rects()
                self.compute_elements_surfaces()
                self.compute_elements_positions()

        if self.rect_get == False and pg.mouse.get_pressed(3)[0] == False:
            self.scene.informer.inform("handle lost")
            self.handle_get = False
            #  0   12    34   56   7
            #  0   1     2    3    4


class TagProperty:
    def __init__(self, fill, border, ttl) -> None:
        self.fill = fill
        self.border = border
        self.ttl = ttl


class InfoTagLevels:
    NOTIFY = TagProperty([0, 70, 0], [0, 170, 0], 100)
    ALERT = TagProperty([70, 70, 0], [170, 170, 0], 250)
    CRITICAL = TagProperty([70, 0, 0], [170, 0, 0], 400)
    SPECIAL = TagProperty([70, 0, 70], [170, 0, 170], 300)


class InfoTagHandler:
    def __init__(self, core) -> None:
        self.core: MayaaCore = core
        self.tags: list[InfoTag] = []
        self.tag_font = pg.font.SysFont(
            MayaaDefaultGUI.DEFAULT_FONT_TYPE, 15, False, True
        )

    def inform(self, information, level=InfoTagLevels.NOTIFY):
        self.tags.append(InfoTag(self, information, level))
        self.update_tag_ids()

    def update_tag_ids(self):
        tag_num = len(self.tags)
        for tag_id, tag in enumerate(self.tags):
            tag.set_id(tag_num - tag_id - 1)

    def update(self):
        for tag in self.tags:
            tag.update()

    def render(self):
        for tag in self.tags:
            tag.render()


class InfoTag:
    def __init__(self, handler, information, level: TagProperty) -> None:
        self.id = 0
        self.information = information
        self.level = level
        self.handler: InfoTagHandler = handler
        self.animation = Animation()
        self.tick = 0
        self.x = AnimVal(self.animation, 0)
        self.y = AnimVal(self.animation, 0)
        self.alpha = AnimVal(self.animation, 255)
        self.text = self.handler.tag_font.render(
            self.information, True, MayaaDefaultGUI.DEFAULT_TEXT_COLOR, wraplength=450
        )
        self.surface = pg.Surface(
            [self.text.get_width() + 50, self.text.get_height() + 20]
        ).convert_alpha()
        self.rect = pg.Rect([0, 0], self.surface.get_size())
        self.x.move_to(60, 60, MayaaAnimationCurves.EASE_OUT_CUBIC)
        self.gap = 20
        self.vanishing_time = 100

    def set_id(self, id):
        self.id = id
        y_difference = 0
        for tag in self.handler.tags:
            if tag.id < self.id:
                y_difference += self.gap
                y_difference += tag.surface.get_height()
        self.y.move_to(-1 * y_difference, 30, MayaaAnimationCurves.EASE_OUT_SINE)

    def update(self):
        self.tick += 1
        self.animation.update()
        self.rect = pg.Rect([0, 0], self.surface.get_size())
        if self.tick == self.level.ttl:
            self.alpha.move_to(
                0, self.vanishing_time, MayaaAnimationCurves.EASE_IN_SINE
            )
        if self.tick >= self.level.ttl + self.vanishing_time:
            self.handler.tags.remove(self)
            self.handler.update_tag_ids()

    def render(self):
        self.surface.fill("black")
        pg.draw.rect(self.surface, self.level.fill, self.rect, 0)
        pg.draw.rect(self.surface, self.level.border, self.rect, 2)
        self.surface.blit(self.text, [25, 10])
        self.surface.set_alpha(self.alpha.value)
        self.handler.core.display.blit(
            self.surface,
            [
                self.x.value,
                self.handler.core.display.get_height()
                - self.gap
                - self.surface.get_height()
                + self.y.value,
            ],
        )


class MayaaCore:
    def __init__(self) -> None:
        pg.init()
        self.perform_late_init = True
        self.display = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.clock = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.clock_type = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.clock_fps = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.rendering_flags = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.bacgkround_color = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.delta_time = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.caption = MayaaCoreFlag.NOT_DECLARED_ON_INIT

        self.info_tag = InfoTagHandler(self)
        self.scene_manager = MayaaSceneManager(self)

    def set_application_name(self, title):
        self.caption = title
        pg.display.set_caption(self.caption)

    def set_rendering_flags(self, *flags):
        self.rendering_flags = flags

    def set_clock(self, fps):
        self.clock = pg.Clock()
        self.clock_type = MayaaCoreFlag.NON_TICK_BUSY_CLOCK
        self.clock_fps = fps

    def set_busy_clock(self, fps):
        self.clock = pg.Clock()
        self.clock_type = MayaaCoreFlag.TICK_BUSY_CLOCK
        self.clock_fps = fps

    def set_display_size(self, height, width):
        if self.rendering_flags == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.rendering_flags = 0
            self.display = pg.display.set_mode(
                [height, width], flags=self.rendering_flags
            )
        else:
            flag = self.rendering_flags[0]
            for f in self.rendering_flags[0:]:
                flag |= f
            self.display = pg.display.set_mode([height, width], flag)

    def late_init(self):
        if self.display == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            raise ValueError(
                "Display was not initialized, perhaps you forgot set_display_size() ?"
            )

        if self.clock == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.set_clock(60)
        if self.bacgkround_color == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.bacgkround_color = MayaaDefaultGUI.DEFAULT_APP_BACKGROUND_COLOR

    def check_events(self):
        self.scene_manager.pump_event(None)
        for event in pg.event.get():
            self.scene_manager.pump_event(event)
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                self.info_tag.inform("Info System", InfoTagLevels.NOTIFY)

            if event.type == pg.VIDEORESIZE:
                self.scene_manager.resize_current_surface()

    def set_background_color(self, color):
        self.bacgkround_color = color

    def update(self):
        ...

    def __coreupdate__(self):
        self.mouse_rel = pg.mouse.get_rel()

        if self.perform_late_init:
            self.late_init()
            self.perform_late_init = not self.perform_late_init

        self.scene_manager.update()
        self.info_tag.update()

    def render(self):
        ...

    def __corerender__(self):
        self.display.fill(self.bacgkround_color)
        self.scene_manager.render()
        self.info_tag.render()

        self.render()
        pg.display.flip()

    def make_clock(self):
        if self.clock_type == MayaaCoreFlag.NON_TICK_BUSY_CLOCK:
            self.delta_time = self.clock.tick(self.clock_fps)
        elif self.clock_type == MayaaCoreFlag.TICK_BUSY_CLOCK:
            self.delta_time = self.clock.tick_busy_loop(self.clock_fps)

    def run(self):
        while True:
            self.make_clock()
            self.check_events()
            self.__coreupdate__()
            self.__corerender__()
