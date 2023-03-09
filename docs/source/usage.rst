===========
Data access
===========

OCTOPUS data can be viewed and exported through a bespoke web interface or accessed directly. For the latter, OCTOPUS database provides web feature service (WFS) allowing users to access database content via third party software such as Geographic Information Systems (GIS), or R language. OCTOPUS data is served by GeoServer [#]_, an open server solution for sharing geospatial data. Unless data from OCTOPUS is explicitly downloaded and locally stored by the user, it will remain cloud-borne, so the user will not have to care about data storage and being up-to-date.

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
| Geospatial and location information development and standardisation globally is overseen by the Open Geospatial Consortium (OGC) [#]_. Web Feature Service (WFS) is an OGC interface standard that enables platform independent requests for spatial features across the internet. This is accomplished by Geography Markup Language (GML), an XML derivative. Unlike for WMS (Web Map Service), where immutable map tiles are returned, WFS vector entities can be queried, altered, and spatially analysed.
| WFS functionality knows three basal operations - ``GetCapabilities``, ``DescribeFeatureType``, and ``GetFeature``. Calling ``GetCapabilities`` will generate a standardised, human readable meta-dataset that describes a WFS service and its functionality. ``DescribeFeatureType`` produces an overview of supported feature types, and ``GetFeature`` fetches features including their geometry and attribite values, i.e, variable fields.

OCTOPUS WFS data access via QGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. After opening QGIS, start a new project: *Project > New*
2. In the Browser pane, select WFS/OGC API Features > New Connection…

.. image:: ./images/fig1.png
   :width: 100.0%

3. Name the new connection (e.g., ‘OCTOPUS’) and insert the link http://geoserver.octopusdata.org/geoserver/wfs in the URL field.
|  Click OK. All available OCTOPUS collections will appear in the Browser pane once a connection is established

.. image:: ./images/fig2.png
   :width: 50.0%

4. To add a collection of interest, right click on that collection in the Browser pane and select *Add Layer to Project*. The collection will appear in the Layers pane. Alternatively, click + drag the layer of interest into the Layers pane
5. To locally store a collection, select *Export Layer > To File*
6. Select a file format and specify a file name and save location via the ‘…’ button. Select the coordinate reference system (CRS) of choice; OCTOPUS v.2 collections use EPSG: 3857 (WGS84 Pseudo-Mercator)

.. image:: ./images/fig3.png
   :width: 100.0%

7. To add a saved shapefile to the project, navigate to the *main menu > Layer > Add Layer > Add Vector Layer*.
|  Selecting the .shp, .dbf or .shx file (of the six separate files that constitute the shapefile) will open the collection in the Layers pane


  
.. rubric:: Footnotes

.. [#] `http://geoserver.octopusdata.org/ <http://geoserver.octopusdata.org/>`_
.. [#] `https://www.ogc.org <https://www.ogc.org>`_
