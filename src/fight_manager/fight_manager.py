import random

from src.abilities.ability import Ability
from src.display_manager import DisplayManager
from src.enemy_manager.enemy_manager import EnemyManager
from src.models.deck import Deck


class FightManager:
    def __init__(
            self,
            deck: Deck,
            enemy_manager: EnemyManager,
            num_blood: int,
    ):
        self._enemy_manager = enemy_manager
        self._display_manager = DisplayManager(
            enemy_manager=enemy_manager,
        )
        self._draw_pile: list[Ability] = deck.abilities[:]
        self._hand: list[Ability] = []
        self._num_shield: int = 0
        self._num_blood: int = num_blood

    def start_fight(self):
        self._shuffle_draw_pile()
        self._draw_abilities()
        self._display_fight()

    # def choose_enemy_attack(self, index: int):
    #     # TODO: validate flow
    #     # TODO: choose something
    #     self._display_new_ability_menu()

    # def choose_new_ability(self, index: int):
    #     # TODO: validate flow
    #     # TODO: choose something
    #     # TODO: update deck
    #     self._display_fight()

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

    def _shuffle_draw_pile(self):
        random.shuffle(self._draw_pile)

    def _draw_abilities(self, num_abilities: int = 5):
        for _ in range(num_abilities):
            ability = self._draw_ability()
            self._hand.append(ability)

    def _draw_ability(self) -> Ability:
        try:
            return self._draw_pile.pop()
        except IndexError:
            raise  # TODO: shuffle discard pile

    # def _display_enemy_attack_menu(self):
    #     self._display_manager.display_enemies()
    #     self._display_manager.display_enemy_attacks_menu()

    # def _display_new_ability_menu(self):
    #     self._display_manager.display_enemies_and_attacks()
    #     self._display_manager.display_new_abilities()

    def _display_fight(self):
        self._display_manager.display_fight(
            hand=self._hand,
            num_shield=self._num_shield,
            num_blood=self._num_blood,
        )
