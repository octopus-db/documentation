============================
Output table fields & values
============================

| To serve OCTOPUS database collections as geospatial layers via an interactive map :ref:`Web_interface` and to allow for data manipulation via the :ref:`Web_Feature_Service` protocol, data sub-collections are served to GeoServer as a flat data tables, which are described in detail below [#]_.
| When downloading data from OCTOPUS, users are presented with point or polygon geospatial data files with associated attribute tables. Direct connections to the PostgreSQL/PostGIS database are possible upon request. Munack and Codilean (`2022 <https://doi.org/10.5281/zenodo.7352807>`_) provide a complete documentation of the relational database, including a detailed database model diagram and searchable HTML documentation generated using SchemaSpy (https://schemaspy.org, last access: 04 May 2023).

.. note::

  The above section is a modified version of Section 3 from `Codilean et al. 2022 <https://doi.org/10.5194/essd-14-3695-2022>`_

..  _CRN_output:

CRN output
----------
| OCTOPUS CRN 10Be and 26Al data have been recalculated [#]_ so that nuclide concentrations and denudation rates are internally consistent and comparable. These and related data, including concentrations and denudation rates as published, are served as geospatial vector layers (see :ref:`CRN_vector_data`).
| In addition, OCTOPUS CRN collections also provide :ref:`CRN_ancillary_data` comprising **raster layers**, including a *digital elevation model*, *gradient raster*, *flow direction* and *flow accumulation rasters*, *atmospheric pressure raster*, and *CRN production scaling* and *topographic shielding factor* rasters, as well as a set of **structured input data files** (see :ref:`CSV_folder` subsection) for data recalculation integrity. The idea behind the above is that, since the CAIRN algorithm is automated, users can simply publish a DEM of their study area, CRN data files, and CAIRN input files, and denudation rates should be reproducible. 

..  _CRN_vector_data:

CRN vector data
^^^^^^^^^^^^^^^
The vector spatial data uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system.

.. csv-table::
   :file: ./csv_tables/crn_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _CRN_ancillary_data:

CRN ancillary data
^^^^^^^^^^^^^^^^^^

..  _CSV_folder:

'CSV' folder
~~~~~~~~~~~~
* s..._CRNData.csv -- ``description missing``
* s..._CRNRasters.csv -- ``description missing``
* s..._CRNResults.csv -- ``description missing``
* s..._CRONUSInput.txt -- ``description missing``
* s....CRNParam -- ``description missing``

..  _Raster_folder:

'Raster' folder
~~~~~~~~~~~~~~~
The raster data uses the WGS84/UTM projected coordinate reference system, UTM zones depending on the extent and location of each data package.

* s..._atmospres.bil -- Atmospheric pressure grid (raster)
* s..._atmospres.hdr -- *s..._atmospres.bil* header file
* s..._d8flowdir.bil -- Flow direction grid (raster)
* s..._d8flowdir.hdr -- *s..._d8flowdir.bil* header file
* s..._demhydro.bil -- Digital Elevation Model (raster)
* s..._demhydro.hdr -- *s..._demhydro.bil* header file
* s..._flowacc.bil -- Flow accumulation grid (raster)
* s..._flowacc.hdr -- *s..._flowacc.bil* header file
* s..._gradmkm.bil -- Topographic (slope) gradient grid (raster)
* s..._gradmkm.hdr -- *s..._gradmkm.bil* header file
* s..._prodscale.bil -- Cosmogenic nuclide production scaling factor grid (raster)
* s..._prodscale.hdr -- *s..._prodscale.bil* header file
* s..._toposhield.bil -- Topographic shielding grid (raster)
* s..._toposhield.hdr -- *s..._toposhield.bil* header file

.. note::

  Raster files are provided in .bil (**B**\ and **I**\ nterleaved by **L**\ ine) image encoding format, which cannot be considered an image format itself, but is depended on the accompanying header (.hdr) file meaning that users will always need the pair of files with one and the same filename.

..  _SahulArch_output:

SahulArch output
----------------

..  _SahulArch_C14_output:

SahulArch C14 output
^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/arch_c14_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _SahulArch_OSL_output:

SahulArch OSL output
^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/arch_osl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _SahulArch_TL_output:

SahulArch TL output
^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/arch_tl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _SahulSed_output:

SahulSed output
---------------

..  _SahulSed_OSL_output:

SahulSed OSL output
^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/sed_osl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _SahulSed_TL_output:

SahulSed TL output
^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/sed_tl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _FosSahul_output:

FosSahul output
---------------

.. csv-table::
   :file: ./csv_tables/fos_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

..  _expage_output:

ExpAge output
-------------

.. csv-table::
   :file: ./csv_tables/expage_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

.. rubric:: Footnotes

.. [#] The deployed version of GeoServer does not accept dynamically generated PostgreSQL virtual tables (knows as “views”); therefore, the generation of static flat data tables was required to serve the purpose of a view. Newer versions of GeoServer, however, accept materialised views, and an upgrade would present a possible improvement in the database by eliminating the need to store duplicate data.

..
    to do: review ref links and revise references!!!
.. [#] 10Be and 26Al concentrations (atoms g-1) were renormalised to the Nishiizumi 2007 10Be AMS standard (Nishiizumi et al., 2007) and to the Nishiizumi 2004 26Al AMS standard (Nishiizumi, 2004) respectively. Basin-wide denudation rates were recalculated with the open-source program CAIRN (Mudd et al., 2016) with the following parameter settings: (i) nuclide production from neutrons and muons was calculated with the approximation of Braucher et al. (2011) using a sea-level and high-latitude total production rate of 4.3 atoms g-1 yr-1 for 10Be and of 31.1 atoms g-1 yr-1 for 26Al; (ii) latitude and altitude scaling factors were calculated using the time-independent Lal--Stone scaling scheme (Stone, 2000) with atmospheric pressure calculated via interpolation from the National Centers for Environmental Prediction NCEP2 reanalysis data (Compo et al., 2011); and (iii) topographic shielding was calculated from the same digital elevation model (DEM) using the method of Codilean (2006). 