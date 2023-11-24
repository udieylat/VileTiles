import emoji
# https://carpedm20.github.io/emoji/

from src.abilities.change_tile import ChangeTile
from src.display_manager import DisplayManager
from src.enemy_attacks.enemy_attack import NumberOfXTiles
from src.enemy_generator.enemy_generator import EnemyGenerator
from src.models.colors import Green, Purple, Orange

eg = EnemyGenerator()
enemies = [
    eg.generate_bullseye_enemy()
    for _ in range(6)
]

disp = DisplayManager(
    enemies=enemies[:3],
)

# ea = NumberOfXTiles(
#     color=Green,
# )

# disp.display_enemy_attacks(
#     enemy_attack=ea,
# )
disp.display_enemies()

disp2 = DisplayManager(
    enemies=enemies[3:],
)
print()
print()
disp2.display_enemies()
ct = ChangeTile(
    from_color=Green,
    to_color=Orange,
)
# ct.play(
#     ability_args={
#         "enemy": enemies[0],
#         "tile_index": 0,
#     },
# )
#
# disp.display_enemy_attacks(
#     enemy_attack=ea,
# )
# disp.display_enemies()

print()
print(ct)
print()
print(emoji.emojize(":drop_of_blood:") * 25)
print((emoji.emojize(":shield:") + ' ') * 3)
