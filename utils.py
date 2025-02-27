def generate_html_file(filename, videos, pdfs, others):
    batch_name = filename.replace(".txt", "").replace("_", " ").title()
    learning_quote = "The beautiful thing about learning is that no one can take it away from you. - B.B. King"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{batch_name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px; }}
            h1 {{ color: #333; text-align: center; }}
            .quote {{ text-align: center; font-style: italic; color: #555; margin-top: 10px; }}
            .extracted-by {{ text-align: center; margin-top: 10px; font-size: 14px; color: #777; }}
            .section {{ background-color: #fff; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }}
            .section h2 {{ color: #555; border-bottom: 2px solid #ddd; padding-bottom: 10px; }}
            .link {{ display: block; margin: 10px 0; color: #007bff; text-decoration: none; }}
            .link:hover {{ text-decoration: underline; }}
            .button {{ display: inline-block; padding: 5px 10px; background-color: #28a745; color: #fff; text-decoration: none; border-radius: 4px; font-size: 14px; }}
            .button:hover {{ background-color: #218838; }}
        </style>
    </head>
    <body>
        <h1>{batch_name}</h1>
        <div class="quote">{learning_quote}</div>
        <div class="extracted-by">Extracted By: <a href="https://t.me/Engineers_Babu" target="_blank">Engineer Babu</a></div>
        <div class="section">
            <h2>Videos</h2>
            {"".join(f'<a class="link" href="{url}" target="_blank">{name}</a>' for url, name in videos)}
        </div>
        <div class="section">
            <h2>PDFs</h2>
            {"".join(f'<a class="link" href="{url}" target="_blank">{name}</a> <a class="button" href="{url}" download>Download PDF</a>' for url, name in pdfs)}
        </div>
        <div class="section">
            <h2>Others</h2>
            {"".join(f'<a class="link" href="{url}" target="_blank">{name}</a>' for url, name in others)}
        </div>
    </body>
    </html>
    """

    html_filename = f"{batch_name.replace(' ', '_')}.html"
    with open(html_filename, "w") as file:
        file.write(html_content)
    return html_filename
