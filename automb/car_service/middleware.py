from django.conf import settings 

class MobileMiddleware(object):
    def process_request(self, request):
        subdomain = request.META.get('HTTP_HOST', '').split('.')
        if 'm' in subdomain:
            settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS_MOBILE
        else:
            settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS_DESKTOP