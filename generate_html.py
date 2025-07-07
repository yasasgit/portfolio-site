import os
import markdown

# Layout template
layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Yasas Harshana's DevOps Portfolio and Tutorials">
    <meta name="author" content="Yasas Harshana">
    <!-- font icons -->
    <link rel="stylesheet" href="assets/vendors/themify-icons/css/themify-icons.css">
    <!-- Bootstrap + Meyawo main styles -->
    <link rel="stylesheet" href="assets/css/meyawo.css">
</head>

<body data-spy="scroll" data-target=".navbar" data-offset="40" id="home">

<!-- Page Navbar -->
<nav class="custom-navbar" data-spy="affix" data-offset-top="20">
    <div class="container">
        <a class="logo" href="index.html">Yasas</a>
        <ul class="nav">
            <li class="item"><a class="link" href="index.html">Home</a></li>
            <li class="item"><a class="link" href="about.html">About</a></li>
            <li class="item"><a class="link" href="projects.html">Projects</a></li>
            <li class="item"><a class="link" href="articles.html">Articles</a></li>
        </ul>
        <a href="javascript:void(0)" id="nav-toggle" class="hamburger hamburger--elastic">
            <div class="hamburger-box"><div class="hamburger-inner"></div></div>
        </a>
    </div>
</nav>
<!-- End of Navbar -->

<!-- Hero Header -->
<header id="home" class="header">
    <div class="overlay"></div>
    <div class="header-content container">
        <h1 class="header-title">
            <span class="up">HI!</span>
            <span class="down">I am Yasas Harshana</span>
        </h1>
        <p class="header-subtitle">DevOps & SRE Enthusiast</p>
        <a href="projects.html" class="btn btn-primary">View My Projects</a>
    </div>
</header>
<!-- End of Hero -->

<!-- Dynamic Page Content -->
<section class="section" id="content">
    <div class="container mt-5">
        {content}
    </div>
</section>

<!-- Footer -->
<div class="container">
    <footer class="footer">
        <p class="mb-0">
            &copy; <script>document.write(new Date().getFullYear())</script> Yasas Harshana.
        </p>
        <div class="social-links text-right m-auto ml-sm-auto">
            <a href="#" class="link"><i class="ti-github"></i></a>
            <a href="#" class="link"><i class="ti-linkedin"></i></a>
        </div>
    </footer>
</div>

<!-- Scripts -->
<script src="assets/vendors/jquery/jquery-3.4.1.js"></script>
<script src="assets/vendors/bootstrap/bootstrap.bundle.js"></script>
<script src="assets/vendors/bootstrap/bootstrap.affix.js"></script>
<script src="assets/js/meyawo.js"></script>

</body>
</html>
"""

# Static pages
pages = {
    "index.html": {
        "title": "Welcome to Yasas' DevOps Portfolio",
        "content": "<h1>Welcome</h1><p>This is my portfolio and documentation site. Browse articles and tutorials below!</p>"
    },
    "projects.html": {
        "title": "Projects",
        "content": "<h1>My Projects</h1><ul><li>DevOps Portfolio Site</li><li>Dockerized Flask App</li></ul>"
    },
    "about.html": {
        "title": "About Me",
        "content": "<h1>About</h1><p>I'm Yasas Harshana, a DevOps enthusiast with experience in CI/CD, Linux, and AWS.</p>"
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
