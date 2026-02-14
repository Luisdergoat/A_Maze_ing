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
from asciimatics.renderers import FigletText, StaticRenderer
from asciimatics.exceptions import StopApplication, ResizeScreenError
from asciimatics.event import KeyboardEvent


class ColorStars(Effect):
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



class ExitOnKey(Effect):
    def __init__(self, screen):
        super().__init__(screen)
        self.key = None

    def _update(self, frame_no):
        pass

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code in (ord('1'), ord('2'), ord('3'), ord('4'), ord('5')):
                self.key = event.key_code
                raise StopApplication("key pressed")
        return event

    @property
    def stop_frame(self):
        return 0

    def reset(self):
        pass


def _options(screen: Screen) -> int | None:
    banner = FigletText("A _ MAZE _ ING", font="big")
    terminal_size = os.get_terminal_size()
    generate_maze = "1: Generate Maze"
    edit_config = "2: Edit config"
    change_colour = "3: Change colours"
    normal_exit = "4: Exit without cleanup"
    clean_exit = "5: Exit with cleanup"
    star_count = terminal_size.columns + terminal_size.lines
    exit_effect = ExitOnKey(screen)
    options = [
            generate_maze,
            edit_config,
            change_colour,
            normal_exit,
            clean_exit,
            ]
    effects = [
        ColorStars(screen, star_count),
        Print(
            screen,
            banner,
            y=max(0, screen.height // 15),
            colour=Screen.COLOUR_WHITE,
            transparent=True,
        ),
        exit_effect,
    ]

    height = screen.height // 2
    space = height // (height // 2)
    height = height - space - space
    for option in options:
        effects.append(
            Print(
                screen,
                StaticRenderer([option]),
                y=int(height),
                colour=Screen.COLOUR_WHITE,
                transparent=True,
                ),
            )
        height = height + space

    try:
        screen.play(
            [Scene(effects, 0, clear=True)],
            stop_on_resize=True,
        )
    except StopApplication:
        pass
    return exit_effect.key
    

def play_option_menu() -> None:
    while True:
        try:
            return Screen.wrapper(_options)
        except ResizeScreenError:
            continue
        except StopApplication:
            break


if __name__ == "__main__":
    play_option_menu()
