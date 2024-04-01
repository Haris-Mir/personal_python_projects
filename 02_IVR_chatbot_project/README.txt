## Part 2 Task

medium blog: 

Pick one of the interactions from Part 1 and implement it, using audio input and output on your computer. Instead of putting you into a telephone queue (or doing some other action), the program will just print out the queue/action it would have done. There is a step-by-step breakdown and marking rubric later in this document.

Step-by-step breakdown

Start by writing a program that can play audio through the speakers (or headphones). Test that the system audio is enabled. There are many dfferent audio file formats (MP3, WAV, AU); if you need to, ask ChatGPT for ways to load these files into a format that your program can use. I found the sounddevice library easy to set up and use. If you get stuck, just print something out with print() and use it as a placeholder.

Then write a program that can record 3 seconds of audio. I found it helpful to print something out to mark the time that it started recording, and then print something out 3 seconds later. If you get stuck, record some audio samples on your phone and copy them on to your computer.

Write a program that takes an audio  le and transcribes it. This is a handy little program to have around anyway; I write a lot of stu  using speech recognition nowadays. If you get stuck, you can use input() and have someone type the transcript in instead.

Record some audio files in your best sounding voice (or get someone else to do it, find a text-to-speech system or find some samples on the internet). You'll need a greeting, and a confirmation message for each dfferent intent.

Play around with a few different (local) generative language models. This will involve a lot of downloading and waiting, so do this somewhere where you have a lot of band-width. (Or when you have a lot of chores to do.) Come up with a prompt that includes some examples and make sure that it works with your intents. Once you have that figured out, turn it into a program that prints out what the language model returned.

Now modify that program so that you can identify the intent that is being mentioned in the output. Maybe you will look for a keyword being used. You can see whether the model has a JSON mode. That might make it easier to process the model's output. Remember that these generative language models aren't always super-reliable, so don't stress out if you can't get something to work 100% of the time. 80% is good enough for this project. Also, don't stress out if it takes a long time to run. It's easier for debugging if you can make it faster (you could see if there's a streaming mode... maybe you can stop processing after a few tokens).

