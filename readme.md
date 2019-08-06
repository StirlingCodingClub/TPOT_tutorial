# **WORK IN PROGRESS - DO NOT CLONE YET!**


## Introduction to AutoML using the TPOT package


### 1) Setting up a Python work environment

The best way to work with Python scientifically is to use Anaconda. Anaconda is a management system for installing Python (and other languages too!) on your system, which offers a few advantages:

- It keeps installations separate from your system Python installation (on Linux or Mac), avoiding unintended updates;
- It has its own package repository (conda-forge) and package installation tools, including automatic resolution of dependencies;
- It comes withy several packages commnly used for data analysis pre-instalkled ('Anaconda is Python with batteries included' is they like to call it)
- Let's you create **virtual environments**, which are like separeate Python installations. Each virtualenv can have be based on a different version of Python (2.7, 3.5, 3.6, etc.), and can have a separate list of packages with respective versions installed. But it is smart in that iwont install multiple copies of the same package, just link it to the different virtualenvs
    - Example: for one project, you need a Python package that depends on the library `gdal_3.01`. On a second project, you need a different package, that only works with `gdal_2.4.2`. And on a third project, you use a third different package that also needs `gdal_3.01`. You then create a new environment called "project_1", and asks conda to install the package you need. Conda will download and install the package plus all necessary dependencies, including `gdal_3.01`. You then create a second environment called "project_2", and ask conda to install the second package. Ity will download and install it, as well the dependencies including `gdal_2.4.2`. You finally create an environment called 'project+3', and asks Anaconda to install the third package. It will download and install it and any other dependencies, but will only link the previous installation of `gdal_3.01`, without re-downloading or using more disk space to duplicate the installation
- Environments are great when you need packages that don't play nice with other packages because of conflicting dependencies, and are also a great way to make sure you have a functional work enviroment for each project you are working on, whithout worrying that packages needed for one project will interfere with the packages need for the other package.

You can dowload Anaconda installers for your system at https://www.anaconda.com/distribution. Installation instructions for each OS are available here: https://docs.anaconda.com/anaconda/install/ .

Once you have Anaconda installed, it will be accessible via your terminal on Linux and Mac, and via the *Anaconda Prompt* application on Windows.

We can then create an environment for our tutorial session, and then install the necessary packages:

```
> conda create --name tpot_env

```

Accept the transaction, and it should be created. We can then switch to out new environment using:

```
> conda activate tpot_env
```

And then we install the packages we will need for this tutorial session: tpot itself, pandas and geopandas, and :

```
conda install -c conda-forge tpot, pandas, geopandas
```

We will use Jupyter notebook to run the code, so install it to your environment as well:

```
conda install -c conda-forge jupyter 
```

Finally, download or clone this repository to your machine to have all necessary data. Don't forget to change your terminal to the intendend folder you want the repository to be in:

```
> git clone 
```


    
    