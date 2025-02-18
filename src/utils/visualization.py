import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def odometer_histogram(df: pd.DataFrame):
    """
    Generate a histogram showing the distribution of the distance traveled by vehicles.

    :param df: DataFrame containing vehicle data
    :return: Plotly Express figure with the generated chart
    """

    fig = px.histogram(df, x="odometer") # histogram
    return fig 




def odometer_price_scatterplot(df: pd.DataFrame):
    """
    Generate a scatterplot showing the number of kilometers traveled and the price.

    :param df: DataFrame containing vehicle data.
    :return: Plotly Express figure with the generated chart.
    """
    fig = px.scatter(df, x="odometer", y="price") # scatterplot
    return fig




