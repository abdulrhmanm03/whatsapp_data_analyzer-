import re
import pandas as pd
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




def encode_fig(fig, dpi = 300):
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', dpi = dpi)
    buffer.seek(0)
    encoded_fig = base64.b64encode(buffer.read()).decode('utf-8')
    return encoded_fig  
