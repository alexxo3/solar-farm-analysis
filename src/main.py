import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, perform_eda

st.title("Solar Farm Analysis Dashboard")

# Load data
data = load_data("data/solar_data.csv")

# Perform EDA
perform_eda(data)
