from fastapi import FastAPI
import yt_dlp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "YouTube Downloader API is running!"}

@app.get("/download")
def download(url: str):
    ydl_opts = {"quiet": True, "format": "best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title"),
            "url": info.get("url")
        }
