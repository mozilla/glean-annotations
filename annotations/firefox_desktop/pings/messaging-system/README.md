The following is a detailed overview of the different kinds of data we collect
in the Messaging System and the New Tab Page.

# Messaging System pings

These pings record impressions and user interactions for messages served by the
Messaging System.

## Important `client_id` note
All uses of `client_id` in this documentation refer to [`messaging_system_client_id`](https://dictionary.telemetry.mozilla.org/apps/firefox_desktop/metrics/messaging_system_client_id), which is (usually) a copy of 
[`legacy telemetry client ID`](https://dictionary.telemetry.mozilla.org/apps/firefox_desktop/metrics/legacy_telemetry_client_id),
not the [`Glean client ID`](https://dictionary.telemetry.mozilla.org/apps/firefox_desktop/metrics/client_id).
As a result, when wishing to `JOIN` `messaging_system` and `onboarding` with other tables, it will be necessary to `JOIN` on
`metrics.uuid.legacy_telemetry_client_id` (or, in Looker, to use `legacy.telemetry.client_id`)

## Moments page pings

This records when a moments page message has set the user preference for
`browser.startup.homepage_override.once`. Its telemetry policy excludes
`message_id` and `client_id` for Release channel users.

```js
// Release channel
{
  "action": "cfr_user_event"
  "addon_version": "20200225022813"
  "bucket_id": "WNP_THANK_YOU"
  "event": "MOMENTS_PAGE_SET"
  "impression_id": "{d85d2268-b751-9543-b6d7-aad523bf2b26}"
  "experiments": {
    "experiment_1": {"branch": "control"},
    "experiment_2": {"branch": "treatment"}
  },
  "locale": "en-US"
  "message_id": "n/a"
  "source": "CFR"
}

// Prerelease channels and experiment audiences
{
  "source": "CFR",
  "message_id": "WNP_THANK_YOU",
  "bucket_id": "WNP_THANK_YOU",
  "event": "MOMENTS_PAGE_SET",
  "addon_version": "20200225022813",
  "experiments": {
    "experiment_1": {"branch": "control"},
    "experiment_2": {"branch": "treatment"}
  },
  "locale": "en-US",
  "client_id": "21dc1375-b24e-984b-83e9-c8a9660ae4ff"
}
```

## InfoBar pings

This records when the user interacts with an infobar message (messaging row
between the toolbars and the content area). `client_id` is recorded in all
channels.

```js
{
  "experiments": {
    "exp1": {
      "branch": "treatment-a"
    }
  },
  "addon_version": "20210115035053",
  "release_channel": "release",
  "locale": "en-US",
  "event": [
    "IMPRESSION",
    "CLICK_PRIMARY_BUTTON",
    "CLICK_SECONDARY_BUTTON",
    "DISMISSED"
  ],
  "client_id": "c4beb4bf-4feb-9c4e-9587-9323b28c2e50",
  "version": "86",
  "message_id": "INFOBAR_ACTION_86",
  "browser_session_id": "93714e76-9919-ca49-b697-5e7c09a1394f"
}
```

## Spotlight pings

This records impressions and interactions for Spotlight messages. `client_id` is
recorded in all channels.

```js
{
  "experiments": {
    "exp1": {
      "branch": "treatment-a"
    }
  },
  "addon_version": "20210115035053",
  "release_channel": "release",
  "locale": "en-US",
  "event": ["IMPRESSION" | "CLICK" | "DISMISS"],
  "client_id": "c4beb4bf-4feb-9c4e-9587-9323b28c2e50",
  "version": "93",
  "message_id": "SPOTLIGHT_MESSAGE_93",
  "browser_session_id": "93714e76-9919-ca49-b697-5e7c09a1394f"
}
```

## ToastNotification pings

This records when the user interacts with a toast notification: an OS-level
toast notification UI affordance or a pop-up OS-level window. `client_id` is
recorded in all channels. Currently this is only used in experiments.

```js
{
  "experiments": {
    "exp1": {
      "branch": "treatment-a"
    }
  },
  "addon_version": "20210115035053",
  "release_channel": "release",
  "locale": "en-US",
  "event": ["IMPRESSION"],
  "client_id": "c4beb4bf-4feb-9c4e-9587-9323b28c2e50",
  "version": "86",
  "message_id": "TOAST_NOTIFICATION_EXAMPLE_ID",
  "browser_session_id": "93714e76-9919-ca49-b697-5e7c09a1394f"
}
```

## Contextual Feature Recommendation (CFR) pings

### CFR impressions

A CFR impression ping has two forms: one for release channels and private
browsing windows that excludes `client_id` to comply with our data collection
policy, and another for prerelease channels and experiments that includes it.

#### CFR impression for all the prerelease channels and shield experiment

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "action": "cfr_user_event",
  "impression_id": "n/a",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "source": "CFR",
  // message_id could be the ID of the recommendation, such as "wikipedia_addon"
  "message_id": "wikipedia_addon",
  "event": "IMPRESSION"
}
```

#### CFR impression for the release channel and for private browsing windows

```js
{
  "client_id": "n/a",
  "action": "cfr_user_event",
  "impression_id": "{005deed0-e3e4-4c02-a041-17405fd703f6}",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "source": "CFR",
  // message_id should be a bucket ID in the release channel, we may not use the
  // individual ID, such as addon ID, per legal's request
  "message_id": "bucket_id",
  "event": "IMPRESSION"
}
```

### CFR interaction pings

This records the user's interaction with CFR messages.

#### CFR interaction pings for all the prerelease channels and shield experiment

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "action": "cfr_user_event",
  "addon_version": "20180710100040",
  "impression_id": "n/a",
  "locale": "en-US",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "source": "CFR",
  // message_id could be the ID of the recommendation, such as "wikipedia_addon"
  "message_id": "wikipedia_addon",
  "event": ["IMPRESSION" | "INSTALL" | "PIN" | "BLOCK" | "DISMISS" | "RATIONALE" | "LEARN_MORE" | "CLICK" | "CLICK_DOORHANGER" | "MANAGE"],
  // "modelVersion" records the model identifier for the CFR machine learning experiment, see more detail in Bug 1594422.
  // Non-experiment users will not report this field.
  "event_context": "{ \"modelVersion\": \"some_model_version_id\" }"
}
```

#### CFR interaction pings for release channel

```js
{
  "client_id": "n/a",
  "action": "cfr_user_event",
  "addon_version": "20180710100040",
  "impression_id": "{005deed0-e3e4-4c02-a041-17405fd703f6}",
  "locale": "en-US",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "source": "CFR",
  // message_id should be a bucket ID in the release channel, we may not use the
  // individual ID, such as addon ID, per legal's request
  "message_id": "bucket_id",
  "event": ["IMPRESSION" | "INSTALL" | "PIN" | "BLOCK" | "DISMISS" | "RATIONALE" | "LEARN_MORE" | "CLICK" | "CLICK_DOORHANGER" | "MANAGE"],
}
```

### Targeting error pings

This records when an error has occurred when parsing/evaluating a JEXL targeting string in a message.

```js
{
  "client_id": "n/a",
  "action": "asrouter_undesired_event",
  "addon_version": "20180710100040",
  "impression_id": "{005deed0-e3e4-4c02-a041-17405fd703f6}",
  "locale": "en-US",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "message_id": "some_message_id",
  "event": "TARGETING_EXPRESSION_ERROR",
  "event_context": ["MALFORMED_EXPRESSION" | "OTHER_ERROR"]
}
```

### Remote Settings error pings

This records a failure in the Remote Settings loader to load messages into the Messaging System.

```js
{
  "action": "asrouter_undesired_event",
  "client_id": "n/a",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "user_prefs": 7,
  "event": ["ASR_RS_NO_MESSAGES" | "ASR_RS_ERROR"],
  // The value is set to the ID of the message provider. For example: remote-cfr, remote-onboarding, etc.
  "event_context": "REMOTE_PROVIDER_ID"
}
```

## CFR Toolbar Badge interaction pings

This records when a user has seen or clicked a CFR badge/notification in the
browser toolbar in a non-PBM window.

```js
{
  "locale": "en-US",
  "client_id": "9da773d8-4356-f54f-b7cf-6134726bcf3d",
  "version": "70.0a1",
  "release_channel": "default",
  "addon_version": "20190712095934",
  "action": "cfr_user_event",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "source": "CFR",
  "message_id": "FXA_ACCOUNTS_BADGE",
  "event": ["CLICK" | "IMPRESSION"]
}
```

## Firefox Onboarding (about:welcome) pings

These record the telemetry metrics during the Firefox onboarding experience.

### Onboarding impressions

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "version": "76.0a1",
  "locale": "en-US",
  "experiments": {},
  "release_channel": "default",
  "addon_version": "20200330194034",
  "message_id": [
    | "DEFAULT_ABOUTWELCOME"
    | "DEFAULT_ABOUTWELCOME_AW_GET_STARTED"
    | "DEFAULT_ABOUTWELCOME_SITES"
    | "DEFAULT_ABOUTWELCOME_AW_IMPORT_SETTINGS"
    | "DEFAULT_ABOUTWELCOME_AW_CHOOSE_THEME"
    | "RTAMO_DEFAULT_WELCOME"
  ],
  "event": "IMPRESSION",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "event_context": { "page": "about:welcome" },
  "attribution": {
    "source": "mozilla.org",
    "medium": "referral",
    "campaign": "Firefox-Brand-US-Mozilla-Org",
    "content": "test-addon@github.io",
    "experiment": "ua-onboarding",
    "variation": "chrome",
    "ua": "firefox"
  }
}
```

### Onboarding button clicks

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "version": "76.0a1",
  "locale": "en-US",
  "experiments": {},
  "release_channel": "default",
  "addon_version": "20200330194034",
  "message_id": [
    | "DEFAULT_ABOUTWELCOME_AW_GET_STARTED"
    | "DEFAULT_ABOUTWELCOME_AW_IMPORT_SETTINGS"
    | "DEFAULT_ABOUTWELCOME_AW_CHOOSE_THEME"
    | "RTAMO_DEFAULT_WELCOME"
  ],
  "event": "CLICK_BUTTION",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "event_context": { "page": "about:welcome", "source": ["primary_button" | "secondary_button"] },
  "attribution": {
    "source": "mozilla.org",
    "medium": "referral",
    "campaign": "Firefox-Brand-US-Mozilla-Org",
    "content": "test-addon@github.io",
    "experiment": "ua-onboarding",
    "variation": "chrome",
    "ua": "firefox"
  }
}
```

### Onboarding Return-To-AMO install ping

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "version": "76.0a1",
  "locale": "en-US",
  "experiments": {},
  "release_channel": "default",
  "addon_version": "20200330194034",
  "message_id": "RTAMO_DEFAULT_WELCOME",
  "event": "INSTALL",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "event_context": { "page": "about:welcome", "source": "ADD_EXTENSION_BUTTON" },
  "attribution": {
    "source": "mozilla.org",
    "medium": "referral",
    "campaign": "Firefox-Brand-US-Mozilla-Org",
    "content": "test-addon@github.io",
    "experiment": "ua-onboarding",
    "variation": "chrome",
    "ua": "firefox"
  }
}
```

### Onboarding embedded migration interactions

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "version": "76.0a1",
  "locale": "en-US",
  "experiments": {},
  "release_channel": "default",
  "addon_version": "20200330194034",
  "message_id": "MR_WELCOME_DEFAULT_0_AW_IMPORT_SETTINGS_EMBEDDED",
  "event": "CLICK_BUTTION",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "event_context": {
    "page": "about:welcome",
    "source": ["primary_button" | "migrate_close"],
  }
}
```

