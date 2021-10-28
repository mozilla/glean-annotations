This metric was impacted by [bug 1733757][bzbug] since at least March 2020.
The bug resulted in data not being collected after a certain point.
The data collected up to this point was correctly stored and eventually sent.

The bug was fixed in Glean v42.0.1 and shipped in Fenix Nightly 2021-10-13 and Fenix Beta 94.0.0-beta.3 (2021-10-13).
Data from clients with the fixed Glean version is likely to report higher values for this metric.

All details can be found in the [data incident report][report].

[bzbug]: https://bugzilla.mozilla.org/show_bug.cgi?id=1733757
[report]: https://docs.google.com/document/d/14FWle43oHbDqJUoLBuV7-rEpR0rQyO1caC5j69fRZr8/
