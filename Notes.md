# Notes

These are notes about the background and development of the document and
static site generator.

See [Conversion](#conversion) for information on how the document was
converted from the web.

[TOC]

## Todo

These are improvements pending or under consideration.

The sections could benefit from some reordering.  The main topics are
principles, code, process, tools, resources.  Everything else should be rolled
into those or somehow indented in the index.

"Practice Priming" in the "Updating the Guidelines" should be in a skills
development section, maybe next to all the other resources for skills
development.

Other updates to make:

- add something about versioning: semantic versioning reference page,
  how to balance generated revisions with explicit tagged versions,
  importance of building releases from clean tag revisions rather
  than working directories, testing and CI for releases

- options for storing release artifacts: github, ftp, software center?

- web APIs: link to Erik's pages on SEW

These pages can be replaced with links to the full guidelines:

https://wiki.ucar.edu/display/SEW/SoftwarePractice
https://wiki.ucar.edu/display/SEW/ProjectTracking

This page should be deleted:

https://wiki.ucar.edu/display/SEW/ProjectPlanning

After cleaning up the two pages which link to it:

https://wiki.ucar.edu/display/SEW/ProjectManagement
https://wiki.ucar.edu/display/SEW/SoftwareProjects

Other things to update:

Add section about DEI and references to lingo changes.

Update tool references:

- remove mentions of bugzilla
- mention jira and github as issue trackers
- mention tradeoffs to both
- probably most referenes to subversion can be replaced with git
- include ansible and containers and provenance
- make sure system configuration and software configuration are tracked
- update release versioning
- dangers of automatic versions with git (not like subversion)
- update documentation tools: trend is markdown, github-hosted, jekyll

And consolidate this page into it, then just replace links to this page
with links to the github version.

https://wiki.ucar.edu/display/SEW/SoftwarePractice

Include these lessons learned from coding sprints:

- It takes longer that you think it will.

- There is definitely a benefit to being removed from distractions and
  working in a concentrated group.

- Perhaps it would have helped to make more people aware of what we were
  doing and where we were, just so it doesn't appear like we're trying to
  ignore everyone, and because others have a stake in the outcome.

- It is invaluable to have test suites in place before the sprint, and the
  tests of course should all be passing. The tests help verify that the
  changes have not broken anything that was working before the sprint. The
  more automated, comprehensive, and convenient the tests are, the more
  effective they are.

Look for diagram of syslog/journald log flows and management and current
best practices for application logging.

Add security practices to guidelines:

- no credentials in repo, documents, wikis
- github credentials
- git commit authorship for shared accounts
- password management and cycling
- ssh key cycling

Link to [Guide to Securing Scientific Software](https://drive.google.com/file/d/19ScxwNNAs5TRIhyZ8tsEa5QF2NozqV2P/view?usp=sharing).

Link to SAST information, mention Synopsys Coverity, both licensed and open
source.

Add latest thinking about revisioning and packaging:

[Fedora Packaging Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/)

Prefer a fixed version string rather than automatic, so the source archive can
be exported directly and easily from the repo, usually as a complete copy but
if necessary with some files omitted.

Likewise packaging version does not automatically track the latest repo
version.  The packaging version is managed and specified separately.  A
(release) package is built from a clean source archive of a specific release,
rather than the package version being whatever automatic revision number can
be determined from the current working repo.  It should be possible to test
package builds from a working tree, but those should not be released.

It is still useful to include automatic revisions in the builds, but those
do not need to serve as the software version.  Use a `version.h` file with
a hardcoded version:

```c
#define VERSION "1.2.3"
```

Commit that with tag `v1.2.3`.  Then immediately commit another revision which
uses an "indeterminate" form of the version, to indicate versions under
development and not released.  If development is happening on a `1.2` branch,
then:

```c
#define VERSION "1.2.x"
```

Add something about licenses?  At least some references to past practice, like
the BSD recommendation, and some way to find out more information when
selecting a license.

Style formatting

It seems like a growing trend and a good idea to enforce consistent coding
style with a tool, at least within the same code base.  There are many capable
formatters for most languages, and they can get close to current practice.
The headache of embedding editor hints in every source file is just not worth
it anymore.

- clang-format for C++
- black and others for python

Use linters for interpreted languages

A good linter is invaluable for python code and probably most interpreted
code, since the interpreter only needs to parse code and does not need to
validate it or typecheck it until it is run.

Likewise for testing for python.  Without good code coverage for tests, there
could be code in an application that will cause a crash the first time it runs
because of a simple typo.

References

C++ references to add:

- [cppreference.com](https://cppreference.com/)
- [CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines): also a C++ reference
- [C++ Super FAQ](https://isocpp.org/faq)

Add `eol-prog` email list as a resource also.

https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/

https://www.altexsoft.com/blog/business/technical-documentation-in-software-development-types-best-practices-and-tools/

### Other potential additions

Best practices for source releases (semantic versions), source release
archives, and binary packaging and package versions:

https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/

Add C++ guidelines somewhere, like to best practices or a wiki page:

https://github.com/isocpp/CppCoreGuidelines
https://github.com/Microsoft/GSL
https://github.com/catchorg/Catch2
https://www.softwarecollections.org/en/

OSCON
uberconf - no fluff just stuff
C++ Now

OReilly has online tutorials and sessions: oreilly.com

LinkedIn Learning courses are free through UCAR.  How could we build up a list
of courses that others have taken and found useful, so we can prioritize
higher-quality courses?

## Static site generators

There was significant effort put into selecting a static site generator for
this document and for technical documentation in general.

These were the desired features for a technical documentation system:

- easy to learn how to add content, with accessible formatting
- web accessible over the Internet (esp github)
- portable for offline access, on field machines or personal devices
- PDF output, partly to enable offline access and portability
- collaborative editing and versioning
- can include photographs and diagrams
- math rendering
- can reference other PDF files or web sites
  - external vendor documentation
  - related software documention (eg, NIDAS, ISFS, DSM have separate documentation)

An ePub output option might be nice for personal mobile devices, to get the
benefit of using an e-reader app to read and bookmark documents.  Maybe
there's a way to get PDF into e-readers?

Note that Confluence is always considered as an option, since it is available
to all staff, it is meant to be a collaborative space for iterative
documentation, and it already holds much technical documentation.  It also can
be made to produce reasonable PDF output, with some work.  However, the pages
can only be edited when online, the raw formatting syntax is not well known,
versioning is by page and not by site, and the web form is only available
online.  In the end, it has the same big problem as the Drupal and Sundog CMS
systems: the content and version information is difficult to export and
migrate if the system ever goes away or someone decides it doesn't belong
there.

Jekyll is a de facto standard for github web sites.  However, jekyll has
proved complicated to install and configure, and GitHub Markdown is not that
powerful on its own for actual documentation.  So jekyll with the default
github-pages action works well for simple sites but is otherwise rather
limited.

The general practice for nicer (and thus more complicated) documentation sites
is to generate the static site and push it to the gh-pages branch of a repo,
either in the same repo or a different one.  Where PDF output is desired, it
has to be generated also to be available for download on the web site.  (It
might be nice to provide a page/table to download all the PDFs on a site, both
the generated one and any other technical or vendor documents, even if it's
just links to the vendor documents.)

Thus this documentation uses custom tools and configuration to build the
static web site and the PDF output.  The built documentation is committed to
the repo and hosted on github.  Therefore the repo does not need a github
action (although I assume one could be added), but more importantly the repo
and the static site can be cloned and hosted elsewhere (eg, field servers)
without having to install the tools, especially jekyll.  It would still be
nice to be able to edit and regenerate the documentation locally, but it
wouldn't be strictly necessary.

The current site generator is `mkdocs` with the
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
theme.  It
looks nice right out of the box, installs easily (especially when already
familiar with python packaging), interactive search works well and works
offline, permalinks and anchors on headers, and table of contents.

By using a static site generator, it will be possible to integrate other
generated html documentation into the site, such as API docs from
[doxygen](https://www.doxygen.nl/index.html), [Swagger](https://swagger.io/),
or [AsyncAPI](https://www.asyncapi.com).

### Survey of static site generators

This page gives a helpful rundown of several static site generators:

- [Docusaurus](https://docusaurus.io/docs)

Docusaurus looks very capable and emphasizes javascript interactivity, but not
sure about a PDF output option.

Sphinx should be a viable option, especially now that it handles markdown
files as well as restructured text.

- [Sphinx](https://www.sphinx-doc.org/)

This tool might prove a viable alternative to `sphinx` to extract python
documentation from docstrings:

- [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)

[gitbook.com](gitbook.com) looked like a nice option, but apparently it has
become more of a commercial solution.  Maybe the cost is worth it if it works
for everything and is not difficult to learn and setup.

This looks nice, but it's based on R and looks harder to setup:

- [bookdown](https://bookdown.org/)

[AspenDocs](https://ncar.github.io/aspendocs/) has been a premier example of
online and pdf technical documentation for EOL software.  It requires
[Prince](https://www.princexml.com/doc/installing/) and some extensive jekyll
configuration,
[documented here](https://idratherbewriting.com/documentation-theme-jekyll/mydoc_generating_pdfs.html).
It meets all the requirements above, except for the dependencies on jekyll and
Prince.

[Hugo](https://gohugo.io/about/features/) might be nice as a single standalone
app, but it was not investigated thoroughly.

Google seems to use [Gitiles](https://gerrit.googlesource.com/gitiles/) for
sites like the style guide.  It has some nice markdown extensions, like
anchors and tables of contents and simpler configuration.  It's a Java
program, but maybe it's still easier to install and run and configure than
jekyll.

Here is a [table of SSGs on jamstack](https://jamstack.org/generators/).

[DASH](https://kapeli.com/dash) is meant for offline API documentation
browsing, but it is targeted at MacOS.
[BookStackApp](https://www.bookstackapp.com/) is more of a Confluence
alternative, where documents are stored in a database and not as plain text in
a repo.

[Read the Docs](https://software-documentation-template.readthedocs.io/en/latest/readme.html)
templates could be used to generate the static site even if not used to host
it, presumably with all the capabilities that Sphinx provides like ePub and
PDF output.

### Examples

Noteworthy examples of github doc repos:

- [CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines)
- [Prometheus Docs](https://github.com/prometheus/docs#contributing-changes)
- [Google style guide](https://code.google.com/p/google-styleguide/)

## Conversion

The guidelines have never had a reliable home.  They were on the EOL web site
in Drupal at one point, and somewhere along the way a backup was added to
Confluence.  Then it was moved to sundog internal before the EOL web site was
migrated to a new Drupal version.

There was an outdated copy on Confluence, and that will be removed when this
version is viable.

- [Software Development Guidelines](https://wiki.ucar.edu/display/~granger/Software+Development+Guidelines) on Confluence

The sundog version was here, after being migrated from Drupal:

- [Sundog version](https://sundog.ucar.edu/Interact/Pages/Section/ContentListing.aspx?subsection=3953)

The conversion was done by downloading the raw html for each page on sundog
into a file in html.  Those files are in the history for this repository in a
directory called `sundog`.  Those html files were converted to markdown with
`html2text` (from `python3-html2text` package) using the python script
[extract-sundog-docs.py](python/extract-sundog-docs.py).  The script just
adjusts the file names and extracts the appropriate content section from the
html page.  Any linking problems in the markdown files were fixed manually.
