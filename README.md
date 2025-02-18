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
  
## Future Goals and Improvements
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
python main.py
```

4. Branches:
 - There are two branches right now and you can switch between them:
   - `main` for the the grid version, no GUI
   - `multi_location` for the grid version with GUI

  
5. Credits:
 - The project is inspired by this link:
https://shorturl.at/bagnp
 - But it is designed from scratch and improvised the idea by myself.