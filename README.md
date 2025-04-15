# Boxxy Roads — Neuroevolution Meets Classic Arcade

<p align="center">
  <img src="readme-images/boxxy-roads-demo.png" alt="Main Menu" width="608">
</p>

**Boxxy Roads** is a modern take on the arcade-style "Crossy Road" genre — built from scratch using Python's Turtle graphics engine and evolved with NEAT (NeuroEvolution of Augmenting Topologies) to train AI agents capable of playing the game autonomously.

## Project Overview

Originally inspired by Day 23 of the 100 Days of Python course, this project began as a simple user-controlled game. Over time, it was transformed into an evolving AI simulation sandbox. While the original course offered a minimal scaffold, all mechanics, graphics, animations, and NEAT-based learning components were built independently.


* ⚡ Dynamic obstacle generation with adaptive spawning

* 🚧 Real-time collision detection and physics-safe obstacle spacing

* 🧬 AI-controlled agents powered by NEAT (genetic algorithm + neural net)

* 🎯 Fitness-driven learning with smart input encoding

* 📈 Progressive difficulty scaling via level-up system

* 💡 Minimalist aesthetic with hand-crafted visual tweaks

## 🧪 NEAT: Making Turtles Smarter

| Parameter          | Value / Rationale                                                                 |
|--------------------|------------------------------------------------------------------------------------|
| **Inputs**         | 2D Vector — Obstacle’s relative X and Y distance from player                      |
| **Output**         | Single value: Should the agent move forward? (`True` = advance, `False` = stay)   |
| **Activation**     | `tanh` — Chosen for its smooth gradient and bounded output between (-1, 1)         |
| **Population**     | 50–100 — Enough diversity for innovation without high evaluation cost             |
| **Fitness**        | Euclidean distance from start to current Y-position                               |
| **Max Generations**| 20 — Prevents stagnation and keeps training time reasonable                        |

### Why `tanh`?

`tanh` is a classic activation function well-suited for binary decision tasks in reinforcement-style environments. It introduces non-linearity, ensures centered output (zero-mean), and naturally encourages exploration early on by producing diverse activation levels across the genome population.

---

## References

1. [Turtle Graphics](https://docs.python.org/3/library/turtle.html) — Used as the primary graphics and animation library to render the game environment and sprites.
2. [NEAT-Python](https://neat-python.readthedocs.io/en/latest/) — The library used to evolve neural networks through genetic algorithms (NeuroEvolution of Augmenting Topologies).
3. [100 Days of Code – Day 23](https://www.udemy.com/course/100-days-of-code/) — The original inspiration for the project.

## Bugs or Issues

If you find a bug or have an issue with Boxxy Roads, feel free to [Submit an Issue](https://github.com/unix2dossss/boxxy-roads/issues/new)


## License

MIT License. Do whatever you want, just don’t train your AI to cross actual roads unsupervised. 🐢🚧