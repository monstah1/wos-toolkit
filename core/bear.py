from math import sqrt

from core.constants import (
    BEAR_DAMAGE_CONSTANT,
    MARKSMAN_VS_INFANTRY,
)

from core.combat import attack_factor


def troop_damage(
    troop_count: int,
    base_attack: float,
    attack_bonus: float,
    lethality_bonus: float,
    modifier: float = 1.0,
) -> float:
    """
    Calculates the damage contribution of one troop type.

    D = K × √N × BaseAttack × AttackFactor × Modifier
    """

    A = attack_factor(attack_bonus, lethality_bonus)

    return (
        BEAR_DAMAGE_CONSTANT
        * sqrt(troop_count)
        * base_attack
        * A
        * modifier
    )