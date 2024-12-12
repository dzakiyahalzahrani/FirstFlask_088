from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form['nama']
    nim = request.form['nim']
    prodi = request.form['prodi']
    return render_template('submit.html', nama=nama, nim=nim, prodi=prodi)  # Kirim data ke submit.html

if __name__ == '__main__':
    app.run(debug=True)
