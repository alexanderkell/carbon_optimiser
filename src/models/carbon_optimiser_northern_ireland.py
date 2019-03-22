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
from ray.tune.schedulers import PopulationBasedTraining
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
    number_of_steps = 40
    scenario = "{}/data/processed/scenarios/scenario_NI.py".format(ROOT_DIR_carbon)
    register_env("MyEnv-v3", lambda config: WorldEnvironment(config))

    pbt_scheduler = PopulationBasedTraining(
        time_attr='time_total_s',
        reward_attr='episode_reward_mean',
        perturbation_interval=6000.0,
        hyperparam_mutations={
            "lr": [1e-3, 5e-4, 1e-4, 5e-5, 1e-5]
        })
    number_of_workers = 2
    ray.init(object_store_memory=2000000000, num_cpus=8)
    run_experiments({
        "demo":{
            "run":"DDPG",
            "env": "MyEnv-v3",
            "stop": {
                "timesteps_total":10000000000,
            },
            "checkpoint_freq": 1,
            "config":{
                "lr": grid_search([1e-2, 1e-4, 1e-6]),
                "num_workers": number_of_workers,
                "gamma": 0.9,
                "timesteps_per_iteration": 40*number_of_workers,
                "learning_starts": 120,
                "parameter_noise": True,
                "log_level":"INFO",
                "horizon": number_of_steps,
                "env_config": {
                    "max_number_of_steps": number_of_steps,
                    "scenario_file": scenario,
                    "data_folder":"myvol",
                },
            },
        },
    },
    scheduler=pbt_scheduler
    )