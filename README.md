### Setup

A few attachments under `2024_content/slides` are not included in this folder to meet the size limit requirement. When generating the website, they should be added back locally to the folder.

$ python3 -m venv venv # venv has been added to .gitignore
$ source venv/bin/activate
$ pip install -r requirements.txt
$ make html && make serve        # Serve website locally. Point browser to: localhost:8000. The output folder has been added to .gitignore.

### Development workflow

1. Make changes to the source files under `2024_content/`
2. Run `make html` and `make serve` to preview the changes.
3. Once you are satisfied, commit the changes to the repo `git push origin main` (if committing to the main branch)
4. Run `ghp-import -n -p -f 2024/` to publish the website to GitHub Pages.
