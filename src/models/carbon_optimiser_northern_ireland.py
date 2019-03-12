"""
File name: carbon_optimiser
Date created: 19/02/2019
Feature: # Running of world to optimise for carbon tax using reinforcement learning
"""
from ray.tune import grid_search
from ray.tune import register_env
import ray
from ray.tune import run_experiments
from ray.tune import function
from elecsim.reinforcement_learning.gym_elecsim.gym_elecsim.envs.world_environment import WorldEnvironment

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../..'))
from constants import ROOT_DIR_carbon

__author__ = "Alexander Kell"
__copyright__ = "Copyright 2018, Alexander Kell"
__license__ = "MIT"
__email__ = "alexander@kell.es"

import logging

logging.basicConfig(level=logging.INFO)





if __name__ == "__main__":
    number_of_steps = 1
    scenario = "{}/data/processed/scenarios/scenario_NI.py".format(ROOT_DIR_carbon)
    register_env("MyEnv-v3", lambda config: WorldEnvironment(config))

    ray.init(object_store_memory=2000000000)
    run_experiments({
        "demo":{
            "run":"DDPG",
            "env": "MyEnv-v3",
            "stop": {
                "timesteps_total":number_of_steps,
            },
            "config":{
                # "lr": grid_search([1e-2, 1e-4, 1e-6]),
                "num_workers": 3,
                "gamma": 0.9,
                # "monitor":True,
                "timesteps_per_iteration": 1,
                "learning_starts": 1,
                "log_level":"INFO",
                "horizon": number_of_steps,
                "sample_batch_size": 128,
                "train_batch_size": 128,
                "env_config": {
                    "max_number_of_steps": number_of_steps,
                    "scenario_file": scenario,
                    "data_folder":"myvol",
                },
            },
        },
    })