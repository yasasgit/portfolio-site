import os
import markdown
import re

layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Start your development with Meyawo landing page.">
    <meta name="author" content="Devcrud">
    <title>{title}</title>
    <!-- font icons -->
    <link rel="stylesheet" href="assets/vendors/themify-icons/css/themify-icons.css">
    <!-- Bootstrap + Meyawo main styles -->
    <link rel="stylesheet" href="assets/css/meyawo.css">
</head>

<body data-spy="scroll" data-target=".navbar" data-offset="40" id="home">

<!-- Page Navbar -->
    <nav class="custom-navbar" data-spy="affix" data-offset-top="20">
        <div class="container">
            <a class="logo" href="#">Meyawo</a>
            <ul class="nav">
                <li class="item">
                    <a class="link" href="index.html">Home</a>
                </li>
                <li class="item">
                    <a class="link" href="blog.html">Blog</a>
                </li>
                <li class="item">
                    <a class="link" href="contact.html">Contact</a>
                </li>
                <li class="item ml-md-3">
                    <a href="components.html" class="btn btn-primary">Components</a>
                </li>
            </ul>
            <a href="javascript:void(0)" id="nav-toggle" class="hamburger hamburger--elastic">
                <div class="hamburger-box">
                    <div class="hamburger-inner"></div>
                </div>
            </a>
        </div>
    </nav><!-- End of Page Navbar -->

{hero}

<!-- Dynamic Page Content -->
<section class="section pt-0" id="content">
        <!-- container -->
        <div class="container text-center">
        {content}
    </div>
</section>
    <!-- footer -->
    <div class="container">
        <footer class="footer">
            <p class="mb-0">Copyright
                <script>document.write(new Date().getFullYear())</script> &copy; <a
                    href="http://www.devcrud.com">DevCRUD</a> Distribution <a
                    href="https://themewagon.com">ThemeWagon</a>
            </p>
            <div class="social-links text-right m-auto ml-sm-auto">
                <a href="javascript:void(0)" class="link"><i class="ti-facebook"></i></a>
                <a href="javascript:void(0)" class="link"><i class="ti-twitter-alt"></i></a>
                <a href="javascript:void(0)" class="link"><i class="ti-google"></i></a>
                <a href="javascript:void(0)" class="link"><i class="ti-pinterest-alt"></i></a>
                <a href="javascript:void(0)" class="link"><i class="ti-instagram"></i></a>
                <a href="javascript:void(0)" class="link"><i class="ti-rss"></i></a>
            </div>
        </footer>
    </div> <!-- end of page footer -->

    <!-- core  -->
    <script src="assets/vendors/jquery/jquery-3.4.1.js"></script>
    <script src="assets/vendors/bootstrap/bootstrap.bundle.js"></script>

    <!-- bootstrap 3 affix -->
    <script src="assets/vendors/bootstrap/bootstrap.affix.js"></script>

    <!-- Meyawo js -->
    <script src="assets/js/meyawo.js"></script>

</body>
</html>
"""

hero_section = """
            <!-- page header -->
<header id="home" class="header">
    <div class="overlay"></div>
    <div class="header-content container">
        <h1 class="header-title">
            <span class="up">Heyy!</span>
            <span class="down">I am Yasas Harshana</span>
        </h1>
        <p class="header-subtitle">SOFTWARE ENGINEER & DEVOPS ENTHUSIAST</p>
        <a href="blog.html" class="btn btn-primary">Read My DevOps Articles</a>
    </div>
</header><!-- end of page header -->
<div class="about">
    <div class="about-img-holder">
        <img src="assets/imgs/man.png" class="about-img" alt="yasas harshana avatar">
    </div>
    <div class="about-caption">
        <p class="section-subtitle">Who Am I?</p>
        <h2 class="section-title mb-3">About Me</h2>
        <p>
            I'm Yasas Harshana, a DevOps enthusiast with 1.5+ years of experience in software delivery, CI/CD, and healthcare system reliability. I enjoy automating deployments, optimizing Linux systems, and enabling scalable backend operations using cloud technologies.
        </p>
        <a href="assets/Yasas_Harshana_CV.pdf" class="btn-rounded btn btn-outline-primary mt-4">Download CV</a>
    </div>
