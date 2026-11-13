
# ❤️ A Heart in Three Dimensions

*A little heart, beyond two dimensions, made for Val.*

This project is a Python experiment that combines 3D particle generation, mathematical transformations, and perspective projection to create an animated three-dimensional heart.

Using Turtle Graphics, randomly generated particles form a volumetric heart that gradually comes to life through rotation, depth, and a subtle heartbeat effect.

Because love has no dimensions, but this one has three. ♡

---

## 💗 Graphical Representation

### The final result

![3D particle heart](graphical-representation/heart-3d.png)

### 🎬 Animation preview

Watch the heart take shape, rotate, and beat in three dimensions:

[▶ Watch the animation — heart-3d.mp4](graphical-representation/heart-3d.mp4)

---

## ✨ About the project

The program generates a three-dimensional particle system based on a mathematical heart-shaped function.

Unlike a traditional two-dimensional heart, this version introduces depth by distributing particles across a volumetric shape.

Each particle receives individual properties, including its 3D coordinates, appearance timing, and size.

The animation then applies rotational transformations, camera inclination, and perspective projection to create the illusion of a three-dimensional object.

### Features

- ❤️ Three-dimensional heart generation using parametric equations.
- ✨ Volumetric particle system with 1,800 particles.
- 🔄 Continuous rotation around the Y-axis.
- 📐 Perspective projection for realistic depth representation.
- 🌌 3D coordinate transformations and camera inclination.
- 🎨 Dynamic color interpolation based on particle depth.
- 💓 Pulsating heartbeat effect.
- ⚡ Depth sorting using the Painter's Algorithm.
- 💗 A three-dimensional expression of love, made for Val.

---

## 🛠️ Built with

- **Python 3**
- **Turtle Graphics** — Particle rendering and animation.
- **Math** — Trigonometric functions, rotations, and perspective calculations.
- **Random** — Randomized particle generation and distribution.

---

## 📂 Project structure

```text
a-heart-in-three-dimensions/
│
├── main.py
├── README.md
│
└── graphical-representation/
    ├── heart-3d.png
    └── heart-3d.mp4
```

| File | Description |
|---|---|
| `main.py` | Main script responsible for generating and animating the 3D heart. |
| `graphical-representation/heart-3d.png` | Screenshot of the final 3D heart illustration. |
| `graphical-representation/heart-3d.mp4` | Video showing the 3D particle animation. |
| `README.md` | Project documentation. |

---

## 🚀 Getting started

### Requirements

- Python 3.x
- Tkinter support for Python Turtle.

### Installation

Clone the repository:

```bash
git clone https://github.com/laetg404/a-heart-in-three-dimensions.git
```

Navigate to the project directory:

```bash
cd a-heart-in-three-dimensions
```

Run the script:

```bash
python main.py
```

---

## ⚙️ How it works

1. Defines a mathematical function to generate the heart-shaped contour.
2. Generates 1,800 particles distributed throughout a three-dimensional heart volume.
3. Assigns each particle its coordinates, depth, size, and appearance timing.
4. Applies rotational transformations around the Y-axis.
5. Introduces camera inclination using an X-axis rotation.
6. Calculates perspective projection to transform 3D coordinates into 2D screen positions.
7. Sorts particles by depth using the Painter's Algorithm.
8. Renders particles with colors determined by their depth.
9. Applies a pulsating scale transformation to simulate a heartbeat.
10. Updates the animation continuously using Turtle's timer system.

---

## ♡ A little dedication

Some things go beyond what the eyes can see.

They have depth, movement, and countless little pieces that come together to create something beautiful.

This little heart was built in three dimensions, but inspired by something that has no limits.

**My heart, in every dimension, belongs to you, Val. My princess, always. ♡**

---

<sub>Part of a collection of little projects created with love.</sub>

❤️
