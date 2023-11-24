import emoji
# https://carpedm20.github.io/emoji/

from src.abilities.ability import ChangeAbility
from src.display_manager import DisplayManager
from src.enemy_attacks.enemy_attack import NumberOfXTiles
from src.enemy_generator.enemy_generator import EnemyGenerator
from src.models.colors import Green, Purple

eg = EnemyGenerator()
enemies = [
    eg.generate_random_enemy()
    for _ in range(3)
]

disp = DisplayManager(
    enemies=enemies,
)

ea = NumberOfXTiles(
    color=Green,
)

disp.display_enemy_attacks(
    enemy_attack=ea,
)
disp.display_enemies()

ca = ChangeAbility()
ca.play(
    ability_args={
        "enemy": enemies[0],
        "tile_index": 0,
        "to_color": Purple,
    },
)

disp.display_enemy_attacks(
    enemy_attack=ea,
)
disp.display_enemies()

print()
print('\U0001FA78' * 25)
print('\U0001F6E1 ' * 3)
