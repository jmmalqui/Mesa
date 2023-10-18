import math
import random
from typing import Dict, Union
import pygame as pg
from enum import Enum


def color_lerp(c1, c2, val, max):
    c1 = pg.Vector3(c1)
    c2 = pg.Vector3(c2)
    diff = c2 - c1
    step = diff / max
    return c1 + step * val


def color_picker(color, size=100, step=10):
    surface = pg.Surface([size, size])
    left_color = []
    color_per_row = int(size // step)
    for i in range(color_per_row):
        left_color.append(color_lerp([255, 255, 255], [0, 0, 0], i, color_per_row))
    right_color = []
    for i in range(color_per_row):
        right_color.append(color_lerp(color, [0, 0, 0], i, color_per_row))
    for y in range(color_per_row):
        for x in range(color_per_row):
            pg.draw.rect(
                surface,
                color_lerp(left_color[y], right_color[y], x, color_per_row),
                pg.Rect(step * x, step * y, step, step),
                0,
            )
    pg.draw.rect(surface, "white", surface.get_rect(), 1)
    return surface


def circle_chop(surface: pg.Surface):
    radius = min(*surface.get_size()) // 2
    frame = pg.Surface([radius * 2, radius * 2], pg.SRCALPHA)
    pg.draw.circle(frame, "white", [radius, radius], radius, 0)
    return_surface = surface.subsurface(
        pg.Rect(
            (pg.Vector2(surface.get_rect().center) - pg.Vector2(radius, radius)),
            (radius * 2, radius * 2),
        )
    ).copy()
    return_surface.blit(frame, [0, 0], None, pg.BLEND_RGBA_MIN)
    return return_surface


def rounded_border(surface: pg.Surface, border_radius: int):
    size = surface.get_size()
    frame = pg.Surface(size, pg.SRCALPHA)
    pg.draw.rect(frame, "white", pg.Rect(0, 0, *size), 0, border_radius)
    return_surface = surface.copy()
    return_surface.blit(frame, [0, 0], None, pg.BLEND_RGBA_MIN)
    return return_surface


def deform(surface: pg.Surface, x: int):
    pixelarray = pg.surfarray.array3d(surface)
    width = surface.get_width()
    height = surface.get_height()
    new_surf = pg.Surface([width, height + x], pg.SRCALPHA)
    newpixelarray = pg.surfarray.array3d(new_surf)
    for i, row in enumerate(pixelarray):
        space = int(x - (x * i / width))
        pref = [[0, 0, 0] for a in range(space)]
        if space == 0:
            newpixelarray[i][0:height] = pixelarray[i]
        if space != 0:
            newpixelarray[i][0:space] = pref
            newpixelarray[i][space : space + height] = pixelarray[i]
        if x - space != 0:
            sub = [[0, 0, 0] for b in range(x - space)]
            newpixelarray[i][space + height :] = sub
    pg.surfarray.blit_array(new_surf, newpixelarray)
    return new_surf


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
    SLIDABLE_CONTAINER_VERTICAL = 9
    SLIDABLE_CONTAINER_HORIZONTAL = 10

    TEXT_CENTERED_V = 11
    TEXT_CENTERED_H = 12
    ELEMENT_CENTERED_V = 13
    ELEMENT_CENTERED_H = 14


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


class TextBuffer:
    def __init__(self) -> None:
        self.buffer = ""
        self.pointer = 0

    def shift_left(self):
        if self.pointer != 0:
            self.pointer -= 1

    def shift_right(self):
        if self.pointer != len(self.buffer):
            self.pointer += 1

    def add(self, char):
        if self.pointer == 0:
            self.buffer = char + self.buffer
        elif self.pointer == len(self.buffer):
            self.buffer = self.buffer + char
        else:
            self.left_part = self.buffer[: self.pointer]

            self.right_part = self.buffer[self.pointer :]
            self.buffer = self.left_part + char + self.right_part

    def pop(self):
        if self.pointer == len(self.buffer):
            self.buffer = self.buffer[:-1]
        else:
            self.left_part = self.buffer[: self.pointer - 1]

            self.right_part = self.buffer[self.pointer :]
            self.buffer = self.left_part + self.right_part
        self.shift_left()

    def delete(self):
        self.buffer = ""
        self.pointer = 0


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
        print(self.current_scene_name)

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
            self.current_scene.container.remake_rendering_tree_from_here()

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
        self.modals = []
        self.informer = self.core.info_tag
        self.surface = pg.Surface(self.core.display.get_size())
        self.is_active = False
        self.background_color = MayaaDefaultGUI.DEFAULT_SCENE_BACKGROUND_COLOR

    def set_background_color(self, color):
        self.background_color = color

    def resize(self):
        self.surface = pg.Surface(pg.display.get_window_size())
        self.container.set_size_as_display()
        self.container.set_position_as_core()
        self.container.remake_rendering_tree_from_here()

    def update(self):
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
            self.should_late_init = True
            self.radius = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.debug_color = [
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ]

    def set_rounded_borders(self, radius):
        self.radius = radius

    def late_init(self):
        ...

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
        if element.parent.type_flag == MayaaRenderFlag.SLIDABLE_CONTAINER_HORIZONTAL:
            return element.parent.width // 2
        if element.parent.type_flag == MayaaRenderFlag.SLIDABLE_CONTAINER_VERTICAL:
            return element.parent.width

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
        if element.parent.type_flag == MayaaRenderFlag.SLIDABLE_CONTAINER_HORIZONTAL:
            return element.parent.height
        if element.parent.type_flag == MayaaRenderFlag.SLIDABLE_CONTAINER_VERTICAL:
            return element.parent.height // 2
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
                ],
                flags=pg.SRCALPHA,
            )

            if isinstance(element, _MayaaContainer):
                element.compute_elements_surfaces()

    def compute_extra_inherit(self):
        for element in self.elements:
            element.compute_extra_inherit()

    def remake_rendering_tree_from_here(self):
        self.compute_elements_surfaces()
        self.compute_elements_positions()
        self.compute_extra_inherit()

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
        if self.should_late_init:
            self.late_init()
            self.should_late_init = False
        self.update()
        self.inherit_update()
        for element in self.elements:
            element.__coreupdate__()

    def render(self):
        ...

    def inherit_render(self):
        ...

    def __corerender__(self):
        self.surface.fill(self.background_color)

        self.render_borders()
        self.render()

        for element in self.elements:
            element.__corerender__()
        self.inherit_render()
        if self.radius != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.surface = rounded_border(self.surface, self.radius)
        if self.scene.core.on_debug == False:
            self.surface.set_alpha(255)

            self.parent.surface.blit(self.surface, self.position)
        else:
            thick = 2

            pg.draw.rect(
                self.surface,
                self.debug_color,
                self.surface.get_rect(),
                thick,
            )

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
        self.type_flag = MayaaRenderFlag.CORE_CONTAINER
        self.width_flag = MayaaRenderFlag.DISPLAY_WIDTH_PANEL
        self.height_flag = MayaaRenderFlag.DISPLAY_HEIGHT_PANEL

    def late_init(self):
        return super().late_init()


