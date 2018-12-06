# Speech-To-text-Converter
Library for performing speech recognition, with support for several engines and APIs, online and offline.

**Speech recognition engine/API support:**

CMU Sphinx (works offline)
Google Speech Recognition
Google Cloud Speech API
Wit.ai
Microsoft Bing Voice Recognition
Houndify API
IBM Speech to Text
Snowboy Hotword Detection (works offline)
Quickstart: pip install SpeechRecognition. 

To quickly try it out, run python -m speech_recognition after installing.

Examples
See the examples/ directory in the repository root for usage examples:

Recognize speech input from the microphone
Transcribe an audio file
Save audio data to an audio file
Show extended recognition results
Calibrate the recognizer energy threshold for ambient noise levels (see recognizer_instance.energy_threshold for details)
Listening to a microphone in the background
Various other useful recognizer features
Installing
First, make sure you have all the requirements listed in the "Requirements" section.

The easiest way to install this is using pip install SpeechRecognition.

Otherwise, download the source distribution from PyPI, and extract the archive.


**Requirements**

To use all of the functionality of the library, you should have:

Python 2.6, 2.7, or 3.3+ (required)
PyAudio 0.2.11+ (required only if you need to try microphone input, Microphone)
PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X)
