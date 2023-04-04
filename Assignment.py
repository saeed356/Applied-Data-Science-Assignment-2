import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import os

#reading files and path
input_path = os.getcwd() + "\\datasource.csv"

data = ['Australia', 'United Kingdom', 'Pakistan']
data_2 = ['Pakistan', 'United Kingdom', 'Australia', 'Belgium', 'Bolivia', 'Georgia', 'Libya']

#Input file
def read_file(input_file):
    climate_data_1 = pd.read_csv(input_file, skiprows=4)
    climate_data_1 = climate_data_1.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    climate_data_1 = climate_data_1.dropna(how='all')
    climate_data_1 = climate_data_1.set_index('Country Name')
    climate_data_2 = climate_data_1.T


    return climate_data_1, climate_data_2

def chart2(location):
    #Declaring countries
    climate_data_1.loc[location, '2005':].plot()
    #plotting
    plot.ylabel('CO2 emissions (metric tons per capita)')
    mng = plot.get_current_fig_manager()
    # mng.window.state('zoomed')
    #show plot
    plot.show()
    #reading dataframe again to make another chart
    my_df = pd.read_csv('datasource.csv', skiprows=4)
    #rows skipped as data was not correct on 1st 4 rows
    my_df = my_df.drop_duplicates(subset=["Country Name"], keep='first').head(4)
    #plotting
    plot.plot(my_df["Country Name"], my_df["2000"])
    mng = plot.get_current_fig_manager()
    # mng.window.state('zoomed')
    plot.show()

def chart(location):
    #declaring x and y axis
    sns.boxplot(x='Country Name', y='2016', data=climate_data_1.loc[location].reset_index())
    #plotting
    plot.ylabel('CO2 emissions per capita (metric tons)')
    mng = plot.get_current_fig_manager()
    # mng.window.state('zoomed')
    plot.show()


def chart4():
    #Too much data, so only selecting few countries
    location = ['Antigua and Barbuda', 'Qatar', 'Romania', 'Russian Federation']
    climate_data_1.loc[location, '2015':].plot()
    #plotting
    plot.ylabel('Renewable energy consumption (% of total final energy consumption)')
    plot.show()

def chart5():
    #reading dataframe again to make another chart
    my_df = pd.read_csv('datasource.csv', skiprows=4)
    #removing duplicates to avoid access data
    my_df = my_df.drop_duplicates(subset=["Country Name"], keep='first').head(10)
    #selecting top 10 rows only as data size is way much large
    my_df.plot.bar(x="Country Name", y="2008", rot=70, title="Bar Graph")
    plot.show(block=True)


# two dataframes returning from function.
climate_data_1, climate_data_2 = read_file(input_path)
print(climate_data_1.loc[data, '2014'].describe())

# Plot 1 function call
chart(data)
# Plot 2 function call
chart2(data_2)

# Plot 4 function call
chart4()
# Plot 5 function call
chart5()