from flask import Flask, render_template
import qrcode
import os

app = Flask(__name__, template_folder='view', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/qr/<text>', methods=['POST', 'GET'])
def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"{text}.png"
    img.save(os.path.join('static/qr/', filename))
    return render_template('display.html', img=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
