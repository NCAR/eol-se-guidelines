# Source files for EOL Software Development Guidelines

This repository contains the source for the web and PDF forms of the EOL
Software Development Guidelines.  Currently the static web site is generated
with these tools:

- [Mkdocs](https://www.mkdocs.org/)
- [Mkdocs with PDF](https://pypi.org/project/mkdocs-with-pdf/)
- [Mkdocs Material theme](https://squidfunk.github.io/mkdocs-material)
- [Arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/) python markdown extension
- [MathJax](https://www.mathjax.org/)

This repository can also serve as a template for similar documentation
projects.

## Install

Install the python packages with your favorite virtualenv, mamba, or conda
python environment manager.

```sh
pip install mkdocs mkdocs-with-pdf mkdocs-material
```

Install `google-chrome`.  The `mkdocs-with-pdf` extension is configured to use
the Google Chrome desktop application with the headless option to render pages
which run javascript.  On Fedora `google-chrome` can be installed like below
after the google RPM repository is installed.

```sh
dnf install google-chrome
```

If the PDF command below fails with an error like below:

```sh
  File "/opt/local/miniforge3/lib/python3.12/site-packages/mkdocs_with_pdf/generator.py", line 381, in _render_js
    tag.text = self._mixed_script
    ^^^^^^^^
AttributeError: property 'text' of 'Tag' object has no setter
```

Then one workaround is to edit the `generator.py` file, replacing `tag.text` with `tag.string`:

```python
                    tag = soup.new_tag('script')
                    tag.string = self._mixed_script
                    body.append(tag)
```

## Build

Generate the documentation web site and serve it locally:

```sh
env ENABLE_PDF_EXPORT=1 mkdocs serve
```

Build the web site and the PDF file.  The PDF file will be in
`_site/eol-se-guidelines.pdf`.  The environment setting enables the PDF
output, so leaving it off saves some time and builds just the static html
site.

```sh
env ENABLE_PDF_EXPORT=1 mkdocs build
```

## Publish

Use the `gh-deploy` operation to build the site, commit it to the `gh-pages`
branch, and push that branch to `github`.  Make sure to build the PDF when
deploying the site, so it will be available for download.

```sh
env ENABLE_PDF_EXPORT=1 mkdocs gh-deploy
```
