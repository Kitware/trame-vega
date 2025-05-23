.. |pypi_download| image:: https://img.shields.io/pypi/dm/trame-vega

Vega visual grammar for trame |pypi_download|
===========================================================================

.. image:: https://github.com/Kitware/trame-vega/actions/workflows/test_and_release.yml/badge.svg
    :target: https://github.com/Kitware/trame-vega/actions/workflows/test_and_release.yml
    :alt: Test and Release

trame-vega extend trame **widgets** with a Figure component that is capable of rendering Vega grammars such as `Altair <https://altair-viz.github.io/>`__ plots.

Installing
-----------------------------------------------------------

trame-vega can be installed with `pip <https://pypi.org/project/trame-vega/>`_:

.. code-block:: bash

    pip install --upgrade trame-vega


Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/guide/tutorial>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.


License
-----------------------------------------------------------

trame-vega is made available under the BSD-3 License. For more details, see `LICENSE <https://github.com/Kitware/trame-vega/blob/master/LICENSE>`_
This license has been chosen to match the one use by `Vega <https://github.com/vega/vega/blob/main/LICENSE>`_ and `Altair <https://github.com/altair-viz/altair/blob/master/LICENSE>`_
which are either used within that trame widget or will be use by the user to create the content for those Figures.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.


Example: Vega + Altair
-----------------------------------------------------------

The Python interface of `Altair provide examples <https://altair-viz.github.io/>`__ on how to create various visualization.

.. code-block:: python

    import altair as alt
    from vega_datasets import data

    from trame.widgets import vega

    # Generate chart
    source = data.cars()
    fig = (
        alt.Chart(source)
        .mark_circle()
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            color="Origin:N",
        )
        .properties(width=200, height=200)
        .repeat(
            row=["Horsepower", "Acceleration", "Miles_per_Gallon"],
            column=["Miles_per_Gallon", "Acceleration", "Horsepower"],
        )
        .interactive()
    )

    # Display it
    widget = vega.Figure(figure=None) # could pass fig at construction
    widget.update(fig) # or update later


JavaScript dependency
-----------------------------------------------------------

This Python package bundle the ``vega@5.27.0``, ``vega-embed@6.24.0`` and ``vega-lite@5.16.3`` JavaScript libraries. If you would like us to upgrade it, `please reach out <https://www.kitware.com/trame/>`_.
        
