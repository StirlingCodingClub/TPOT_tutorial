## A brief tutorial on AutoML using the TPOT package

This is a simple demo of how to use TPOT ion Python. 

As the developers say, [TPOT](https://epistasislab.github.io/tpot/) is "(a) Data Science Assistant. TPOT is a Python Automated Machine Learning tool that optimizes machine learning pipelines using genetic programming. (It) will automate the most tedious part of machine learning by intelligently exploring thousands of possible pipelines to find the best
one for your data."

This is what TPOT devs call a pipeline:

![ML pipleine](https://raw.githubusercontent.com/EpistasisLab/tpot/master/images/tpot-ml-pipeline.png)





### 1) Setting up a Python work environment

The best way to work with Python scientifically is to use Anaconda. Anaconda is a management system for installing Python (and other languages too!) on your system, which offers a few advantages:

- It keeps installations separate from your system Python installation (on Linux or Mac), avoiding unintended updates;
- It has its own package repository (conda-forge) and package installation tools, including automatic resolution of dependencies;
- It comes with several packages commonly used for data analysis pre-installed ('Anaconda is Python with batteries included' is they like to call it)
- Let's you create **virtual environments**, which are like separate Python installations. Each virtualenv can have be based on a different version of Python (2.7, 3.5, 3.6, etc.), and can have a separate list of packages with respective versions installed. But it is smart in that it won't install multiple copies of the same package, just link it to the different virtualenvs
    - Example: for one project, you need Python `pkg1` that depends on the library `gdal_3.01`. On a second project, you need package `pkg2`, that only works with `gdal_2.4.2`. And on a third project, you need package `pkg3` that also needs `gdal_3.01`. 
    - You then create a new environment called "project_1", and asks `conda` (Anaconda's package manager) to install `pkg1`. `conda` will download and install the package plus all necessary dependencies, including `gdal_3.01`. You then create a second environment called "project_2", and ask `conda` to install the `pkg2`. It will download and install it, as well the dependencies including `gdal_2.4.2`. You finally create an environment called 'project+3', and asks `conda` to install `pkg3`. It will download and install it and any other dependencies, but will only link the previous installation of `gdal_3.01`, without re-downloading or using any more disk space by duplicating the installation.
- Environments are great when you need packages that don't play nice with other packages because of conflicting dependencies, and are also a great way to make sure you have a functional work environment for each project you are working on, without worrying that packages needed for one project will interfere with the packages needed for the other project.



You can download Anaconda installers for your system at https://www.anaconda.com/distribution. 

Installation instructions for each OS are available here: https://docs.anaconda.com/anaconda/install/ .



Once you have Anaconda installed, it will be accessible via your terminal on Linux and Mac, and via the *Anaconda Prompt* application on Windows.

We can then create an environment named `tpot_env` for our tutorial session:

```
> conda create --name tpot_env

```

Accept the transaction, and it should be created. We can then switch to out new environment using:

```
> conda activate tpot_env
```

And then we install the packages we will need for this tutorial session: `tpot` itself, `pandas` ,`scikit-learn` (the main ML library in Python) and `xgboost` (a pretty good ML algorithm that is not originally part of `scikit-learn`) .  We will also use a *Jupyter notebook* to run the code, so we install it on our environment as well:

```
conda install -c conda-forge tpot pandas jupyter scikit-learn
```

The Jupyter notebook depends on having a  *python kernel* installed for it to work, which we do by: 

```
python -m ipykernel install --user --name tpot_env --display-name "Python (tpot_env)"
```

Then, download or clone this repository to your machine to have all the necessary data. Don't forget to change your terminal to the intended folder you want the repository to be in:

```
> git clone https://github.com/StirlingCodingClub/TPOT_tutorial.git 
```

 Finally, launch a new Jupyter notebook from  within  your project folder

``` 
> jupyter notebook
```

 We start the tutorial session from here.

