#!/usr/bin/env python

from math import sin, cos, pi

def trajectory(velocity, angle):
    """Oblicz czas lotu i zasi�g pocisku.
    
    Dla kuli wystrzelonej z pr�dko�ci� wylotow� 'velocity' podan� w
    metrach na sekund� pod k�tem 'angle' w stponiach wzgl�dem poziomu
    zwraca czas lotu i zasi�g w metrach, pomijaj�c tarcie."""

    # Przyspieszenie grawitacyjne w m/s^2.
    g = 9.8
    # Konwersja 'angle' na radiany.
    angle = angle * pi / 180
    # Obliczenie pionowegoi poziomego komponentu pr�dko�ci.
    v_h = velocity * cos(angle)
    v_v = velocity * sin(angle)
    # Obliczenie czasu lotu i zasi�gu.
    tof = 2 * v_v / g
    range = tof * v_h
    return tof, range
