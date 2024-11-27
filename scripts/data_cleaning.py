import pandas as pd

data = pd.read_csv('/content/drive/MyDrive/911.csv')
df = pd.DataFrame(data)
df.head() 

def clean_data(df):
    """Clean the data and create new features."""
    # Convert 'timeStamp' to datetime
    df['timeStamp'] = pd.to_datetime(df['timeStamp'])
    
print(df['timeStamp'].dtype)

    # Create new columns for Hour, Month, Day of Week
    df['Hour'] = df['timeStamp'].dt.hour
    df['Month'] = df['timeStamp'].dt.month
    df['Day of Week'] = df['timeStamp'].dt.dayofweek

    # Map the Day of Week to actual names
    dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    df['day_of_week'] = df['Day of Week'].map(dmap)

    # Extract Reason from title
    df['Reasons'] = df['title'].apply(lambda x: x.split(':')[0])

    df.to_csv('/content/drive/MyDrive/cleaned_911_calls.csv', index=False) 
    