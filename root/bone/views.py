'''from django.views import View
from django.http import JsonResponse

# Create your views here.

class JetCheck(View):
    def get(self, request):
        data = {
            'success': True,
            'method': str(request.method).lower(),
            'message': 'Alion API. Stay away.',
        }
        return JsonResponse(data, status=200)
'''
