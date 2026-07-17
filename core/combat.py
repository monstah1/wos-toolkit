def attack_factor(attack_bonus, lethality_bonus):
    """
    A = (1 + atk/100) * (1 + lethality/100)
    """
    return (1 + attack_bonus / 100) * (1 + lethality_bonus / 100)


def defense_factor(defense_bonus, health_bonus):
    """
    D = (1 + defense/100) * (1 + health/100)
    """
    return (1 + defense_bonus / 100) * (1 + health_bonus / 100)