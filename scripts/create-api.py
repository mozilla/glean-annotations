#!/usr/bin/env python

import copy
import json
import os
import re
import sys
from collections import defaultdict

import frontmatter
import yaml

from constants import ANNOTATIONS_DIR

STMO_QUERIES_RE = [
    re.compile(r"(https://sql.telemetry.mozilla.org/queries/([0-9]+)[^\s\.]*)"),
    re.compile(r"(https://sql.telemetry.mozilla.org/dashboard/([A-z\-]+)[^\s\.]*)"),
]

data = defaultdict(lambda: defaultdict(lambda: {}))

apps = os.listdir(ANNOTATIONS_DIR)


def linkify(text):
    """
    Gives bare URLs and additional context

    This saves effort when writing annotations. Currently only handles
    STMO URLs
    """
    for stmo_pattern in STMO_QUERIES_RE:
        text = stmo_pattern.sub(
            r"[STMO#\2](\1)🔒",
            text,
        )
    return text


def read_annotation(filename, annotation_type, valid_tags=None):
    annotation_md = frontmatter.load(filename)

    # use everything in the YAML frontmatter
    annotation = copy.copy(annotation_md.metadata)

    # only specify commentary if we actually have some
    if annotation_md.content.strip():
        annotation["commentary"] = linkify(annotation_md.content)

    tags = annotation_md.get("tags")
    if tags and annotation_type != "app":
        invalid_tags = [tag for tag in tags if tag not in valid_tags]
        if invalid_tags:
            sys.stderr.write(
                f"Invalid tags found in {filename}: {invalid_tags}; "
                f" if these should be accepted values, update annotations/{app}/metadata.yaml"
            )
            sys.exit(1)

    return annotation


for app in apps:
    try:
        data[app]["app"] = read_annotation(
            os.path.join(ANNOTATIONS_DIR, app, "README.md"), "app"
        )
    except FileNotFoundError:
        # no top-level annotation for this application
        pass

    app_dir = os.path.join(ANNOTATIONS_DIR, app)
    valid_tags = []
    try:
        metadata = yaml.load(open(os.path.join(app_dir, "metadata.yaml")))
        data[app].update(metadata)
        valid_tags = metadata.get("tags", []).keys()
    except:
        pass
    for annotation_type in ("metrics", "pings"):
        annotation_dir = os.path.join(app_dir, annotation_type)
        if not os.path.isdir(annotation_dir):
            # for some apps, we may have annotations for one annotation type
            # but not another
            continue
        annotation_ids = os.listdir(annotation_dir)
        for annotation_id in annotation_ids:
            data[app][annotation_type][annotation_id] = read_annotation(
                os.path.join(annotation_dir, annotation_id, "README.md"),
                annotation_type,
                valid_tags,
            )

print(json.dumps(data))
