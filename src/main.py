from rich import print
from rich.console import Console, ConsoleOptions, Measurement
from rich.panel import Panel
from rich.text import Text
import sys
from rich.layout import Layout
from rich.table import Table
from time import sleep
from rich.align import Align
from rich.prompt import Confirm
from rich.live import Live
import random


def generate_game_map() -> Layout:
    """Make a new game area."""
    global score_a
    layout = Layout()
    layout.split_column(
        Layout(name="score_top", size=3), Layout(name="game_area", size=35)
    )
    value = random.random() * 100
    score_a += value
    layout["score_top"].split_row(
        Layout(Panel(f"Score A: {score_a}"), name="score_a"),
        Layout(Panel(Text("Score B: 15", justify="right")), name="score_b"),
    )
    return layout


def main():
    with Live(
        generate_game_map(), refresh_per_second=1, transient=True, screen=True
    ) as live:
        for _ in range(40):
            sleep(0.4)
            live.update(generate_game_map())


if __name__ == "__main__":
    score_a = 0
    main()
