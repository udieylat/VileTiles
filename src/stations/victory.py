import emoji

from src.stations.station import Station


class Victory(Station):

    victory_text = (
        f"{emoji.emojize(':victory_hand_light_skin_tone:')}"
        f" VICTORY! "
        f"{emoji.emojize(':victory_hand_light_skin_tone:')}"
    )

    def __repr__(self) -> str:
        return self.victory_text

    def _start(self) -> None:
        print(self.victory_text)
