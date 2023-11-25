from src.enemy_attacks.enemy_attack_generator import EnemyAttackGenerator
from src.enemy_generator.enemy_generator import EnemyGenerator
from src.enemy_manager.enemy_manager import EnemyManager


class EnemyManagerFactory:

    @classmethod
    def generate_enemy_manager(
            cls,
            enemy_generator: EnemyGenerator,
            enemy_attack_generator: EnemyAttackGenerator,
            num_enemies: int = 3,
            num_enemy_attacks: int = 1,
    ) -> EnemyManager:
        enemies = enemy_generator.generate_random_enemies(
            num_enemies=num_enemies,
        )
        enemy_attacks = enemy_attack_generator.generate_enemy_attacks(
            num_enemy_attacks=num_enemy_attacks,
        )
        return EnemyManager(
            enemies=enemies,
            enemy_attacks=enemy_attacks,
        )
