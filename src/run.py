from elecsim.data_manipulation.data_modifications.scenario_modifier import overwrite_scenario_file
import scenario_file

from elecsim.model.world import World

if __name__ == "__main__":
    overwrite_scenario_file(scenario_file)
    world = World(2018, log_level="info")
    for i in range(20):
        world.step()
        
