from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='geoze_token_image.png')
    return f'''
    <h1>Welcome to the Geoze Meme Token Landing Page!</h1>
    <p>Early access GEOZE MEME TOKEN -- the most outrageous token on planet Earth that aims to send your DNA to the universe in a tardigrade!</p>
    <img src="{image_url}" alt="Geoze Token Image" style="width: 100%; max-width: 600px;">
    '''

if __name__ == '__main__':
    app.run(debug=True)
