from src.abilities.ability import Ability
from src.display_manager import DisplayManager
from src.enemy_attacks.enemy_attack import EnemyAttack
from src.enemy_attacks.enemy_attack_generator import EnemyAttackGenerator
from src.models.enemy import Enemy


class FightManager:
    def __init__(
            self,
            enemies: list[Enemy],
    ):
        self._enemies = enemies
        self._enemy_attack_generator = EnemyAttackGenerator()
        self._display_manager = DisplayManager(
            enemies=enemies,
        )
        self._hand: list[Ability] = []
        self._start()

    # TODO: design enemy attack choice
    # TODO: design new ability choice
    # TODO: design deck management

    def _start(self):
        # TODO: shuffle draw pile
        enemy_attacks = self._enemy_attack_generator.generate_enemy_attacks()
        self._display_enemy_attack_menu(
            enemy_attacks=enemy_attacks,
        )

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
        # TODO: verify index
        ability = self._hand[hand_index]
        # TODO: play ability
        # TODO: if successful, move to discard pile
        self._display_fight()

    def _display_enemy_attack_menu(
            self,
            enemy_attacks: list[EnemyAttack],
    ):
        self._display_manager.display_enemies()
        self._display_manager.display_enemy_attacks_menu(
            enemy_attacks=enemy_attacks,
        )

    def _display_new_ability_menu(self):
        self._display_manager.display_enemy_attacks()
        self._display_manager.display_enemies()
        self._display_manager.display_new_abilities()

    def _display_fight(self):
        self._display_manager.display_enemy_attacks()
        self._display_manager.display_enemies()
        # TODO: draw abilities
        self._display_manager.display_hand()

