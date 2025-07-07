# 🚀 DevOps Portfolio & Blog Site

This is a personal **portfolio website and DevOps blog** built using Python, GitHub Actions, and hosted on GitHub Pages — with zero server costs!

It showcases my **DevOps skills** and serves as a learning hub for others with tutorials and articles on CI/CD, Docker, AWS, Linux, monitoring, and more.

---

## 🛠 Tech Stack

- **Python**: Generates static HTML from Markdown files
- **GitHub Actions**: CI/CD pipeline for linting, building, and deploying
- **GitHub Pages**: Free hosting of the static site
- **Markdown**: Authoring articles and blog posts
- **Meyawo Bootstrap Template**: Clean responsive frontend UI
- **Flake8 & Black**: Python linting and formatting
- **Markdownlint**: Linting Markdown content

---

## 📁 Project Structure

```

├── articles/              # Markdown articles (blog posts)
├── assets/                # CSS, JS, images (Meyawo theme)
├── build/                 # Auto-generated HTML site (deployed)
├── generate\_html.py       # Python script to generate HTML
├── requirements.txt       # Python dependencies
├── .github/workflows/     # GitHub Actions CI/CD workflow
└── README.md              # You're here

````

---

## 🚀 Deployment Pipeline

On every push to the `main` branch:

1. ✅ Python and Markdown linting
2. 🔄 Converts Markdown to styled HTML
3. 📦 Copies assets and builds full site
4. 🚀 Automatically deploys to GitHub Pages (`gh-pages` branch)

> All deployments are fully automated using GitHub Actions.

---

## ✍️ Contributing Articles

Want to contribute? Add a new `.md` file to the `articles/` folder with an optional metadata block like this:

```markdown
<!--
author: Yasas Harshana
date: 2025-07-01
image: assets/imgs/blog-image.jpg
-->
# How to Use GitHub Actions for CI/CD

Your content here...
````

---

## 📌 Live Site

👉 **[yasasgit.github.io](https://yasasgit.github.io)**
(Automatically updated on every push to `main`)

---

## 📄 License

Open source under [MIT License](LICENSE).

---