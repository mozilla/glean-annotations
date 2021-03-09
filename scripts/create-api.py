#!/usr/bin/env python

import frontmatter
import json
import os

# ... process annotations directory, just create one big
# json blob, I think

ANNOTATIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "annotations")

apps = os.listdir(ANNOTATIONS_DIR)
data = {app: {} for app in apps}
for app in apps:
    metrics = os.listdir(os.path.join(ANNOTATIONS_DIR, app))
    for metric in metrics:
        annotation_md = frontmatter.load(os.path.join(ANNOTATIONS_DIR, app, metric, "README.md"))
        annotation = {
            "content": annotation_md.content
        }
        for key in ["component", "features"]:
            if annotation_md.get(key):
                annotation.update({key: annotation_md[key]})
        data[app][metric] = annotation

print(json.dumps(data))
