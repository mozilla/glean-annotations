#!/usr/bin/env python

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
        data[app][metric] = open(
            os.path.join(ANNOTATIONS_DIR, app, metric, "README.md")
        ).read()

print(json.dumps(data))