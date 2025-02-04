# from src.taxi_env import TaxiEnv
# from src.q_agent import QLearningAgent
# from src.taxi_gui import TaxiGUI
# import pygame
# import time
#
#
# def train_agent(episodes=10000):
#     env = TaxiEnv()
#     agent = QLearningAgent(env, epsilon=0.2)
#
#     print("Training agent...")
#     for episode in range(episodes):
#         state = env.reset()
#         total_reward = 0
#         done = False
#
#         while not done:
#             action = agent.choose_action(state)
#             next_state, reward, done = env.step(action)
#             agent.learn(state, action, reward, next_state)
#             state = next_state
#             total_reward += reward
#
#         if (episode + 1) % 1000 == 0:
#             print(f"Episode {episode + 1}, Total Reward: {total_reward}")
#
#     return agent
#
#
#
#
#
# def test_agent(agent):
#     env = TaxiEnv()
#     gui = TaxiGUI(env)
#
#     while True:
#         pickup = input("Enter pickup point (A/B/C/D): ").upper()
#         destination = input("Enter destination point (A/B/C/D): ").upper()
#
#         if pickup not in ['A', 'B', 'C', 'D'] or destination not in ['A', 'B', 'C', 'D']:
#             print("Invalid input! Use A/B/C/D")
#             continue
#
#         state = env.reset(pickup, destination)
#         done = False
#         total_reward = 0
#
#         clock = pygame.time.Clock()
#         running = True
#
#         while not done and running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                     break
#
#             action = agent.choose_action(state)
#             next_state, reward, done = env.step(action)
#             total_reward += reward
#
#             gui.render(reward, total_reward)
#             time.sleep(0.5)  # Update every 0.5 seconds
#
#             state = next_state
#             clock.tick(30)  # Limit to 30 FPS
#
#         gui.close()
#         print(f"Total Reward: {total_reward}")
#         print("Mission Completed!\n")
#         if not running:
#             break
#
#
# if __name__ == "__main__":
#     agent = train_agent()
#     for i in range(5):
#         test_agent(agent)
#
#

from src.taxi_env import TaxiEnv
from src.q_agent import QLearningAgent
from src.taxi_gui import TaxiGUI
import pygame
import time


def train_agent(episodes=10000):
    env = TaxiEnv()
    agent = QLearningAgent(env, epsilon=0.2)

    print("Training agent...")
    for episode in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        if (episode + 1) % 1000 == 0:
            print(f"Episode {episode + 1}, Total Reward: {total_reward}")

    return agent


def test_agent(agent):
    pygame.init() #Initialize Pygame once
    env = TaxiEnv()
    gui = TaxiGUI(env)

    try:
        while True:
            pickup = input("Enter pickup point (A/B/C/D) or 'q' to quit: ").upper()
            if pickup == 'Q':
                break

            destination = input("Enter destination point (A/B/C/D): ").upper()

            if pickup not in ['A', 'B', 'C', 'D'] or destination not in ['A', 'B', 'C', 'D']:
                print("Invalid input! Use A/B/C/D")
                continue

            state = env.reset(pickup, destination)
            done = False
            total_reward = 0
            clock = pygame.time.Clock()

            while not done:
                # Handle Pygame events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                action = agent.choose_action(state)
                next_state, reward, done = env.step(action)
                total_reward += reward

                gui.render(reward, total_reward)
                time.sleep(0.5)
                state = next_state
                clock.tick(30)

            print(f"Total Reward: {total_reward}")
            print("Mission Completed!\n")

    finally:
        pygame.quit()


if __name__ == "__main__":
    agent = train_agent()
    test_agent(agent)