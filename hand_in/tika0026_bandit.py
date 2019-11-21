# epsilon-greedy example implementation of a multi-armed bandit
import random

# generic epsilon-greedy bandit
class Bandit:
    def __init__(self, arms, epsilon=0.1):
        self.arms = arms
        self.epsilon = epsilon
        self.frequencies, self.sums, self.expected_values = [0] * len(arms)

    def run(self, expected_values):
        if random.random() < self.epsilon:
            return self.arms[random.randint(0, len(self.arms) - 1)]
        return self.arms[expected_values.index(max(expected_values))]

    def give_feedback(self, arm, reward):
        arm_index = self.arms.index
        sum = self.sums[arm_index] + reward
        self.sums[arm_index] = sum
        frequency = self.frequencies[arm_index] + 1
        self.frequencies[arm_index] = frequency
        expected_value = sum / frequency
        self.expected_values[arm_index] = expected_value

# configuration
arms = [
    'Configuration a',
    'Configuration b',
    'Configuration c',
    'Configuration d',
    'Configuration e',
    'Configuration f'
]

# instantiate bandit


