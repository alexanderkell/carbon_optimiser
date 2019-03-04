import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from mesa.batchrunner import BatchRunnerMP

from elecsim.model.world import World


from elecsim.scenario.scenario_data import power_plants

# import data.processed.scenarios.scenario_NI
# from data.processed.scenarios.scenario_scotland import scenario

"""
File name: batch_run_timer
Date created: 25/01/2019
Feature: # Functionality to test different models in parallel
"""

__author__ = "Alexander Kell"
__copyright__ = "Copyright 2018, Alexander Kell"
__license__ = "MIT"
__email__ = "alexander@kell.es"


class DemandTimer:

    def __init__(self):
        self.power_plants = power_plants


    def run_world_with_demand_and_power_plants(self):

        number_of_steps = 40
        data_folder = "/data/processed/runs/testing_scotland_and_NI/scotland_NI_run"

        fixed_params = {
            "initialization_year": 2018,
            "number_of_steps": number_of_steps,
            "demand_change": [1.0] * 50,
            "carbon_price_scenario": [10]*50,
            "data_folder": data_folder,
            "time_run":True,
            "log_level":"info"
        }

        variable_params = {
            "scenario_file": [
                "/Users/b1017579/Documents/PhD/Projects/11-carbon_optimiser/data/processed/scenarios/scenario_scotland.py",
                "/Users/b1017579/Documents/PhD/Projects/11-carbon_optimiser/data/processed/scenarios/scenario_NI.py"
            ]
        }



        batch_run = BatchRunnerMP(World,
                                  fixed_parameters=fixed_params,
                                  variable_parameters=variable_params,
                                  iterations=1,
                                  max_steps=number_of_steps, nr_processes=3)

        batch_run.run_all()


if __name__ == "__main__":
    DemandTimer().run_world_with_demand_and_power_plants()
