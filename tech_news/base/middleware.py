from .logic.hits.ip_address_logic import IPAddressLogic


class SaveIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_address_logic = IPAddressLogic()
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        ip_address = self.ip_address_logic.get_or_save_user_ip_address(ip_address=ip)
        request.user.ip_address = ip_address

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
