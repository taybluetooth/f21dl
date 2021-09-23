# Python ≥3.5 is required
import sys
# Scikit-Learn ≥0.20 is required
import sklearn
# Common imports
import numpy as np
import pandas as pd
import os
import tarfile
import urllib.request

import matplotlib as mpl
import matplotlib.pyplot as plt

assert sys.version_info >= (3, 5)

assert sklearn.__version__ >= "0.20"

mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "dataset_assets"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


def load_skyserver_data():
    csv_path = os.path.join("SkySloanDataset2019.csv")
    return pd.read_csv(csv_path)


skyserver = load_skyserver_data()
