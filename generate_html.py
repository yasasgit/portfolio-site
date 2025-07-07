import os

# Template layout
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

# Page definitions
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
    },
    "articles.html": {
        "title": "Articles",
        "content": "<h1>Articles</h1><p>Coming soon: tutorials on GitHub Actions, Terraform, Docker!</p>"
    },
}

# Create build directory
os.makedirs("build", exist_ok=True)

# Generate each page
for filename, data in pages.items():
    full_html = layout.format(title=data["title"], content=data["content"])
    with open(os.path.join("build", filename), "w") as f:
        f.write(full_html)
