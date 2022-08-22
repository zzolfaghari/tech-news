from base.models import Category, IPAddress


class IpAddressDao:
    def __init__(self):
        super().__init__()

    def get_or_save_user_ip_address(self, ip_address):
        ip_address = IPAddress.objects.get_or_create(ip_address=ip_address)
        return ip_address[0]
