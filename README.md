# Choppy Orc

Early prototype: a 2D puzzle-platformer built as a precursor to
[Nymphiad](https://github.com/alexbilat/Nymphiad) — most of the lessons
learned here (project structure, avoiding hardcoded level design) carried
directly into that later project.

![Choppy Orc gameplay](Images/demo.gif)

## About

Control an orc with a throwable axe. Open every chest in a level and reach
the end to complete it. Beating the game saves your score and username to
`highscores.txt`.

## Controls

| Action              | Key                  |
|---------------------|-----------------------|
| Move / Jump          | WASD or Arrow keys    |
| Throw / recall axe   | Spacebar               |
| Menus                | Mouse                  |

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## Notes

Levels in this version were hardcoded as rectangles in a single ~1500-line
file — a pain point that directly led to switching to the Tiled level
editor for Nymphiad. This project is preserved as-is as an early milestone
rather than actively developed further.

Credit: graphics and original concept by eddynardo.
