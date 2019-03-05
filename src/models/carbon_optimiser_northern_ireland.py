"""
File name: carbon_optimiser
Date created: 19/02/2019
Feature: # Running of world to optimise for carbon tax using reinforcement learning
"""
from ray.tune import grid_search
from ray.tune import register_env
import ray
from ray.tune import run_experiments

from elecsim.reinforcement_learning.gym_elecsim.gym_elecsim.envs import WorldEnvironment

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../../..'))

print(os.path.join(os.path.dirname(__file__),'../..'))

from constants import ROOT_DIR_carbon

__author__ = "Alexander Kell"
__copyright__ = "Copyright 2018, Alexander Kell"
__license__ = "MIT"
__email__ = "alexander@kell.es"

import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    scenario = "{}/data/processed/scenarios/scenario_NI.py".format(ROOT_DIR_carbon)
    register_env("MyEnv-v0", lambda config: WorldEnvironment(scenario_file=scenario))

    ray.init(object_store_memory=2000000000)
    run_experiments({
        "demo":{
            "run":"PPO",
            "env": "MyEnv-v0",
            "stop": {
                "timesteps_total":50
            },
            "config":{
                "lr": grid_search([1e-2, 1e-4, 1e-6]),
                "num_workers": 1,
            }
        }
    })
