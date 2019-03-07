Carbon Optimiser
================

.. image:: https://img.shields.io/pypi/v/carbon_optimiser.svg
    :target: https://pypi.python.org/pypi/carbon_optimiser
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/alexanderkell/carbon_optimiser.png
   :target: https://travis-ci.org/alexanderkell/carbon_optimiser
   :alt: Latest Travis CI build status

This repository contains code to optimise the long-term strategy of setting carbon tax to reduce carbon emissions and costs of an electricity market.

We use [ElecSim](https://github.com/alexanderkell/elecsim) as the simulation model and [Ray Rllib](https://ray.readthedocs.io/en/latest/rllib.html) as a package for distributed reinforcement learning.

Usage
-----

To use this, use the WorldEnvironment class of ElecSim, and create a reinforcement learning algorithm in rllib. An example of this is shown [here](https://github.com/alexanderkell/carbon_optimiser/blob/master/src/models/carbon_optimiser_northern_ireland.py).

Installation
------------

This requires the installation of ``elecsim`` and ``ray[rllib]``.

To do so, make sure you have installed python and the python installer, pip and run the following commands:
```
pip install elecsim
pip install ray[rllib]
```

Docker
______

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

Ray rllib is not compatible with windows, however it will run on unix based systems (linux, mac os)

Licence
-------

MIT License

Authors
-------

`carbon_optimiser` was written by `Alexander Kell <alexander@kell.es>`_.
