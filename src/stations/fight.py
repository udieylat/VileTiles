import random
import emoji

from src.abilities.ability import Ability, AbilityResponse
from src.display_manager import DisplayManager
from src.enemy_generator.pattern_generator import PatternGenerator
from src.enemy_manager.enemy_manager import EnemyManager
from src.game_manager.blood_manager import BloodManager
from src.models.colors import PATTERN_COLORS
from src.models.deck import Deck
from src.models.exceptions import InvalidPlay
from src.models.pattern import Pattern
from src.stations.station import Station


class Fight(Station):
    def __init__(
            self,
            deck: Deck,
            enemy_manager: EnemyManager,
            blood_manager: BloodManager,
    ):
        super().__init__()
        self._deck = deck
        self._enemy_manager = enemy_manager
        self._blood_manager = blood_manager
        self._display_manager = DisplayManager(
            enemy_manager=enemy_manager,
        )
        self._draw_pile: list[Ability] = deck.abilities[:]
        self._hand: list[Ability] = []
        self._discard_pile: list[Ability] = []
        self._num_shield: int = 0

        self._patterns = self._generate_fight_patterns()

    def __repr__(self) -> str:
        self._display_fight()
        return ""

    def _start(self):
        self._shuffle_draw_pile()
        self._draw_abilities()
        self._trigger_elimination_conditions()
        self._display_fight()

    def show_draw_pile(self):
        self._display_manager.display_abilities(
            abilities=self._draw_pile,  # TODO: hide order
        )

    def show_discard_pile(self):
        self._display_manager.display_abilities(
            abilities=self._discard_pile,
        )

    def show_deck(self):
        self._display_manager.display_abilities(
            abilities=self._deck.abilities,
        )

    def play_ability(
            self,
            hand_index: int,
            **kwargs: dict,
    ):
        if hand_index <= 0 or hand_index > len(self._hand):
            raise IndexError(f"Hand size: {len(self._hand)}, invalid input index: {hand_index}")
        ability = self._hand[hand_index - 1]
        if "enemy_index" in kwargs:
            enemy_index = kwargs["enemy_index"]
            kwargs["enemy"] = self._enemy_manager.enemies[enemy_index]
        try:
            ability_response: AbilityResponse = ability.play(
                ability_args=kwargs,
            )
        except InvalidPlay as e:
            print(f"Invalid play: {str(e)}")
            self._display_fight()
            return

        self._handle_ability_response(
            ability_response=ability_response,
        )
        self._trigger_elimination_conditions()
        if not self.is_active:
            return
        self._hand.remove(ability)
        self._discard_pile.append(ability)
        self._display_fight()

    def end_turn(self):
        if not self.is_active:
            return
        total_attack_for = self._enemy_manager.total_attack_for()
        if total_attack_for <= self._num_shield:
            self._num_shield -= total_attack_for
        else:
            self._blood_manager.set_num_blood(
                num_blood=self._blood_manager.num_blood + self._num_shield - total_attack_for,
            )

        self._num_shield = 0
        self._discard_hand()
        if self._blood_manager.is_dead():
            self._game_over()
            return
        self._draw_abilities()
        self._display_fight()

    @classmethod
    def _generate_fight_patterns(
            cls,
            num_patterns: int = 1,
    ) -> list[Pattern]:
        pattern_generator = PatternGenerator(
            colors_pull=PATTERN_COLORS,
        )
        pattern_strings = [
            "000111222",
            "010121010",
            "012121210",
            "012111210",
            "010010222",
            "001001220",
        ]
        return [
            pattern_generator.generate_pattern_from_str(
                pattern_str=pattern_str,
            )
            for pattern_str in random.sample(pattern_strings, num_patterns)
        ]

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

    def _trigger_elimination_conditions(self):
        self._enemy_manager.trigger_elimination_conditions()
        if self._enemy_manager.all_enemies_are_disabled():
            self.complete()

    def _discard_hand(self):
        self._discard_pile += self._hand[:]
        self._hand = []

    def _display_fight(self):
        self._display_manager.display_fight(
            hand=self._hand,
            patterns=self._patterns,
            num_shield=self._num_shield,
            num_blood=self._blood_manager.num_blood,
        )

    def _game_over(self):
        print()
        print(
            f"{emoji.emojize(':face_with_crossed-out_eyes:')}"
            f" GAME OVER "
            f"{emoji.emojize(':face_with_crossed-out_eyes:')}"
        )
        print()
        self._display_fight()
