# Geophysical inversions with SimPEG: an example with airborne electromagnetic data
## A SimPEG tutorial for the SEG Near Surface Webinar series.

**Instructors:**
[Joseph Capriotti][jcapriot]<sup>1</sup>
[Lindsey Heagy][lindsey]<sup>2</sup>
and
[Seogi Kang][seogi]<sup>3</sup>


> <sup>1</sup>
> Center for Gravity, Electrical, and Magnetic Studies,
> Department of Geophysics, Colorado School of Mines.
> <br>
> <sup>2</sup>
> Geophysical Inversion Facility. Earth, Ocean and Atmospheric
> Sciences. University of British Columbia.
> <br>
> <sup>3</sup>
> Environmental Geophysics Research Group, Department of Geophysics, Stanford University


| **Information** | |
|---|---|
| When | Feb 14, 2024  11 am CST|
| Materials | [Intro Slides](https://docs.google.com/presentation/d/1a2mtYsiRe_ylpGesgdkZJxeG_9tDjO8TPXVV6gzD0Ss/edit?usp=sharing) |


## About

We were invited by the SEG Near-Surface Geophysics Student Subcommittee to give a tutorial
as part of their Open-Source Software webinar series.

> Discover the powerful open-source [SimPEG][simpeg] framework.
> You will learn how to simulate and invert airborne electromagnetic (AEM) data using a real-world dataset.

During this tutorial we will go through a notebook describing how to invert AEM
data collected in the Salinas Valley of California using the SkyTEM system to monitor salt water intrusion. For details
about the dataset please checkout [Gottschalk et. al. 2017][case-study]. We will focus on
how to simulate and invert the data by representing the parameters of the SkyTEM system
using SimPEG components.

This notebook is what we will use and modify during the live tutorial:

- [live-skytem-inversion.ipynb](notebooks/live-skytem-inversion.ipynb)


Alternatively there is also a filled version of this notebook available if you do not want to follow
along with the coding.

- [skytem-inversion.ipynb](notebooks/skytem-inversion.ipynb)

## Setup

During this workshop we'll use [Juptyer notebooks][jupyter] to simulate and invert
SkyTEM data.

To be able to follow the tutorial and run the notebook, you'll need to have
access to a Python environment. This could be done through a **local Python
installation** like [Anaconda][anaconda] or [Miniforge][miniforge], or through
**online services** like [Google Colab][colab].

We recommend installing locally so you can save your progress. In google colab, your
progress is not saved between sessions, but if you are struggling getting the correct
environment setup locally it should work as a backup option.

Here will provide instructions to:

- [Install Python locally](#install-python-locally)
- or [Configure Google Colab](#configure-google-colab)

## Install Python locally

To be able to run the Jupyter notebooks for this tutorial in our own machines,
we'll have to follow these steps:

1. Install a Python distribution (like [Anaconda][anaconda] or
   [miniforge][miniforge]).
1. Create a [_conda environment_][conda-environ] with all the Python packages
   needed (for example, SimPEG).
1. Activate this conda environment and run [JupyterLab][jupyterlab] to start
   coding.

### Step 1: Install a Python distribution

We recommend installing a Python distribution like [miniforge][miniforge] or
[Anaconda][anaconda].

Both of them will install Python and a package manager that allows us to
install new Python libraries (like SimPEG for example), and also create
_environments_.

Anaconda uses the `conda` package manager, while Miniconda uses the new
`mamba`, which works faster than `conda`.

If you have either of both installed, you can skip this step. Otherwise, please
follow their installation instructions:

- Install miniforge: https://github.com/conda-forge/miniforge#install
- Install Anaconda: https://docs.anaconda.com/anaconda/install

### Step 2: Create the `simpeg-segns2024` conda environment

> [!IMPORTANT]
> In the following steps we'll make use of the `mamba` package manager. In case
> you installed Anaconda, use `conda` instead. You can simply replace `mamba`
> for `conda` on every command we ask to use it and it'll work fine.

1. Download the [`environment.yml`][environment_yml] file from
   (right-click and select "Save page as" or similar).
1. Make sure that the file is called `environment.yml`.
   Windows sometimes adds a `.txt` to the end, which you should remove.
1. Open a terminal (_Anaconda Prompt_ or _Miniforge Prompt_ if you are running
   Windows). The following steps should be done in the terminal.
1. Navigate to the folder that has the downloaded environment file
   (if you don't know how to do this, take a moment to read [the Software
   Carpentry lesson on the Unix shell][shell-novice]).
1. Create the conda environment by running
   ```
   mamba env create --file environment.yml
   ```
   (this will download and install all of the packages used in
   the tutorial). If you installed Anaconda, then replace `mamba` for `conda`
   in the previous line.

### Step 3: Get the repository's utility code and data.

If you are not comfortable using git, you will need to at a bare minimum you will
need to download:

- The data configuration file: [configuration](data/20170606_337m2_Cal_DualWaveform_60Hz_414_412_418.gex)
- A parser script to read the configuration file: [gex_parser.py](notebooks/utilities/gex_parser.py)
- The environment [`environment.yml`][environment_yml] as detailed above in Step 2.

If you are comfortable using git, you have likely already cloned this repository and
received all of the files you will need.

>[!TIP]
> You don't need to explicitly download the data file from github, we will be able to use
> `pandas.read_csv` to retrieve the file for us.


### Step 4: Activate the `simpeg-segns2024` environment and start JupyterLab

> [!TIP]
> You'll need a browser that is able to run JupyterLab (basically anyone except
> Internet Explorer). If you are in Windows, make sure you change your
> default browser to a different one.

Now we can activate the newly created `simpeg-segns2024` environment.

1. Open a terminal (_Anaconda Prompt_ or _Miniforge Prompt_ if you are running
   Windows).
1. Activate the `simpeg-segns2024` environment by running:
   ```
   conda activate simpeg-segns2024
   ```
1. With the `simpeg-segns2024` environment activated, we can start JupyterLab
   by running 
   ```terminal
   jupyter-lab
   ```
   in the terminal. A new tab in our web browser should
   open showing JupyterLab's interface.
1. Navigate to the [live-skytem-inversion.ipynb](notebooks/live-skytem-inversion.ipynb) notebook.

## Configure Google Colab

To be able to run the Jupyter notebooks for this tutorial in Google Colab,
we'll need to follow these steps:

1. Login to our Google Colab account.
1. Copy the live notebook from GitHub.
1. Install some Python libraries that we'll need to use, such as
   [SimPEG][simpeg].

### Step 1: Login to our Google Colab account

If you don't have a Google account, create one and log in. If you do, you just
need to log in.

### Step 2: Open the Live notebook in Colab

1. Access to Google Colab by going to: https://colab.research.google.com
1. Find the top menu and choose `File` > `Open Notebook`.
1. Select the GitHub option
1. Paste the URL of this repository into the space: https://github.com/simpeg/segns-2024-tutorial
2. Select the [live-skytem-inversion.ipynb](notebooks/live-skytem-inversion.ipynb) notebook.

### Step 3: Install some Python libraries

To be able to follow this workshop we need to install some Python libraries
that aren't preinstalled in the default Google Colab environment.

1. Click on the first cell of the notebook (Create
   a new _Code_ cell and move it to the first position with the arrows icons
   that appear on its top-right).
1. Type the following line in the selected cell:
   ```
   !pip install simpeg==0.20.0 discretize==0.10.0
   ```
   Note the `!` sign at the beginning of the line, **don't remove it**.
1. Run that cell by clicking the _Play_ button on its left or by pressing
   `Shift+Enter` in your keyboard. `pip` should install all the packaged listed
   in that line. If installation goes smoothly, you should see a line that
   reads `Successfully installed ...` and lists all the new packages that had
   been installed.

### Step 4: Copy the repository's utility code and data to Colab.

To be able to follow along with the tutorial, you will need to copy at least
two files directly to Google Colab: the configuration file and the parser script.
You can download them directly from github to Google Colab by typing in another cell (and then executing it):

```
!wget https://raw.githubusercontent.com/simpeg/segns-2024-tutorial/main/data/20170606_337m2_Cal_DualWaveform_60Hz_414_412_418.gex
!wget https://raw.githubusercontent.com/simpeg/segns-2024-tutorial/main/notebooks/utilities/gex_parser.py
```

This will download the SkyTEM configuration file and a parser to easily read it into python.


> [!IMPORTANT]
> Every time you open a notebook in Colab or create a new one, you'll have to
> reinstall these packages and download the data again (Google Colab doesn't save
> installed states across notebooks).
>
> If it's a new notebook, just follow the previous instructions from the top.
>
> If it's an existing notebook, make sure that it has the `!pip install ...`
> and the `!wget ...` lines at the top (add it otherwise), and run it.

## Acknowledgement
AEM data used in this tutorial were acquired with funding from MCWRA (Monterey County Water Resources Agency) with the [SkyTEM](https://skytem.com/) system; acquisition oversight, planning, and processing by [Aqua Geo Framework](https://www.aquageoframeworks.com/).

## License

This work is licensed under the [MIT
License](https://opensource.org/license/mit/).

[jcapriot]: https://www.github.com/jcapriot
[lindsey]: https://lindseyjh.ca/
[seogi]: https://sgkang.github.io/
[simpeg]: https://www.simpeg.xyz
[case-study]: https://library.seg.org/doi/10.1190/geo2019-0272.1
[jupyter]: https://jupyter.org/
[colab]: https://colab.research.google.com
[anaconda]: https://www.anaconda.com/download
[miniforge]: https://github.com/conda-forge/miniforge
[conda-environ]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[jupyterlab]: https://jupyterlab.readthedocs.io
[environment_yml]: https://raw.githubusercontent.com/simpeg/agrogeo24/main/environment.yml
[shell-novice]: http://swcarpentry.github.io/shell-novice
