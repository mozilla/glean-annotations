# Adding metadata

Glean Annotations also allow specifying properties via YAML-based front matter before the markdown-based content.
This is the same approach [used by Jekyll](https://jekyllrb.com/docs/front-matter/) and other systems that process and render markdown.

## Tags

For each annotation, you can specify a list of tags that will be displayed alongside them in the [Glean Dictionary].
For example, consider this annotation for the `addons.enabled_addons` metric in Firefox for Android:

```md
---
tags:
  - WebExtensions
---

This is a stub commentary for the `addons.enabled_addons` metric: please feel free to edit (read the
[contributing guidelines](https://github.com/mozilla/glean-annotations/blob/main/CONTRIBUTING.md)
if you haven't done this before)
```

To prevent the proliferation of arbitrary and/or inconsistent tag data, we require every tag used to be defined
in a per-application metadata schema defined in the root of the application's annotations
(`annotations/<application name>/metadata.yaml`).
Here's the beginning of one we created for Fenix, based off their feature labels:

```yaml
tags:
  Accounts: Corresponds to the [Feature:Accounts](https://github.com/mozilla-mobile/fenix/issues?q=label%3AFeature%3AAccounts)
    label on GitHub.
  AndroidIntegration: Corresponds to the [Feature:AndroidIntegration](https://github.com/mozilla-mobile/fenix/issues?q=label%3AFeature%3AAndroidIntegration)
    label on GitHub.
  ...
```

Here's a link to the [full file](https://github.com/mozilla/glean-annotations/blob/main/annotations/fenix/metadata.yaml), current as of June 2021.

If you wish to add tags to a new application, you need to come up with a similar schema.
Using a set of tags that correspond to what's in your issue tracker is one recommended
approach: that helps create a uniform vocabulary for Telemetry that will feel
familiar to people working in a variety of roles (engineers, product managers, and quality
assurance).

Note that we do not currently support adding tags to libraries used by applications.
However, the Glean Dictionary does render the library name (for example, `glean-core`) alongside any
metrics coming from that library.

## Warnings

You can specify a warning inside the front matter if you want to highlight a caveat within the [Glean Dictionary].
For example, as of this writing we have the following warning in the
[application-wide annotation for Firefox Desktop](https://github.com/mozilla/glean-annotations/blob/d4cb7ac383d9076a9a54f8cec3aa0c525e74a255/annotations/firefox_desktop/README.md):

```md
---
warning: >
  Most Firefox Desktop telemetry is still being collected via the legacy Firefox Telemetry
  collection system. A full list of this telemetry is available in the [probe dictionary](https://probes.telemetry.mozilla.org).
---

Most Firefox Desktop telemetry is still being collected via the legacy Firefox Telemetry
infrastructure and is documented on the [probe dictionary](https://probes.telemetry.mozilla.org).
For updates on the current status, see the [Firefox on Glean](https://firefox-source-docs.mozilla.org/toolkit/components/glean/index.html) documentation.
```

[glean dictionary]: https://dictionary.telemetry.mozilla.org
