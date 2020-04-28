# Reinforcement-Learning-DQN-Banana-Navigation
[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

## Introduction
For this project, an agent will be trained to navigate and collect bananas in a large, square world.  The task is to collect as many "Yellow" bananas while avoid to collect "Blue" bananas.  A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

## Getting Started
Please follow the instructions in `Navigation.ipynb` to get started to train your own agent to collect "Yellow" Banana!

![Trained Agent][image1]

#### Code Module Descriptions

- `model.py` defines the Q-network architecture
- `dqn_agent.py` defines a DQN agent
- `double_dqn_agent.py` defines a double DQN agent
- `prioritised_ double_dqn_agent.py` defines a double DQN agent with prioritised experience replay

#### Training the Agent

Both of these files can be run by invoking python 3 at the command line:

- `project1_doubleDQN.py` is used to train a DQN or double DQN agent. On line 2, you can import the agent from either the `dqn_agent` or `double_dqn_agent` modules mentioned above
- `project1_prioritisedDoubleDQN.py` is used to train a double DQN agent with prioritised experience replay


#### The Trained Agent

- `trained_agent_weights.pth` contains the weights of the best Q-network (see Report.md)
- `trained_agent.py` loads the optimised weights and runs the trained agent for 1 episode

## Enviornment
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:
-	0 - move forward.
-	1 - move backward.
-	2 - turn left.
-	3 - turn right.
The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

### Installing
Follow the instructions below to explore the environment on your own machine! You will also learn how to use the Python API to control your agent.

Step 1: Clone the DRLND Repository
If you haven't already, please follow the instructions in the [DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. These instructions can be found in README.md at the root of the repository. By following these instructions, you will install PyTorch, the ML-Agents toolkit, and a few more Python packages required to complete the project.

(For Windows users) The ML-Agents toolkit supports Windows 10. While it might be possible to run the ML-Agents toolkit using other versions of Windows, it has not been tested on other versions. Furthermore, the ML-Agents toolkit has not been tested on a Windows VM such as Bootcamp or Parallels.

Step 2: Download the Unity Environment
For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
Then, place the file in the p1_navigation/ folder in the DRLND GitHub repository, and unzip (or decompress) the file.

(For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (To watch the agent, you should follow the instructions to enable a virtual screen, and then download the environment for the Linux operating system above.)

1. Create and activate a new environment with Python 3.6
    
   ###### Linux or Mac:
   
    `conda create --name drlnd python=3.6`
    
    `source activate drlnd`

   ###### Windows:

    `conda create --name drlnd python=3.6`
    
    `activate drlnd`

2. Install of OpenAI gym in the environment

   `pip install gym`
 
3. Install the classic control and box2d environment groups

   `pip install 'gym[classic_control]'`
   
   `pip install 'gym[box2d]'`

4. Clone the following repository and install the additional dependencies

   `git clone https://github.com/udacity/deep-reinforcement-learning.git`
   
   `cd deep-reinforcement-learning/python`
   
   `pip install .`

## Project Starter Code
The original Udacity repo for this project can be found [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation).