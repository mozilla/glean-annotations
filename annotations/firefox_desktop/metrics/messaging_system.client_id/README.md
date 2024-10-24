IMPORTANT NOTE: this is the [legacy telemetry client ID](https://dictionary.telemetry.mozilla.org/apps/firefox_desktop/metrics/legacy_telemetry_client_id),
not the [Glean client ID](https://dictionary.telemetry.mozilla.org/apps/firefox_desktop/metrics/client_id).
As a result, when wishing to`JOIN` `messaging_system` and `onboarding` with other tables, it will be necesssary to `JOIN` on
`metrics.uuid.legacy_telemetry_client_id` (or, in Looker, to use `legacy.telemetry.client_id`)

Note that this `client_id` may or may not be present in all cases. Here is [the policy code](https://searchfox.org/mozilla-central/search?q=symbol:TelemetryFeed%23createASRouterEvent&redirect=true) that applies per-surface policies to telemetry which regulate the contents of `client_id` (and certain other metrics).
