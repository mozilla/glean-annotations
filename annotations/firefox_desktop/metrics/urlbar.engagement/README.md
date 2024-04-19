**Question 1:** When an engagement event is sent, regardless of engagement_type, does the urlbar menu of results collapse so that the user has to start over in a new search?

**Answer 1:** It depends on the engagement. The results panel remains open when these engagement types occur: dismiss, inaccurate_location, not_interested, not_relevant, show_less_frequently
  Of those types, not only does the panel stay open, the suggestion also remains present for the following: inaccurate_location, show_less_frequently
  That means it's possible for more than one engagement to occur with a suggestion while the panel remains open. e.g., `inaccurate_location` followed by `click`, or `show_less_frequently` followed by `not_interested`.
  For all other engagement types not listed above, the results panel closes.

**Question 2:** What is the difference between `selected_result='addon'` and `selected_result='addon_experimental'`? Why is `addon_experimenntal` a valid value for `selected_result`, but not in the `results` string?

**Answer 2:** `addon`: Used for extensions that use the [omnibox WebExtensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox). There are a number of these out in the wild, so this value will show up in the data occasionally.
  `experimental_addon`: Used for extensions created by the Firefox Search Engineering Team using the experimental urlbar WebExtensions API. We don’t actually use this API anymore or create extensions with it. It’s how we used to implement experiments several years ago. No plans to start using it again. Should not appear in the data.

**Question 3:** What is the difference between `suggest_sponsor` vs (`merino_adm_sponsored` + `rs_adm_sponsored`)?

**Answer 3:** `suggest_sponsor` is on Firefox 113 and earlier and includes sponsored suggestions from both Merino and remote settings. In 114, `suggest_sponsor` was replaced with `merino_adm_sponsored` and `rs_adm_sponsored`, which break out the suggestion source, either Merino or remote settings.

**Question 4:** What is the difference between `suggest_non_sponsor` vs (`merino_wikipedia` + `rs_adm_nonsponsored`)?

**Answer 4:** `suggest_non_sponsor` is on Firefox 113 and earlier and includes non-sponsored suggestions (a.k.a. "expanded Wikipedia") from both Merino and remote settings. In 114, `suggest_non_sponsor` was replaced with `merino_adm_nonsponsored` and `rs_adm_nonsponsored`. In all cases, "non-sponsored" means expanded Wikipedia.
  `merino_wikipedia` is dynamic Wikipedia. There is no `rs_` version because by their nature these suggestions are provided only by Merino.

**Question 5:** What does `merino_top_picks` mean?

**Answer 5:** In Firefox 114+, it refers to navigational suggestions.

**Question 6:** How do we identify Dynamic Wikipedia suggestions?

**Answer 6:** Dynamic Wikipedia was recorded as `dynamic_wikipedia` in 113, which is the version that the dynamic Wikipedia experiment targeted. In 114 and later, it's recorded as `merino_wikipedia`. 

**Question 7:** How does the search session end for each `engagement_type` value?

**Answer 7:**
- For `click`, `enter`, `go_button`: the user has selected one of the results displayed in the panel. The panel closes and the selected result page loads.
- For `drop_go`, `paste_go`: the user has dropped or pasted text into the URLbar
  and immediately navigated to it (either a URL, or a SERP if the text was interpreted as a search query). The results panel did not open and no results were shown. The `selected_result` type is `input_field`.
- For `help`: the user has selected "Learn More" from the meatball menu next to one of the results displayed in the panel. The panel closes and a support page loads.
- For `dismiss`,  `not_interested`, `not_relevant`: the user has selected an option from the meatball menu next to one of the results displayed in the panel. The panel stays open. The affected result is removed from the panel, but the current search string and other results remain in view. The search session has not ended.
- For `inaccurate_location`, `show_less_frequently`: the user has selected an option from the meatball menu next to one of the results displayed in the panel. The panel stays open, and the current search string and all results remain in view. The search session has not ended.


| Date       | Note   |
| ---------- | ------ |
| 2024-03-19 | The urlbar event telemetry was rolled out worldwide. Initially, it was only enabled in the US. You may see a spike in the volume of urlbar events as a result. |

