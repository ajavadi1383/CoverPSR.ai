import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)
stripe.api_key = 'your_stripe_secret_key'

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = request.get_json()
        intent = stripe.PaymentIntent.create(
            amount=data['amount'],
            currency='usd'
        )
        return jsonify({'client_secret': intent.client_secret})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == "__main__":
    app.run()