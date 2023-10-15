import pygame as pg
import numpy as np


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
    # Here i'll like to convert new_surf with the pg.SRCALPHA flag so black pixels are not rendered
    return new_surf
