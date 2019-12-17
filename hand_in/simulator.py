from random import random, shuffle
from random import gauss

def generate_reward(arm_index, expected_rewards_approx):
    return gauss(expected_rewards_approx[arm_index], 0.5) + random() / 2

def simulate(bandit):
    acc_rewards = [0 for _ in range(6)]
    expected_rewards_approx = [
        1 + (random() / 2) for _ in range(4)
    ]
    expected_rewards_approx.append(-5)
    expected_rewards_approx.append(-10)
    shuffle(expected_rewards_approx)
    for _ in range(10000):
        for arm_index in range(6):
            acc_rewards[arm_index] = acc_rewards[arm_index] + generate_reward(arm_index, expected_rewards_approx)

    print('Reward comparison of the different arms:')
    print([r / 10000 for r in acc_rewards])

    for _ in range(1000):
        arm = bandit.run()
        reward = generate_reward(bandit.arms.index(arm), expected_rewards_approx)
        bandit.give_feedback(arm, reward)
    print('Frequencies')
    print(bandit.frequencies)
    return sum(bandit.sums)
