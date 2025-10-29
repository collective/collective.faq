from plone.app.relationfield.behavior import IRelatedItems
from plone.indexer.decorator import indexer
from plone.uuid.interfaces import IUUID


@indexer(IRelatedItems)
def getRawRelatedItems(obj):
    result = []
    for relation in obj.relatedItems:
        try:
            to_obj = relation.to_object
            if to_obj:
                uuid = IUUID(to_obj)
                if uuid:
                    result.append(uuid)
        except AttributeError:
            pass
    return result
