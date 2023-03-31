import io
import config

from flask import Flask, render_template
import qrcode
import os
import boto3

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
    qr_url = upload_to_s3(img, filename)
    return render_template('display.html', img=qr_url)


def upload_to_s3(img, filename):
    s3 = boto3.resource('s3',
                        aws_access_key_id=config.aws_access_key,
                        aws_secret_access_key=config.aws_secret_key
                        )
    bucket = s3.Bucket(aws_bucket_name=config.aws_bucket_name)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    bucket.put_object(Key=filename, Body=img_byte_arr)
    return f"https://{config.aws_bucket_name}.s3.amazonaws.com/{filename}"


if __name__ == '__main__':
    app.run(debug=True)
