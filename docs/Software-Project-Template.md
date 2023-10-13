# Software Project Template

This is a template for an overview and checklist of a software development
project. The intention is to provide a quick summary and an index of important
links.

There is a table rendition of this checklist for the CAMS project:
[CAMS LabVIEW Software Development](https://wiki.ucar.edu/display/camssoftware).

## Software Project Overview Template (SPOT) Fields

### Name:

Example: Hello World

### Description:

Example: As part of the observation sensing network, this software will
monitor hardware sensors and display "Hello World" whenever the instrument is
being observed by someone, and otherwise it will do nothing.

### Inception date:

Just to give some idea of the age of the project.

### Current status:

Use this to distinguish lifecycle phases, from inception to active development
to maintenance. The status fields used in the software inventory might already
suffice for this.

### Release information:

Give the current version, if any, where downloads are available, perhaps
upcoming release dates.

### Software process:

Identify the parts of the software guideline chosen to be followed for this
project, or name a specific process to be followed, like XP or TDD or pair
programming. The point is not to restrict or formalize the process, only to
think about it ahead of time and to give developers on the project a picture
of how the process should work.

### Revision control links:

Provide URLs to subversion or git repositories for this software which
developers and others should use to access the source.

### Links to other software artifacts:

For example, this could be links to web documentation or wiki pages for
discussion.

### Developers:

List the programmers on this project, who are not necesarily all software
engineers.

### Users:

Name the intended users of this software. Again, the idea is to be clear and
complete about for whom the software needs to work. This could be only a few
specific people if it's a one-off data analysis, or it could be the entire
research radar community. The users will be scientists or engineers or
technicians or the general public, but almost absolutely the users will not be
just other software engineers.

### Domain experts:

Name specific people who will consult on technical matters related to the
software's domain. This could be one or several people. The domain experts may
also be users, but not necessarily. These are the people the developers must
go to to resolve questions about the requirements, the problem being solved,
or the vocabulary and concepts specific to the domain. If the software will
process radar data, the domain experts likely will include a radar scientist
or engineer. In many cases the developers might also be considered domain
experts. The point is that software development requires intimate
understanding of the problem domain, and it's important to recognize the role
of domain expert and to rely on that resource for development.

### Requirements overview:

For simple projects, just state the requirements. For larger projects, provide
a link to the requirements discussion or documentation. Obviously it is
important to be able to state the requirements to keep the big picture in mind
and as a check on the direction of development. For iterative agile
development processes, these are not the requirements of each individual
development stage. These are the guides by which the final product will be
judged whether it works or not.

### Design overview:

Provide the basic approach to the design or a link to it. As for requirements,
this just gives an idea of the fundamental design. The larger the project, the
more complicated this can be. Note that it is useful to document critical
design alternatives which were considered but rejected.

### Security issues:

Don't forget to think about security implications: data security (including
redundancy and access restrictions), system reliability, operator
authentication, logging and auditing, user privacy, and so on.

### Related projects:

Name projects or provide links to projects which are similar or somehow
related to this project. It's important to think about this to identify what
parts of the problem might have already been solved or to find out what has
been learned from past mistakes.

### Implementation overview:

These are nuts and bolts questions to answer at the beginning of the project.
They give an idea of the development and deployment environments, and they are
a checklist for infrastructure which should be in place when the project
begins.

### Programming languages:

C++, Java, Ruby, Perl, Python, ad infinitum

### Platforms:

Linux embedded, Linux desktop, web server, Windows, Mac, ...

### Data formats:

### GUI framework:

### Build system:

Examples: SCons, make, qmake, automake, cmake, Visual Studio, ...

### Sources for test data:

It is important to identify test data from the start, since sometimes it will
take a while to obtain them, and sometimes the design of the instrument and
the software must specifically be designed to accommodate test data. Virtually
all EOL software projects will either consume or produce data, or both, and
there must be some way to verify the operation initially, then later also
verify that maintenance and improvements do not produce unexpected results.
For research instruments collecting one-chance-only observational data in the
field, it is especially critical that data not be lost or munged on their way
through software.  
Having test data easily accessible, perhaps even packaged with the software,
makes it easier for others to try out the software and run their own tests.

### Test frameworks:

There are many testing frameworks and utilities available. Even if a specific
framework is not chosen, it should be possible to identify how tests will be
automated, such as with scripts or built into the program.

### Other frameworks and libraries:

Examples: Boost, OpenDDS, Qwt, Netcdf, Jambi, and so on.

### Links to automated build (CIT) reports:

Examples: buildbot

### Links to issue tracker:

This is a reminder to setup a place to record problem reports and feature
requests. Once that's created, this is a convenient place to put a link to it.  
Examples: JIRA Bugzilla Github

