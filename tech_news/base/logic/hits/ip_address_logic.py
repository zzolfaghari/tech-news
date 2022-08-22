from base.dal.dao.hits.ip_address_dao import IpAddressDao


class IPAddressLogic:
    def __init__(self):
        super().__init__()
        self.ip_address_dao = IpAddressDao()

    def get_or_save_user_ip_address(self, ip_address):
        return self.ip_address_dao.get_or_save_user_ip_address(ip_address)