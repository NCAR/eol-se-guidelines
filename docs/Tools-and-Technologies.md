## Editing

There are several tools in use in EOL for editing source code. Besides emacs
and vi, there are Integrated Development Environments (IDE) VS Code, Eclipse,
and JetBrains. No particular IDE or tool should be mandated or standardized
across EOL, since that runs contrary to flexibility, individuality, and the
investigation of new technology. Instead, we can continue to encourage
communication, share what works, and consolidate tools when prudent.

### Revision Control

There are two major revision control tools in use in EOL: subversion and git.
It makes sense to standardize on these two since the infrastructure is in
place and there has been plenty of experience with them. There is an [EOL
organization at github](https://github.com/ncareol/) for both private and
public repositories. By now most new projects should use the [NCAR
organization](https://github.com/NCAR) on github.  There is also a subversion
server in EOL, but most software has migrated away from that to github.  See
the [EOL wiki](Resources-and-References.md#eol-wiki) for more information on
git, subversion, and migrating to git.

### Unit Testing

[Test-driven development](http://en.wikipedia.org/wiki/Test-driven_development)
is a valuable practice that can be used in projects of any
scale. It forces developers to consider requirements and expected behaviour
from the beginning, and then unit tests verify the behavior and provide some
assurances that code still works after the changes. Various libraries and
harnesses have been used in EOL to facilitate testing.

Java in general can use [JUnit](http://junit.org/), for which Eclipse has
plugins.

For python, there are [pylint](http://www.logilab.org/projects/pylint) and
[unittest](http://docs.python.org/lib/module-unittest.html) and
[py.test](http://pytest.org/).

C++ projects have used [CppUnit](http://sourceforge.net/projects/cppunit/),
[Boost Test](http://www.boost.org/doc/libs/1_37_0/libs/test/index.html),
[CxxTest](http://cxxtest.com/), and [Google
Test](https://github.com/google/googletest).

### Memory Checking

A valuable tool for checking for memory errors in an application is
[valgrind](https://valgrind.org/). It is a very good practice to run compiled
applications through valgrind. If the tests can be scripted and automated,
then valgrind can easily check for memory errors and memory leaks each time
the tests are run. The more source code exercised by the tests (code
coverage), the more thorough the memory checking.

### Issue Tracking

The default issue tracking tool in EOL was
[JIRA](http://www.atlassian.com/software/jira/), and several projects still
use it. However, github has its own issue tracking, and sometimes a wiki is
used to track issues. Email does not make a good issue tracking tool, because
the thread is spread across emails, it is difficult to catch someone up, and
it is difficult to search for past similar issues. Note that field deployment
issues can be tracked and not just software issues. [UCAR
JIRA](http://jira.ucar.edu/) is now used to track the tasks and problems
related to software and systems deployments for various ISF and RAF platforms.

### Continuous Integration

EOL migrated from [Buildbot](http://wiki.eol.ucar.edu/sew/Buildbot) to
[Jenkins](https://wiki.jenkins-ci.org/) for continuous integration and
testing. See the EOL Software Engineering Wiki for information on how to use
the EOL instance.

### Builds

EOL software has been known to use make, autoconf, shell scripts, SCons,
Visual Studio, cmake, and qmake to build and install. There are many possibilities,
but should EOL try to settle on just a few? [SCons](http://www.scons.org/) is
used by several projects in EOL, and many of them share extensions to SCons
called [eol_scons](https://github.com/ncar/eol_scons).

### Code Reviews

There seems to be two common approaches to code reviews: emails and github
comments.  It has been very helpful and effective to send email notifications
on each code commit, especially if they contain diffs.  Then other developers
know what is being changed and can reply with comments about the changes.
Github also provides ways to comment on pull requests and directly on code in
commits, and that has proved convenient and effective also.  Formal code
reviews, however, have probably only rarely happened in EOL, if ever.

### Packaging, Distribution, and Installation

Some projects provide targets to assemble an installation package. The package
can be an RPM or a tar.gz file. Providing a standard installation package
facilitates deployment to multiple field systems and to internal EOL servers.
RPM's can be deployed through the [EOL YUM
repository](http://wiki.eol.ucar.edu/sew/EOL_YUM_Repository).

If an application is being installed from the source tree, such as with a
build target, or it is being packaged in an archive, then certain conventions
should be followed as to where to install the necessary files. Linux has a
standard for where files are installed on a system called the Linux Standards
Base. Likewise, it is good practice to not install unstable software into
production locations. On EOL servers and desktop systems, these directories
are for stable, production software: /usr and other system directories,
/usr/local, and shared network directories like /net/opt_lnx, /opt/local. Do
not install by default into these locations, lest operational versions get
overwritten. For Linux installations, follow the standard layout of lib, bin,
and include subdirectories beneath a configurable prefix directory.

It is helpful to have a single build target for installing from within a
source tree. This allows multiple software packages to be installed into a
single integration test tree and run against each other, without affecting the
rest of the system. When source code changes in one source tree, the build
installs the changed files so that other packages will build against the
latest changes from the integration tree.

It is not known what is the best practice for installing libraries and source
needed to build software. Sometimes a common prefix can be used for all
dependencies, other times packages will have their own separate installation
tree, and those directories will need to be added explicitly to the build
paths.

There is a recommended installer tool for Windows applications, used in
particular by ASPEN. Ask Charlie about it.

### Graphical User Interface Frameworks

The majority of current EOL (non-Web-based) applications use Qt. Should that
become the preferred GUI library for EOL? Other GUI frameworks have been used
over the years, but experience and current practice suggest that using Qt for
GUI applications is a best practice in EOL. That could include Qt bindings in
python using either [PyQt](https://wiki.python.org/moin/PyQt) or
[PySide](http://wiki.qt.io/PySide).

### Web Application Frameworks

There are many web applications developed in EOL using several technologies,
including Ruby on Rails, Groovy with Grail, Django, HTML, Javascript, Tomcat,
Python CGI, ION (IDL), PHP, Mapserver, Perl CGI, Java Server Pages, and so on.
It would be difficult to standardize on a particular web technology since they
change so quickly and since there is no clear trend in EOL. Nevertheless,
maybe a few standard web frameworks should be considered. At the very least,
before adopting yet another web application platform, consider very carefully
the long-term maintenance of the application. Now there is also a variety of
JavaScript libraries to choose from.

### Application Configuration

There are many mechanisms and libraries to configure applications at runtime.
There are Windows INI files, for which there are few different libraries in
use. Qt provides a cross-platform configuration API that stores configuration
parameters as INI files. Boost provides an API for command-line and file-
backed program options, as well as a serialization library. There are the
standard getopt() and getenv() GNU and POSIX calls. Java now has a standard
API for application configuration (Java Preferences API), besides also having
core support for serialization (persistence). Some applications store
configuration data in XML and use the Apache Xerces-C library to read and
write XML files. Here are some guidelines despite all this variety:

- Use a text-based, line-based configuration file format, even if users will
  never be expected to edit the configuration files. This format can be
  deciphered by developers when there are problems, and different versions of
  configuration files can be managed and compared by revision control systems.
  It is a good practice to store examples of configuration files as well as
  test and production configurations in revision control.

- Related to revision control, when modifying a configuration in software,
  avoid gratuitous formatting or structure changes (like changing node order)
  so that differences between revisions will be meaningful. In the XML DOM
  this is possible by modifying the document model in parallel with the
  configuration changes. Other formats might require always ordering nodes
  alphabetically when writing them out.

- Provide as many reasonable defaults as possible, so software can work as
  quickly and as automatically as possible without requiring too much
  configuration from the user.

### Commercial Tools

It seems we should identify some best practices for selecting and adopting
commercial tools. There may be IDE's, memory checkers, static analysis and
code coverage tools, advanced compilers, web and GUI test harnesses, database
tools, and software diagramming tools which would be worth their cost to EOL,
but we do not have any methods in place to evaluate them. The best approach
may be to suggest that developers seek out tools that may be helpful for a
particular project and then report on whether the tools should be used more
widely in EOL. EOL has taken advantage of commercial tools for which there are
UCAR site licenses, such as the MagicDraw UML tool and the Atlassian products.

Tools like LabVIEW and FPGA compilers are also used in EOL for specialized
needs.

### Code Analysis Tools

Memory checking tools have been used in the past, such as Purify and
Testcenter, and they proved useful. Perhaps it is time to adopt the latest
generation of such tools. CERN has benefitted from the static code analysis
tool Coverity, the tool known for checking the Linux kernel. Here is a list of
"more well- known" commercial code analysis tools:

- [Coverity](http://coverity.com/)
- [Parasoft](http://parasoft.com/)
- [LDRA Testbed](http://www.ldra.com/)

Likely EOL software would benefit from at least adopting open source and
research code analysis tools into the development process. A quick search of
the web yields a few possibilities, at least for Linux and C++. There are also
many for Java and Python ([pylint](http://www.logilab.org/projects/pylint)).

- [Splint](http://lclint.cs.virginia.edu/)
- [Mozilla Static Analysis Tools](https://wiki.mozilla.org/Static_Analysis)
- [CppCheck](http://sourceforge.net/apps/mediawiki/cppcheck)

[Next page: Logging Frameworks](Logging-Frameworks.md)
