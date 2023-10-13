# Development Process

This section outlines phases and infrastructure related to the software
development lifecycle, but not a sequential timeline.

## Requirements

Rather than suggest a specific requirements discovery process, here are some
issues that should always be considered when identifying the requirements for
an EOL software project. These are not necessarily important for all EOL
software, but they should not be overlooked. For example, for data-critical
applications, the requirements must address data integrity and redundancy.
High-bandwidth applications must identify the total throughput needed, so the
throughput can be tested and verified.

As part of the requirements process, it is especially important to identify
the users, since users must be involved in defining the requirements. In other
words, a requirement can be posed as a question, and the users and domain
experts should answer it, not the developer. (Unless the developer is a user
also, of course.) The intended users also impact the target platforms,
implementation language, and dependencies.

As a practical implication, users should be invited to any meeting where
requirements will be discussed.
[[HFSD](Resources-and-References.md#head-first)] and
[[FOWLER](Resources-and-References.md#uml-distilled)] have straightforward
explanations of the necessity and value of close user involvement for
iterative requirements analysis and development.

Some statement of requirements is necessary for any size of development, large
or small. Larger developments will have more requirements, but they do not
need to be specified all at once. Instead they may be discovered as part of an
iterative process. The important thing is that they be defined and documented
along the way, so the software can be developed with the correct requirements
in mind, ideally to the point of developing tests to verify the requirements.

Writing use cases and user stories is good practice for elucidating
requirements. They can be written from the user's point of view, and they only
present the behavior expected by users without being biased by design or
implementation. It is natural to describe software by telling a story about
what it does and how the functionality will be used. Stories also force
consideration of error handling from the user's point of view: how should the
application and user interact when an error case occurs?

Here is a list of requirements to consider, in no particular order:

- **software lifetime**: How long will the software be needed? This
  requirement distinguishes the one-off fixes from longer term software
  infrastructure.
- **external support**: Does the software need to be deployed for users
  outside of EOL?
- **target platforms**: Does the software need to run on multiple platforms,
  embedded or not, particular operating systems, and so on? Is there a
  requirement for data portability between architectures?
- **data security**: How robust and redundant does the data manipulation and
  storage need to be? Raw data recording obviously needs stricter data
  security requirements than reprocessing software, but someone still needs to
  decide how many backups are enough.
- **access security**: Do user authentication and authorization need to be built
  into the software?
- **monitoring**: How will users and operators monitor the status and progress
  of the software?
- **auditing**: When processing data, what metadata will be preserved and
  augmented and tracked?
- **data formats**: What data file formats must be supported for input and
  output?
- **error recovery**: Does the software need to be able to recover quickly
  from problems, such as during field operations? Perhaps it needs to save
  checkpoints and be able to resume from the last checkpoint. What errors need
  to be detected automatically and how will the operator be alerted?
- **data throughput**: What is the minimum data throughput requirement? Even
  post-processing software may have a throughput requirement, if the users
  want to process field project data in hours instead of days.
- **algorithm flexibility**: Some software may need special accommodation to
  support alternative and evolving algorithms.
- **configuration**: How flexible does the software configuration need to be?
  Will it operate for different field projects, test modes, and instrument
  modes?  Will different users need to run it with their own customizations?
  Where will it get configuration settings and metadata?

## Design

In any software project, there are many alternative designs which all meet the
requirements. The challenge for developers is finding a design which meets the
requirements but also can be implemented, communicated, maintained, and
elaborated as effectively as possible. The software abstraction should map
well to the domain, and the language and concepts in the design should
facilitate communication about the problem rather than confuse it. Thus
documentation of the design is important.

One best practice seems to be a coherent and consistent partition of the
problem into logical components, a basic block diagram, following as closely
as possible the vocabulary of the problem domain. The partitioning then maps
directly to the namespaces and symbol names used in the code. A design
document or block diagram describes the components, their responsibilities,
and their collaborations, and as such it serves as an overview of the design
as well as a guide to the symbols in the source code.

UML diagramming tools can be helpful here, but so far the experience with them
in EOL is limited. As more EOL developers become familiar with UML notation,
it will be more feasible to share and discuss designs through UML diagrams.

## Design reviews

Software design reviews have not really been tried in EOL, but they still seem
like a good idea. As an action item from this report, we should make an effort
to hold design reviews before anything is implemented, even if the review is
informal.

Typically, the participants in design reviews will be other developers, as
well as perhaps a domain expert to help clarify the requirements. That said,
EOL software designs often must compromise between requirements. For example,
there may be trade-offs between bandwidth available on the current hardware
versus new software that would be needed for new hardware. Also, the priority
of each requirement must be decided by the users. (For iterative developments,
this relates to selecting which feature to implement in the next iteration.)
For these reasons, users often need to be involved in design reviews also.

An iterative development will have multiple reviews, one for each iteration of
the design.

## Documentation

Documentation is part of both process and infrastructure. There are certain
aspects to a software development that should be documented before coding
should continue:

- Requirements
- Design
- User experts
- Guidelines checklist
- Project home page

For smaller projects (or small iterations), the requirements may be just a
statement about objective, and the design documentation may not be very
involved either. However, even a small project requires decisions about
implementation language, data formats, GUI framework (or not), basic classes,
and so on. As part of the design documentation, it is helpful to document
critical design choices which were rejected rather than only the choices which
were selected.

The domain experts are the stakeholders in the software and those who will
know the most about whether the software is accurately modeling the
application domain. Usually the domain experts are obvious, but it helps to
name them explicitly in the documentation, since they are important references
for the software developers. As the wisdom goes, software analysis does not
happen unless a domain expert is involved.
[[FOWLER](Resources-and-References.md#uml-distilled)]

An example has been created for the checklist, linked below:

- [Software Project Template](Software-Project-Template.md)

The purpose of the checklist is to communicate to others, clarify who has a
role in the development and what that role is, provide a quick overview for
those not directly involved in the project, and provide a single point of
reference for project status and all artifacts of the project. Filling in a
checklist assures that important infrastructure is planned for and taken care
of ahead of time, such as revision control, wiki pages (or wherever the
project checklist will reside), issue tracking, and so on.

Note that for an iterative development, where features are implemented in
incremental changes to working software, all of the above documentation
requirements still hold. Before a new feature can be implemented, requirements
should state what the feature will do, there must be a design in mind for the
feature, and user experts must have been consulted about the feature.

## Code reviews

This is another idea from industry, promoted as beneficial and worth the
effort, which EOL has never really tried. Emails on code commits allow for
sporadic code review of a sort, and we have the Crucible code review tool
available in EOL, but we're not taking full advantage of this. The report
[Software Practice in the Ptolemy
Project](http://ptolemy.eecs.berkeley.edu/publications/papers/99/sftwareprac/)
is very positive about code reviews, and the experience there should be very
relevant to EOL.

As a minimal guideline, since every project should be using revision control,
every project should likewise be taking advantage of commit emails. Setting up
emails on code changes is convenient, and it greatly boosts communication and
awareness between developers as far as notifying everyone exactly what is
happening in the source tree.

## Releases

Software releases are very ad hoc at the moment across all the projects. We
need to adopt a more consistent process for software release. To avoid
confusion, the process should be the same for users both inside and outside
EOL, even if some software is only available within EOL. More formal releases
make for more consistent software quality and revision tracking "in the wild".
It also eases the maintenance burden on users, especially "unintended side
effects" when production software is upgraded without warning and at arbitrary
times. A release should be tagged, tested, packaged, advertised, available,
and supported. Release announcements and release notes should be in a single
location on the web. Release notes should include a summary of what has
changed in the release.

## Acceptance or bug-fix phase

All software when first released goes through a phase where users first start
using it, learning it, and discovering bugs in it. We may as well identify
this phase and work to make it go smoothly. Many open-source projects (GCC,
KDE, Linux Kernel) have a bug-fix-only phase, where work on new features stops
in favor of fixing all of the high-priority bugs. This phase can be helped by
running (and passing!) tests to verify requirements as well as regression
tests to prevent bugs from recurring. Perhaps EOL developments don't warrant a
formal or even an informal acceptance phase, but all projects should plan to
spend time focusing exclusively on fixing bugs. [See the
[Joel Test](Resources-and-References.md#joel-test), step 5.]

## Maintenance

In many ways maintenance is its own step in the software development process.
Porting to new environments or OS revisions likely does not require analysis
or design, but it does require development time. It is difficult to predict
the resources needed for maintenance, but some maintenance issues can be seen
coming. For example, external dependencies may go away or change (Qt4),
formats may change (netcdf 4), hardware may change (64-bit), and new
technologies may need to be adopted (web, rpm).

## Pair programming

Pair programming is a technique from agile software development where two
programmers work simultaneously developing code, side-by-side at the console,
each with a specific role. It has been used in EOL before, but otherwise there
has been little experience with it. Pair programming may be a good way to
spread and encourage "good coding habits", besides the potential for producing
better code.

## Share programming

This is an idea to increase cooperation, collaboration, and mentoring
opportunities among EOL programmers by purposely sharing development projects
among multiple developers. Unlike pair programming, programmers can still code
separately, but they cooperate on the same project and the same source tree.
For example, instead of two developers each working alone on a single project,
two developers could share development on two projects.

As a general rule, programmers should not hesitate to seek discussion with
other programmers to help solve a problem or share techniques. This practice
can guard against the single point of failure problem. When only one
programmer works on software, then support and fixes fall on that programmer,
and that can be a bottleneck. If instead more than one programmer is familiar
with the software, then support can be distributed. This may be an item to
address explicitly in the project checklist. A project should decide ahead of
time how critical cross-training and distributed support will be for the
success of the software. If it is critical, then shared programming or other
practices could be employed to spread out the support responsibilities.

## Code sprints

Sprints have proved useful in EOL as a way to focus a group of people for a
short period on solving a particular problem.

[Next page: Code Sprints](Code-Sprints.md)
