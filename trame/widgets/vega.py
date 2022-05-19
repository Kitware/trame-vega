from trame_vega.widgets.vega import *


def initialize(server):
    from trame_vega import module

    server.enable_module(module)
