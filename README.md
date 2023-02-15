# jupyter-kg
Simple Graph +  SparQL examples in Jupyter


## Usage

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/WWU-AMM/jupyter-kg/HEAD?labpath=index.ipynb)

## Testing

On each push a GitHub Action is triggered to build a docker image, just like mybinder.org would.
All `.py` and `.ipynb` files in the `image-tests` subdir are then executed with 
`pytest` and `pytest-notebook` respectively. Commited notebook outputs are checked against the results from
execution.

## Deploy

Deployed on [mybinder](https://mybinder.org/v2/gh/WWU-AMM/jupyter-kg/HEAD?labpath=example_01.ipynb)
