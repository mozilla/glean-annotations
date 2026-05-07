The `microsurvey` ping is mostly equivalent to the
[messaging-system](https://dictionary.telemetry.mozilla.org/apps/firefox_desktop/pings/messaging-system)
ping. The main difference is that it handles potentially sensitive user inputs,
so it has additional access controls and is recorded with OHTTP. It was designed
to record qualitative user feedback in the form of free write-in responses.

The ping can be accessed through two different datasets:

- The `microsurvey` dataset contains all metrics, including free write-in
  responses (which are highly sensitive as users can input personally
  identifiable information). It is only accessible to members of the
  [microsurvey workgroup](https://protosaur.dev/dawg/workgroup/microsurvey).
- The `microsurvey_redacted` dataset is accessible to all Mozilla employees but
  excludes these sensitive responses.

You can use these datasets exactly like the `messaging-system` dataset. The
following is a list of differences:

- ⚠️ As with the `messaging-system` dataset, `client_id` is not directly
  available. But rather than adding a legacy client id metric like
  `metrics.uuid.messaging_system_client_id`, the ping includes
  `metrics.uuid.microsurvey_impression_id`. This is an entirely different
  identifier. It is unique to a session but does not persist across sessions.
  This means it cannot be joined with other datasets, but it allows funnel
  analysis within the microsurvey dataset.
- `metrics.text.event_input_value` contains the user's free write-in response,
  and is only available in the `microsurvey` dataset, not the
  `microsurvey_redacted` dataset. If you need to access these responses, please
  contact [Shane Hughes](https://people.mozilla.org/p/aminomancer). This dataset
  can only be accessed via BigQuery in the Google Cloud console, and not through
  Looker or Redash.
- Global metadata like `os`, `locale`, and `app_version` are omitted from the
  dataset. However, selected metadata is included in the form of metrics:
  - `metrics.string.microsurvey_os`
  - `metrics.string.microsurvey_os_version`
  - `metrics.quantity.microsurvey_windows_build_number`
  - `metrics.string.microsurvey_app_display_version`
  - `metrics.string.microsurvey_app_channel`
  - `metrics.string.microsurvey_locale`
- Otherwise, the structure of the ping is the same as the `messaging-system`
  ping, and it includes the same fields for `message_id`, `event_context`, etc.

To make your messages record to this ping rather than the `messaging-system`
ping, set the `write_in_microsurvey` field to true in your message definition.
For example:

```jsonc
{
  "id": "EXAMPLE_SURVEY_MESSAGE",
  "template": "feature_callout",
  "content": {
    "write_in_microsurvey": true
    // ...
  }
}
```

Further details about write-in microsurveys are available in the [Messaging System documentation](https://firefox-source-docs.mozilla.org/browser/components/asrouter/docs/feature-callout.html).
