from ccxtws.poloniex import poloniex, poloniex_observer  # noqa: F401
from ccxtws.biki import biki, biki_observer  # noqa: F401
from ccxtws.huobipro import huobipro, huobipro_observer  # noqa: F401
from ccxtws.gateio import gateio, gateio_observer  # noqa: F401

exchanges_ws = [
    'poloniex', 'poloniex_observer',
    'biki', 'biki_observer',
    'huobipro', 'huobipro_observer',
    'gateio', 'gateio_observer',
]

__all__ = exchanges_ws