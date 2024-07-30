import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

def load_data(file_path, sep=","):
    return pd.read_csv(file_path, sep=sep)

def inspect_data(df):
    print("First Few Rows:")
    print(df.head())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nBasic Statistics:")
    print(df.describe())
    print("\nData Types:") 
    print(df.dtypes)
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

def clean_data(df):
    df = df.dropna()  # Example: drop rows with missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df

def merge_data(df1, df2, df3):
    df_merged = df1.merge(df2, on='client_id', how='left').merge(df3, on='client_id', how='left')
    return df_merged

def handle_missing_values(df):
    df = df.fillna(method='ffill')  # Forward fill missing values
    return df

def ensure_correct_data_types(df):
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')
    print("\nData Types after Conversion:")
    print(df.dtypes)

def visualize_distributions(df):
    if 'clnt_age' in df.columns:
        sns.histplot(df['clnt_age'], kde=True)
        plt.title('Age Distribution of Clients')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("The 'clnt_age' column does not exist in the DataFrame.")

    sns.countplot(x='gendr', data=df)
    plt.title('Gender Distribution of Clients')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

def client_behavior_analysis(df):
    sns.histplot(df['clnt_tenure_mnth'], bins=9, kde=True)
    plt.title('Distribution of Customer Logins in the Last 6 Months')
    plt.xlabel('Months')
    plt.ylabel('Frequency')
    plt.show()

    sns.histplot(df['clnt_tenure_yr'], bins=6, kde=True)
    plt.title('Distribution of Customer Service Calls in the Last Years')
    plt.xlabel('Years')
    plt.ylabel('Frequency')
    plt.show()

def calculate_kpis(df):
    completion_rate = df.groupby('design')['completed'].mean()
    time_spent = df.groupby('design')['time_spent'].mean()
    error_rate = df.groupby('design')['errors'].mean()

    print("Completion Rate:")
    print(completion_rate)
    print("\nTime Spent on Each Step:")
    print(time_spent)
    print("\nError Rates:")
    print(error_rate)

    plt.figure(figsize=(10, 5))
    completion_rate.plot(kind='bar', title='Completion Rate')
    plt.xlabel('Design')
    plt.ylabel('Completion Rate')
    plt.show()

    plt.figure(figsize=(10, 5))
    time_spent.plot(kind='bar', title='Time Spent on Each Step')
    plt.xlabel('Design')
    plt.ylabel('Time Spent (seconds)')
    plt.show()

    plt.figure(figsize=(10, 5))
    error_rate.plot(kind='bar', title='Error Rates')
    plt.xlabel('Design')
    plt.ylabel('Error Rate')
    plt.show()

def hypothesis_testing(df):
    control_group = df[df['design'] == 'control']['completed']
    test_group = df[df['design'] == 'test']['completed']
    t_stat, p_value = ttest_ind(control_group, test_group)
    print(f"T-statistic: {t_stat}, P-value: {p_value}")
    if p_value < 0.05:
        print("Significant difference in completion rates between control and test groups.")
    else:
        print("No significant difference in completion rates between control and test groups.")

    control_successes = df[df['design'] == 'control']['completed'].sum()
    test_successes = df[df['design'] == 'test']['completed'].sum()
    control_total = df[df['design'] == 'control']['completed'].count()
    test_total = df[df['design'] == 'test']['completed'].count()

    z_stat, p_value = proportions_ztest([control_successes, test_successes], [control_total, test_total])
    print(f"Z-statistic: {z_stat}, P-value: {p_value}")

    threshold = 0.05
    control_rate = control_successes / control_total
    test_rate = test_successes / test_total
    pooled_rate = (control_successes + test_successes) / (control_total + test_total)
    se = (pooled_rate * (1 - pooled_rate) * (1/control_total + 1/test_total))**0.5
    z_stat_threshold = (test_rate - control_rate - threshold) / se
    p_value_threshold = 1 - stats.norm.cdf(z_stat_threshold)
    print(f"Z-statistic (threshold): {z_stat_threshold}, P-value (threshold): {p_value_threshold}")

    control_age = df[df['design'] == 'control']['age']
    test_age = df[df['design'] == 'test']['age']
    t_stat, p_value_age = stats.ttest_ind(control_age, test_age)
    print(f"T-statistic: {t_stat}, P-value: {p_value_age}")

def save_cleaned_data(df, file_path='clean.csv'):
    df.to_csv(file_path, index=False)
    print(f"{file_path} saved to CSV successfully.")
