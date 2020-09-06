# -*- coding: utf-8 -*-
from collective.faq.interfaces import IFAQ
from collective.faq.interfaces import IFAQItem
from plone import api
from plone.dexterity.browser.view import DefaultView


class FAQView(DefaultView):
    """Defaul view for FAQ content type."""

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

    def nested_item(self, obj):
        return IFAQ.providedBy(obj)


class FAQItemView(DefaultView):
    """Defaul view for FAQ Item content type."""
