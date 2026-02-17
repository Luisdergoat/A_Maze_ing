"""
Intro animation for A_MAZE_ING using asciimatics.
"""

from __future__ import annotations

import os
from random import choice, randint
from typing import Any, Dict, List, Optional

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Effect, Print
from asciimatics.renderers import FigletText
from asciimatics.exceptions import StopApplication, ResizeScreenError


def _quit_on_input(event: Optional[object]) -> None:
    if event is not None:
        raise StopApplication("Intro finished")


class ColorStars(Effect):  # type: ignore[misc]
    def __init__(
        self,
        screen: Screen,
        count: int = 180,
        **kwargs: Any,
    ) -> None:
        super().__init__(screen, **kwargs)
        self._count: int = count
        self._stars: List[Dict[str, int]] = []
        self._chars: List[str] = [".", "+", "*"]
        self._colours: List[int] = [
            Screen.COLOUR_WHITE,
            Screen.COLOUR_CYAN,
            Screen.COLOUR_BLUE,
            Screen.COLOUR_MAGENTA,
            Screen.COLOUR_YELLOW,
        ]

    def reset(self) -> None:
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

    def _update(self, frame_no: int) -> None:
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
    def stop_frame(self) -> int:
        return 0


def _intro(screen: Screen) -> None:
    banner = FigletText("A _ MAZE _ ING", font="big")
    terminal_size = os.get_terminal_size()
    star_count = terminal_size.columns + terminal_size.lines
    effects = [
        ColorStars(screen, star_count),
        Print(
            screen,
            banner,
            y=max(0, screen.height // 2 - 4),
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
