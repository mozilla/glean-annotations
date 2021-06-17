# Glean Annotations

[![CircleCI](https://circleci.com/gh/mozilla/glean-annotations.svg?style=svg)](https://circleci.com/gh/mozilla/glean-annotations)

This repository stores user-defined annotations against glean metrics: both those defined in applications (for example, "fenix" aka "Firefox for Android") as well as libraries like [android-components].

The published set of annotations is available at: https://mozilla.github.io/glean-annotations/api.json

Documentation on how this repository works, as well as contribution information, is available at: https://mozilla.github.io/glean-annotations/

[android-components]: https://github.com/mozilla-mobile/android-components

## Local development

In general, the idea behind this repository is that most people will edit annotations from the Glean Dictionary.
However, if you want to do local development the recommended setup process is to create a virtual environment
and install the dependencies inside it. This requires a recent version of python (3.7+):

```bash
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

After creating activating a virtual environment and installing the dependencies, run:

```bash
./scripts/create-api.py > api.json
```

This will create a JSON file which should be the same as the published set of annotations above.
