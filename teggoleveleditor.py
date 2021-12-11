import teggogame as tg

tg.CAPTION = "Teggo Level Editor 2021"

OUTPUT_FOLDER = "data/game-scenes/"


class Editor:
    def __init__(self):
        pass


def main():
    game = tg.Game()
    game.loop()


if __name__ == "__main__":
    main()
