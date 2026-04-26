import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    
    sea_level_data = pd.read_csv("epa-sea-level.csv")
    x = sea_level_data["Year"]
    y = sea_level_data["CSIRO Adjusted Sea Level"]

    #print(sea_level_data["Year"])

    # Create scatter plot

    plt.scatter(x, y)

    # Create first line of best fit

    emt = linregress(x, y)
    #print(emt)
    #plt.plot(x, emt. intercept + emt.slope*x)

    # Predicting year 2050
    prediction_x = np.arange(sea_level_data['Year'].min(), 2051)
    prediction_y = emt.intercept + emt.slope * prediction_x

    plt.plot(prediction_x, prediction_y, color="orange")

    # Create second line of best fit

    recent_sea_level_data = sea_level_data[sea_level_data["Year"] >= 2000]
    x_recent = recent_sea_level_data["Year"]
    y_recent = recent_sea_level_data["CSIRO Adjusted Sea Level"]

    emt_recent = linregress(x_recent, y_recent)

    prediction2_x = np.arange(recent_sea_level_data['Year'].min(), 2051)
    prediction2_y = emt_recent.intercept + emt_recent.slope * prediction2_x

    plt.plot(prediction2_x, prediction2_y, color="red")

    # Add labels and title

    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()