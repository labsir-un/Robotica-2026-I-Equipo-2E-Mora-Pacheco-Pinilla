#!/usr/bin/env python3
"""Actividad 12 — Cinemática Inversa

Recibe (x, y, z, θ) en metros y grados, calcula configuraciones
articulares válidas (codo arriba/abajo) y retorna la más cercana
a la configuración actual.
"""
import math

L0 = 0.089
L1 = 0.101
L2 = 0.101
L3 = 0.119
DEG = math.pi / 180.0

JOINT_NAMES = ['waist', 'shoulder', 'elbow', 'wrist']
JOINT_LIMITS_DEG = {
    'waist':    (-150, 150),
    'shoulder': (-150, 150),
    'elbow':    (-150, 150),
    'wrist':    (-150, 150),
}


def ik(x, y, z, elbow_up=False):
    q1 = math.degrees(math.atan2(y, x))
    r = math.sqrt(x*x + y*y)
    z_eff = L0 + L3 - z
    d_sq = r*r + z_eff*z_eff
    max_reach = L1 + L2
    if d_sq > max_reach * max_reach:
        return None
    d = math.sqrt(d_sq)
    cos_q3 = (d*d - L1*L1 - L2*L2) / (2 * L1 * L2)
    if cos_q3 < -1 or cos_q3 > 1:
        return None
    q3 = math.degrees(math.acos(cos_q3))
    if elbow_up:
        q3 = -q3
    alpha = math.atan2(L2 * math.sin(math.radians(q3)), L1 + L2 * math.cos(math.radians(q3)))
    q2 = math.degrees(math.atan2(z_eff, r) - alpha)
    q4 = -90 - q2 - q3
    result = [q1, q2, q3, q4]

    limits = [JOINT_LIMITS_DEG[j] for j in JOINT_NAMES]
    for i in range(4):
        if result[i] < limits[i][0] or result[i] > limits[i][1]:
            return None
    return result


def nearest_solution(x, y, z, current_q=None):
    sols = []
    for elbow_up in [False, True]:
        q = ik(x, y, z, elbow_up)
        if q is not None:
            sols.append((elbow_up, q))
    if not sols:
        return None, None
    if current_q is None or len(sols) == 1:
        return sols[0]
    best = None
    best_dist = float('inf')
    for elbow_up, q in sols:
        dist = sum((q[i] - current_q[i])**2 for i in range(4))
        if dist < best_dist:
            best_dist = dist
            best = (elbow_up, q)
    return best


def main():
    print()
    print('  ╔══════════════════════════════════════════════════╗')
    print('  ║   Actividad 12 — Cinemática Inversa             ║')
    print('  ╚══════════════════════════════════════════════════╝')
    print()
    print(f'  L₀ = {L0*1000:.0f} mm, L₁ = {L1*1000:.0f} mm, L₂ = {L2*1000:.0f} mm, L₃ = {L3*1000:.0f} mm')
    print()

    TEST_POINTS = [
        {'name': 'Frente centro',     'x': 0.13, 'y': 0.00, 'z': 0.10},
        {'name': 'Frente derecha',    'x': 0.13, 'y': 0.04, 'z': 0.10},
        {'name': 'Frente izquierda',  'x': 0.13, 'y':-0.04, 'z': 0.10},
        {'name': 'Arriba',            'x': 0.13, 'y': 0.00, 'z': 0.14},
        {'name': 'Abajo',             'x': 0.13, 'y': 0.00, 'z': 0.07},
        {'name': 'Esquina lejana',    'x': 0.16, 'y': 0.05, 'z': 0.10},
    ]

    print('  Pruebas con 6 puntos cartesianos:')
    print(f'  {"Punto":20s} {"x(mm)":>7s} {"y(mm)":>7s} {"z(mm)":>7s} {"Codo":>6s} {"q1°":>7s} {"q2°":>7s} {"q3°":>7s} {"q4°":>7s}')
    print(f'  {"-"+("-"*76)}')

    for pt in TEST_POINTS:
        elbow_up, q = nearest_solution(pt['x'], pt['y'], pt['z'], current_q=[0, 0, 0, 0])
        if q:
            elbow_str = 'ARRIBA' if elbow_up else 'ABAJO'
            print(f'  {pt["name"]:20s} {pt["x"]*1000:>7.1f} {pt["y"]*1000:>7.1f} {pt["z"]*1000:>7.1f} '
                  f'{elbow_str:>6s} {q[0]:>7.2f} {q[1]:>7.2f} {q[2]:>7.2f} {q[3]:>7.2f}')
        else:
            print(f'  {pt["name"]:20s} {pt["x"]*1000:>7.1f} {pt["y"]*1000:>7.1f} {pt["z"]*1000:>7.1f} '
                  f'{"—":>6s} [FUERA DE ALCANCE]')

    print()
    print('  Prueba individual: ingresa x(mm) y(mm) z(mm)')
    print('  o presiona Enter para salir.')
    print()
    while True:
        try:
            inp = input('  x y z > ').strip()
            if not inp:
                break
            vals = [float(v) for v in inp.split()]
            if len(vals) < 3:
                print('  Se requieren x y z en mm.')
                continue
            x, y, z = vals[0] / 1000.0, vals[1] / 1000.0, vals[2] / 1000.0
            print()
            print(f'  Buscando soluciones para ({x*1000:.1f}, {y*1000:.1f}, {z*1000:.1f}) mm')
            for elbow_up in [True, False]:
                q = ik(x, y, z, elbow_up)
                label = 'ARRIBA' if elbow_up else 'ABAJO '
                if q:
                    print(f'    Codo {label}: q=[{q[0]:>7.2f}, {q[1]:>7.2f}, {q[2]:>7.2f}, {q[3]:>7.2f}]°')
                else:
                    print(f'    Codo {label}: [FUERA DE ALCANCE O LÍMITES]')
        except (ValueError, EOFError):
            break
    print()
    print('  Hecho.')


if __name__ == '__main__':
    main()
