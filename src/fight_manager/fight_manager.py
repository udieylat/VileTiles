from src.display_manager import DisplayManager
from src.models.enemy import Enemy


class FightManager:
    def __init__(
            self,
            enemies: list[Enemy],
    ):
        self._enemies = enemies
        self._display_manager = DisplayManager(
            enemies=enemies,
        )
        self.start()

    # TODO: design enemy attack choice
    # TODO: design new ability choice
    # TODO: design deck management

    def start(self):
        # TODO: shuffle draw pile
        self._display_enemy_attack_menu()

    def choose_enemy_attack(self, index: int):
        # TODO: validate flow
        # TODO: choose something
        self._display_new_ability_menu()

    def choose_new_ability(self, index: int):
        # TODO: validate flow
        # TODO: choose something
        # TODO: update deck
        self._display_fight()

    def play_ability(
            self,
            hand_index: int,
            ability_args: dict,
    ):
        # TODO
        self._display_fight()

    def _display_enemy_attack_menu(self):
        self._display_manager.display_enemies()
        self._display_manager.display_enemy_attack_menu()

    def _display_new_ability_menu(self):
        self._display_manager.display_enemy_attacks()
        self._display_manager.display_enemies()
        self._display_manager.display_new_abilities()

    def _display_fight(self):
        self._display_manager.display_enemy_attacks()
        self._display_manager.display_enemies()
        # TODO: draw abilities
        self._display_manager.display_hand()

