class PagerTransport(object):

    def initialize(self):
        raise RuntimeError("represents a vendor class requiring install on server")

    def transmit(self, target_device, page_text):
        raise RuntimeError("represents a vendor class requiring install on server")

    def transmit_requiring_acknowledgement(self, target_device, page_text):
        raise RuntimeError("represents a vendor class requiring install on server")