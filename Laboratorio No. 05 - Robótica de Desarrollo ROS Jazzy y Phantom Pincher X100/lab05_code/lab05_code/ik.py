#!/usr/bin/env python3
"""Actividad 12 — Cinemática Inversa
Recibe (x, y, z) en metros, calcula configuraciones articulares.
"""
import math

L0 = 0.089
L1 = 0.101
L2 = 0.101
L3 = 0.119
DEG = math.pi / 180.0
MAX_ARM = L1 + L2
MAX_REACH = L1 + L2 + L3
SHOULDER_Z = L0

JOINT_LIMITS_DEG = {
    'waist':    (-150, 150),
    'shoulder': (-120, 120),
    'elbow':    (-139, 139),
    'wrist':    (-98, 103),
}


def ik(x, y, z, elbow_up=False):
    """Solve IK for TCP (x,y,z). Returns [q1,q2,q3,q4]° or None."""
    q1 = math.degrees(math.atan2(y, x))
    r = math.sqrt(x*x + y*y)
    z_rel = z - SHOULDER_Z
    d_tcp = math.sqrt(r*r + z_rel*z_rel)
    if d_tcp > MAX_REACH + 0.002 or d_tcp < 0.001:
        return None

    # Buscar punto de muñeca resolviendo intersección de círculos:
    #   muñeca a distancia ≤ MAX_ARM del hombro
    #   muñeca a distancia = L3 del TCP
    # Parametrizamos la dirección del segmento muñeca→TCP con ángulo phi
    # muñeca = TCP - L3 * (cos(phi), sin(phi))
    best = None
    best_dist = float('inf')
    for phi_deg in range(-180, 181, 5):
        phi = math.radians(phi_deg)
        r_wrist = r - L3 * math.cos(phi)
        z_wrist_rel = z_rel - L3 * math.sin(phi)
        d_wrist = math.sqrt(r_wrist*r_wrist + z_wrist_rel*z_wrist_rel)
        if d_wrist > MAX_ARM + 0.001:
            continue
        d = max(0.0001, d_wrist)
        cos_q3 = max(-1.0, min(1.0, (d*d - L1*L1 - L2*L2) / (2*L1*L2)))
        q3r = math.acos(cos_q3)
        q3_val = -math.degrees(q3r) if elbow_up else math.degrees(q3r)
        alpha = math.atan2(L2 * math.sin(math.radians(q3_val)),
                           L1 + L2 * math.cos(math.radians(q3_val)))
        q2 = math.degrees(math.atan2(z_wrist_rel, r_wrist) - alpha)
        q4 = -90 - q2 - q3_val
        q = [q1, q2, q3_val, q4]
        limits = [(JOINT_LIMITS_DEG[j]) for j in ['waist','shoulder','elbow','wrist']]
        if any(q[i] < limits[i][0] or q[i] > limits[i][1] for i in range(4)):
            continue
        dist = abs(phi_deg)
        if dist < best_dist:
            best_dist = dist
            best = q
    return best


def nearest_solution(x, y, z, current_q=None):
    sols = []
    q1 = math.degrees(math.atan2(y, x))
    r = math.sqrt(x*x + y*y)
    z_rel = z - SHOULDER_Z
    d_tcp = math.sqrt(r*r + z_rel*z_rel)
    if d_tcp > MAX_REACH + 0.002 or d_tcp < 0.001:
        return None, None

    for phi_deg in range(-180, 181, 5):
        phi = math.radians(phi_deg)
        r_wrist = r - L3 * math.cos(phi)
        z_wrist_rel = z_rel - L3 * math.sin(phi)
        d_wrist = math.sqrt(r_wrist*r_wrist + z_wrist_rel*z_wrist_rel)
        if d_wrist > MAX_ARM + 0.001:
            continue
        d = max(0.0001, d_wrist)
        cos_q3 = max(-1.0, min(1.0, (d*d - L1*L1 - L2*L2) / (2*L1*L2)))
        for sign in [1, -1]:
            q3_val = sign * math.degrees(math.acos(cos_q3))
            alpha = math.atan2(L2 * math.sin(math.radians(q3_val)),
                               L1 + L2 * math.cos(math.radians(q3_val)))
            q2_val = math.degrees(math.atan2(z_wrist_rel, r_wrist) - alpha)
            q4_val = -90 - q2_val - q3_val
            q = [q1, q2_val, q3_val, q4_val]
            limits = [(JOINT_LIMITS_DEG[j]) for j in ['waist','shoulder','elbow','wrist']]
            if all(limits[i][0] <= q[i] <= limits[i][1] for i in range(4)):
                sols.append((sign > 0, q))
    if not sols:
        return None, None
    if current_q is None or len(sols) == 1:
        return sols[0]
    best, best_dist = None, float('inf')
    for eu, q in sols:
        dist = sum((q[i] - current_q[i])**2 for i in range(4))
        if dist < best_dist:
            best_dist = dist
            best = (eu, q)
    return best


def main():
    print()
    print('  Actividad 12 — Cinemática Inversa')
    print(f'  L0={L0*1000:.0f} L1={L1*1000:.0f} L2={L2*1000:.0f} L3={L3*1000:.0f} mm')
    print(f'  Espacio trabajo: {MAX_REACH*1000:.0f} mm max')
    print()
    tests = [
        ('Home FK',        0.321, 0.00, 0.089),
        ('Frente centro',  0.130, 0.00, 0.100),
        ('Frente derecha', 0.130, 0.04, 0.100),
        ('Arriba',         0.100, 0.00, 0.180),
        ('Abajo',          0.100, 0.00, 0.050),
        ('Cerca base',     0.080, 0.00, 0.050),
    ]
    print(f'  {"Punto":20s} {"x":>6s} {"y":>6s} {"z":>6s} {"Codo":>6s} {"q1°":>7s} {"q2°":>7s} {"q3°":>7s} {"q4°":>7s}')
    for name, x, y, z in tests:
        eu, q = nearest_solution(x, y, z, current_q=[0,0,0,0])
        if q:
            print(f'  {name:20s} {x*1000:>6.0f} {y*1000:>6.0f} {z*1000:>6.0f} {"ARRIBA" if eu else "ABAJO":>6s} {q[0]:>7.2f} {q[1]:>7.2f} {q[2]:>7.2f} {q[3]:>7.2f}')
        else:
            print(f'  {name:20s} {x*1000:>6.0f} {y*1000:>6.0f} {z*1000:>6.0f}  NO ALCANZABLE')
    print()
    print('  Manual: x(mm) y(mm) z(mm) o Enter para salir.')
    while True:
        try:
            inp = input('  > ').strip()
            if not inp: break
            x,y,z = [float(v)/1000.0 for v in inp.split()[:3]]
            eu, q = nearest_solution(x, y, z, [0,0,0,0])
            if q:
                print(f'    Codo {"ARRIBA" if eu else "ABAJO"}: q=[{q[0]:.2f}, {q[1]:.2f}, {q[2]:.2f}, {q[3]:.2f}]°')
            else:
                print('    NO ALCANZABLE')
        except: break
    print('  Hecho.')

if __name__ == '__main__':
    main()
