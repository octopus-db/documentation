===========
Data access
===========

.. _installation:

Web interface
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

OCTOPUS v.2 Web Feature Service (WFS) - A user guide and brief demonstration of capabilities
--------------------------------------------------------------------------------------------

This user guide outlines how to use WFS through third-party software, specifically `QGIS <https://qgis.org>`__ and/or `R software <https://www.r-project.org/>`__ environment as these software solutions are free, open-source and highly versatile.

WFS in a nutshell
~~~~~~~~~~~~~~~~~
| Geospatial and location information development and standardisation globally is overseen by the Open Geospatial Consortium (OGC). Web Feature Service (WFS) is an OGC interface standard that enables platform independent requests for spatial features across the internet. This is accomplished by Geography Markup Language (GML), an XML derivative. Unlike for WMS (Web Map Service), where immutable map tiles are returned, WFS vector entities can be queried, altered, and spatially analysed.
| WFS functionality knows three basal operations - ``GetCapabilities``, ``DescribeFeatureType``, and ``GetFeature``. Calling ``GetCapabilities`` will generate a standardised, human readable meta-dataset that describes a WFS service and its functionality. ``DescribeFeatureType`` produces an overview of supported feature types, and ``GetFeature`` fetches features including their geometry and attribite values, i.e, variable fields.
  
