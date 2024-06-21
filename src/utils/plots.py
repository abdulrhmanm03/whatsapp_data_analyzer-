import matplotlib.pyplot as plt



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
