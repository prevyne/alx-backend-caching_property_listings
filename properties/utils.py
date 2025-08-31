# properties/utils.py

from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_all_properties():
    """
    Retrieves all properties from the cache if available,
    otherwise fetches from the database and caches the result.
    """
    cache_key = 'all_properties'
    properties = cache.get(cache_key)

    if properties is None:
        logging.info("Cache miss for 'all_properties'. Fetching from DB.")
        properties = Property.objects.all()
        # Cache for 1 hour (3600 seconds)
        cache.set(cache_key, properties, 3600)
    else:
        logging.info("Cache hit for 'all_properties'. Serving from Redis.")

    return properties

def get_redis_cache_metrics():
    """
    Connects to Redis to retrieve and analyze cache performance metrics.
    """
    try:
        # Get the raw Redis connection client
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        # Extract hits and misses
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total = hits + misses

        # Calculate hit ratio, avoiding division by zero
        hit_ratio = (hits / total) * 100 if total > 0 else 0

        metrics = {
            'hits': hits,
            'misses': misses,
            'total_lookups': total,
            'hit_ratio_percent': f"{hit_ratio:.2f}%"
        }

        logging.info(f"Redis Cache Metrics: {metrics}")
        return metrics
    except Exception as e:
        logging.error(f"Could not connect to Redis to get metrics: {e}")
        return None