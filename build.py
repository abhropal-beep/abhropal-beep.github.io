import os
import re
import markdown

POSTS_DIR = "posts"
OUTPUT_DIR = "posts"
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            line-height: 1.8;
            color: #1a1a1a;
            max-width: 680px;
            margin: 0 auto;
            padding: 60px 20px;
            background: #fafafa;
        }}
        a {{ color: #1a1a1a; }}
        .back {{ font-size: 0.9rem; color: #666; text-decoration: none; }}
        .back:hover {{ text-decoration: underline; }}
        h1 {{ font-size: 1.8rem; font-weight: 700; margin: 20px 0 8px; line-height: 1.3; }}
        h2 {{ font-size: 1.25rem; font-weight: 600; margin: 40px 0 12px; }}
        p {{ margin-bottom: 20px; }}
        em {{ font-style: italic; }}
        hr {{ border: none; border-top: 1px solid #eee; margin: 48px 0; }}
        .meta {{ color: #999; font-size: 0.85rem; margin-bottom: 40px; }}
    </style>
</head>
<body>
    <a href="../index.html" class="back">&larr; Back</a>
    {content}
</body>
</html>"""

def build():
    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(POSTS_DIR, fname), "r", encoding="utf-8") as f:
            md_text = f.read()

        # Extract title from first # heading
        title_match = re.match(r"^#\s+(.+)", md_text)
        title = title_match.group(1) if title_match else fname.replace(".md", "")

        # Convert markdown to HTML
        html_content = markdown.markdown(md_text)

        # Wrap in template
        output = TEMPLATE.format(title=title, content=html_content)

        out_fname = fname.replace(".md", ".html")
        with open(os.path.join(OUTPUT_DIR, out_fname), "w", encoding="utf-8") as f:
            f.write(output)

        print(f"  Built: {out_fname}")

if __name__ == "__main__":
    build()
    print("Done!")
