from elecsim.model.world import World
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("Hello")
    world = World(2018)
    for i in range(20):
    world.step()
