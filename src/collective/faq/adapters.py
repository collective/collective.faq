from collective.faq.interfaces import IFAQItem
from Products.CMFPlone.patterns.settings import PatternSettingsAdapter

import json


class RestrictedTinyMCEPatternSettingsAdapter(PatternSettingsAdapter):
    """Adapter to provide restricted TinyMCE pattern settings.

    We want this for the 'answer' field of an FAQ Item.

    This is an adapter on: context, request, field.
    We could define this for context IFAQItem, but then it does not work on
    the 'add' form, because there the context is the FAQ folder.
    """

    def tinymce(self):
        """Return custom pattern options for TinyMCE.

        From upstream we get:

            {"data-pat-tinymce": json.dumps(configuration)}

        Google Search displays the following HTML tags:
        <h1> through <h6>, <br>, <ol>, <ul>, <li>, <a>, <p>,
        <div>, <b>, <strong>, <i>, and <em>.
        All other tags are ignored.  See
        https://developers.google.com/search/docs/appearance/structured-data/faqpage

        It may be fine if other tags are visible on the page,
        but here we configure TinyMCE to be very strict.

        We completely hide the menubar (with View, Insert, etc).
        We restrict the toolbar.  Especially no 'styleselect' menu.
        """
        result = super().tinymce()
        if self.field.interface != IFAQItem:
            return result
        key = "data-pat-tinymce"
        json_config = result.get(key)
        if not json_config:
            return result
        configuration = json.loads(json_config)
        # Now modify the configuration as needed.
        tiny = configuration.get("tiny")
        if not tiny or not isinstance(tiny, dict):
            return result
        tiny["toolbar"] = 'ltr rtl | undo redo | bold italic | bullist numlist | h1 h2 h3 h4 | unlink plonelink'
        tiny["menubar"] = ""
        result[key] = json.dumps(configuration)
        return result
