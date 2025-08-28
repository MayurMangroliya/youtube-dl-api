from http.server import BaseHTTPRequestHandler
from yt_dlp import YoutubeDL
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        url = params.get("url", [""])[0]
        if not url:
            self.send_error(400, "Missing ?url=")
            return

        ydl_opts = {"format": "best[ext=mp4]", "quiet": True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            direct = info["url"]

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"url": direct}).encode())
