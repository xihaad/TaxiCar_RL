from src.taxi_env import TaxiEnv
from src.q_agent import QLearningAgent


def train_agent(episodes=1000):
    env = TaxiEnv()
    agent = QLearningAgent(env)

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

        if (episode + 1) % 100 == 0:
            print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

    return agent


def test_agent(agent):
    env = TaxiEnv()
    state = env.reset()
    done = False
    total_reward = 0

    print("\nTesting trained agent:")
    while not done:
        env.render()
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        state = next_state
        total_reward += reward
        input("Press Enter to continue...")

    print(f"Total Reward: {total_reward}")


if __name__ == "__main__":
    trained_agent = train_agent(episodes=1000)
    test_agent(trained_agent)