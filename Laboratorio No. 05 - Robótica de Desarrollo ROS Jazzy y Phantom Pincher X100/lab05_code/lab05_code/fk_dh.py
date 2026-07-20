#!/usr/bin/env python3
"""Actividad 11 — Cinemática Directa (Denavit–Hartenberg)

Recibe q1..q4 en grados, calcula (x, y, z, roll, pitch, yaw) del TCP
y evalúa las 5 configuraciones de la Actividad 7.
"""
import math
import numpy as np

L0 = 0.089
L1 = 0.101
L2 = 0.101
L3 = 0.119

DEG = math.pi / 180.0

DH_PARAMS = [
    (0,        0,      L0),
    (-math.pi/2, 0,    0),
    (0,        L1,     0),
    (0,        L2,     0),
    (0,        L3,     0),
]


def dh_transform(alpha, a, d, theta):
    ct = math.cos(theta)
    st = math.sin(theta)
    ca = math.cos(alpha)
    sa = math.sin(alpha)
    return np.array([
        [ct, -st, 0, a],
        [st*ca, ct*ca, -sa, -d*sa],
        [st*sa, ct*sa, ca, d*ca],
        [0, 0, 0, 1],
    ])


def fk(q_deg):
    q = [math.radians(v) for v in q_deg[:4]]
    T = np.eye(4)
    for i, (alpha, a, d) in enumerate(DH_PARAMS):
        th = q[i] if i < 4 else 0
        T = T @ dh_transform(alpha, a, d, th)
    x = T[0, 3]
    y = T[1, 3]
    z = T[2, 3]
    R = T[:3, :3]
    roll = math.degrees(math.atan2(R[2, 1], R[2, 2]))
    pitch = math.degrees(math.atan2(-R[2, 0], math.sqrt(R[2, 1]**2 + R[2, 2]**2)))
    yaw = math.degrees(math.atan2(R[1, 0], R[0, 0]))
    return x, y, z, roll, pitch, yaw


ACT7_CONFIGS = [
    {'name': 'Home',       'q': [  0,   0,   0,   0,   0]},
    {'name': 'Config 2',   'q': [ 25,  25,  20, -20,   0]},
    {'name': 'Config 3',   'q': [-35,  35, -30,  30,   0]},
    {'name': 'Config 4',   'q': [ 85, -20,  55,  25,   0]},
    {'name': 'Config 5',   'q': [ 80, -35,  55, -45,   0]},
]


def main():
    print()
    print('  ╔══════════════════════════════════════════════════╗')
    print('  ║   Actividad 11 — Cinemática Directa (DH)        ║')
    print('  ╚══════════════════════════════════════════════════╝')
    print()
    print(f'  Parámetros DH:')
    print(f'    L₀ (base)    = {L0*1000:.0f} mm')
    print(f'    L₁ (brazo)   = {L1*1000:.0f} mm')
    print(f'    L₂ (antebrazo) = {L2*1000:.0f} mm')
    print(f'    L₃ (muñeca)  = {L3*1000:.0f} mm')
    print()
    print(f'  {"Config":15s} {"q1":>7s} {"q2":>7s} {"q3":>7s} {"q4":>7s} {"x(mm)":>8s} {"y(mm)":>8s} {"z(mm)":>8s} {"roll°":>7s} {"pitch°":>7s} {"yaw°":>7s}')
    print(f'  {"-"*98}')

    for cfg in ACT7_CONFIGS:
        q = cfg['q']
        x, y, z, roll, pitch, yaw = fk(q)
        print(f'  {cfg["name"]:15s} {q[0]:>7.1f} {q[1]:>7.1f} {q[2]:>7.1f} {q[3]:>7.1f} '
              f'{x*1000:>8.1f} {y*1000:>8.1f} {z*1000:>8.1f} '
              f'{roll:>7.1f} {pitch:>7.1f} {yaw:>7.1f}')

    print()
    print('  Prueba individual: ingresa q1 q2 q3 q4 en grados (separados por espacio)')
    print('  o presiona Enter para salir.')
    print()
    while True:
        try:
            inp = input('  q1 q2 q3 q4 > ').strip()
            if not inp:
                break
            vals = [float(v) for v in inp.split()]
            if len(vals) != 4:
                print('  Deben ser 4 valores.')
                continue
            x, y, z, roll, pitch, yaw = fk(vals)
            print(f'  → TCP: x={x*1000:.1f} mm, y={y*1000:.1f} mm, z={z*1000:.1f} mm')
            print(f'    Orientación: roll={roll:.1f}°, pitch={pitch:.1f}°, yaw={yaw:.1f}°')
        except (ValueError, EOFError):
            break

    print()
    print('  Hecho.')


if __name__ == '__main__':
    main()
