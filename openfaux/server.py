from twisted.python import log
from twisted.web import http, proxy

__author__ = "Yashin Mehaboobe (@sp3ctr3)"


class ProxyClient(proxy.ProxyClient):
    """
    Modify response as well as header here.
    """
    def handleHeader(self, key, value):
        """
        Modify header here
        """
        log.msg("Header: %s: %s" % (key, value))
        proxy.ProxyClient.handleHeader(self, key, value)

    def handleResponsePart(self, buffer):
        """
        Modify buffer to modify response. For example replacing buffer with
        buffer[::-1] will lead to a reversed output. This might cause content
        encoding errors. Currently test only on text only websites
        """
        log.msg("Content: %s" % (buffer,))
        proxy.ProxyClient.handleResponsePart(self, buffer)


class ProxyClientFactory(proxy.ProxyClientFactory):
    protocol = ProxyClient


class ProxyRequest(proxy.ProxyRequest):
    protocols = dict(http=ProxyClientFactory)


class Proxy(proxy.Proxy):
    requestFactory = ProxyRequest


class ProxyFactory(http.HTTPFactory):
    protocol = Proxy
