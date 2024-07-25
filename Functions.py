## Load and Explore the Datasets
import pandas as pd
import seaborn as sns
#Digital footprints # Read data

file_final_demo =r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_demo.txt'
file_experiment_clients =r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_experiment_clients.txt'


file_path_1= r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_web_data_pt_1.txt'
file_path_2= r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_web_data_pt_2.txt'

#Inspect the datasets:   Check for missing values, data types, and basic statistics.
pd.read_csv(file_final_demo, sep=",")
df_final_demo = pd.read_csv(file_final_demo, sep=",")
df_final_experiment_clients= pd.read_csv(file_experiment_clients, sep=",")

#Merge Digital Footprints.

#Combine the two parts of the digital footprints dataset.
df1=pd.read_csv(r"C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_web_data_pt_1.txt")
df2=pd.read_csv(r"C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_web_data_pt_2.txt")
#combined the data
df_combined = pd.concat([df1, df2])
df_combined

 ## Exploring the data & Clean the Data
Handle missing values, outliers, and any inconsistencies in the data.
df_final_demo.head()
df_final_experiment_clients.head()
df_combined.head()

# Check for missing values
print(df_final_demo.isnull().sum())
print(df_combined.isnull().sum())
print(df_final_experiment_clients.isnull().sum())

# Handle missing values (e.g., fill, drop, or impute)
df_demo = df_final_demo.dropna()  # Example: drop rows with missing values
df_web_data = df_combined.fillna(method='ffill')  # Example: forward fill missing values
df_experiment = df_final_experiment_clients.dropna()  # Example: drop rows with missing values

# Check for duplicates
print(df_final_demo.duplicated().sum())
print(df_combined.duplicated().sum())
print(df_final_experiment_clients.duplicated().sum())

# Remove duplicates if any
df_demo = df_final_demo.drop_duplicates()
df_web_data = df_combined.drop_duplicates()
df_experiment = df_final_experiment_clients.drop_duplicates()

import matplotlib.pyplot as plt

print(df_demo.describe())
print(df_web_data.describe())
print(df_experiment.describe())
print(df_demo.columns)
print(df_demo.columns)

# Verify column names
print("Column Names:", df_final_demo.columns)

# Inspect the first few rows
print("First Few Rows:")
print(df_final_demo.head())

df_demo

# Check for the presence of the 'clnt_age' column and plot
if 'clnt_age' in df_final_demo.columns:
    sns.histplot(df_final_demo['clnt_age'], kde=True)
    plt.title('Age Distribution of Clients')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("The 'clnt_age' column does not exist in the DataFrame.")

# Gender distribution
sns.countplot(x='gendr', data=df_demo)
plt.title('Gender Distribution of Clients')
plt.xlabel('gender')
plt.ylabel('Count')
plt.show()



# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 30, 10, 25]
}
df = pd.DataFrame(data)

# Summary statistics
summary_stats = df.describe()
print(summary_stats)

# Pivot table to summarize data
pivot_table = pd.pivot_table(df, values='Value', index='Category', aggfunc=['mean', 'sum'])
print(pivot_table)

# Custom summary function
def custom_summary(group):
    return pd.Series({
        'Count': group.count(),
        'Sum': group.sum(),
        'Mean': group.mean()
    })

custom_summary_table = df.groupby('Category')['Value'].apply(custom_summary).unstack()
print(custom_summary_table)

from IPython.display import display

# Displaying the summaries
display(summary_stats)
display(grouped_summary)
display(pivot_table)
display(custom_summary_table)

## Week 5, Day 1 & 2: EDA & Data Cleaning
# #For the project requirements and instructions for today’s tasks in full, please refer to the project brief. However, in order to keep on track you may refer to the daily goals outlined below:

# By the end of the first two days, we recommend you have:

# Done dataset discovery: Understood the nature and structure of your datasets using Python with libraries such as Pandas, Matplotlib, and Seaborn.

# Carried out data cleaning and fix any problems if there are any.

# Answered the following questions about demographics:

# Who are the primary clients using this online process?
# Are the primary clients younger or older, new or long-standing?

# Carried out a client behaviour analysis to answer any additional relevant questions you think are important.
## Merge Data:
df_demo
df_web_data
df_experiment

# Initial Inspection:
print(df_merged.head())
print(df_merged.info())
print(df_merged.describe())

# Data Cleaning:

Missing Values:
#  Handle missing values appropriately
df_merged.isnull().sum()


# Duplicates

df_merged =df_merged.drop_duplicates()

# Data Types : # Convert other columns if necessary
df_merged['date_time'] = pd.to_datetime(df_merged['date_time'])


df_merged['date_time'] = pd.to_numeric(df_merged['date_time'], errors='coerce')

# Check Data Types:
print(df_merged.dtypes)

df_merged
##  Demographics Analysis

# 1 Who are the primary clients using this online process?

# Visualize Distributions:
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df_merged['clnt_age'], kde=True)
plt.title('Age Distribution')
plt.show()

sns.countplot(x='gendr', data=df_merged)
plt.title('Gender Distribution')
plt.show()


# Account type distribution
sns.countplot(x='num_accts', data=df_merged)
plt.title('Account Type Distribution')
plt.show()

# 2.  Are the primary clients younger or older, new or long-standing?
# Age groups: younger vs older
younger_clients = df_merged[df_merged['clnt_age'] < df_merged['clnt_age'].median()]
older_clients = df_merged[df_merged['clnt_age'] >= df_merged['clnt_age'].median()]


print (younger_clients)
print(older_clients)

# New vs long-standing clients
new_clients = df_merged[df_merged['clnt_age'] < df_merged['clnt_age'].median()]
long_standing_clients = df_merged[df_merged['clnt_age'] >= df_merged['clnt_age'].median()]

print(new_clients)
print(long_standing_clients)

sns.histplot(younger_clients['clnt_age'], kde=True, color='blue', label='Younger Clients')
sns.histplot(older_clients['clnt_age'], kde=True, color='red', label='Older Clients')
plt.title('Age Distribution: Younger vs Older Clients')
plt.legend()
plt.show()

sns.histplot(new_clients['clnt_age'], kde=True, color='green', label='New Clients')
sns.histplot(long_standing_clients['clnt_age'], kde=True, color='purple', label='Long-Standing Clients')
plt.title('Account Age Distribution: New vs Long-Standing Clients')
plt.legend()
plt.show()

df_Merged = df_merged.merge(df_demo, on='client_id', how='left').merge(df_experiment, on='client_id', how='left')
## Client Behavior Analysis

Interaction Patterns:
import matplotlib.pyplot as plt

# Plot Distribution of Logins
plt.figure(figsize=(10, 5))
sns.histplot(df_merged['clnt_tenure_mnth'], bins=9, kde=True)
plt.title('Distribution of Customer Logins in the Last 6 Months')
plt.xlabel('clnt_tenure_mnth')
plt.ylabel('clnt_age')
plt.show()

# Plot Distribution of Calls
plt.figure(figsize=(10, 5))
sns.histplot(df_merged['clnt_tenure_yr'], bins=6, kde=True)
plt.title('Distribution of Customer Service Calls in the Last years')
plt.xlabel('clnt_tenure_yr')
plt.ylabel('clnt_age')
plt.show()
## Day 3 (Week 5): KPIs & Metrics

## Hypothesis 

# 1 Completion Rate
# To test if the difference in completion rate between the test and control groups is statistically significant, we can use a two-proportion z-test.

# Null Hypothesis (H0): The completion rate for the control group is equal to the completion rate for the test group.
# Alternative Hypothesis (H1): The completion rate for the control group is not equal to the completion rate for the test group.

# 2 Completion Rate with a Cost-Effectiveness Threshold
# To test if the observed increase in completion rate from the A/B test meets or exceeds the 5% threshold, we can again use a two-proportion z-test but with a specific threshold.

# Null Hypothesis (H0): The completion rate for the test group is less than or equal to the completion rate for the control group plus 5%.
# Alternative Hypothesis (H1): The completion rate for the test group is greater than the completion rate for the control group plus 5%.

# 3 Other Hypothesis Example
# Let's test whether the average age of clients engaging with the new process is the same as those engaging with the old process using a two-sample t-test.

# Null Hypothesis (H0): The average age of clients is the same for the control and test groups.
# Alternative Hypothesis (H1): The average age of clients is different for the control and test groups.


# Tasks:

# Review KPIs and Metrics:

# Understand the concepts and importance of KPIs and metrics in evaluating performance.
# Identify Success Indicators:

# Define KPIs like completion rate, time spent on each step, and error rates.
# Identify any additional relevant KPIs.
# Redesign Outcome:

# nalyze the data to determine if the new design improves the KPIs.
print(df_merged.columns)

# Verify Column Names and Merge Datasets
# Ensure that the merging and data cleaning steps correctly include all necessary columns. Here’s the corrected and detailed merging process:

import pandas as pd

# Sample data for demonstration (replace with actual data)
data_demo = {'client_id': [1, 2, 3, 4, 5], 'age': [25, 30, 35, 40, 45], 'gender': ['M', 'F', 'M', 'F', 'M']}
data_experiment = {'client_id': [1, 2, 3, 4, 5], 'design': ['control', 'control', 'test', 'test', 'control']}
data_web = {'client_id': [1, 2, 3, 4, 5], 'logins': [10, 15, 10, 5, 8], 'calls': [3, 4, 2, 1, 5], 'completed': [1, 1, 0, 1, 0], 'time_spent': [300, 320, 310, 250, 260], 'errors': [0, 1, 2, 0, 1]}

df_demo = pd.DataFrame(data_demo)
df_experiment = pd.DataFrame(data_experiment)
df_web_data = pd.DataFrame(data_web)

# Merge the DataFrames
df_merged = df_experiment.merge(df_demo, on='client_id', how='left').merge(df_web_data, on='client_id', how='left')

# Check the merged DataFrame
print(df_merged.head())

# Calculate KPIs
completion_rate = df_merged.groupby('design')['completed'].mean()
time_spent = df_merged.groupby('design')['time_spent'].mean()
error_rate = df_merged.groupby('design')['errors'].mean()



# Print KPIs
print("Completion Rate:")
print(completion_rate)
print("\nTime Spent on Each Step:")
print(time_spent)
print("\nError Rates:")
print(error_rate)

# Completion Rate
plt.figure(figsize=(10, 5))
completion_rate.plot(kind='bar', title='Completion Rate')
plt.xlabel('Design')
plt.ylabel('Completion Rate')
plt.show()

# Time Spent
plt.figure(figsize=(10, 5))
time_spent.plot(kind='bar', title='Time Spent on Each Step')
plt.xlabel('Design')
plt.ylabel('Time Spent (seconds)')
plt.show()


# Error Rate
plt.figure(figsize=(10, 5))
error_rate.plot(kind='bar', title='Error Rates')
plt.xlabel('Design')
plt.ylabel('Error Rate')
plt.show()

# Step 3: Interpret Results
# Here is an example of how you might interpret the results based on the visualizations and printed KPIs:

# Completion Rate:

# If the completion rate is higher for the test group, it indicates that the new design helps more users complete the process.
# Time Spent on Each Step:

# If the average time spent on each step is lower for the test group, it suggests that the new design is more efficient and helps users navigate through the steps more quickly.
# Error Rates:

# If the error rate is lower for the test group, it indicates that users are experiencing fewer issues and are less confused by the new design.
# Day 4 & 5 (Week 5): Hypothesis Testing & Experiment Evaluation
# Tasks:

# Hypothesis Testing:

# Conduct hypothesis tests to compare the old and new designs.
# Test for completion rates, cost-effectiveness, and other relevant metrics.
# Experiment Evaluation:

# Assess the overall design effectiveness.
# Evaluate the duration of the experiment.
# Identify any additional data needs for future experiments.
# 1. Hypothesis Testing for Completion Rate:

from scipy.stats import ttest_ind

# Hypothesis Testing for Completion Rate
control_group = df_merged[df_merged['design'] == 'control']['completed']
test_group = df_merged[df_merged['design'] == 'test']['completed']
t_stat, p_value = ttest_ind(control_group, test_group)

print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Interpret results
if p_value < 0.05:
    print("Significant difference in completion rates between control and test groups.")
else:
    print("No significant difference in completion rates between control and test groups.")

# Two-sample t-test for average age
control_age = df_merged[df_merged['design'] == 'control']['age']
test_age = df_merged[df_merged['design'] == 'test']['age']
t_stat, p_value_age = ttest_ind(control_age, test_age)
print(f"T-statistic: {t_stat}, P-value: {p_value_age}")

df_merged
# Experiment Evaluation
# Assess Duration of the Experiment:

# Make sure to use the correct columns for the dates:

# Example: Assess the duration of the experiment
experiment_duration = df_merged['logins'].max() - df_merged['time_spent'].min()
print(f"Experiment Duration: {experiment_duration}")