### Onboarding session end ping

```js
{
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "version": "76.0a1",
  "locale": "en-US",
  "experiments": {},
  "release_channel": "default",
  "addon_version": "20200330194034",
  "message_id": "DEFAULT_ABOUTWELCOME",
  "event": "SESSION_END",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "event_context": {
    "page": "about:welcome",
    "reason": [
      | "welcome-window-closed"
      | "welcome-tab-closed"
      | "app-shut-down"
      | "address-bar-navigated"
    ]
  },
  "attribution": {
    "source": "mozilla.org",
    "medium": "referral",
    "campaign": "Firefox-Brand-US-Mozilla-Org",
    "content": "test-addon@github.io",
    "experiment": "ua-onboarding",
    "variation": "chrome",
    "ua": "firefox"
  }
}
```

### Select checkbox/radio button

Messaging surfaces that use the aboutwelcome bundle can render checkboxes and
radio groups. This is most commonly used in about:welcome and feature callout
microsurveys. The user's selection is not recorded until a button is clicked
that "collects" the selection. This means two events are recorded simultaneously.
The first event would typically be a CLICK event, indicating which button was
pressed to submit the action, and the second event would be a SELECT_CHECKBOX
event, indicating which checkboxes/radio buttons were selected. Checkboxes and
radio buttons must be given unique ids to be distinguished in telemetry.

