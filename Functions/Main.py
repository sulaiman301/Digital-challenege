import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

def load_data(file_paths): 
    return [pd.read_csv(file, sep=",") for file in file_paths]

def inspect_data(dfs):
    for df in dfs:
        print(df.head())
        print(df.info())
        print(df.describe())
        print(df.isnull().sum())
        print(df.duplicated().sum())

def clean_data(dfs):
    cleaned_dfs = []
    for df in dfs:
        df = df.dropna().drop_duplicates()
        cleaned_dfs.append(df)
    return cleaned_dfs

def merge_data(df_demo, df_web_data, df_experiment):
    df_merged = df_web_data.merge(df_demo, on='client_id', how='left').merge(df_experiment, on='client_id', how='left')
    df_merged['date_time'] = pd.to_datetime(df_merged['date_time'], errors='coerce')
    return df_merged

def analyze_demographics(df_merged):
    sns.histplot(df_merged['clnt_age'], kde=True)
    plt.title('Age Distribution')
    plt.show()

    sns.countplot(x='gendr', data=df_merged)
    plt.title('Gender Distribution')
    plt.show()

def analyze_client_behavior(df_merged):
    plt.figure(figsize=(10, 5))
    sns.histplot(df_merged['clnt_tenure_mnth'], bins=9, kde=True)
    plt.title('Distribution of Customer Logins in the Last 6 Months')
    plt.xlabel('clnt_tenure_mnth')
    plt.ylabel('clnt_age')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(df_merged['clnt_tenure_yr'], bins=6, kde=True)
    plt.title('Distribution of Customer Service Calls in the Last years')
    plt.xlabel('clnt_tenure_yr')
    plt.ylabel('clnt_age')
    plt.show()

def calculate_kpis(df_merged):
    completion_rate = df_merged.groupby('design')['completed'].mean()
    time_spent = df_merged.groupby('design')['time_spent'].mean()
    error_rate = df_merged.groupby('design')['errors'].mean()
    
    print("Completion Rate:", completion_rate)
    print("Time Spent on Each Step:", time_spent)
    print("Error Rates:", error_rate)

    completion_rate.plot(kind='bar', title='Completion Rate')
    plt.xlabel('Design')
    plt.ylabel('Completion Rate')
    plt.show()

    time_spent.plot(kind='bar', title='Time Spent on Each Step')
    plt.xlabel('Design')
    plt.ylabel('Time Spent (seconds)')
    plt.show()

    error_rate.plot(kind='bar', title='Error Rates')
    plt.xlabel('Design')
    plt.ylabel('Error Rate')
    plt.show()

def hypothesis_testing(df_merged):
    control_group = df_merged[df_merged['design'] == 'control']['completed']
    test_group = df_merged[df_merged['design'] == 'test']['completed']
    t_stat, p_value = ttest_ind(control_group, test_group)
    print(f"T-statistic: {t_stat}, P-value: {p_value}")

    control_successes = control_group.sum()
    test_successes = test_group.sum()
    control_total = control_group.count()
    test_total = test_group.count()

    z_stat, p_value = proportions_ztest([control_successes, test_successes], [control_total, test_total])
    print(f"Z-statistic: {z_stat}, P-value: {p_value}")

    threshold = 0.05
    pooled_rate = (control_successes + test_successes) / (control_total + test_total)
    se = (pooled_rate * (1 - pooled_rate) * (1/control_total + 1/test_total))**0.5
    z_stat_threshold = (test_rate - control_rate - threshold) / se
    p_value_threshold = 1 - stats.norm.cdf(z_stat_threshold)
    print(f"Z-statistic (threshold): {z_stat_threshold}, P-value (threshold): {p_value_threshold}")

    control_age = df_merged[df_merged['design'] == 'control']['age']
    test_age = df_merged[df_merged['design'] == 'test']['age']
    t_stat, p_value_age = stats.ttest_ind(control_age, test_age)
    print(f"T-statistic: {t_stat}, P-value: {p_value_age}")

def experiment_evaluation(df_merged):
    print(df_merged['design'].value_counts())

    experiment_duration = df_merged['logins'].max() - df_merged['time_spent'].min()
    print(f"Experiment Duration: {experiment_duration}")

    additional_data_suggestions = [
        "User feedback on the new design",
        "More granular interaction data (e.g., clickstream data)",
        "Detailed demographic data (e.g., income, education level)"
    ]
    print("Additional Data Suggestions:", additional_data_suggestions)

def main():
    file_paths = [
        r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_demo.txt',
        r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_experiment_clients.txt',
        r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_web_data_pt_1.txt',
        r'C:\Users\User\Documents\IRON HACK DA 2024\Project Digital Challenge\New folder\Digital-challenege\DATA\raw\df_final_web_data_pt_2.txt'
    ]

    df_final_demo, df_final_experiment_clients, df1, df2 = load_data(file_paths)
    df_combined = pd.concat([df1, df2])

    dfs = [df_final_demo, df_combined, df_final_experiment_clients]
    inspect_data(dfs)

    cleaned_dfs = clean_data(dfs)
    df_demo, df_web_data, df_experiment = cleaned_dfs

    df_merged = merge_data(df_demo, df_web_data, df_experiment)
    analyze_demographics(df_merged)
    analyze_client_behavior(df_merged)
    calculate_kpis(df_merged)
    hypothesis_testing(df_merged)
    experiment_evaluation(df_merged)

    df_merged.to_csv('clean.csv', index=False)
    print("clean.csv saved to CSV successfully.")

if __name__ == "__main__":
    main()

    