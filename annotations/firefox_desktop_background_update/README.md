As of this writing, the [Firefox Background Updater](https://firefox-source-docs.mozilla.org/toolkit/mozapps/update/docs/BackgroundUpdates.html) is Windows-only.
The data it sends is operational and is not designed to answer questions about user behaviour.

Firefox itself also sends an "update" ping when an update is available and after one has been applied (on all platforms).
This is probably what you'll want to use for most analysis use cases. 
For more information, see the ["update" ping](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/data/update-ping.html) in the Firefox Source Documentation.
