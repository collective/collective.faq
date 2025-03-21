"""Module where all interfaces, events and exceptions live."""

from collective.faq import _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectivefaqCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFAQ(model.Schema):
    """FAQ content type interface."""


class IFAQItem(Interface):
    """FAQ Item content type interface."""

    title = schema.TextLine(
        title=_("Question"),
        required=True,
    )

    detailed_question = schema.Text(
        title=_("Detailed Question"),
        description=_("More details on the question, if not evident from the title"),
        required=False,
    )

    answer = RichText(
        title=_("Answer"),
        description=_("Meaningful sentences that explains the answer"),
        required=False,
    )