```ts
{
  "experiments": {},
  "locale": "en-US",
  "version": "145.0a1",
  "release_channel": "default",
  "event": "SELECT_CHECKBOX",
  "event_context": {
    "source": "checkbox-1,checkbox-2" | "radio-1",
    "page": "spotlight" | "about:welcome" | "chrome"
  },
  "message_id": "some_message_id",
  "addon_version": "20221013100028",
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3"
}
```

## Feature Callout pings

Impressions and most interactions in Feature Callouts are handled by the
Onboarding pings above, but since Feature Callouts are inserted into other
content, they have some additional capabilities.

### Page event ping for Feature Callouts

Feature Callout messages can include properties to listen for specific events on
the host page and perform an action when fired. For example, Feature Callouts
pointing to a button can be dismissed when that button is clicked. This metric
records the event type, event target, and action.

```js
{
  "experiments": {},
  "locale": "en-US",
  "version": "107.0a1",
  "release_channel": "default",
  "event": "PAGE_EVENT",
  "event_context": {
    "action": "DISMISS",
    "reason": "CLICK",
    "source": "button.primary#some-button",
    "page": "about:firefoxview"
  },
  "message_id": "FIREFOX_VIEW_TAB_PICKUP_REMINDER",
  "addon_version": "20221013100028",
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3"
}
```

