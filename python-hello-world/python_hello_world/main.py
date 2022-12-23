import typer
from rich import print


def main():
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")
    return 0


if __name__ == "__main__":
    typer.run(main)
