import emoji
# https://carpedm20.github.io/emoji/

from src.abilities.change_tile import ChangeTile
from src.display_manager import DisplayManager
from src.enemy_attacks.enemy_attack_generator import EnemyAttackGenerator
from src.enemy_attacks.numer_of_x_tiles import NumberOfXTiles
from src.enemy_generator.enemy_generator import EnemyGenerator
from src.enemy_manager.enemy_manager import EnemyManager
from src.enemy_manager.enemy_manager_factory import EnemyManagerFactory
from src.models.colors import Green, Purple, Orange


enemy_generator = EnemyGenerator()
enemy_attack_generator = EnemyAttackGenerator()
enemy_manager: EnemyManager = EnemyManagerFactory.generate_enemy_manager(
    enemy_generator=enemy_generator,
    enemy_attack_generator=enemy_attack_generator,
)

disp = DisplayManager(
    enemy_manager=enemy_manager,
)

# ea = NumberOfXTiles(
#     color=Green,
# )
#
# disp.display_enemy_attacks(
#     enemy_attack=ea,
# )
disp.display_enemies_and_attacks()

# eag = EnemyAttackGenerator()
# enemy_attack_choices = eag.generate_enemy_attacks()
# disp.display_enemy_attacks_menu(
#     enemy_attacks=enemy_attack_choices,
# )

# ct = ChangeTile(
#     from_color=Green,
#     to_color=Orange,
# )

print()
print((emoji.emojize(":shield:") + ' ') * 3)
print(emoji.emojize(":drop_of_blood:") * 25)
