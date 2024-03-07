#!/bin/bash

# To run: 
#   $: cd /path/to/Gridwise_Data_Visualization/
#   $: bash setup/setup-conda.sh

# To activate environment: 
#   $: conda activate hive_extension

# Author's Note: The location & Version of Conda were chosen
# to be the same as those used in the OpenPATH `e-mission-server`.

export EXP_CONDA_VER=23.5.2
export EXP_CONDA_VER_SUFFIX=0

INSTALL_PREFIX=$HOME/miniconda-$EXP_CONDA_VER
SOURCE_SCRIPT="$HOME/miniconda-$EXP_CONDA_VER/etc/profile.d/conda.sh"
source $SOURCE_SCRIPT

conda env update --name parse_gridwise --file setup/parse_gridwise.yml
