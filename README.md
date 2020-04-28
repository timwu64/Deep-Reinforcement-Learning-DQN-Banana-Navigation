# Reinforcement-Learning-DQN-Banana-Navigation
[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

## Introduction
For this project, an agent will be trained to navigate and collect bananas in a large, square world.  Shown below:
![Trained Agent][image1]
A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

## Enviornment
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:
- `W` - move forward.
- `S` - move backward.
- `A` - turn left.
- `D` - turn right.
The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

## Getting Started
#### Descriptions
- `README.md` describe the environment, along with how to install the requirements.

#### Code
- `Navigation.ipynb` defines and train a DQN agent
- `model.py` defines the DQN network architecture

#### Report
- `REPORT.md` describe the learning algorithm and the details of the implementation, along with ideas for future work.

#### The Trained Agent
- `checkpoints` folder contains the weights of the all the DQN implementation (see `REPORT.md` for details)

### Installation
- `python` folder contains the installation dependencies

Follow the instructions below to explore the environment on your own machine! You will also learn how to use the Python API to control your agent.

The Step by Step installation example shown below:

1. Clone the DRLND Repository

    If you haven't already, please follow the instructions in the [DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. These instructions can be found in README.md at the root of the repository. By following these instructions, you will install PyTorch, the ML-Agents toolkit, and a few more Python packages required to complete the project.

    (For Windows users) The ML-Agents toolkit supports Windows 10. While it might be possible to run the ML-Agents toolkit using other versions of Windows, it has not been tested on other versions. Furthermore, the ML-Agents toolkit has not been tested on a Windows VM such as Bootcamp or Parallels.

2. Download the Unity Environment

    For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

      - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
      - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
      - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
      - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
      Then, place the file in the p1_navigation/ folder in the DRLND GitHub repository, and unzip (or decompress) the file.

    (For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (To watch the agent, you should follow the instructions to enable a virtual screen, and then download the environment for the Linux operating system above.)

3. Create and activate a new environment with Python 3.6
    
     ###### Linux or Mac:
     
      `conda create --name drlnd python=3.6`
      
      `source activate drlnd`

     ###### Windows:

      `conda create --name drlnd python=3.6`
      
      `activate drlnd`

4. Clone the following repository 

    `git clone https://github.com/udacity/deep-reinforcement-learning.git`

    and start to run the first cell of the  to install all the dependencies

    or you can install the dependencies as below (optional)
   
   `cd ./python`
   
   `pip install .`

   `pip install torchsummary`

### Play it as a human agent
- `play` folder contains the manual game play enviornment installation dependencies
  Follow the instructions in the Jupyter notebook `play.ipynb` in the play folder to play the game, 

  Spend a couple of minutes to move around and collect some yellow bananas.

### Explore the Environment and Run it
- After you have followed the instructions above, open `Navigation.ipynb` and and follow the instructions to learn how to use the Python API to control the agent.

## Project Starter Code
The original Udacity repo for this project can be found [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation).