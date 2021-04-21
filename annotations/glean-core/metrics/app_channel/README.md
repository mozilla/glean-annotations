Can't be used by most mobile products to signify the channel since app stores require separate application ids per channel.

On Firefox Desktop this represents the channel the binary was built on,
not the channel the profile asks for updates on.
This means that
[Release Candidate (RC)](https://firefox-source-docs.mozilla.org/contributing/pocket-guide-shipping-firefox.html#rc)
builds served to beta-channel profiles will temporarily make it look as though there are few beta clients and somewhat more release clients.
This will appear in channel-based analyses as a seasonal population shift with a period of the release cadence
([usually four weeks](https://wiki.mozilla.org/RapidRelease/Calendar)).
