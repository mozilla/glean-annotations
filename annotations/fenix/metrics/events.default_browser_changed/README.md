This event records only when Fenix recognizes that the default browser changed to _Fenix_. We can reliably use this event to understand the occurrence of setting Fenix to the default browser.

See the [event recording code](https://github.com/mozilla-mobile/fenix/blob/6913cd59c9429df6a44cfcc544c9b511c026a134/app/src/main/java/org/mozilla/fenix/HomeActivity.kt#L369), and [associated gating function](https://github.com/mozilla-mobile/fenix/blob/dda6719c32dd8ecdeb7d8516716711dd0018f25a/app/src/main/java/org/mozilla/fenix/utils/Settings.kt#L551).
