from flask import Flask, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/sozcu.m3u8')
def get_m3u8():
    yt_url = "https://www.youtube.com/@SozcuTelevizyonu/live"
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(yt_url, download=False)
            stream_url = info.get('url')
            if not stream_url and 'formats' in info:
                stream_url = info['formats'][-1].get('url')
                
            if stream_url:
                return redirect(stream_url, code=302)
            else:
                return "Yayın adresi çözülemedi.", 500
    except Exception as e:
        return f"Hata oluştu: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

