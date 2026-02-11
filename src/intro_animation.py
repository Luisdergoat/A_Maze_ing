"""
Intro animation for A_MAZE_ING using asciimatics.
"""

from random import choice, randint

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Effect, Print, Matrix
from asciimatics.renderers import FigletText, StaticRenderer
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


class BlinkText(Effect):
    def __init__(
        self,
        screen: Screen,
        renderer,
        y: int,
        colour: int = Screen.COLOUR_WHITE,
        rate: int = 12,
        **kwargs,
    ):
        super().__init__(screen, **kwargs)
        self._renderer = renderer
        self._y = y
        self._colour = colour
        self._rate = rate

    def reset(self):
        pass

    def _update(self, frame_no):
        if (frame_no // self._rate) % 2 == 0:
            y = self._y
            image, _ = self._renderer.rendered_text
            for line in image:
                if self._screen.is_visible(0, y):
                    self._screen.centre(line, y, self._colour)
                y += 1

    @property
    def stop_frame(self):
        return 0


def _intro(screen: Screen) -> None:
    banner = FigletText("A _ MAZE _ ING", font="big")
    prompt = StaticRenderer([""])
    effects = [
        ColorStars(screen, 200),
        Print(
            screen,
            banner,
            y=max(0, screen.height // 2 - 4),
            colour=Screen.COLOUR_WHITE,
            transparent=True,
        ),
        BlinkText(
            screen,
            prompt,
            y=max(0, screen.height - 2),
            colour=Screen.COLOUR_WHITE,
            rate=12,
        ),
    ]
    screen.play(
        [Scene(effects, -1, clear=True)],
        stop_on_resize=True,
        unhandled_input=_quit_on_input,
    )


def _hacker(screen: Screen) -> None:
    title = StaticRenderer([""])
    prompt = StaticRenderer([""])
    effects = [
        Matrix(screen),
        Print(
            screen,
            title,
            y=max(0, screen.height // 2 - 1),
            colour=Screen.COLOUR_GREEN,
            transparent=True,
        ),
        BlinkText(
            screen,
            prompt,
            y=max(0, screen.height - 2),
            colour=Screen.COLOUR_WHITE,
            rate=12,
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


def play_hacker_screen() -> None:
    while True:
        try:
            Screen.wrapper(_hacker)
            break
        except ResizeScreenError:
            continue
        except StopApplication:
            break


if __name__ == "__main__":
    play_intro()
