from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from spleeter.spleeter_run import separate_audio
from voice_conversion.tacotron.convert import convert_voice
from auth.auth import login
from payment.payment import create_payment

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/separate-audio', methods=['POST'])
@jwt_required()
def separate_audio_route():
    input_path = request.json.get('input_path')
    output_path = request.json.get('output_path')
    separate_audio(input_path, output_path)
    return jsonify({'message': 'Audio separation completed'}), 200

@app.route('/convert-voice', methods=['POST'])
@jwt_required()
def convert_voice_route():
    input_audio = request.json.get('input_audio')
    output_audio = request.json.get('output_audio')
    convert_voice(input_audio, output_audio)
    return jsonify({'message': 'Voice conversion completed'}), 200

@app.route('/create-payment-intent', methods=['POST'])
@jwt_required()
def create_payment_route():
    return create_payment()

if __name__ == "__main__":
    app.run()