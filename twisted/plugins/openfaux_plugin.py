from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.web import server

import openfaux


class Options(usage.Options):
    optParameters = [["port", "p", 8080, "The port to listen on."]]


class OpenFauxServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "openfaux"
    description = "OpenFaux data collector server"
    options = Options

    def makeService(self, options):
        return internet.TCPServer(int(options["port"]),
            server.Site(openfaux.server.ProxyFactory()))

serviceMaker = OpenFauxServiceMaker()
