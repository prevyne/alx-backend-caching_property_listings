from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
import json
from django.core.serializers import serialize

@cache_page(60 * 15)
def property_list(request):
    """
    A view that returns all properties, cached at the view level.
    """
    properties = Property.objects.all()
    data = serialize('json', properties)
    return JsonResponse(json.loads(data), safe=False)