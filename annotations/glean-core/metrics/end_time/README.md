This ends up being a string in the data and is not easily parsed into a `DATE` or `TIMESTAMP`, thus there is a 
pre-parsed version that is much easier to use `ping_info.parsed_end_time` when writing queries.

This metric is no longer sent in the usage reporting ping. See [Bug 1929832](https://bugzilla.mozilla.org/show_bug.cgi?id=1929832).