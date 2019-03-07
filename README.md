Carbon Optimiser
================

This repository contains code to optimise the long-term strategy of setting carbon tax to reduce carbon emissions and costs of an electricity market.

We use [ElecSim](https://github.com/alexanderkell/elecsim) as the simulation model and [Ray Rllib](https://ray.readthedocs.io/en/latest/rllib.html) as a package for distributed reinforcement learning.

Usage
-----

The WorldEnvironment class of ElecSim is used as an [OpenAI gym](https://gym.openai.com/) interface to the reinforcement learning algorithm 

We use the [Ray RLlib](https://ray.readthedocs.io/en/latest/rllib.html) for distributed reinforcement learning algorithms. We then run a number of different reinforcement algorithm experiments. An example of this is shown [here](https://github.com/alexanderkell/carbon_optimiser/blob/master/src/models/carbon_optimiser_northern_ireland.py).

Installation
------------

For this, the installation of ``elecsim`` and ``ray[rllib]`` are required.

To do so, make sure you have installed python and the python installer, pip and run the following commands:
```
pip install elecsim
pip install ray[rllib]
```

Once this is done, you can run your desired reinforcement algorithm as shown [here](https://github.com/alexanderkell/carbon_optimiser/blob/master/src/models/carbon_optimiser_northern_ireland.py). 

Docker
------

This can be run with your own custom reinforcement learning file through docker.

Simply pull from dockerhub with the following command:
```
docker pull alexkell/carbon-optimiser
```
Next, to run the reinforcement algorithm whilst saving the run data and ray results data run the following command:
```
docker run --shm-size=2G -it -v <path/to/run_data>:/myvol -v <path/to/ray_results>:/root/ray_results alexkell/carbon-optimiser:latest </path/to/reinforcement_algorithm_runner>
```
Replacing the paths in ```"<>"``` with your own directories. 

- ```<path/to/run_data>``` is where data is written that is output from elecsim. Enabling you to visualise individual run characteristics such as carbon tax, cost of electricty and electricity supply type. 
- ```<path/to/ray_results>``` is where you would like data output from ray rllib to be written. This provides information on the reinforcement algorithm which can be visualised using [tensorboard](https://www.tensorflow.org/guide/summaries_and_tensorboard). Checkpoints of the weights for the reinforcement algorithm are also saved here
- Finally, ```</path/to/reinforcement_algorithm_runner>``` is the path where you have stored your version of [reinforcement algorithm](https://github.com/alexanderkell/carbon_optimiser/blob/master/src/models/carbon_optimiser_northern_ireland.py).


Compatibility
-------------

Ray RLlib is not compatible with windows, however it will run on unix based systems (linux, mac os)

Licence
-------

MIT License

Authors
-------

`carbon_optimiser` was written by `Alexander Kell <alexander@kell.es>`.
