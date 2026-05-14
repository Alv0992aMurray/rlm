"""rlm - Reinforcement Learning with Language Models.

A library for training and evaluating language models using
reinforcement learning techniques.

Note: Forked from alexzhang13/rlm for personal experimentation.
See https://github.com/alexzhang13/rlm for the original project.
"""

__version__ = "0.1.0"
__author__ = "rlm contributors"

from rlm.agent import RLMAgent
from rlm.environment import TextEnvironment
from rlm.trainer import RLMTrainer

__all__ = [
    "RLMAgent",
    "TextEnvironment",
    "RLMTrainer",
    "__version__",
]
