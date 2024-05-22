import pyttsx3 as pysx3
from googletrans import Translator
import PyPDF2 as pypdf
from gtts import gTTS
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from pocketsphinx import LiveSpeech, get_model_path
from scipy.io.wavfile import write

engine = pysx3.init()

def summarize_text(text):
    nltk.download('stopwords')  
    nltk.download('punkt')
    # Tokenizing
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict() #freqTable = frequency of words in a text
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)#create dictionary to store text
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))#average val

    summary = '' #storing sentences using summary
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    return summary


def speak(text):
    engine.say(text)
    engine.runAndWait()

def translate(text="Hello", text_language="en", language_to_translate_to="de"):
    translator = Translator()
    result = translator.translate(text, src=text_language, dest=language_to_translate_to)
    speak(result.text)

def read_pdf_out(path_to_pdf):
    with open(path_to_pdf, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            text = pdf_reader.pages[page_num].extract_text()

            speak(text)
        
        engine.runAndWait()

def save_audio(text, language, output_path, file_name):
    tts = gTTS(text=text, lang=language)
    file_path = os.path.join(output_path, file_name)
    tts.save(file_path)

def summarize_and_read_out(text_to_summarize):
    speak(summarize_text(text_to_summarize))

