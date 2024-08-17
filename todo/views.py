import random
from django.http import JsonResponse
from .models import MyModel

def image_urls_view(request):
    # Get all instances of MyModel
    instances = MyModel.objects.all()

    # Check if there are any instances
    if not instances:
        return JsonResponse({'error': 'No images available'}, status=404)

    # Choose a random instance
    instance = random.choice(instances)

    # Generate the URL for the chosen instance
    image_url = request.build_absolute_uri(instance.upload.url)

    # Return the URL as a JSON response
    return JsonResponse({'name': instance.name, 'image_url': image_url})
