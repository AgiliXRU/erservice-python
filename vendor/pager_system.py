from vendor.pager_transport import PagerTransport


class PagerSystem(object):
    @classmethod
    def get_transport(cls):
        return PagerTransport()

    def close_transport(self, transport):
        raise RuntimeError("represents a vendor class requiring install on server")
