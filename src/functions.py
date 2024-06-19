import re
import pandas as pd
import matplotlib.pyplot as plt


def file_to_pd_frame(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            chat_data = file.readlines()
    except Exception as e:
        return f'Failed to load file: {e}'     
    
    pattern = r'(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}\u202F(?:am|pm)) - ([\w\s]+): (.*)'
    message_regex = re.compile(pattern)
    
    messages = []
    
    for line in chat_data:
        match = message_regex.match(line)
        if match:
            date, time, sender, message = match.groups()
            messages.append([date, time, sender, message])
            
    df = pd.DataFrame(messages, columns=['Date', 'Time', 'Sender', 'Message'])
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    return df       



def time_plot(df):
    plt.figure(figsize=[10, 5])
    
    senders = df['Sender'].unique()
    for sender in senders:
        filter = (df['Sender'] == sender)
        s = df.loc[filter, 'Date']
        s = s.reset_index().drop(['index'], axis=1)
        
        plt.plot(s['Date'], s.index, label=sender) 
    
    plt.legend(loc='upper left')    
    plt.title("Messages sent over time")
    plt.xlabel("Time")
    plt.xticks(rotation=45)
    plt.ylabel("Number of messages")    
    plt.grid(True)  
    plt.tight_layout() 
    plt.box(False) 
    
    
def bar_plot(df):
    x = df['Sender'].value_counts()
    plt.figure(figsize=[8, 5])
    plt.title("Messages sent over time")
    plt.xlabel("members")
    plt.ylabel("Number of messages")    
    plt.bar(x.index, x.values, color='orange')
    plt.xticks(rotation=30)
    plt.tight_layout() 
    plt.box(False)    
        
        
def pie_plot(df):
    x = df['Sender'].value_counts()
    plt.figure(figsize=[5, 5])
    plt.title("Messages sent")  
    plt.pie(x.values, labels=x.index)
    plt.tight_layout()         
       