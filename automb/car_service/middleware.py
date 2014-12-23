from django.conf import settings 

class MobileMiddleware(object):
    def process_request(self, request):
        settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS_DESKTOP
        subdomain = request.META.get('HTTP_HOST', '').split('.')
        if 'm' in subdomain:
            settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS_MOBILE
            return
        else:
            #for test
            port=request.META.get('SERVER_PORT')
            if port=='8000':
                settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS_MOBILE
            else:
                settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS_DESKTOP


