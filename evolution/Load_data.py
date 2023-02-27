import os
from pathlib import Path
import pandas as pd
from rp2.paths import get_data_path, get_output_path


def load_analysis_genes():
    folder = get_data_path("RP2")
    path=os.path.join(folder, 'analysis_genes.csv')
    return pd.read_csv(path)

def load_responsive_analysis_genes():
    folder = get_output_path("Responsive_genes")
    path=os.path.join(folder, 'responsive_analysis_genes.csv')
    return pd.read_excel(path, index_col=1)

def load_trends_responsive_subset(species):
    folder = get_output_path("Mean_var")
    path = str(folder) + "/" + f"{species}_trend_info_responsive_subset.csv"
    return pd.read_csv(path)

def load_trends_good_fits(species):
    folder = get_output_path("Mean_var")
    path = str(folder) + "/" + f"{species}_trend_info_responsive_good_fit_subset.csv"
    return pd.read_csv(path)

def load_condition_info_responsive_subset(species):
    folder = get_output_path("Mean_var")
    condition_path = str(folder) + "/" + f"{species}_condition_info_responsive_subset.csv"
    return pd.read_csv(condition_path)

def load_condition_info_good_fits(species):
    folder = get_output_path("Mean_var")
    condition_path = str(folder) + "/" + f"{species}_condition_info_responsive_good_fit_subset.csv"
    return pd.read_csv(condition_path)


