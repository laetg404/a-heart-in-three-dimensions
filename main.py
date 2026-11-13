import turtle as t
import math as m
import random as r

SCALE = 100          # tamaño en pantalla
CAM = 5.0            # distancia de la cámara (perspectiva)
THICK = 0.8          # grosor del corazón en 3D
N = 1800             # partículas (bájalo si va lento)
TILT = 0.25          # inclinación fija hacia la cámara (radianes)

s = t.Screen()
s.setup(600, 700)
s.bgcolor("#050002")
s.tracer(0)

p = t.Turtle()
p.hideturtle()
p.penup()


def heart(u):
    x = 1.6 * (m.sin(u) ** 3)
    y = (
        1.3 * m.cos(u)
        - 0.5 * m.cos(2 * u)
        - 0.2 * m.cos(3 * u)
        - 0.1 * m.cos(4 * u)
    )
    return x, y - 0.25


def get_col(f):
    f = max(0.0, min(1.0, f))
    r1, g1, b1 = 60, 0, 10
    r2, g2, b2 = 255, 40, 70
    return (
        f"#{int(r1 + (r2 - r1) * f):02x}"
        f"{int(g1 + (g2 - g1) * f):02x}"
        f"{int(b1 + (b2 - b1) * f):02x}"
    )


# -------------------------
# PARTÍCULAS EN 3D
# -------------------------
# Cada sección del corazón se infla hacia delante y hacia atrás,
# formando un volumen. La mayoría de puntos se concentran en la
# superficie para que se vea sólido.

pts = []

for _ in range(N):
    u = r.uniform(0, 2 * m.pi)
    hx, hy = heart(u)

    rad = r.random() ** 0.4                  # sesgo hacia el borde
    x = hx * rad
    y = hy * rad

    h = THICK * m.sqrt(max(0.0, 1 - rad ** 2))   # altura del "domo"
    if r.random() < 0.8:
        z = r.choice((-1, 1)) * h * r.uniform(0.9, 1.0)   # superficie
    else:
        z = h * r.uniform(-1, 1)                          # interior

    pts.append((x, y, z, r.random(), r.uniform(1.2, 3.2)))

# -------------------------
# ANIMACIÓN
# -------------------------

FORM_END = 1.6
t_val = 0.0
angle = 0.0
frame = 0

cos_t, sin_t = m.cos(TILT), m.sin(TILT)
ZMAX = 1.9


def loop():
    global t_val, angle, frame

    p.clear()
    p.penup()

    progress = min(1.0, t_val)

    # Giro con aceleración suave + latido
    angle += 0.045 * min(1.0, t_val)
    ca, sa = m.cos(angle), m.sin(angle)

    pulse = 1.0
    if t_val > FORM_END:
        pulse = 1 + 0.06 * max(0.0, m.sin(frame * 0.18)) ** 2

    # Proyección: rotar en Y, inclinar en X y aplicar perspectiva
    proj = []
    for x, y, z, appear, size in pts:
        if appear > progress:
            continue

        x *= pulse
        y *= pulse
        z *= pulse

        # rotación sobre el eje Y
        x1 = x * ca + z * sa
        z1 = -x * sa + z * ca

        # inclinación sobre el eje X
        y2 = y * cos_t - z1 * sin_t
        z2 = y * sin_t + z1 * cos_t

        k = CAM / (CAM - z2)                 # perspectiva
        proj.append((z2, x1 * k, y2 * k, k, size))

    # Algoritmo del pintor: primero lo lejano, después lo cercano
    proj.sort(key=lambda a: a[0])

    for z2, px, py, k, size in proj:
        f = (z2 + ZMAX) / (2 * ZMAX)         # cerca = más brillante
        p.goto(px * SCALE, py * SCALE)
        p.color(get_col(f ** 1.2))
        p.dot(size * k)

    t_val += 0.02
    frame += 1

    s.update()
    s.ontimer(loop, 16)


loop()
t.mainloop()