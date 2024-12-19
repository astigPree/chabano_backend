from flask import Flask, jsonify 
from flask_ninja import NinjaAPI
from pydantic import BaseModel
from .model_loader import *



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
        global tagalog_english_model, tagalog_english_tokenizer
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
    
    if from_language == "en" and to_language == "tl": 
        global english_tagalog_model, english_tagalog_tokenizer
        # Test the loaded model
        if english_tagalog_tokenizer is None:
            return jsonify({
                "error": "Model not loaded",
                "message": "Model not loaded"
            }) , 500
        inputs = english_tagalog_tokenizer(sentence, return_tensors="pt", max_length=128, truncation=True)
        translation = english_tagalog_model.generate(**inputs)
        translated_text = english_tagalog_tokenizer.decode(translation[0], skip_special_tokens=True)
        print(f"Translated text: {translated_text}")
        return TranslateResponse(translated_text=translated_text, voice_url="")

    return TranslateResponse(translated_text=sentence, voice_url="")

















 
if __name__ == '__main__':
    app.run(debug=True)
