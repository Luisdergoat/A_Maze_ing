"""
Intro animation for A_MAZE_ING using asciimatics.
"""

import os

from random import choice, randint

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Effect, Print
from asciimatics.renderers import FigletText
from asciimatics.exceptions import ResizeScreenError, StopApplication


def _quit_on_input(event):
    if event is not None:
        raise StopApplication("Intro finished")


class ColorStars(Effect):
    def __init__(self, screen: Screen, count: int = 180, **kwargs):
        super().__init__(screen, **kwargs)
        self._count = count
        self._stars = []
        self._chars = [".", "+", "*"]
        self._colours = [
            Screen.COLOUR_WHITE,
            Screen.COLOUR_CYAN,
            Screen.COLOUR_BLUE,
            Screen.COLOUR_MAGENTA,
            Screen.COLOUR_YELLOW,
        ]

    def reset(self):
        self._stars = []
        for _ in range(self._count):
            self._stars.append(
                {
                    "x": randint(0, self._screen.width - 1),
                    "y": randint(0, self._screen.height - 1),
                    "cycle": randint(0, len(self._chars) - 1),
                    "rate": randint(4, 12),
                    "colour": choice(self._colours),
                }
            )

    def _update(self, frame_no):
        for star in self._stars:
            if frame_no % star["rate"] == 0:
                star["cycle"] = (star["cycle"] + 1) % len(self._chars)
                if randint(0, 3) == 0:
                    star["colour"] = choice(self._colours)
            if self._screen.is_visible(star["x"], star["y"]):
                self._screen.print_at(
                    self._chars[star["cycle"]],
                    star["x"],
                    star["y"],
                    star["colour"],
                )

    @property
    def stop_frame(self):
        return 0


def _intro(screen: Screen) -> None:
    banner = FigletText("A _ MAZE _ ING", font="big")
    stars = os.get_terminal_size()
    stars = stars.columns + stars.lines
    effects = [
        ColorStars(screen, stars),
        Print(
            screen,
            banner,
            y=max(0, screen.height - int((screen.height / 0.5))),
            colour=Screen.COLOUR_WHITE,
            transparent=True,
        ),
    ]
    screen.play(
        [Scene(effects, -1, clear=True)],
        stop_on_resize=True,
        unhandled_input=_quit_on_input,
    )


def play_intro() -> None:
    while True:
        try:
            Screen.wrapper(_intro)
            break
        except ResizeScreenError:
            continue
        except StopApplication:
            break


if __name__ == "__main__":
    play_intro()
