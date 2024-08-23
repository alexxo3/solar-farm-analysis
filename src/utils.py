import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load the dataset from the given file path."""
    data = pd.read_csv(file_path)
    return data

def perform_eda(data):
    """Perform exploratory data analysis on the dataset."""
    st.header("Summary Statistics")
    st.write(data.describe())

    st.header("Correlation Heatmap")
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
    st.pyplot()

    st.header("Time Series Analysis")
    fig, ax = plt.subplots()
    data.plot(x='Timestamp', y=['GHI', 'DNI', 'DHI'], ax=ax)
    plt.title("Irradiance over Time")
    st.pyplot(fig)
