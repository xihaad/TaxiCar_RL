# TaxiCar_RL
# AI TaxiCar Navigator with Q-Learning 


A reinforcement learning project implementing Q-Learning to train a taxi agent in a 10x10 grid environment with obstacles and dynamic passenger/destination locations.

## Key Features
- 🚕 **10x10 Grid World** with complex wall configurations
- 🧭 **4 Corner Locations** (A, B, C, D) for passenger pickup/dropoff
- 🧠 **Learning Algorithms**:
  - Tabular Q-Learning

- 🎮 **Pygame Visualization** with real-time agent tracking
- ⚖️ **Custom Reward System**:
  - +20 for successful dropoff
  - -1 per timestep penalty
  - -10 for invalid pickup/dropoff
  - -2 for wall collisions
  
## Future Goals
  - Deep Q-Network (DQN) with bigger state and multiple Passenger/Destination locations

## Installation
1. Clone the repository:
```bash
git clone https://github.com/xihaad/TaxiCar_RL.git
cd TaxiCar_RL
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the agent:
```bash
python train_dqn.py
```