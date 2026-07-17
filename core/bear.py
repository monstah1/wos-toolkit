from math import sqrt

from core.constants import (
    BEAR_DAMAGE_CONSTANT,
    MARKSMAN_BEAR_MODIFIER,
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

    A = attack_factor(
        attack_bonus,
        lethality_bonus
    )

    return (
        BEAR_DAMAGE_CONSTANT
        * sqrt(troop_count)
        * base_attack
        * A
        * modifier
    )


def bear_troop_damage(
    troop_type: str,
    troop_count: int,
    base_attack: float,
    attack_bonus: float,
    lethality_bonus: float,
) -> float:
    """
    Calculates Bear damage for a troop type.
    Applies Bear-specific modifiers.
    """

    modifier = 1.0

    if troop_type == "Marksman":
        modifier = MARKSMAN_BEAR_MODIFIER

    return troop_damage(
        troop_count,
        base_attack,
        attack_bonus,
        lethality_bonus,
        modifier,
    )