# -*- coding: utf-8 -*-
"""Task_2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y5tTlxsC-qOkYaWzmvWy6ym4tNKBQpJv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
  file_path = '/content/Al_Amin_Process_Efficiency_and_Resource_Utilization_Simulation.csv'

# 1. Data Import and Cleaning
def import_and_clean_data(file_path):
    # Import the CSV file
    data = pd.read_csv(file_path)

    # Replace missing values with the median of the corresponding column
    for column in data.select_dtypes(include=[np.number]):
        median_value = data[column].median()
        data[column].fillna(median_value, inplace=True)

    return data
def main():
  file_path = '/content/Al_Amin_Process_Efficiency_and_Resource_Utilization_Simulation.csv'

# 1. Data Import and Cleaning
def import_and_clean_data(file_path):
    # Import the CSV file
    data = pd.read_csv(file_path)

    # Replace missing values with the median of the corresponding column
    for column in data.select_dtypes(include=[np.number]):
        median_value = data[column].median()
        data[column].fillna(median_value, inplace=True)

    return data

# 2. Basic Analysis
def calculate_average_processing_time(data):
    return data.groupby('Task_ID')['Processing_Time (min)'].mean()

def compute_resource_utilization(data):
    total_time = data['Processing_Time (min)'].sum()
    utilization = (data.groupby('Resource_Usage (%)')['Processing_Time (min)'].sum() / total_time) * 100
    return utilization

def identify_highest_resource_consumption(data):
    resource_usage = data.groupby('Task_ID')['Processing_Time (min)'].sum()
    return resource_usage.idxmax(), resource_usage.max()

# 3. Trend Analysis
def compare_processing_times(data):
    return data.groupby('Task_Category')['Processing_Time (min)'].mean()

def group_tasks_by_resource_usage(data):
    usage = data.groupby('Task_ID')['Processing_Time (min)'].sum()
    categories = pd.cut(usage, bins=3, labels=['Low', 'Medium', 'High'])
    return usage.groupby(categories).mean()

# 4. Visualization
def create_visualizations(data):
    # Bar chart: Processing times across tasks
    avg_processing_time = calculate_average_processing_time(data)
    avg_processing_time.plot(kind='bar', title='Average Processing Time by Task', xlabel='Task', ylabel='Time (s)')
    plt.show()

    # Line chart: Resource utilization trends
    resource_utilization = compute_resource_utilization(data)
    resource_utilization.plot(kind='line', title='Resource Utilization Trends', xlabel='Resource', ylabel='Utilization (%)')
    plt.show()

    # Pie chart: Resource usage distribution
    resource_usage = data.groupby('Resource_Usage (%)')['Processing_Time (min)'].sum()
    resource_usage.plot(kind='pie', title='Resource Usage Distribution', autopct='%1.1f%%')
    plt.ylabel('')
    plt.show()

# Main Function
def main():
    # File path to the CSV file
    file_path = '/content/Al_Amin_Process_Efficiency_and_Resource_Utilization_Simulation.csv'

    # Step 1: Data Import and Cleaning
    data = import_and_clean_data(file_path)

    # Step 2: Basic Analysis
    print("Average Processing Time by Task:")
    print(calculate_average_processing_time(data))

    print("\nResource Utilization Rates (%):")
    print(compute_resource_utilization(data))

    highest_task, highest_time = identify_highest_resource_consumption(data)
    print(f"\nTask with Highest Resource Consumption: {highest_task} ({highest_time}s)")

    # Step 3: Trend Analysis
    print("\nAverage Processing Times by Task Category:")
    print(compare_processing_times(data))

    print("\nResource Usage Grouped by Levels:")
    print(group_tasks_by_resource_usage(data))

    # Step 4: Visualization
    create_visualizations(data)

if __name__ == "__main__":
    main()