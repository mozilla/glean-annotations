The description indicates that this could be divided by the number of baseline pings to get an average tabs open per "session"
but that's no longer accurate since baseline pings are now sent at both foreground and background. Filtering for just baseline
pings with `ping_info.reason="inactive"` should still work for this.
