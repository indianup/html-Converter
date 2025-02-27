import re
import os
from telegram import InputFile
from utils import generate_html_file
from logs import logger

def extract_urls_and_names(text):
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(text)
    names = [url.split('/')[-1].split('.')[0] for url in urls]
    return urls, names

def categorize_urls(urls, names):
    videos = []
    pdfs = []
    others = []

    for url, name in zip(urls, names):
        if "media-cdn.classplusapp.com/drm/" in url or "cpvod.testbook" in url:
            new_url = f"https://dragoapi.vercel.app/video/{url}"
            videos.append((new_url, name))
        elif "pdf" in url:
            pdfs.append((url, name))
        else:
            others.append((url, name))

    return videos, pdfs, others

def start(update, context):
    update.message.reply_text("Welcome! Please upload a .txt file.")

def handle_file(update, context):
    file = update.message.document.get_file()
    filename = update.message.document.file_name

    if not filename.endswith(".txt"):
        update.message.reply_text("Please upload a .txt file.")
        return

    file.download(filename)
    with open(filename, "r") as f:
        text = f.read()

    urls, names = extract_urls_and_names(text)
    videos, pdfs, others = categorize_urls(urls, names)
    html_filename = generate_html_file(filename, videos, pdfs, others)

    with open(html_filename, "rb") as f:
        update.message.reply_document(document=InputFile(f))

    # Clean up files
    os.remove(filename)
    os.remove(html_filename)
    logger.info(f"Processed file: {filename}")
