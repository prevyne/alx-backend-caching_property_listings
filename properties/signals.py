from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property
import logging

@receiver([post_save, post_delete], sender=Property)
def invalidate_property_cache(sender, instance, **kwargs):
    """
    Invalidates the 'all_properties' cache key whenever a Property
    is created, updated, or deleted.
    """
    cache_key = 'all_properties'
    if cache.has_key(cache_key):
        cache.delete(cache_key)
        logging.info(f"Cache invalidated for '{cache_key}' due to model change.")