import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/drive/MyDrive/911.csv')
df = pd.DataFrame(data)

def analyze_data(df):
    """Perform analysis on the cleaned data."""
    # Top 5 zip codes for 911 calls
    top5zip = df['zip'].value_counts().head()
    print("Top 5 Zipcodes for 911 calls:\n", top5zip)

    # Top 5 townships for 911 calls
    top5townships = df['twp'].value_counts().head()
    print("Top 5 Townships for 911 calls:\n", top5townships)

    # Unique title codes
    unique_titles = len(df['title'].unique())
    print("Number of Unique Title Codes:", unique_titles)

    # Countplot of 911 calls by Reason
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Reasons', data=df)
    plt.title('Count of 911 Calls by Reason')
    plt.show()

     # Count of calls per month
    by_month = df.groupby('Month').count()['twp']
    plt.figure(figsize=(10, 6))
    plt.plot(by_month)
    plt.title('911 Calls per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Calls')
    plt.show()

    # Heatmap for Day of Week vs Hour
    dayHour = df.groupby(by=['day_of_week', 'Hour']).count()['Reasons'].unstack()
    plt.figure(figsize=(12, 6))
    sns.heatmap(dayHour, cmap='viridis')
    plt.title('Heatmap of 911 Calls by Day of Week and Hour')
    plt.show()

    # Clustermap for Day of Week vs Hour
    sns.clustermap(dayHour, cmap='viridis')
    plt.title('Clustermap of 911 Calls by Day of Week and Hour')
    plt.show()

df.to_csv('/content/drive/MyDrive/analysed_911_calls.csv', index=False) 