import re
import pandas as pd
import matplotlib.pyplot as plt
import io, base64


def file_to_pd_frame(decoded_file): 
    
    lines = decoded_file.splitlines()   
    
    pattern = r'(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}\u202F(?:am|pm)) - ([\w\s]+): (.*)'
    message_regex = re.compile(pattern)
    
    messages = []
    
    for line in lines:
        match = message_regex.match(line)
        if match:
            date, time, sender, message = match.groups()
            messages.append([date, time, sender, message])
            
    df = pd.DataFrame(messages, columns=['Date', 'Time', 'Sender', 'Message'])
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    return df       



def time_plot(df):
    fig, ax = plt.subplots(figsize=[10, 5])
    
    senders = df['Sender'].unique()
    for sender in senders:
        
        sender_df = df[df['Sender'] == sender]
        data = sender_df['Date'].reset_index(drop=True)
        x = data
        y = data.index
        
        ax.plot(x, y, label=sender)
        
    
    ax.legend(loc='upper left')
    
    ax.set_title("Messages sent over time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of messages")
    
    ax.grid(True)
    ax.tick_params(axis='x', rotation=45)
    ax.set_frame_on(False)
    
    fig.tight_layout()
    
    return fig
  
        
        
def pie_plot(df):
    x = df['Sender'].value_counts()

    fig, ax = plt.subplots(figsize=[5, 5])
    ax.set_title("Messages sent")
    ax.pie(x.values, labels=x.index)

    fig.tight_layout()    
      
    return fig 


def encode_fig(fig, dpi = 300):
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', dpi = dpi)
    buffer.seek(0)
    encoded_fig = base64.b64encode(buffer.read()).decode('utf-8')
    return encoded_fig  
