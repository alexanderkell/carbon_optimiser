from elecsim.model.world import World 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'../..'))
from constants import ROOT_DIR_carbon


if __name__ == "__main__":
    scenario_file = "{}/data/processed/scenarios/scenario_NI.py".format(ROOT_DIR_carbon)
    world = World(initialization_year=2018, scenario_file=scenario_file, data_folder="myvol", number_of_steps=40, log_level="debug")
    for i in range(40):
        world.step()