from zc.relation.interfaces import ICatalog
from zope.component import getUtility

import logging


logger = logging.getLogger(__name__)


def update_related_items(context):
    """Upgrade step to update the related items in the catalog.

    We look for all objects that have the relatedItems relation field,
    and reindex the getRawRelatedItems index for them.  Also update their
    metadata, so the getRawRelatedItems metadata column is updated as well.
    """
    relation_catalog = getUtility(ICatalog)
    if not relation_catalog:
        logger.warning("Relations catalog not found.")
        return
    logger.info("Looking for objects with related items.")
    for number, relation in enumerate(
        relation_catalog.findRelations({"from_attribute": "relatedItems"}), 1
    ):
        try:
            source_obj = relation.from_object
            print("Reindexing object:", source_obj)
            if source_obj:
                source_obj.reindexObject(idxs=["getRawRelatedItems"], update_metadata=1)
        except AttributeError:
            pass
        if number % 1000 == 0:
            logger.info(
                "Updated getRawRelatedItems for %d objects so far...",
                number,
            )
    logger.info("Updated getRawRelatedItems for all objects.")
