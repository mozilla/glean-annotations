# Contributing to the Glean Annotations Repository

Thank you for your interest in contributing to the Glean Annotations. This
document tries to codify some best practices for contribution to this
repository.

## Participation guidelines

All communication (on Slack and Matrix, on mailing lists, and in pull requests and issues) is expected to follow the [Mozilla Community Participation Guidelines](https://www.mozilla.org/about/governance/policies/participation/).
For more information, see the [code of conduct document](./CODE_OF_CONDUCT.md)
in the root of this repository.

## Creating new annotations

There are two recommended workflows for adding new annotations to this repository:

1. Via the Metric's commentary section in the [Glean Dictionary](https://dictionary.protosaur.dev). This
   will either create a new markdown document for you to put information in or allow you to modify the
   existing one. When you're happy with your changes, convert your changes into a pull request. After
   it is merged, your annotations should appear in the Glean Dictionary within a day.
2. By directly adding a README.md (or a set of them) to the repository. Be sure to use the same application
   and metric identifiers as used in the Glean Dictionary, or your annotations will not be picked up. If
   you need help with this, [feel free to ask](https://docs.telemetry.mozilla.org/concepts/getting_help.html).

At the moment, there are no strong guidelines on what content should be in an annotations file. Include
whatever you think might be helpful to someone looking at a metric in the context of an analysis.

That said, there are a couple of points to bear in mind:

1. The people reading your annotation will come from a diverse set of backgrounds: in language,
   culture, experience, and role as Mozillians. Avoid using flowery prose and unnecessary
   jargon. The
   [guidelines for writing content for docs.telemetry.mozilla.org](https://docs.telemetry.mozilla.org/contributing/style_guide.html)
   may be helpful reading.
2. These annotations are in a public repository which is world readable. Avoid putting
   in partner-specific information which is under NDA or anything otherwise sensitive.
   Generally speaking, information on how our software behaves is innocuous and fine to
   talk about, so don't over-rotate on this: talking about how we use data
   in public forums helps build trust with our community. It's ok to put in links to dashboards
   or other resources which are private (behind SSO), but please mark them as such and prefer
   public references where they exist.
