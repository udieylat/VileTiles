import random

from src.abilities.ability import Ability, AbilityResponse
from src.display_manager import DisplayManager
from src.enemy_manager.enemy_manager import EnemyManager
from src.models.deck import Deck
from src.models.exceptions import InvalidPlay


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
        self._discard_pile: list[Ability] = []
        self._num_shield: int = 0
        self._num_blood: int = num_blood

    def start_fight(self):
        self._shuffle_draw_pile()
        self._draw_abilities()
        self._display_fight()

    def show_draw_pile(self):
        self._display_manager.display_abilities(
            abilities=sorted(self._draw_pile),
        )

    def show_discard_pile(self):
        self._display_manager.display_abilities(
            abilities=sorted(self._discard_pile),
        )

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
        if hand_index <= 0 or hand_index > len(self._hand):
            raise IndexError(f"Hand size: {len(self._hand)}, invalid input index: {hand_index}")
        ability = self._hand[hand_index - 1]
        try:
            ability_response: AbilityResponse = ability.play(
                ability_args=ability_args,
            )
        except InvalidPlay as e:
            print(f"Invalid play: {str(e)}")
            self._display_fight()
            return

        self._handle_ability_response(
            ability_response=ability_response,
        )
        self._hand.remove(ability)
        self._discard_pile.append(ability)
        self._display_fight()

    def _shuffle_draw_pile(self):
        random.shuffle(self._draw_pile)

    def _draw_abilities(self, num_abilities: int = 5):
        for _ in range(num_abilities):
            self._draw_ability()

    def _draw_ability(self):
        try:
            ability = self._draw_pile.pop()
            self._hand.append(ability)
        except IndexError:
            if len(self._discard_pile) == 0:
                return None
            self._draw_pile = self._discard_pile[:]
            self._shuffle_draw_pile()
            self._discard_pile = []
            self._draw_ability()

    def _handle_ability_response(
            self,
            ability_response: AbilityResponse,
    ):
        self._num_shield += ability_response.num_shields

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
