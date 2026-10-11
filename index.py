from flask import Flask, render_template

app = Flask(__name__)

# Controller untuk rute utama (Beranda)
@app.route('/')
def index():
    # Contoh data yang dikirim dari controller ke view (HTML)
    data_untuk_html = {
        'judul': 'Halaman Beranda',
        'pesan': 'Selamat! Aplikasi Flask pertama Anda berhasil berjalan.'
    }
    
    # render_template akan otomatis mencari di dalam folder 'templates'
    return render_template('index.html', data=data_untuk_html)

if __name__ == '__main__':
    # debug=True membuat server otomatis restart jika ada perubahan kode
    app.run(debug=True)