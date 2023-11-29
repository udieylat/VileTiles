from src.enemy_manager.enemy_manager_factory import EnemyManagerFactory
from src.fight_manager.fight_manager import FightManager
from src.game_manager.blood_manager import BloodManager
from src.starter_deck_generator.starter_deck_generator import StarterDeckGenerator


class GameManager:

    def __init__(
            self,
            num_blood: int = 25,
    ):
        self._deck = StarterDeckGenerator.generate_starter_deck()
        self._enemy_manager = EnemyManagerFactory.generate_enemy_manager()  # TODO: should be generated per fight?
        self._blood_manager = BloodManager(
            num_blood=num_blood,
        )

    # TODO: build stations

    def start_fight(self) -> FightManager:
        fight_manager = FightManager(
            deck=self._deck,
            enemy_manager=self._enemy_manager,
            blood_manager=self._blood_manager,
        )
        fight_manager.start_fight()
        return fight_manager
