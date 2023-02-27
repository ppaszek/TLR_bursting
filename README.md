# TLR_bursting #
Set of codes for the analysis of scRNA-seq from the paper "Variability of the innate immune response is globally constrained by transcriptional bursting"


The codes here underpin the data analysis and theoretical arguments in

> N. Alachkar, D. Norton, Z. Wolkensdorfer, M. Muldoon, P. Paszek,*Variability of the innate immune response is globally constrained by transcriptional bursting* 


### Outline of the files ###

Repository includes a set of Python files for the analysis of the mRNA count data associated with the study by Hagai et al. Nature volume 563, pages 197–202 (2018). The code, among many things displays fitted mean-variance relationships for mouse and orthologue genes.

Raw data, i.e., E-MTAB-6754.processed.2.zip file, should be downloaded from ArrayEpress (E-MTAB-674) and copierd into Data/ArrayExpress folder. In order to work with the dat, first execute 001_Data_Setup which allows to open the original data, followed by 002_Burst_Model_fitting which fits Beta-Posisson model for all the response genes. Subsequently, two analysis piplines are provied for the mouse and the all species data, wich should be executed with appriopriate order- as indicated in the naming noatation. Aditional files allow extraction of mRNA count distibutions and additional analyses.



## Python environment

## Creating an environment

A list of required packages can be found in the file `./conda/env.yml` which can be used directly to create a conda environment. For example, the following commands will create a new conda environment in the folder `./conda/env_windows` and activate it.
```commandline
conda env create -f ./conda/env.yml -p ./conda/env_windows
conda activate ./conda/env_windows
```

If you prefer to use JupyterLab (rather than classic Jupyter) then you will also need to install `nodejs` and enable the ipywidgets extension:
```commandline
conda install jupyterlab nodejs">=10.0.0"
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
### Updating an environment

To update an existing conda environment with the required packages, run the following command with the environment activated.
```commandline
conda env update -f ./conda/env.yml
```



### Whom to contact ###
Questions about the code should be directed to 

* Pawel Paszek [pawel.paszek@manchester.ac.uk](mailto:pawel.paszek@manchester.ac.uk)