### Feature Callout dismissal

A Feature Callout can be dismissed by clicking its dismiss button directly or
pressing the Escape key. With a page event listener, it can also be configured
to dismiss the callout when an event in the page happens, such as clicking the
target of the callout (see the page event ping above).

```js
{
  "experiments": {},
  "locale": "en-US",
  "version": "108.0a1",
  "release_channel": "default",
  "event": "DISMISS",
  "event_context": {
    "source": [
      "dismiss_button",
      "KEY_Escape",
      "PAGE_EVENT:button.primary#some-button"
    ],
    "page": ["about:firefoxview", "chrome://browser/content/browser.xhtml"]
  },
  "message_id": "some_feature_callout_id",
  "addon_version": "20221013100028",
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3"
}
```

## Nimbus messaging experiment pings

All Firefox Messaging System experiments are deployed via Nimbus, including the
first-run experience (about:welcome), Spotlights, Feature Callouts, and Moments
pages.

### Enrollment & Unenrollment pings

Under the hood, Nimbus makes use of the Normandy API for experiment management.
Therefore, the enrollment and unenrollment pings are collected through the
Normandy counterparts. See the
[`normandy`](https://searchfox.org/mozilla-central/source/toolkit/components/telemetry/Events.yaml#764)
telemetry event category for more details.

### Experiment reach ping

This records whether a branch's targeting and trigger are satisfied for
Messaging System experiments. The branch slug will be recorded in the
`extra_keys` property, and the event `value` will be the experiment slug.

When the specified trigger fires, targeting will be evaluated for each branch,
and each qualified message _other than_ the active branch will be recorded in
this way.

This can be used to measure the reach of a trigger + targeting combination
without actually showing a message
([see here](https://experimenter.services.mozilla.com/nimbus/understanding-the-reach-of-our-triggers-fx112release-part-1/summary) for example).
To measure the reach of targeting without considering the reach of the trigger,
use the `messagesLoaded` trigger, which fires as soon as messages are loaded and
therefore has nearly 100% reach.

Unlike other Messaging System pings, this is a legacy Firefox telemetry event,
and it is sent only for users enrolled in a Messaging System experiment.

```js
{
  "category": "messaging_experiments",
  "method": "reach",
  // message group: ["cfr", "cfr-experiments", "eco", "import-spotlights", "micro-surveys", "moments-pages"]
  "object": "cfr"
  "value": "experiment_slug",
  "extra_keys": {
    "branches": "branch_slug"
  }
}
```

### Experiment attribute errors

This records whether issues were encountered with any of the targeting
attributes used in the experiment enrollment or message targeting. Two different
types of events are sent: `attribute_error` and `attribute_timeout` along with
the attribute that caused it. An attribute is a variable inside the JEXL
targeting expression that is evaluated client side by the browser.

```js
{
  "messaging_experiments",
  "targeting",
  "attribute_error", // event
  "foo", // attribute,
  "extra_keys": {
    "source": "message id or experiment slug",
  },
},
{
  "messaging_experiments",
  "targeting",
  "attribute_timeout", // event
  "bar", // attribute,
  "extra_keys": {
    "source": "message id or experiment slug",
  },
}
```

# New Tab Page pings

These pings are related to the New Tab Page. Although the New Tab Page is
distinct from the Messaging System, it shares some code and telemetry structure.

## New Tab Page user event pings

These pings are captured when a user **performs some kind of interaction** in
the New Tab Page.

### Basic shape

A user event ping includes some basic metadata (tab id, addon version, etc.) as
well as variable fields which indicate the location and action of the event.

```js
{
  // This indicates the type of interaction
  "event": [
    "CLICK",
    "SEARCH",
    "BLOCK",
    "DELETE",
    "IMPRESSION",
    "OPEN_NEW_WINDOW",
    "OPEN_PRIVATE_WINDOW",
    "BOOKMARK_DELETE",
    "BOOKMARK_ADD",
    "OPEN_NEWTAB_PREFS",
    "CLOSE_NEWTAB_PREFS",
    "SEARCH_HANDOFF",
    "SHOW_PERSONALIZE",
    "HIDE_PERSONALIZE"
  ],

  // Optional field indicating the UI component type
  "source": "TOP_SITES",

  // Optional field if there is more than one of a component type on a page.
  // It is zero-indexed.
  // For example, clicking the second Highlight would result in an action_position of 1
  "action_position": 1,

  // Basic metadata
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "action": "activity_stream_event",
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "user_prefs": 7
}
```

### Types of user interactions

#### Show/hide Personalization Panel

```js
{
  "event": ["SHOW_PERSONALIZE" | "HIDE_PERSONALIZE"], // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Performing a search

```js
{
  "event": "SEARCH",

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Performing a search handoff

```js
{
  "event": "SEARCH_HANDOFF",

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Clicking a top site item

```js
{
  "event": "CLICK",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "card_type": ["pinned" | "search" | "spoc"],
    "icon_type": ["screenshot_with_icon" | "screenshot" | "tippytop" | "rich_icon" | "no_image" | "custom_screenshot"],
    // only exists if its card_type = "search"
    "search_vendor": "google"
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Clicking a top story item

```js
{
  "event": "CLICK",
  "source": ["CARDGRID" | "CARDGRID_WIDGET"],
  "action_position": 2,
  "value": {
    // "spoc" for sponsored stories, "organic" for regular stories.
    "card_type": ["organic" | "spoc" | "topics_widget"],
    // topic and position only exists if its card_type = "topics_widget"
    "topic": "entertainment"
    // The index position of the topic link within the card
    "position_in_card": 0
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Clicking a popular topic link

```js
{
  "event": "CLICK",
  "source": "POPULAR_TOPICS",
  "value": {
    "topic": ["must-reads" | "productivity" | "health" | "finance" | "technology" | "more-recommendations"]
  }
  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Adding a search shortcut

```js
{
  "event": "SEARCH_EDIT_ADD",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "search_vendor": "google"
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Showing privacy information

```js
{
  "event": "SHOW_PRIVACY_INFO",
  "source": "TOP_SITES",
  "action_position": 2,

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Clicking on privacy information link

```js
{
  "event": "CLICK_PRIVACY_INFO",
  "source": "DS_PRIVACY_MODAL",

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Deleting a search shortcut

```js
{
  "event": "SEARCH_EDIT_DELETE",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "search_vendor": "google"
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Deleting an item from history

```js
{
  "event": "DELETE",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "card_type": "pinned",
    "icon_type": ["screenshot_with_icon" | "screenshot" | "tippytop" | "rich_icon" | "no_image" | "custom_screenshot"]
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Blocking a site

```js
{
  "event": "BLOCK",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "card_type": ["pinned" | "search" | "spoc"],
    "icon_type": ["screenshot_with_icon" | "screenshot" | "tippytop" | "rich_icon" | "no_image" | "custom_screenshot"],
    // only exists if its card_type = "search"
    "search_vendor": "google"
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Bookmarking a link

```js
{
  "event": "BOOKMARK_ADD",
  "source": "HIGHLIGHTS",
  "action_position": 2,
  "value": {
    "card_type": "trending"
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Removing a bookmark from a link

```js
{
  "event": "BOOKMARK_DELETE",
  "source": "HIGHLIGHTS",
  "action_position": 2,
  "value": {
    "card_type": "bookmark"
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Opening a link in a new window

```js
{
  "event": "OPEN_NEW_WINDOW",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "card_type": "pinned",
    "icon_type": ["screenshot_with_icon" | "screenshot" | "tippytop" | "rich_icon" | "no_image" | "custom_screenshot"]
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Opening a link in a new private window

```js
{
  "event": "OPEN_PRIVATE_WINDOW",
  "source": "TOP_SITES",
  "action_position": 2,
  "value": {
    "card_type": "pinned",
    "icon_type": ["screenshot_with_icon" | "screenshot" | "tippytop" | "rich_icon" | "no_image" | "custom_screenshot"]
  }

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Opening the new tab preferences pane

```js
{
  "event": "OPEN_NEWTAB_PREFS",

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Closing the new tab preferences pane

```js
{
  "event": "CLOSE_NEWTAB_PREFS",

  // Basic metadata
  "action": "activity_stream_event",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Changing preferences from about:preferences#home or on the customize menu on the newtab page.

```js
{
  "event": "PREF_CHANGED",
  "source": ["TOP_STORIES" | "POCKET_SPOCS" | "HIGHLIGHTS" | "TOP_SITES" | "SPONSORED_TOP_SITES"],
  "value": "{\"status\":true|false,\"menu_source\":\"ABOUT_PREFERENCES|CUSTOMIZE_MENU\"}"
  "release_channel": "default",
  "experiments": {},
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "user_prefs": 7
}
```

#### Pinning a tab

```js
{
  "event": "TABPINNED",
  "source": "TAB_CONTEXT_MENU",
  "value": "{\"total_pinned_tabs\":2}",

  // Basic metadata
  "action": "activity_stream_user_event",
  "client_id": "aabaace5-35f4-7345-a28e-5502147dc93c",
  "version": "67.0a1",
  "addon_version": "20190218094427",
  "locale": "en-US",
  "user_prefs": 59,
  "page": "n/a",
  "session_id": "n/a",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3"
}
```

#### Adding or editing a new TopSite

```js
{
  "event": "TOP_SITES_EDIT",
  "source": "TOP_SITES_SOURCE",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  // "-1" Is used for prepending a new TopSite at the front of the list, while
  // any other possible value is used for editing an existing TopSite slot.
  "action_position": [-1 | "0..TOP_SITES_LENGTH"]
}
```

#### Requesting a custom screenshot preview

```js
{
  "event": "PREVIEW_REQUEST",
  "browser_session_id": "e7e52665-7db3-f348-9918-e93160eb2ef3",
  "source": "TOP_SITES"
}
```

## New Tab Page session end pings

When a session ends, the browser will send a `"activity_stream_session"` ping to our metrics servers. This ping contains the length of the session, a unique reason for why the session ended, and some additional metadata.

### Basic event

All `"activity_stream_session"` pings have the following basic shape. Some fields are variable.

```js
{
  "action": "activity_stream_session",
  "client_id": "26288a14-5cc4-d14f-ae0a-bb01ef45be9c",
  "session_id": "005deed0-e3e4-4c02-a041-17405fd703f6",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "session_duration": 4199,
  "profile_creation_date": 14786,
  "experiments": {
    "experiment_1": { "branch": "control" },
    "experiment_2": { "branch": "treatment" }
  },
  "user_prefs": 7
}
```

### What causes a session end?

Here are different scenarios that cause a session end event to be sent:

1. After a search
2. Clicking on something that causes navigation (top site, highlight, etc.)
3. Closing the browser
4. Refreshing
5. Navigating to a new URL via the url bar or file menu

### Session performance data

This data is held in a child object of the `activity_stream_session` event called `perf`. All fields suffixed by `_ts` are type `DOMHighResTimeStamp` (aka a double of milliseconds, with a 5 microsecond precision) with 0 being the [timeOrigin](https://developer.mozilla.org/en-US/docs/Web/API/DOMHighResTimeStamp#The_time_origin) of the browser's hidden chrome window.

An example might look like this:

```js
perf: {
  // Timestamp of the action perceived by the user to trigger the load
  // of this page.
  //
  // Not required at least for error cases where the
  // observer event doesn't fire
  "load_trigger_ts": 1,

  // What was the perceived trigger of the load action:
  "load_trigger_type": [
    "first_window_opened" | // home only
    "menu_plus_or_keyboard" | // newtab only
    "unexpected" // sessions lacking actual start times
  ],

  // when the page itself receives an event that document.visibilityStat=visible
  "visibility_event_rcvd_ts": 2,

  // When did the topsites element finish painting?  Note that, at least for
  // the first tab to be loaded, and maybe some others, this will be before
  // topsites has yet to receive screenshots updates from the add-on code,
  // and is therefore just showing placeholder screenshots.
  "topsites_first_painted_ts": 5,

  // The 6 different types of TopSites icons and how many of each kind did the
  // user see.
  "topsites_icon_stats": {
    "custom_screenshot": 0,
    "screenshot_with_icon": 2,
    "screenshot": 1,
    "tippytop": 2,
    "rich_icon": 1,
    "no_image": 0
  },

  // The number of Top Sites that are pinned.
  "topsites_pinned": 3,

  // The number of search shortcut Top Sites.
  "topsites_search_shortcuts": 2,

  // How much longer the data took, in milliseconds, to be ready for display
  // than it would have been in the ideal case. The user currently sees placeholder
  // cards instead of real cards for approximately this length of time. This is
  // sent when the first call of the component's `render()` method happens with
  // `this.props.initialized` set to `false`, and the value is the amount of
  // time in ms until `render()` is called with `this.props.initialized` set to `true`.
  "highlights_data_late_by_ms": 67,
  "topsites_data_late_by_ms": 35,

  // Whether the page is preloaded or not.
  "is_preloaded": [true|false],
}
```

## New Tab Page Top Story pings

When Top Story (currently powered by Pocket) is enabled in Activity Stream, the browser will send following `activity_stream_impression_stats` to our metrics servers.

### Impression stats

This records all the Pocket recommended articles (a list of `id`s) when the user opens a newtab.

```js
{
  "impression_id": "{005deed0-e3e4-4c02-a041-17405fd703f6}",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "source": "pocket",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "user_prefs": 7,
  "window_inner_width": 1000,
  "window_inner_height" 900,
  "experiments": {
    "experiment_1": {"branch": "control"},
    "experiment_2": {"branch": "treatment"}
  },
  "tiles": [{"id": 10000}, {"id": 10001}, {"id": 10002}]
}
```

### Click/block/save_to_pocket ping

This records the user's interaction with those Pocket tiles.

```js
{
  "impression_id": "{005deed0-e3e4-4c02-a041-17405fd703f6}",
  "addon_version": "20180710100040",
  "locale": "en-US",
  "source": "pocket",
  "page": ["about:newtab" | "about:home" | "about:welcome" | "unknown"],
  "experiments": {
    "experiment_1": {"branch": "control"},
    "experiment_2": {"branch": "treatment"}
  },
  "user_prefs": 7,
  "window_inner_width": 1000,
  "window_inner_height" 900,

  // "pos" is the 0-based index to record the tile's position in the Pocket section.
  // "shim" is a base64 encoded shim attached to spocs, unique to the impression from the Ad server.
  "tiles": [{"id": 10000, "pos": 0, "shim": "enuYa1j73z3RzxgTexHNxYPC/b,9JT6w5KB0CRKYEU+"}],

  // A 0-based index to record which tile in the "tiles" list that the user just interacted with.
  "click|block|pocket": 0
}
```

## Save to Pocket button pings

Right now the save to Pocket button, while technically outside of newtab, has some similarities with the newtab telemetry.

These pings record user interaction with the save to Pocket button.

### Click/impression ping

```js
{
  "locale": "en-US",
  "version": "83.0a1",
  "release_channel": "default",
  "model": "",
  "events": [
    {
      "action": "click|impression|unpin",
      "position": 0,
      "source": ["recs_learn_more" | "view_list" | "home_view_list" | "home_topic" | "home_discover" | "save_button" | "home_button" | "on_save_recs" | "learn_more" | "sign_up_1" | "sign_up_2" | "log_in"]
    }
  ],
  "pocket_logged_in_state": true | false,
  "impression_id": "{005deed0-e3e4-4c02-a041-17405fd703f6}",
  "profile_creation_date": 18550
}
```
