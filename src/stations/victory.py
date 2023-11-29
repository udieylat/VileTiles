import emoji

from src.stations.station import Station


class Victory(Station):
    def start(self) -> None:
        print(
            f"{emoji.emojize(':victory_hand_light_skin_tone:')}"
            f" VICTORY! "
            f"{emoji.emojize(':victory_hand_light_skin_tone:')}"
        )
