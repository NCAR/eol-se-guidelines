
# Notes

## Conversion

The guidelines have never had a reliable home.  They were on the EOL web site
in Drupal at one point, and somewhere along the way a backup was added to
Confluence.  Then it was moved to sundog internal before the EOL web site was
migrated to a new Drupal version.

This the outdated copy on Confluence that might be easier to export and
convert to markdown, then updated with any changes from the eol copy:

https://wiki.ucar.edu/display/~granger/Software+Development+Guidelines

This seems to be the most recent location:

https://sundog.ucar.edu/Interact/Pages/Section/ContentListing.aspx?subsection=3953

Converting from drupal:

Looks like the only feasible way to do it is to copy all the raw html for
each page into a file in html, then convert those to markdown with html2text
(from python3-html2text package), then fix all the links either manually or
with macros or scripts.  Viewing the raw html for the page allows only the
content to be copied, without the header, footer, sidebar, and other
navigation links.

Then figure out how to render it nicely in a github repo, what formatting to
use?  md or rst?

## Todo

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

## Examples

Examples of github doc repos that could be worth following:

- [CppCoreGuidelines](https://github.com/isocpp/CppCoreGuidelines): also a C++ reference
