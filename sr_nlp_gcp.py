import speech_recognition as sr  
from time import time
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\GCDCDemo\IntelIoT-GCP-df28e0c7d9bb.json"
  
# obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
   print("Please wait. Calibrating microphone...")  
   # listen for 5 seconds and create the ambient noise energy level  
   r.adjust_for_ambient_noise(source, duration=5)  
   print("Say something!")  
   audio = r.listen(source)  

print("")
print("Speech Recognition:")


start_time = time()  
 # recognize speech using Sphinx  
try:  
   print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
except sr.UnknownValueError:  
   print("Sphinx could not understand audio")  
except sr.RequestError as e:  
   print("Sphinx error; {0}".format(e))  
end_time = time()
time_taken = end_time - start_time 
print ("Time required for Sphinx analysis: " + str(time_taken) + " sec")

start_time = time()
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said '" + r.recognize_google(audio) + "'")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
end_time = time()
time_taken = end_time - start_time 
#print ("Time required for Google Speech Recognition: " + str(time_taken) + " sec"
