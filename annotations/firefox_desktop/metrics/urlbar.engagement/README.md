**Question 1:** When an engagement event is sent, regardless of engagement_type, does the urlbar menu of results collapse so that the user has to start over in a new search?

**Answer 1:** It depends on the engagement. The results panel remains open when these engagement types occur: dismiss, inaccurate_location, not_interested, not_relevant, show_less_frequently
  Of those types, not only does the panel stay open, the suggestion also remains present for the following: inaccurate_location, show_less_frequently
  That means it's possible for more than one engagement to occur with a suggestion while the panel remains open. e.g., `inaccurate_location` followed by `click`, or `show_less_frequently` followed by `not_interested`.
  For all other engagement types not listed above, the results panel closes.

**Question 1:** What is the difference between `selected_result='addon'` and `selected_result='addon_experimental'`? Why is `addon_experimenntal` a valid value for `selected_result`, but not in the `results` string?

**Answer 1:** `addon`: Used for extensions that use the [omnibox WebExtensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox). There are a number of these out in the wild, so this value will show up in the data occasionally.
  `experimental_addon`: Used for extensions created by the Firefox Search Engineering Team using the experimental urlbar WebExtensions API. We don’t actually use this API anymore or create extensions with it. It’s how we used to implement experiments several years ago. No plans to start using it again. Should not appear in the data.
   
    
