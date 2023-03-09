===========
Data access
===========

OCTOPUS data can be viewed and exported through a bespoke web interface or accessed directly. For the latter, OCTOPUS database provides web feature service (WFS) allowing users to access database content via third party software such as Geographic Information Systems (GIS), or R language. OCTOPUS data is served by GeoServer [#]_, an open server solution for sharing geospatial data. Unless data from OCTOPUS is explicitly downloaded and locally stored by the user, it will remain cloud-borne, so the user will not have to care about data storage and being up-to-date.

Web interface
------------

*text to come here*

Web Feature Service
-------------------
This user guide and brief demonstration of capabilities outlines how to use WFS through third-party software, specifically `QGIS <https://qgis.org>`__ and/or `R software <https://www.r-project.org/>`__ environment as these software solutions are free, open-source and highly versatile.

WFS in a nutshell
~~~~~~~~~~~~~~~~~
| Geospatial and location information development and standardisation globally is overseen by the Open Geospatial Consortium (OGC) [#]_. Web Feature Service (WFS) is an OGC interface standard that enables platform independent requests for spatial features across the internet. This is accomplished by Geography Markup Language (GML), an XML derivative. Unlike for WMS (Web Map Service), where immutable map tiles are returned, WFS vector entities can be queried, altered, and spatially analysed.
| WFS functionality knows three basal operations - ``GetCapabilities``, ``DescribeFeatureType``, and ``GetFeature``. Calling ``GetCapabilities`` will generate a standardised, human readable meta-dataset that describes a WFS service and its functionality. ``DescribeFeatureType`` produces an overview of supported feature types, and ``GetFeature`` fetches features including their geometry and attribite values, i.e, variable fields.

OCTOPUS v.2 WFS data access via QGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. After opening QGIS, start a new project: *Project > New*
2. In the Browser pane, select WFS/OGC API Features > New Connection…

.. image:: ./images/fig1.png
   :width: 100.0%

3. Name the new connection (e.g., ‘OCTOPUS’) and insert the link http://geoserver.octopusdata.org/geoserver/wfs in the URL field. Click OK. All available OCTOPUS collections will appear in the Browser pane once a connection is established

.. image:: ./images/fig2.png
   :width: 50.0%

4. To add a collection of interest, right click on that collection in the Browser pane and select *Add Layer to Project*. The collection will appear in the Layers pane. Alternatively, click + drag the layer of interest into the Layers pane
5. To locally store a collection, select *Export Layer > To File*
6. Select a file format and specify a file name and save location via the ‘…’ button. Select the coordinate reference system (CRS) of choice; OCTOPUS v.2 collections use EPSG: 3857 (WGS84 Pseudo-Mercator)

.. image:: ./images/fig3.png
   :width: 100.0%

7. To add a saved shapefile to the project, navigate to the *main menu > Layer > Add Layer > Add Vector Layer*. Selecting the .shp, .dbf or .shx file (of the six separate files that constitute the shapefile) will open the collection in the Layers pane

**Excursus. Obtaining obfuscated geographical coordinates in QGIS**

Sites belonging to OCTOPUS data collections SahulArch and FosSahul are potentially culturally sensitive. As a result, coordinates have been obfuscated for these collections using a 25-km radius randomising algorithm. These former point data are represented by polygons now and coordinates are not pushed with the attribute table, or the .csv file if the collection is exported. Follow these steps to obtain obfuscated coordinates (keeping in mind the ≥ 25 km uncertainty) for these collections by calculating polygon centroid points:

1. Navigate to the *main menu > Vector > Geometry Tools > Centroids*\ …
2. Select the collection of interest as the Input Layer, and click Run

.. image:: ./images/fig4.png
   :width: 100.0%

3. To save coordinates, go to the Processing Toolbox pane and select *Vector table > Add X/Y fields to layer*
4. Input Layer should appear as the generated centroids, and the coordinate system must be kept as default EPSG: 4326 – WGS84
5. Click Run. This will generate a new layer, Added Fields, in the Layers pane. In the Attribute Table, fields for ‘x’ (longitude) and
   ‘y’ (latitude) will appear at the end of the table with corresponding coordinates for each point feature

.. image:: ./images/fig5.png
   :width: 100.0%

OCTOPUS v.2 WFS data access via R/RStudio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The below demo R script fetches, via WFS, spatial layers including rich attribute data from OCTOPUS database and generates a scatter plot and an interactive map representation, respectively.

Note - The script requires the below packages. If not installed on your machine yet, run

.. code-block:: r

    install.packages(c("sf","httr","tidyverse","ows4R","viridis", "mapview", dependencies = TRUE))

and you’ll be all set up.

First we’re going to load the required packages

.. code-block:: r

    library(sf) # Simple features support (sf = standardized way to encode spatial vector data)
    library(httr) # Generic web-service package for working with HTTP
    library(tidyverse) # Workhorse collection of R packages for data sciences
    library(ows4R) # Interface for OGC web-services incl. WFS
    library(viridis) # Predefined colorblind-friendly color scales for R

OK, we’re ready to go now. In the following we store the OCTOPUS WFS URL in an object. Then, using the latter, we establish a connection to OCTOPUS database.

.. code-block:: r

    OCTOPUSdata <- "http://geoserver.octopusdata.org/geoserver/wfs" # store url in object
    OCTOPUSdata_client <- WFSClient$new(OCTOPUSdata, serviceVersion = "2.0.0") # connection to db
 
Let’s see what is there, i.e. show all available layer names and titles
 
.. code-block:: r

    OCTOPUSdata_client$getFeatureTypes(pretty = TRUE) # show available layers and titles
    
The above WFS request should yield the following overview

.. code-block:: r

                                               name                                      title
    1                    be10-denude:crn_aus_basins    CRN Australian collection: River basins
    2                   be10-denude:crn_aus_outlets    CRN Australian collection: Sample sites
    3                    be10-denude:crn_int_basins        CRN Global collection: River basins
    4                   be10-denude:crn_int_outlets        CRN Global collection: Sample sites
    5                    be10-denude:crn_xxl_basins             CRN Large basins: River basins
    6                   be10-denude:crn_xxl_outlets             CRN Large basins: Sample sites
    7                 be10-denude:crn_inprep_basins     CRN UOW (in preparation): River basins
    8                be10-denude:crn_inprep_outlets     CRN UOW (in preparation): Sample sites
    9                      be10-denude:publications                   CRN basin bounding boxes
    10                            opengeo:countries                     Countries of the World
    11                           be10-denude:expage                            ExpAge Database
    12 be10-denude:fossahul_webmercator_nrand_25000                          FosSahul Database
    13                    be10-denude:sahularch_osl          Sahul Archaeology: OSL collection
    14                    be10-denude:sahularch_c14  Sahul Archaeology: Radiocarbon collection
    15                     be10-denude:sahularch_tl           Sahul Archaeology: TL collection
    16             be10-denude:sahulsed_aeolian_osl    Sahul Sedimentary Archives: Aeolian OSL
    17              be10-denude:sahulsed_aeolian_tl     Sahul Sedimentary Archives: Aeolian TL
    18             be10-denude:sahulsed_fluvial_osl    Sahul Sedimentary Archives: Fluvial OSL
    19              be10-denude:sahulsed_fluvial_tl     Sahul Sedimentary Archives: Fluvial TL
    20          be10-denude:sahulsed_lacustrine_osl Sahul Sedimentary Archives: Lacustrine OSL
    21           be10-denude:sahulsed_lacustrine_tl  Sahul Sedimentary Archives: Lacustrine TL

**That’s basically it.** Talking to the database via WFS takes three short lines of code. Everything below this line does not deal with data access anymore, but with data presentation. [#]_

**Example 1. Australian 10Be-derived catchment-averaged denudation rates**

Here we fetch and plot Australian catchment-averaged 10Be denudation rates (i.e., layer *‘be10-denude:crn_aus_basins’* from the above list)

.. code-block:: r

    url <- parse_url(OCTOPUSdata) # parse URL into list
    url$query <- list(service = "wfs",
                      version = "2.0.0",
                      request = "GetFeature",
                      typename = "be10-denude:crn_aus_basins",
                      srsName = "EPSG:900913") # set parameters for url$query

    request <- build_url(url) # build a request URL from 'url' list
    CRN_AUS_basins <- read_sf(request) # read simple features using 'request' URL. Takes few secs...

Now that we have the data available, we define our plot parameters. We want to plot denudation rate ("EBE_MMKYR") over average slope gradient ("SLP_AVE") and call the plot (last line)

.. code-block:: r

    myPlot <- ggplot(CRN_AUS_basins, aes(x=SLP_AVE, y=EBE_MMKYR)) + # plot denudation rate over average slope
    geom_errorbar(aes(ymin=(EBE_MMKYR-EBE_ERR), ymax=(EBE_MMKYR+EBE_ERR)), linewidth=0.3, colour="gray80") + # visualise errors
    geom_point(aes(size=AREA, color=ELEV_AVE), alpha=.5) + # scale pts. to "AREA", colour pts. to "ELEV_AVE"
    scale_color_viridis(option="C", direction = -1) + # use 'viridis' colour scale
    scale_size_continuous(range = c(2, 10)) + # define point size range for better visibility
    xlab("Slope gradient [m km^-1]") + ylab("Denudation rate [mm kyr^-1]") + # define label x and y axes
    ggtitle("Australian 10Be catchment-avg. denudation rates") + # make title
    theme(plot.title = element_text(size = 18, face = "bold")) + # title settings
    labs(size = "Catchment \narea [km^2]", colour = "Average \ncatchment \nelevation [m]") # re-label legend
    myPlot # make plot


.. rubric:: Footnotes

.. [#] `http://geoserver.octopusdata.org/ <http://geoserver.octopusdata.org/>`_
.. [#] `https://www.ogc.org <https://www.ogc.org>`_
.. [#] A full description of OCTOPUS database and its collections can be found in a dedicated `Earth Systems Science Data <https://doi.org/10.5194/essd-14-3695-2022>`_ publication.
