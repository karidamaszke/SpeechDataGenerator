# SpeechDataGenerator

The aim of this project was to create a tool which allows to record audio data for SpeechToText models, e.g. [DeepSpeech](https://github.com/mozilla/DeepSpeech).
It provides data as WAV files with 16kHz sampling ratio and CSV file organized as follow:


**wav file name | size of wav file | transcription**

Feel free to modify the [CommandGenerator](command_generator.py) class in order to meet your project requirements.
