def solution(bandage, health, attacks):
    max_health = health
    max_time = attacks[-1][0]

    attack_dict = {attack[0]: attack[1] for attack in attacks}

    time = 0
    continuous_success = 0

    while time <= max_time:
        if time in attack_dict:
            health -= attack_dict[time]
            continuous_success = 0

            if health <= 0:
                return -1
        else:
            continuous_success += 1
            if continuous_success < bandage[0]:
                health += bandage[1]
                health = min(health, max_health)
            else:
                health += bandage[1] + bandage[2]
                health = min(health, max_health)
                continuous_success = 0

        time += 1

    return health
