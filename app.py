from flask import Flask, jsonify 
from flask_ninja import NinjaAPI
from pydantic import BaseModel

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

    return TranslateResponse(translated_text=sentence, voice_url="")


















 
if __name__ == '__main__':
    app.run(debug=True)
