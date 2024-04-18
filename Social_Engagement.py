# importing relevant libraries
import pandas as pd

from openai import OpenAI

# API key
OPENAI_API_KEY = 'your_key_here'

# context for assistant
context = 'Your name is Dr. Ed Sykes, you are an ' \
            'Educational Psychologist producing statutory assessments ' \
            'for a local authority. You\'re currently working on a section ' \
            'about Social Engagement. You will receive 3 previous ' \
            'examples of your work with \'>\' as a delimiter to ' \
            'remind you of the required writing style, followed by some ' \
            'bullet points for you to create a new Social Engagement section ' \
            'for a different child. Subjects in these reports are referred to by their ' \
            'first or first and last initials. '

# Training data ingestion and separation, this is a csv containing responses to different sections of several example statutory reports
data = pd.read_csv('data.csv')
social_engagement_training_data = data.loc[data.Field == 'Social Engagement'].Response.tolist()

data = 'You need only reply \'Ready\' to this message and then I will give ' \
        'you the prompt. Pay attention to format and writing style. \n'

for response in social_engagement_training_data:
    data += response + '> '

# Creation of prompt, this is notes that the Ed Psych would produce after assessing the CYP.  
prompt = '''
            your_notes_here
            '''
            # Eg. '''lacks rapport with staff. Takes long time to build relationships and can lose these quickly if encountering issues.
            # Has some relationships with friends but quick to lose them when encountering difficulties, struggles with repairing relationships. 
            # Doesn't recognise subtleties in social communication (e.g. that people are teasing, changes to body langauge etc.)
            # Doesn't recognise different behaviours needed for different recipients/audiences.'''

# OpenAI client instance creation
client = OpenAI(
api_key = OPENAI_API_KEY
)

# Calling API to get response to prompt
response = client.chat.completions.create(
    model="gpt-4-turbo-2024-04-09",
    messages=[
        {"role": "system", "content": context},
        {"role": "user", "content": data},
        {"role": "assistant", "content": "Ready"},
        {"role": "user", "content": prompt}
    ],
)

# displaying response from chatGPT
print(response.choices[0].message.content)