</div><!-- end of about wrapper -->
"""

pages = {
    "index.html": {
        "title": "Yasas Harshana",
        "content": ""
    },
    "contact.html": {
        "title": "Contact",
        "content": """
    <!-- contact section -->
<section class="section" id="contact">
    <div class="container text-center">
        <p class="section-subtitle">How can you communicate?</p>
        <h6 class="section-title mb-5">Contact Me</h6>

        <div class="contact-details col-md-8 col-lg-6 m-auto text-left">
            <ul class="list-unstyled">
                <li><strong>Email:</strong> <a href="mailto:yasas99@outlook.com">yasas99@outlook.com</a></li>
                <li><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/yasas-harshana" target="_blank">linkedin.com/in/yasas-harshana</a></li>
                <li><strong>GitHub:</strong> <a href="https://github.com/yasasgit" target="_blank">github.com/yasasgit</a></li>
                <li><strong>Location:</strong> Colombo, Sri Lanka</li>
            </ul>
        </div>
    </div><!-- end of container -->
</section><!-- end of contact section -->

    """
    }
}

os.makedirs("build", exist_ok=True)

for filename, data in pages.items():
    hero = hero_section if filename == "index.html" else ""
    full_html = layout.format(title=data["title"], content=data["content"], hero=hero)
    with open(os.path.join("build", filename), "w") as f:
        f.write(full_html)

article_cards = []
article_dir = "articles"

for md_file in os.listdir(article_dir):
    if md_file.endswith(".md"):
        filepath = os.path.join(article_dir, md_file)
        with open(filepath, "r", encoding="utf-8") as f:
            md_content = f.read()

        metadata = {
            "title": "Untitled",
            "author": "Admin",
            "image": "assets/imgs/img-1.jpg",
            "date": "2025-01-01"
        }

        meta_match = re.search(r"<!--(.*?)-->", md_content, re.DOTALL)
        if meta_match:
            meta_lines = meta_match.group(1).strip().splitlines()
            for line in meta_lines:
                key, _, value = line.partition(":")
                metadata[key.strip()] = value.strip()

        for line in md_content.splitlines():
            if line.startswith("#"):
                metadata["title"] = line.replace("#", "").strip()
                break

        md_content_clean = re.sub(r"<!--(.*?)-->", "", md_content, flags=re.DOTALL)
        html_content = markdown.markdown(md_content_clean)
        article_filename = md_file.replace(".md", ".html")

        text_only = re.sub('<[^<]+?>', '', html_content)
        excerpt = text_only[:300] + "..."

        article_section = f"""
        <section class="section" id="blog-post">
            <div class="container text-left">
                <h2 class="mb-4">{metadata['title']}</h2>
                <p class="text-muted mb-2"><strong>By:</strong> {metadata['author']} | <strong>Date:</strong> {metadata['date']}</p>
                <div class="article-content">
                    {html_content}
                </div>
            </div>
        </section>
        """

        article_page = layout.format(
            title=metadata["title"],
            content=article_section,
            hero=""
        )

        with open(f"build/{article_filename}", "w", encoding="utf-8") as out:
            out.write(article_page)

        blog_card_html = f"""
        <div class="blog-card">
            <div class="blog-card-header">
                <img src="{metadata['image']}" class="blog-card-img" alt="blog image">
            </div>
            <div class="blog-card-body">
                <h5 class="blog-card-title">{metadata['title']}</h5>
                <p class="blog-card-caption">
                    <a href="#">By: {metadata['author']}</a>
                    <a href="#"><i class="ti-calendar"></i> {metadata['date']}</a>
                </p>
                <p>{excerpt}</p>
                <a href="{article_filename}" class="blog-card-link">Read more <i class="ti-angle-double-right"></i></a>
            </div>
        </div>
        """
        article_cards.append(blog_card_html)

blog_html = f"""
<!-- blog section -->
<section class="section" id="blog">
    <div class="container text-center">
        <p class="section-subtitle">Recent Posts</p>
        <h6 class="section-title mb-6">Blog</h6>
        {''.join(article_cards)}
    </div>
</section>
"""

article_index_html = layout.format(title="Blog", content=blog_html, hero="")
with open("build/blog.html", "w", encoding="utf-8") as f:
    f.write(article_index_html)