class MayaaSlidablePanelVertical(MayaaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.type_flag = MayaaRenderFlag.SLIDABLE_CONTAINER_VERTICAL
        self.perform_late_init = True
        self.slider_height = 5
        self.slider_color = "black"
        self.handle_get = False
        self.mouse_handle = pg.Vector2(pg.mouse.get_pos())
        self.separator = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.middle_x = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.middle_y = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.slider = MayaaCoreFlag.NOT_DECLARED_ON_INIT

    def set_slider_color(self, color):
        self.slider_color = color

    def compute_extra_inherit(self):
        self.remake_slider()
        for element in self.elements:
            element.compute_extra_inherit()

    def late_init(self):
        self.remake_slider()
        return super().late_init()

    def remake_slider(self):
        print("im redone :)", self)
        self.middle_x = 0
        self.middle_y = self.height // 2
        self.slider = pg.Rect(
            self.middle_x,
            self.middle_y - self.slider_height,
            self.width,
            self.slider_height,
        )

    def inherit_update(self):
        if len(self.elements) == 0:
            raise ValueError("A Slidable Panel must have children elements")
        if len(self.elements) != 2:
            raise ValueError(f"Panel must have two children elements")
        return super().inherit_update()

    def inherit_render(self):
        pg.draw.rect(self.surface, self.slider_color, self.slider, 0)


class MayaaSlidablePanelHorizontal(MayaaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.type_flag = MayaaRenderFlag.SLIDABLE_CONTAINER_HORIZONTAL
        self.perform_late_init = True
        self.slider_width = 5
        self.handle_get = False
        self.slider_color = "black"
        self.mouse_handle = pg.Vector2(pg.mouse.get_pos())
        self.separator = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.middle_x = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.middle_y = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.slider = MayaaCoreFlag.NOT_DECLARED_ON_INIT

    def set_slider_color(self, color):
        self.slider_color = color

    def compute_extra_inherit(self):
        self.remake_slider()
        for element in self.elements:
            element.compute_extra_inherit()

    def late_init(self):
        self.remake_slider()
        return super().late_init()

    def remake_slider(self):
        print("im redone :)", self)
        self.middle_x = self.width // 2
        self.middle_y = 0
        self.slider = pg.Rect(
            self.middle_x - self.slider_width,
            self.middle_y,
            self.slider_width,
            self.height,
        )

    def inherit_update(self):
        if len(self.elements) == 0:
            raise ValueError("A Slidable Panel must have children elements")
        if len(self.elements) != 2:
            raise ValueError(f"Panel must have two children elements")
        return super().inherit_update()

    def inherit_render(self):
        pg.draw.rect(self.surface, self.slider_color, self.slider, 0)


class MayaaImage(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.image = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.original_image = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.image_pos = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.element_center_v_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.element_center_h_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT

    def border_image(self):
        self.image = circle_chop(self.image)
        self.original_image = self.image.copy()

    def center_element_vertical(self):
        self.element_center_v_flag = MayaaRenderFlag.ELEMENT_CENTERED_V

    def center_element_horizontal(self):
        self.element_center_h_flag = MayaaRenderFlag.ELEMENT_CENTERED_H

    def center_element(self):
        self.center_element_vertical()
        self.center_element_horizontal()

    def set_image(self, path):
        if path == None:
            self.image = None
            self.original_image = None
        else:
            self.image = pg.image.load(path).convert_alpha()
            self.original_image = self.image.copy()

    def resize_image(self, size):
        self.image = pg.transform.smoothscale(self.original_image, size)

    def resize_match_parent_height(self):
        height = self.height
        print(height)
        width = (
            self.original_image.get_width() * height / self.original_image.get_height()
        )
        print(width, height)
        print(self.image.get_size(), self.original_image.copy())
        self.image = pg.transform.smoothscale(self.original_image, [width, height])

    def resize_match_parent_width(self):
        width = self.width
        height = (
            self.original_image.get_height() * width / self.original_image.get_width()
        )
        self.image = pg.transform.smoothscale(self.original_image, [width, height])

    def render(self):
        self.image_pos = pg.Vector2(0, 0)
        if self.element_center_v_flag == MayaaRenderFlag.ELEMENT_CENTERED_V:
            self.image_pos.y = (self.height - self.image.get_height()) // 2

        if self.element_center_h_flag == MayaaRenderFlag.ELEMENT_CENTERED_H:
            self.image_pos.x = (self.width - self.image.get_width()) // 2
        if self.image != None:
            self.surface.blit(self.image, self.image_pos)
        else:
            self.surface.fill("black")


class MayaaSingleContainer(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.element_center_v_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.element_center_h_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT

    def center_element_vertical(self):
        self.element_center_v_flag = MayaaRenderFlag.ELEMENT_CENTERED_V

    def center_element_horizontal(self):
        self.element_center_h_flag = MayaaRenderFlag.ELEMENT_CENTERED_H

    def center_element(self):
        self.center_element_vertical()
        self.center_element_horizontal()

    def compute_elements_positions(self):
        if len(self.elements) != 1:
            raise ValueError(
                f"MayaSingleContainer can only handle one children container, you may have added more than two or not added any.  Num of Children: {len(self.elements)}"
            )
        element: _MayaaContainer = self.elements[0]
        if self.element_center_v_flag == MayaaRenderFlag.ELEMENT_CENTERED_V:
            element.position.y = (self.height - element.surface.get_height()) // 2

            element.absolute_position.y = self.absolute_position.y + element.position.y
            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )
        if self.element_center_h_flag == MayaaRenderFlag.ELEMENT_CENTERED_H:
            element.position.x = (self.width - element.surface.get_width()) // 2
            element.absolute_position.x = self.absolute_position.x + element.position.x

            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )
        return super().compute_elements_positions()

    def late_init(self):
        if len(self.elements) != 1:
            raise ValueError(
                "MayaSingleContainer can only handle one children container"
            )
        return super().late_init()


class TextBox(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.font_name = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.font = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.font_size = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.text = ""
        self.text_surface = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.bold = False
        self.italic = False
        self.text_background_color = None
        self.antialias = True
        self.text_color = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.buffer = TextBuffer()
        self.text_center_v_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.text_center_h_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.metrics = []
        self.pointer_position = self.get_pointer_position()
        self.blink = False
        self.tick = 0

    def get_pointer_position(self):
        return (sum([x[4] for x in self.metrics[: self.buffer.pointer]]),)

    def handle_events(self):
        for event in self.scene.manager.get_events():
            if event.type == pg.TEXTINPUT:
                self.buffer.add(event.text)
                self.text = self.buffer.buffer
                self.make_text_surface()
                self.buffer.shift_right()
                self.metrics = pg.Font.metrics(self.font, self.text)
                self.pointer_position = self.get_pointer_position()

            if event.type == pg.TEXTEDITING:
                self.scene.informer.inform(f"{event}")
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    self.buffer.delete()
                    self.text = self.buffer.buffer
                    self.make_text_surface()
                    self.metrics = pg.Font.metrics(self.font, self.text)
                    self.pointer_position = self.get_pointer_position()
                if event.key == 8:
                    self.buffer.pop()
                    self.text = self.buffer.buffer
                    self.make_text_surface()
                    self.metrics = pg.Font.metrics(self.font, self.text)
                    self.pointer_position = self.get_pointer_position()
                if event.key == pg.K_LEFT:
                    self.buffer.shift_left()
                    self.pointer_position = self.get_pointer_position()
                if event.key == pg.K_RIGHT:
                    self.buffer.shift_right()

                    self.pointer_position = self.get_pointer_position()
                if event.key == pg.K_RETURN:
                    self.text += "\n"
                    self.make_text_surface()
                    self.metrics = pg.Font.metrics(self.font, self.text)
                    self.pointer_position = self.get_pointer_position()

    def set_text_color(self, text_color):
        if self.text_color == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.text_color = text_color
        if self.text_surface != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            if text_color != self.text_color:
                self.text_color = text_color
                self.make_text_surface()

    def set_text_background_color(self, color):
        self.text_background_color = color

    def unset_antialiasing(self):
        self.antialias = False

    def set_bold(self):
        self.bold = True

    def set_italic(self):
        self.italic = True

    def set_font_name(self, font_name):
        self.font_name = font_name

    def set_font_size(self, font_size):
        if self.font_size == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.font_size = font_size
        if self.font_size != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            if font_size != self.font_size:
                self.font_size = font_size
                self.font = pg.font.SysFont(
                    self.font_name, self.font_size, self.bold, self.italic
                )
                self.make_text_surface()

    def set_text(self, text):
        if self.text == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.text = text
        if self.text_surface != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            if text != self.text:
                self.text = text
                self.make_text_surface()

    def make_text_surface(self):
        "called"
        self.text_surface = self.font.render(
            self.text,
            self.antialias,
            self.text_color,
            self.text_background_color,
        )

    def late_init(self):
        self.font = pg.font.SysFont(
            self.font_name, self.font_size, self.bold, self.italic
        )
        self.make_text_surface()
        return super().late_init()

    def inherit_update(self):
        self.tick += 1
        self.handle_events()
        return super().inherit_update()

    def render(self):
        self.text_position = pg.Vector2(0, 0)
        if self.text_center_v_flag == MayaaRenderFlag.TEXT_CENTERED_V:
            self.text_position.y = (self.height - self.text_surface.get_height()) // 2

        if self.text_center_h_flag == MayaaRenderFlag.TEXT_CENTERED_H:
            self.text_position.x = (self.width - self.text_surface.get_width()) // 2
        if self.tick % 5 == 0:
            self.blink = not self.blink
        if self.blink:
            pg.draw.rect(
                self.surface,
                "cyan",
                [self.pointer_position[0], 0, 2, 24],
                0,
            )
        else:
            pg.draw.rect(
                self.surface,
                "black",
                [self.pointer_position[0], 0, 2, 24],
                0,
            )
        self.surface.blit(self.text_surface, self.text_position)


class MayaaTextLabel(_MayaaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.font_name = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.font = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.font_size = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.text = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.text_surface = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.bold = False
        self.italic = False
        self.text_background_color = None
        self.antialias = True
        self.text_color = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.text_center_v_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.text_center_h_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT

    def center_text_vertical(self):
        self.text_center_v_flag = MayaaRenderFlag.TEXT_CENTERED_V

    def center_text_horizontal(self):
        self.text_center_h_flag = MayaaRenderFlag.TEXT_CENTERED_H

    def center_text(self):
        self.center_text_horizontal()
        self.center_text_vertical()

    def set_text_color(self, text_color):
        if self.text_color == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.text_color = text_color
        if self.text_surface != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            if text_color != self.text_color:
                self.text_color = text_color
                self.make_text_surface()

    def set_text_background_color(self, color):
        self.text_background_color = color

    def unset_antialiasing(self):
        self.antialias = False

    def set_bold(self):
        self.bold = True

    def set_italic(self):
        self.italic = True

    def set_font_name(self, font_name):
        self.font_name = font_name

    def set_font_size(self, font_size):
        if self.font_size == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.font_size = font_size
        if self.font_size != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            if font_size != self.font_size:
                self.font_size = font_size
                self.font = pg.font.SysFont(
                    self.font_name, self.font_size, self.bold, self.italic
                )
                self.make_text_surface()

    def set_text(self, text):
        if self.text == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.text = text
        if self.text_surface != MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            if text != self.text:
                self.text = text
                self.make_text_surface()

    def make_text_surface(self):
        self.text_surface = self.font.render(
            self.text, self.antialias, self.text_color, self.text_background_color
        )

    def late_init(self):
        self.font = pg.font.SysFont(
            self.font_name, self.font_size, self.bold, self.italic
        )
        self.make_text_surface()
        return super().late_init()

    def render(self):
        self.text_position = pg.Vector2(0, 0)
        if self.text_center_v_flag == MayaaRenderFlag.TEXT_CENTERED_V:
            self.text_position.y = (self.height - self.text_surface.get_height()) // 2

        if self.text_center_h_flag == MayaaRenderFlag.TEXT_CENTERED_H:
            self.text_position.x = (self.width - self.text_surface.get_width()) // 2

        self.surface.blit(self.text_surface, self.text_position)


class MayaaButtonText(MayaaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.signal = MayaaCoreFlag.NOT_DECLARED_ON_INIT
        self.set_color_as_parent()
        self.callback_result = None

    def get_result(self):
        return self.callback_result

    def set_signal(self, func):
        self.signal = func

    def handle_events(self):
        for event in self.scene.manager.get_events():
            if event.type == pg.MOUSEBUTTONDOWN and self.is_container_hovered():
                self.callback_result = self.signal()

    def inherit_update(self):
        self.handle_events()

        return super().inherit_update()


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
        self.on_debug = False

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

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    self.on_debug = not self.on_debug
            if event.type == pg.MOUSEBUTTONDOWN:
                ...
                # self.info_tag.inform("Info System", InfoTagLevels.NOTIFY)

            if event.type == pg.VIDEORESIZE:
                self.scene_manager.resize_current_surface()
                self.scene_manager.update_scene_sizes()

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

        # self.render()
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
