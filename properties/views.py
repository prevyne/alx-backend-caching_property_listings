# properties/views.py

from django.http import JsonResponse
from .utils import get_all_properties
import json
from django.core.serializers import serialize

def property_list(request):
    """
    A view that returns all properties using low-level queryset caching.
    """
    properties = get_all_properties()
    data = serialize('json', properties)
    return JsonResponse(json.loads(data), safe=False)