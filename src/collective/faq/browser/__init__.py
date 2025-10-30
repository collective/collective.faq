from collective.faq.interfaces import IFAQ
from collective.faq.interfaces import IFAQItem
from plone import api
from plone.dexterity.browser.view import DefaultView
from zope.deprecation import deprecate

import json


class FAQView(DefaultView):
    """Default view for FAQ content type."""

    def _faqs(self):
        return api.content.find(
            context=self.context,
            depth=1,
            object_provides=IFAQ,
            sort_on="getObjPositionInParent",
        )

    def _questions(self, faq):
        return api.content.find(
            context=faq,
            depth=1,
            object_provides=[IFAQItem],
            sort_on="getObjPositionInParent",
        )

    def faqs(self):
        """Return all our FAQ items plus nested FAQs and their items.

        We return a list of dictionaries with 'faq' and 'questions' keys.
        In the first, the faq will be empty: it is the current context
        and we don't want to repeat its title and description.
        """
        # First, our own questions
        faqs = [
            {
                "faq": None,
                "questions": self._questions(self.context),
            }
        ]
        # Then, nested FAQs and their questions
        for faq_brain in self._faqs():
            faq = faq_brain.getObject()
            faqs.append(
                {
                    "faq": faq,
                    "questions": self._questions(faq),
                }
            )
        return faqs

    def jsonld(self):
        """Return JSON-LD representation of the FAQ.

        We only include our own questions, not nested FAQs.
        They will have their own JSON-LD representation on their pages.
        Each question and answer should be in a JSON-LD only once
        per site.
        """
        faq_items = []
        for question_brain in self._questions(self.context):
            question = question_brain.getObject()
            faq_items.append(
                {
                    "@type": "Question",
                    "name": question.title,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": question.answer.output,
                    },
                }
            )
        faq_jsonld = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_items,
        }
        # We don't really need indentation, it can just be on one line.
        # But for readability during debugging, this is much friendlier.
        return json.dumps(faq_jsonld, indent=2)

    @deprecate("This method is only used by an old template. Did you customize it?")
    def questions(self, faq=None):
        provides = [IFAQItem]
        if not faq:
            faq = self.context
            provides += [IFAQ]
        return api.content.find(
            context=faq,
            depth=1,
            object_provides=provides,
            sort_on="getObjPositionInParent",
        )

    @deprecate("This method is only used by an old template. Did you customize it?")
    def nested_item(self, obj):
        return IFAQ.providedBy(obj)


class FAQItemView(DefaultView):
    """Default view for FAQ Item content type."""
