# I have created an IVR System for a telco company called ABC Telecommuncation Services. 
# The program can cater 3 intents "sales", "billing", and "product support"
# The suggested phrases are as follows:
# Negative: I want to cancel my existing service.
# Negative: My phone's connect is quite slow. what to do?
# Positive: I would like to upgrade my plan.
# Positive: I want to buy a new smartphone.


# Libraries
import sounddevice as sd
import scipy.io.wavfile as wavfile
import soundfile as sf
import datetime

# LLM Libraries
from transformers import pipeline
import ollama


# Function 1: Play Audio
def play_audio(file_name):
    # Load data
    fs, data = wavfile.read(file_name)
    # Play data
    sd.play(data, fs)
    status = sd.wait()
    

# Function 2: Record Audio
def record_audio():
    # Define the duration of the recording in seconds
    duration = 3  # seconds
    # Define the sampling frequency
    fs = 44100  # Hz
    # Start recorder with the given sampling frequency and channels as input
    # The default input device will be used
    print("Recording Audio Now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    # Record audio for the given number of frames
    sd.wait()  # Wait until recording is finished
    # Stop recorder
    sd.stop()
    print("Audio Recording Complete!")
    # Save the recording to a .wav file
    sf.write('recorded_audio.wav', recording, fs)
    

# Speech recognition with Whisper pipeline
transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-small")

# Function 4: Speech recognition with Whisper
def speech_recognition(file_name):
    result = transcriber(file_name)
    #print(result)
    text = result['text']
    return text


# Program 6: LLMs for Identifying sentiment analysis (Positive/Negative)
# Initialize the text classification pipeline
classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")

# Function 6:
def classify(transcribed_text):
    # Classify the intent of the transcribed text   
    classification_pred = classifier(transcribed_text)[0]
    print(classification_pred)
    return classification_pred['label']  # Return the label for decision making
    

# Function 7: ollama model for intent identification 
def ollama_model(text):
    # Construct the few-shot learning prompt
    prompt = """
    Customer: I would like to buy a new smartphone.
    Assistant: This is a billing query, I will put you through to our billing team. Is that what you want me to do?

    Customer: Can you tell me about the latest smartphones available?
    Assistant: This is a sales query, I will put you through to our sales team. Is that ok with you?

    Customer: How can I upgrade to a 5G plan?
    Assistant: This is a product support query, I will put you through to our product support team. Is that ok with you?

    Customer: {}
    Assistant: Select the main category that the customer's query is based on. It could be either of the three main categories: product support, sales, or billing.
    """.format(text)


    #Initiate the model
    response = ollama.generate(model='gemma:2b', prompt=prompt)['response']  # + text

    return response #OUTPUT: The customer expressed a desire to inquire about new plans being offered. The assistant should categorize the query as a sales query and provide the customer with information about the latest smartphones available and upgrade options.


## Function 8: Keyword search
category_keywords = {
    "billing": ["bill", "billing", "payment", "invoice", "charge"],
    "sales": ["smartphone", "mobile", "phone", "purchase", "buy", "sales", "upgrade", "plan", "offer"],
    "product support": ["product", "support", "service", "5G", "4G", "internet", "technical"]
}

def categorize_and_respond(output_text):
    # Initialize a variable to store the identified category
    identified_category = None

    # Iterate over each category and its keywords
    for category, keywords in category_keywords.items():
        # Check if any keyword appears in the output text
        if any(keyword.lower() in output_text.lower() for keyword in keywords):
            identified_category = category
            break  # Stop searching once a category has been identified
    
    print(identified_category)     
    return identified_category
        
# Function 9: to append text to a log file
def append_to_log(file_name, text):
    # Get current timestamp to prepend to the log entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Open the log file in append mode
    with open(file_name, "a") as log_file:
        # Write the timestamp and the transcribed text to the log file
        log_file.write(f"{timestamp}: {text}\n")


# Main Function
def main():

    play_audio("greeting.wav")
    record_audio()

    transcribed_text = speech_recognition("recorded_audio.wav")
    print(transcribed_text)

    # Append the transcribed text to a log file
    append_to_log("log.txt", transcribed_text)

    sentiment_label = classify(transcribed_text)  # Get sentiment label

     # Decision making based on sentiment
    if sentiment_label == "LABEL_0":  # Negative
        play_audio("complaint_portal.wav")
        print("I am sorry to hear that. I will put you through to our team member for further assistance. Is that ok with you?")
    elif sentiment_label == "LABEL_1":  # Neutral
        play_audio("neutral.wav")
        print("I'm sorry, I didn't understand that. I am putting you through to our team member for further assistance. Is that ok with you?")
    elif sentiment_label == "LABEL_2":  # Positive
        response = ollama_model(transcribed_text)  # Get ollama model response
        identified_category = categorize_and_respond(response)  # Categorize ollama response and play corresponding audio

        # Based on the identified category, play the corresponding audio file
        if identified_category == "billing":
            print("It seems like a billing query. I am putting you through to the billing section. Is that ok with you?")
            play_audio("billing.wav")
        elif identified_category == "sales":
            print("It seems like a sales query. I am putting you through to the sales section. Is that ok with you?")
            play_audio("sales.wav")
        elif identified_category == "product support":
            print("It seems like a product support query. I am putting you through to the product support section. Is that ok with you?")
            play_audio("product_support.wav")
        else:
            print("I'm not sure how to help with that. Let me transfer you to customer support.")
            play_audio("customer_support.wav")  # An audio file for cases where the category isn't identified

    record_audio()

    next_transcribed_text = speech_recognition("recorded_audio.wav")
    print(next_transcribed_text)

    # Append the transcribed text to a log file
    append_to_log("log.txt", next_transcribed_text)

    next_sentiment_label = classify(next_transcribed_text)  # Get sentiment label

    if next_sentiment_label == "LABEL_0":  # Negative
        print("CONFUSED!")
    elif next_sentiment_label == "LABEL_1":  # Neutral
        print("CONFUSED!")
    elif next_sentiment_label == "LABEL_2":  # Positive
        print('INTENT!')

if __name__ == "__main__":
    main()
