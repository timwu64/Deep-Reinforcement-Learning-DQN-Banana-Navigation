import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, hidden_sizes, dueling):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            hidden_sizes[0] (int): Number of nodes in first hidden layer
            hidden_sizes[1] (int): Number of nodes in second hidden layer
            dueling (bool): Use dueling if 'True'
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.dueling = dueling
        
        if self.dueling:
            self.fc1 = nn.Linear(state_size, hidden_sizes[0])
        
            self.advantage = nn.Linear(hidden_sizes[0], hidden_sizes[1])
            self.advantage2 = nn.Linear(hidden_sizes[1], action_size)
        
            self.value = nn.Linear(hidden_sizes[0], hidden_sizes[1])
            self.value2 = nn.Linear(hidden_sizes[1],1)
            self.activation = nn.ReLU()
        else:
            self.fc1 = nn.Linear(state_size, hidden_sizes[0])
            self.fc2 = nn.Linear(hidden_sizes[0], hidden_sizes[1])
            self.fc3 = nn.Linear(hidden_sizes[1], action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        
        if self.dueling:
            output1 = self.fc1(state)
            output1 = self.activation(output1)
        
            output_advantage = self.advantage(output1)
            output_advantage = self.activation(output_advantage)
            output_advantage = self.advantage2(output_advantage)
        
            output_value = self.value(output1)
            output_value = self.activation(output_value)
            output_value = self.value2(output_value)
        
            output_final = output_value + output_advantage - output_advantage.mean()
            return output_final
        else:
            x = F.relu(self.fc1(state))
            x = F.relu(self.fc2(x))
            return self.fc3(x)