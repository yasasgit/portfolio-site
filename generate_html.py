import os
import markdown

# Layout template
layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: sans-serif; margin: 2rem; }}
        nav a {{ margin-right: 15px; text-decoration: none; color: #0366d6; }}
        footer {{ margin-top: 50px; font-size: 0.8em; color: #888; }}
        pre {{ background: #eee; padding: 1rem; overflow-x: auto; }}
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="projects.html">Projects</a>
        <a href="articles.html">Articles</a>
    </nav>

    <main>
        {content}
    </main>

    <footer>
        <p>© 2025 Yasas Harshana</p>
    </footer>
</body>
</html>
"""

# Static pages
pages = {
    "index.html": {
        "title": "Yasas Harshana - Portfolio",
        "content": "<h1>Welcome!</h1><p>This is my portfolio homepage.</p>"
    },
    "about.html": {
        "title": "About Me",
        "content": "<h1>About Me</h1><p>I’m an aspiring DevOps/SRE engineer passionate about automation and cloud infrastructure.</p>"
    },
    "projects.html": {
        "title": "Projects",
        "content": "<h1>Projects</h1><ul><li>DevOps Portfolio Site</li><li>Dockerized Flask App</li></ul>"
    }
}

# Create build dir
os.makedirs("build", exist_ok=True)

# Generate static pages
for filename, data in pages.items():
    full_html = layout.format(title=data["title"], content=data["content"])
    with open(os.path.join("build", filename), "w") as f:
        f.write(full_html)

# Handle markdown articles
article_links = []
article_dir = "articles"
for md_file in os.listdir(article_dir):
    if md_file.endswith(".md"):
        filepath = os.path.join(article_dir, md_file)
        with open(filepath, "r") as f:
            md_content = f.read()
            html_content = markdown.markdown(md_content)
            title = md_content.splitlines()[0].replace("#", "").strip()
            html_page = layout.format(title=title, content=html_content)

            article_filename = md_file.replace(".md", ".html")
            with open(f"build/{article_filename}", "w") as out:
                out.write(html_page)

            article_links.append(f"<li><a href='{article_filename}'>{title}</a></li>")

# Generate article index page
article_index = "<h1>Articles</h1><ul>" + "\n".join(article_links) + "</ul>"
article_index_html = layout.format(title="Articles", content=article_index)
with open("build/articles.html", "w") as f:
    f.write(article_index_html)
