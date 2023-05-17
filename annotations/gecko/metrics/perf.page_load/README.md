**Mar 17, 2023 - May 9, 2023** - Firefox for Android was collecting but not sending `perf.page_load` events during this period. The recorded events started being sent after May 9, 2023 resulting in a spike of events that eventually returned to normal levels. [bug1833178]

Prior to this, `page_load` events were seen in the `pageload` ping in v110, but this was due to a bug. 

Full support of custom pings sent from Gecko in Firefox for Android landed in v113 and hit release on May 9th, coinciding with a spike of events that had previously been collected by not yet sent. 

See the linked [bug1833178] for more information.

[bug1833178]: https://bugzilla.mozilla.org/show_bug.cgi?id=1833178
