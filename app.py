from flask import Flask, jsonify 
from flask_ninja import NinjaAPI
from pydantic import BaseModel
import os
import pandas as pd
# import torch
from transformers import MarianMTModel, MarianTokenizer, Trainer, TrainingArguments, DataCollatorForSeq2Seq
# from sklearn.model_selection import train_test_split
import threading

mypath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model_selection') 

tagalog_english_model = None
tagalog_english_tokenizer = None
def load_english_model():
    tagalog_english_model = MarianMTModel.from_pretrained(os.path.join(mypath, 'tagalog-english'))
    tagalog_english_tokenizer = MarianTokenizer.from_pretrained(os.path.join(mypath, 'tagalog-english'))
threading.Thread(target=tagalog_english_model).start()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chabano-Backend-Secret-Key'
 
# Initialize Ninja API
api = NinjaAPI(app)

class TranslatePayload(BaseModel):
    sentence: str
    from_language: str
    to_language: str

class TranslateResponse(BaseModel):
    translated_text: str
    voice_url: str
 
@api.post("/translate")
def non_csrf_view(data: TranslatePayload) -> TranslateResponse:
    sentence = data.sentence
    from_language = data.from_language
    to_language = data.to_language

    print(sentence)
    print(from_language)
    print(to_language)
    
    if from_language == "tl" and to_language == "en": 
        # Test the loaded model
        if tagalog_english_tokenizer is None:
            return jsonify({
                "error": "Model not loaded",
                "message": "Model not loaded"
            }) , 500
        inputs = tagalog_english_tokenizer(sentence, return_tensors="pt", max_length=128, truncation=True)
        translation = tagalog_english_model.generate(**inputs)
        translated_text = tagalog_english_tokenizer.decode(translation[0], skip_special_tokens=True)
        print(f"Translated text: {translated_text}")
        return TranslateResponse(translated_text=translated_text, voice_url="")

    return TranslateResponse(translated_text=sentence, voice_url="")

















 
if __name__ == '__main__':
    app.run(debug=True)
