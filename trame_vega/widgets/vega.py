from trame_client.widgets.core import AbstractElement
from trame_vega import module

try:
    from trame_client.encoders.numpy import encode

    has_numpy = True
except ImportError:
    has_numpy = False


def no_encoding(_data):
    return _data


ENCODER = encode if has_numpy else no_encoding


class Figure(AbstractElement):
    """
    Create a Vega figure viewer element

    :param figure: Altair figure to show (default: None)

    >>> component1 = Figure(figure=fig1)
    >>> component2 = Figure()
    >>> component2.update(fig1)
    """
    _next_id = 0

    def __init__(self, figure=None, **kwargs):
        Figure._next_id += 1
        self._key = f"trame__vega_{Figure._next_id}"

        super().__init__("vue-vega", **kwargs)
        if self.server:
            self.server.enable_module(module)

        self._attributes["name"] = f'name="{self._key}"'
        self._attributes["spec"] = f':spec="{self._key}"'
        self._figure = figure
        self.update()

    def update(self, figure=None, **kwargs):
        """
        Update the `Figure <https://altair-viz.github.io/index.html>`_ with new content

        :param figure: Altair chart object
        """
        if figure:
            self._figure = figure

        if self._figure:
            self.server.state[self._key] = ENCODER(self._figure.to_dict())

    @property
    def key(self):
        """Return the name of the state variable used internally"""
        return self._key

    @staticmethod
    def to_data(chart, **kwargs):
        """
        Serialize altair chart
        """
        return ENCODER(chart.to_dict())


__all__ = [
    "Figure",
]
