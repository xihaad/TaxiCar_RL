import numpy as np
import random


class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.95, epsilon=0.1):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_state_key(self, state):
        return tuple(state)

    def choose_action(self, state):
        state_key = self.get_state_key(state)
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.env.actions)
        else:
            q_values = [self.q_table.get((state_key, a), 0)
                        for a in self.env.actions]
            max_q = max(q_values)
            best_actions = [a for a, q in zip(self.env.actions, q_values)
                            if q == max_q]
            return random.choice(best_actions)

    def learn(self, state, action, reward, next_state):
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)

        old_q = self.q_table.get((state_key, action), 0)
        max_next_q = max([self.q_table.get((next_state_key, a), 0)
                          for a in self.env.actions])

        new_q = old_q + self.alpha * (reward + self.gamma * max_next_q - old_q)
        self.q_table[(state_key, action)] = new_q