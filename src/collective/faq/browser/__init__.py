from AccessControl.SecurityManagement import getSecurityManager
from collective.faq.interfaces import IFAQ
from collective.faq.interfaces import IFAQItem
from plone import api
from plone.dexterity.browser.view import DefaultView
from zope.deprecation import deprecate


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
        questions = api.content.find(
            context=faq,
            depth=1,
            object_provides=[IFAQItem],
            sort_on="getObjPositionInParent",
        )
        results = []
        if not questions:
            return results
        checkPermission = getSecurityManager().checkPermission
        for brain in questions:
            # We have brains, but we need the real objects for the answer,
            # detailed question, and related items.
            obj = brain.getObject()
            related = []
            results.append({"question": obj, "related": related})
            for relation in obj.relatedItems:
                if relation.isBroken():
                    continue
                target_obj = relation.to_object
                if not checkPermission("View", target_obj):
                    continue
                related.append(target_obj)
        return results

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
