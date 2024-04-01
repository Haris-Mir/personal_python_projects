#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:33:44 2024

@author: harismir
"""
# Related libraries
from gtts import gTTS
import os

# Program 4: Text to speech function. To be used to save audio files as needed. 
# I am using (Google Text-to-Speech) library in Python to generate text-to-speech audio files. 

# Set up the text to be converted to speech
text = "I'm not sure how to help with that. Let me transfer you to customer support. Is that okay?"
        #"It seems like a product support query. I am putting you through to the product support section. Is that ok with you?"
        #"It seems like a sales query. I am putting you through to the sales section. Is that ok with you?"
        #"It seems like a billing query. I am putting you through to the billing section. Is that ok with you?"
        #"I'm sorry, I didn't understand that. I am putting you through to our team member for further assistance. Is that ok with you?"
        #"I am sorry to hear that. I will put you through to our team member for further assistance. Is that ok with you?"
        #"Welcome to ABC telecommunication services, how may I help you today?"

# Create a gTTS object and set the language and slow parameter
speech = gTTS(text=text, lang='en-us', tld ='co.in', slow=False) #tld ='co.in'

# Save the audio data to a temporary file
speech.save("temp.mp3")

# Convert the temporary file to a .wav file using ffmpeg
os.system("ffmpeg -y -i temp.mp3 -f wav -acodec pcm_s16le customer_support.wav")

# Remove the temporary file
os.remove("temp.mp3")