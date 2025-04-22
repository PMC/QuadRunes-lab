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


def main():
    console = Console(height=33)
    with console.screen(style="bold white on black") as screen:
        # screen.console.print(            "Hello, [bold magenta]World[/bold magenta]!", ":apple:", locals())

        layout = Layout()
        layout.split_column(Layout(name="score_top", size=3), Layout(name="game_area"))
        layout["score_top"].split_row(
            Layout(Panel("Score A: 200"), name="score_a"),
            Layout(Panel(Text("Score B: 15", justify="right")), name="score_b"),
        )

        screen.console.print(layout)
        screen.console.print(layout.tree)
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_column(justify="right")
        grid.add_row(
            "Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:"
        )

        screen.console.print(grid)
        is_rich_great = Confirm.ask("Do you like rich?")


if __name__ == "__main__":
    main()
