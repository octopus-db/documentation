============================
Output table fields & values
============================

| To serve OCTOPUS database collections as geospatial layers via an interactive map :ref:`Web_interface` and to allow for data manipulation via the :ref:`Web_Feature_Service` protocol, data sub-collections are served to GeoServer as a flat data tables, which are described in detail below [#]_.
| When downloading data from OCTOPUS, users are presented with point or polygon geospatial data files with associated attribute tables. Direct connections to the PostgreSQL/PostGIS database are possible upon request. Munack and Codilean (`2022 <https://doi.org/10.5281/zenodo.7352807>`_) provide a complete documentation of the relational database, including a detailed database model diagram and searchable HTML documentation generated using SchemaSpy (https://schemaspy.org, last access: 04 May 2023).

.. note::

  The above section is a modified version of Section 3 from `Codilean et al. 2022 <https://doi.org/10.5194/essd-14-3695-2022>`_

CRN output
----------

.. csv-table::
   :file: ./csv_tables/crn_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

SahulArch output
----------------

SahulArch C14 output
^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/arch_c14_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

SahulArch OSL output
^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/arch_osl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

SahulArch TL output
^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/arch_tl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".


SahulSed output
---------------

SahulSed OSL output
^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/sed_osl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

SahulSed TL output
^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/sed_tl_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".


FosSahul output
---------------

.. csv-table::
   :file: ./csv_tables/fos_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

expage output
-------------

.. csv-table::
   :file: ./csv_tables/expage_output.csv
   :header-rows: 1

.. tip::

  For detailed field / variable descriptions follow the links given under "Origin (Alias)".

.. rubric:: Footnotes

.. [#] The deployed version of GeoServer does not accept dynamically generated PostgreSQL virtual tables (knows as “views”); therefore, the generation of static flat data tables was required to serve the purpose of a view. Newer versions of GeoServer, however, accept materialised views, and an upgrade would present a possible improvement in the database by eliminating the need to store duplicate data.