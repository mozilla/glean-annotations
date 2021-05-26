Can't be used by most mobile products to signify the channel since app stores require separate application ids per channel.

On Firefox Desktop versions 89 and earlier this represents the channel the binary was built on,
not the channel the profile asks for updates on.
This means that
[Release Candidate (RC)](https://firefox-source-docs.mozilla.org/contributing/pocket-guide-shipping-firefox.html#rc)
builds served to beta-channel profiles will temporarily make it look as though there are few beta clients and somewhat more release clients.
This will appear in channel-based analyses as a seasonal population shift with a period of the release cadence
([usually four weeks](https://wiki.mozilla.org/RapidRelease/Calendar)).

On Firefox Desktop versions 90 and later this represents the channel the profile asks for updates on.
This means that RC builds served to beta-channel profiles will still report
"beta" even though they were built with the release build configuration.
For more details, see [bug 1710664](https://bugzilla.mozilla.org/show_bug.cgi?id=1710664).
