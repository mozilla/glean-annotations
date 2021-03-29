#!/usr/bin/env python

import frontmatter
import json
import os
from collections import defaultdict


ANNOTATIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "annotations")

data = defaultdict(lambda: defaultdict(lambda: {}))

apps = os.listdir(ANNOTATIONS_DIR)
for app in apps:
    for annotation_type in ("metrics", "pings"):
        annotation_dir = os.path.join(ANNOTATIONS_DIR, app, annotation_type)
        if not os.path.isdir(annotation_dir):
            # for some apps, we may have annotations for one annotation type
            # but not another
            continue
        annotation_ids = os.listdir(
            annotation_dir
        )
        for annotation_id in annotation_ids:
            annotation_md = frontmatter.load(
                os.path.join(
                    annotation_dir, annotation_id, "README.md"
                )
            )
            annotation = {"content": annotation_md.content}
            for key in ["component", "features"]:
                if annotation_md.get(key):
                    annotation.update({key: annotation_md[key]})
            data[app][annotation_type][annotation_id] = annotation

print(json.dumps(data))
