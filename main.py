from src.taxi_env import TaxiEnv
from src.q_agent import QLearningAgent
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
    env = TaxiEnv()

    while True:
        pickup = input("Enter pickup point (A/B/C/D): ").upper()
        destination = input("Enter destination point (A/B/C/D): ").upper()

        if pickup not in ['A', 'B', 'C', 'D'] or destination not in ['A', 'B', 'C', 'D']:
            print("Invalid input! Use A/B/C/D")
            continue

        state = env.reset(pickup, destination)
        done = False
        total_reward = 0

        print("\nStarting simulation...")
        while not done:
            env.render()
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            state = next_state
            total_reward += reward
            time.sleep(1)

        env.render()
        print(f"Total Reward: {total_reward}")
        print("Mission Completed!\n")


if __name__ == "__main__":
    agent = train_agent()
    test_agent(agent)