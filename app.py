from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chuong-trinh')
def chuong_trinh():
    return redirect(url_for('home'))  # dropdown handled via frontend only

@app.route('/tokutei-gino')
def tokutei_gino():
    return render_template('tokutei_gino.html')

@app.route('/du-hoc')
def du_hoc():
    return render_template('du_hoc.html')

@app.route('/dang-ky', methods=['GET', 'POST'])
def dang_ky():
    if request.method == 'POST':
        hoten = request.form['hoten']
        sdt = request.form['sdt']
        ngaysinh = request.form['ngaysinh']
        diachi = request.form['diachi']
        trinhdo = request.form['trinhdo']
        return redirect(url_for('home'))
    return render_template('dang_ky.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
