import math
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
    DISPLAY_WIDTH_REMAIN = 3
    DISPLAY_WIDTH_WINDOW = 4
    DISPLAY_WIDTH_PARENT = 5


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
        anim_pos = self.animation_curve(self.tick / self.anim_duration)
        self.value = self.start_value + anim_pos * self.value_diff

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


class MayaaComponent:
    def __init__(self) -> None:
        pass


class MayaaScene:
    def __init__(self) -> None:
        pass


class _MayaaContainer:
    def __init__(self, parent) -> None:
        if isinstance(parent, MayaaScene) or isinstance(parent, _MayaaContainer):
            self.parent = parent
            self.parent.container = self
            self.elements = []
            self.width = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.height = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.width_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
            self.height_flag = MayaaCoreFlag.NOT_DECLARED_ON_INIT
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
            self.color = MayaaDefaultGUI.DEFAULT_CONTAINER_BACKGROUND_COLOR
            self.original_color = self.color.copy()
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

    def set_color_as_parent(self):
        self.color = self.parent.color
        self.original_color = self.color.copy()

    def set_background_color(self, color):
        self.color = color
        self.original_color = self.color.copy()

    def get_absolute_position(self):
        return self.parent.absolute_position + self.position

    def is_container_hovered(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

    def compute_elements_positions(self):
        for element in self.elements:
            element.compute_elements_positions()

    def _compute_elements_surfaces_handle_height_case(self, element):
        if element.width_flag == MayaaRenderFlag.DISPLAY_WIDTH_WINDOW:
            element.width = pg.display.get_window_size()[0]
        if element.width_flag == MayaaRenderFlag.DISPLAY_WIDTH_PARENT:
            element.width = element.parent.width
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
            element.width = element.parent.width - accum_width

    def _compute_elements_surfaces_handle_width_case(self, element):
        if element.height_flag == MayaaRenderFlag.DISPLAY_HEIGHT_WINDOW:
            element.height = pg.display.get_window_size()[0]
        if element.height_flag == MayaaRenderFlag.DISPLAY_HEIGHT_PARENT:
            element.height = element.parent.height
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
            element.height = element.parent.height - accum_height

    def compute_elements_surfaces(self):
        for element in self.elements:
            self._compute_elements_surfaces_handle_height_case(element)
            self._compute_elements_surfaces_handle_width_case(element)
            element.surface = pg.Surface([element.width, element.height])
            if isinstance(element, _MayaaContainer):
                element.compute_elements_surfaces()

    def set_as_core(self):
        self.position = pg.Vector2(0, 0)
        self.absolute_position = pg.Vector2(0, 0)
        self.width = pg.display.get_window_size()[0]
        self.height = pg.display.get_window_size()[1]
        self.surface = pg.Surface([self.width, self.height])
        self.rect = pg.Rect(self.abs_pos, self.surface.get_size())

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

    def __coreupdate__(self):
        self.update()
        for element in self.elements:
            element.__coreupdate__()

    def render(self):
        ...

    def __corerender__(self):
        self.surface.fill(self.color)
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
                        self.surface, border[2], pg.Rect(0, 0, border[1], self.height)
                    )
                if index == 1:
                    pg.draw.rect(
                        self.surface,
                        border[2],
                        pg.Rect(
                            self.width - border[1],
                            0,
                            self.width - border[1],
                            self.height,
                        ),
                    )
                if index == 2:
                    pg.draw.rect(
                        self.surface, border[2], pg.Rect(0, 0, self.width, border[1])
                    )
                if index == 3:
                    pg.draw.rect(
                        self.surface,
                        border[2],
                        pg.Rect(0, self.height - border[1], self.width, border[1]),
                    )


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
            self.set_display_size(
                MayaaDefaultGUI.DEFAULT_APP_HEIGHT, MayaaDefaultGUI.DEFAULT_APP_WIDTH
            )

        if self.clock == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.set_clock(60)
        if self.bacgkround_color == MayaaCoreFlag.NOT_DECLARED_ON_INIT:
            self.bacgkround_color = MayaaDefaultGUI.DEFAULT_APP_BACKGROUND_COLOR

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.info_tag.inform("Info System", InfoTagLevels.NOTIFY)

    def set_background_color(self, color):
        self.bacgkround_color = color

    def update(self):
        ...

    def __coreupdate__(self):
        if self.perform_late_init:
            self.late_init()
            self.perform_late_init = not self.perform_late_init
        self.info_tag.update()

    def render(self):
        ...

    def __corerender__(self):
        self.display.fill(self.bacgkround_color)
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
