import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
reader = PyPDF2.PDF
speaker.setProperty('rate',100)

speaker.runAndWait()
