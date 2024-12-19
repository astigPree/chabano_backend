import os
# import pandas as pd
# import torch
from transformers import MarianMTModel, MarianTokenizer
# from sklearn.model_selection import train_test_split
import threading

mypath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model_selection') 

tagalog_english_model = None
tagalog_english_tokenizer = None
def load_tagalog_english_model():
    global tagalog_english_model, tagalog_english_tokenizer
    try :
        tagalog_english_model = MarianMTModel.from_pretrained(os.path.join(mypath, 'tagalog-english'))
        tagalog_english_tokenizer = MarianTokenizer.from_pretrained(os.path.join(mypath, 'tagalog-english'))
    except Exception as e:
        print(f"Failed to load Tagalog to English model: {e}")
threading.Thread(target=load_tagalog_english_model).start()


english_tagalog_model = None
english_tagalog_tokenizer = None
def load_english_tagalog_model():
    global english_tagalog_model, english_tagalog_tokenizer
    try :
        english_tagalog_model = MarianMTModel.from_pretrained(os.path.join(mypath, 'tagalog-english'))
        english_tagalog_tokenizer = MarianTokenizer.from_pretrained(os.path.join(mypath, 'tagalog-english'))
    except Exception as e:
        print(f"Failed to load English to Tagalog model: {e}")
threading.Thread(target=load_english_tagalog_model).start()