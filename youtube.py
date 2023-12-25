from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('url')
        if video_url:
            try:
                yt = YouTube(video_url)
                video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                download_path = 'downloads'
                if not os.path.exists(download_path):
                    os.makedirs(download_path)
                video.download(download_path)
                return f"Video başarıyla indirildi: {video.title}"
            except Exception as e:
                return f"Bir hata oluştu: {e}"
        else:
            return "Lütfen geçerli bir URL girin."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
