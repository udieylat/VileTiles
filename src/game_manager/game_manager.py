from src.enemy_manager.enemy_manager_factory import EnemyManagerFactory
from src.fight_manager.fight_manager import FightManager
from src.starter_deck_generator.starter_deck_generator import StarterDeckGenerator


class GameManager:

    def __init__(
            self,
            num_blood: int = 25,
    ):
        self._deck = StarterDeckGenerator.generate_starter_deck()
        self._enemy_manager = EnemyManagerFactory.generate_enemy_manager()  # TODO: should be generated per fight?
        self._num_blood = num_blood  # TODO: make manager

    # TODO: build stations

    def start_fight(self) -> FightManager:
        fight_manager = FightManager(
            deck=self._deck,
            enemy_manager=self._enemy_manager,
            num_blood=self._num_blood,
        )
        fight_manager.start_fight()
        return fight_manager
