"""
A set of utilities to convert between pytorch and openai gym

States.gym2pytorch - converts a gym state to a pytorch tensor of size (1, -1)
Rewards.pytorch2gym - 
"""
from pg_methods.interfaces import common_interfaces as common


class SimpleActionProcessor(common.Interface):
    def __init__(self, action_space, one_hot=False):
        self.action_space = action_space
        if action_space.n == 2:
            self.action_size = action_space.n - 1
        else:
            self.action_size= action_space.n

    def pytorch2gym(self, action):
        return int(common.pytorch2list(action)[0])

