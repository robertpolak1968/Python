#!/usr/bin/env python

from math import sin, cos, pi

def trajectory(velocity, angle):
    """Oblicz czas lotu i zasiêg pocisku.
    
    Dla kuli wystrzelonej z prêdko¶ci± wylotow± 'velocity' podan± w
    metrach na sekundê pod k±tem 'angle' w stponiach wzglêdem poziomu
    zwraca czas lotu i zasiêg w metrach, pomijaj±c tarcie."""

    # Przyspieszenie grawitacyjne w m/s^2.
    g = 9.8
    # Konwersja 'angle' na radiany.
    angle = angle * pi / 180
    # Obliczenie pionowegoi poziomego komponentu prêdko¶ci.
    v_h = velocity * cos(angle)
    v_v = velocity * sin(angle)
    # Obliczenie czasu lotu i zasiêgu.
    tof = 2 * v_v / g
    range = tof * v_h
    return tof, range
