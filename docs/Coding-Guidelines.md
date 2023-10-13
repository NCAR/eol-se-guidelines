# Coding Guidelines

[TOC]

The coding guidelines relate to source code, implementation, and to the
artifacts and infrastructure which should be part of development. Of course
there is much overlap between process and coding.

## Use automated builds.

Every project should be easy to build from checkout with an automated, batch
build process. For C++ applications, SCons is recommended for its existing
support of EOL tools, libraries, and common third-party components. Java
projects might use ant or Eclipse. Whatever the tool, building and testing
should be turnkey. [See the [Joel Test](Resources-and-References.md#joel-test), step 2.]

## Use automated testing.

Use a testing framework like boost.test, cppunit, JUnit, cxxunit, or whatever,
but integrate the testing into the automated build framework so it is easy to
run the tests and detemine either pass or failure, without manually inspecting
or comparing the output. A script which runs the program and tests for basic
output is still helpful, sometimes called a _smoke test_. The more automated
the testing, the more the computer can help by running the tests continuously
on every change, often while further development continues simultaneously. One
of the ideas behind the test-driven development process is that writing tests
also helps the developer think clearly about the scope and the requirements,
before writing the code.

## Use continuous integration testing.

Take advantage of buildbot or other tools to run builds and tests whenever
code is committed, potentially on multiple platforms, without doing it
manually.

## Use compilers effectively.

Most compilers can warn about questionable code constructs, such as missing
return statements, unreached code, missing cases, unsafe type conversions.
These warnings should always be enabled, and the code should compile cleanly
without any warnings. This also works well with automated testing and
continuous integration, since the compile step will report warnings whenever
suspicious code has been added. When there is a warning, change the code. That
way another developer later does not need to wonder whether the warning or the
code is correct. GCC has the recommended _-Wall_ and _-Wextra_ options, but it
also has the _-Weffc+_ option, which warns about violations of the style rules
in _Effective C++_ [[Meyers](Resources-and-References.md#scott-meyers)].

Very often code quality improves when it must be compiled on different
platforms and with different compilers. On Linux, there are compilers
available besides GCC, such as [Clang](http://clang.llvm.org/) from the
[LLVM](http://llvm.org/) project and the Intel compiler, and these may find
and report different problems in the source code.

## Use revision control.

There are subversion and git servers already available to use. If any of the
guidelines in this document should be an absolute requirement, this is one of
them. Beyond just using revision control, there are also good guidelines for
commits and commit messages, such as this article [On commit messages](Resources-and-References.md#commit-messages).
[See the [Joel Test](http://joelonsoftware.com/articles/fog0000000043.html), step 1.]
Here are a couple highlights:

- Do not mix cosmetic changes with functional changes. It is hard to see from
  a source code diff what behavior changed if many more source lines differ
  just because of reformatting or reindenting or renaming.
- Commit unrelated fixes separately when feasible. That allows individual
  fixes to be understood separately and also backed out separately.
- Do not "break the build". The trunk revision should always build without
  errors so no one has to fix compile problems just to keep working on their
  own changes. Commit intermediate, build-breaking changes onto a branch.
- Write a descriptive log message. On many projects the log message will be
  emailed automatically to other interested persons, so the log message is an
  easy way to send out a simple notice and explanation of a change.

## Use a logging framework

For the original developer, this may not seem useful at first, but it's value
comes for other developers who later have to learn how the software works. Log
messages can be valuable clues into which parts of the code are doing what
when, and where a problem may be happening.

Also, when software runs remotely, perhaps even autonomously, logs are
invaluable because they can be retrieved by logging into the system or by
email from the field operator. A good log can give important diagnostics more
completely and more accurately than can be relayed over a phone call.

See [Logging Frameworks](Logging-Frameworks.md).

## Use a consistent style

There are many coding styles out there, and we will never settle upon just
one, but there are some good conventions to follow. The important thing is to
pick a style and be consistent. See
[[RAL](Resources-and-References.md#ral-wiki)],
the [Google style guide,](Resources-and-References.md#google-style-guide) and
[[KDE](Resources-and-References.md#kde-policies)] for other ideas about style.
For the record, here is a basic list of good practices in EOL:

- Differentiate class members from local variables with a naming convention.

- Use a naming convention for class methods and functions, such as camel case
  (doThat) or underscores (do_that), and then use the convention consistently.

- Use descriptive names. Do not abbreviate too much or leave out arbitrary
  letters just to have a shorter name.

- Avoid long function definitions.

- Separate interface and implementation. In C++, the header file often can use
  forward declarations rather than including other header files, which
  simplifies dependencies and speeds compilation. When implementations are
  defined in source modules rather than header files, then implementations can
  change without forcing clients of the interface to recompile. Consider using
  the pimpl idiom. For languages like Python and Java which force
  implementation to be defined with interface, use the language to make public
  interface explicit. The Python convention is to use leading underscores for
  private methods.

- Favor spaces over tabs. Indenting by 8 spaces is excessive, 2 or 4 is
  adequate.

- Avoid overcrowding source code. Use spaces around operators.

- Keep source code lines within 80 columns.

- Avoid complicating the flow of an algorithm just to optimize it, unless the
  performance has been measured. The compiler optimizes better than
  programmers. Premature optimization is the root of all evil, and often it is
  also the root of all obfuscation.

## Facilitate code reuse.

There are many existing software implementations that we can use in EOL
software projects. We should take advantage of them to avoid duplicating
effort. We should also write our own code to facilitate its reuse in other EOL
projects. Sometimes tools can help in searching for and identifying existing
code. (At one point EOL had an OpenGrok server which could be used to search
almost all of the EOL software repositories for specific code symbols or
arbitrary text.  A capability like that would still be useful.) And of course
there is no substitute for just asking around, either in person or on the
software engineering mailing lists.

There are many scripts and programs which at first look like one-off tasks,
such as data processing specific to a single field project. We know from
experience that usually a very similar task comes along, so software gets
copied and slightly modified. Code reuse implies avoiding these copies.
Instead, make the scripts modular and configurable so code does not need to be
copied in whole, but instead code can be shared and maintained for multiple
projects and similar tasks. Consolidate similar code into functions,
consolidate functions into libraries and packages, share a single code base
instead of duplicating it.

This is similar to the coding maxim
[Don't Repeat Yourself (DRY)](https://en.wikipedia.org/wiki/Don't_repeat_yourself).
Avoid copy-n-paste of more than a few lines of code.

## Deploy tests and logging as part of production software.

It should be possible to test software in its production environment, using
the same automated tests used in the development environment. Likewise, the
built-in logging capabilities should be available in production and not
disabled or compiled out.

## Document.

Short of mandating formal documentation requirements, it would be prudent to
at least have some documentation goals. There are two types of documentation
to address: programmer guides (API) and user guides. For API, at the minimum,
there are almost effort-less tools now for generating API documentation from
source code comments. These include doxygen, pydoc, sphinx, and javadoc.
Public APIs should be commented, and they may as well be commented in a form
from which online documentation can be generated. For user guides, there is no
obvious answer. Some projects have used wikis effectively, especially when the
wiki content can be downloaded for offline access in the field. The important
point is that users should have documentation for basic operations. For
operating instruments or processing data in the field, it is crucial that
users have convenient and documented methods to verify that the software and
instrument are operating normally. This means the software must support
diagnosis (see logging) and troubleshooting, and the user guide must document
the use and meaning of the diagnostics.

## Do not optimize prematurely.

See all the references on the web about Knuth's quote, the 80/20 rule, and
other challenges to performance metrics. Basically, there is little point to
optimizing code unless it's performance will be measured accurately both
before and after the optimization. Never do for the compiler what the compiler
can do for you. In other words, the compiler may already be optimizing code
that you think appears slow, so optimizing manually is like fighting the
compiler. Don't bother unless you can verify where the compiler actually needs
help.

[Next page: Tools and Technologies](Tools-and-Technologies.md)
