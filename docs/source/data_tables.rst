============================
Data tables and their fields
============================
OCTOPUS data tables, using a spatial allegory, can be grouped into a *global*, a *regional*, and a *local* level. While :ref:`Global_tables` can serve any database relation, :ref:`Regional_tables` should be seen as thematic tables matching certain sub-collections. Finally, :ref:`Local_tables` are collection specific tables with a high degree of specialisation compared to the two aforementioned higher-level table groups.

PostgreSQL data types, constraints, and foreign key principles are comprehensibly described in the PostgreSQL online documentation (https://www.postgresql.org/docs/15/datatype.html). Another excellent, more introductory read is Michael J. Hernandez' *Database design for Mere Mortals - A Hands-On Guide to Relational Database Design*.

.. note::

    To ensure database integrity, every OCTOPUS db relation features a "CREATED_AT" (= *record timestamp* with timezone based on UTC) and a "UPDATED_AT" (= *timestamp of record update* with timezone based on UTC) field, respectively. These fields are automatically populated upon db trigger, however, are not displayed as part of this documentation for the sake of readability.

..  _Global_tables:

Global tables
-------------
This section features information about :ref:`Global_lookup_tables` (i.e., indexed arrays of certain data recurring across the entire database), :ref:`Global_georeferencing_tables` (i.e., tables that store information about the spatial context of an observation), and :ref:`Global_references_tables`. The latter relations form the part of OCTOPUS db that allows for definite identification of data sources resp. publications.

..  _Global_lookup_tables:

Global lookup tables
~~~~~~~~~~~~~~~~~~~~

The following tables serve various collections across the entire OCTOPUS database.

..  _global_varunitID:

global_varunitID table
^^^^^^^^^^^^^^^^^^^^^^
The *global_varunitID* table stores **variable units** for those compilations whose values involve different units of measurement. Data tables with invariant variable units, however, do not feature explicit units fields. *global_varunitID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/global_varunitID.csv
   :header-rows: 1

* V_UNITID -- A unique identifier (auto-incrementing serial integer)

* V_UNITABBR -- Unique abbreviation of "V_UNITNAME". For available values refer to :ref:`global_varunitID_Fields`

* V_UNITNAME -- Unit name. For available values refer to :ref:`global_varunitID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "V_UNITID" [#]_


..  _global_GrainSize:

global_GrainSize table
^^^^^^^^^^^^^^^^^^^^^^
The *global_GrainSize* table, focusing on granulomety, stores the **type of (sedimentary rock) material sampled**, serving several collections as for instance :ref:`CRN` ("MATERIAL"), :ref:`expage` ("MATERIAL"), and :ref:`SahulSed` ("SED_MAT").

.. csv-table::
   :file: ./csv_tables/global_GrainSize.csv
   :header-rows: 1

* GRNSIZEID -- A unique identifier (auto-incrementing serial integer)

* GRNSIZE -- Name of grain size fraction / material. For available values refer to :ref:`global_GrainSize_Fields`

* GRNSIZEABB -- Unique abbreviation of "GRNSIZE"

* GRNSIZEMIN -- Lower grainsize fraction limit, if applicable

* GRNSIZEMAX -- Upper grain size fraction limit, if applicable


..  _Global_georeferencing_tables:

Global georeferencing tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  _global_MetaSite:

global_MetaSite table
^^^^^^^^^^^^^^^^^^^^^
The *global_MetaSite* table stores metasite-related information for all compilations. A 'metasite', according to OCTOPUS semantic framework, is a similarity-based cluster of sites. In OCTOPUS data model hierarchy global_MetaSite is superordinate to global_SiteMaster, <collection name>_Sample, and <sub-collection name>_DataCore tables (in this decreasing order). However, whilst the latter three levels can't be NULL, “METASITE” is quasi nullable.

.. csv-table::
   :file: ./csv_tables/global_MetaSite.csv
   :header-rows: 1

* METASITEID -- A unique identifier

* METANAME -- Metasite name

* META_WKT -- Metasite WKT notation describing a bounding box

* META_AREA -- Metasite area, i.e., area of the bounding box

* META_COMMT -- Metasite comment

* META_DESCR -- Metasite description

* FEATURESRC -- Source of the feature that is represented by a bounding box for the sake of plainness. For available values refer to :ref:`cabah_datasourceID`

* FEATURETYP -- If the 'metasite' is related to a natural (e.g. lake) or anthropogenic feature (e.g. quarry): type of the feature, if meaningful and available. For available values refer to :ref:`global_SiteCode`


..  _global_SiteCode:

global_SiteCode table
^^^^^^^^^^^^^^^^^^^^^
The *global_SiteCode* table stores **site types characterising the dominant attribute of a site**. *global_SiteCode* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/global_SiteCode.csv
   :header-rows: 1

* SITECODEID -- A unique identifier (auto-incrementing serial integer)

* SITECODE -- For available values refer to :ref:`global_SiteCode_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "SITECODEID"

* SITEDESCR -- A concise description of “SITECODE”


..  _global_SiteMaster:

global_SiteMaster table
^^^^^^^^^^^^^^^^^^^^^^^
The *global_SiteMaster* table stores an information set that enables **georeferencing and description of a sampled site**.

.. note::

    Site coordinates for both SahulArch and FosSahul collections, for cultural reasons, were obfuscated within a radius of 25 km. Spatial data for those collections includes sample locations as circular polygons.

.. csv-table::
   :file: ./csv_tables/global_SiteMaster.csv
   :header-rows: 1

* SITEID -- A unique site identifier provided as part of the compilation

* METASITEID -- Is fkey. Refer to :ref:`global_MetaSite` table

* CNTRY -- `ISO 3166 Alpha-3 country code <https://www.iso.org/obp/ui/#search>`_. ('ND' = no data)

* REGION_INT -- Region where the study site is located. ('ND' = no data)

* REGION_REG -- Refers to Sahul region. Same as “CNTRY” but needed to accommodate for 'TSI'. ('ND' = no data)

* DIV_ADMIN -- ISO 3166 code of the administrative region where the study site is located. ('ND' = no data). *Geospatial source files have been stored in the non-public part of OCTOPUS database documentation, but will be made available upon request.*

* DIV_OTHER -- Geographical region in 'PNG' and 'TSI' where study site is located. ('ND' = no data), ('NA' = not applicable). *Geospatial source files have been stored in the non-public part of OCTOPUS database documentation, but will be made available upon request.*

* ISL_NAME -- Name of island where study site is located. ('ND' = no data), ('NA' = not applicable)

* LAKE -- Name of lake where study site is located. ('ND' = no data), ('NA' = not applicable)

* BASIN -- Name of river basin where study site is located. ('ND' = no data), ('NA' = not applicable)

* RIVID -- Is fkey. For available values refer to :ref:`global_rivID` table

* IBRAID -- Is fkey. For available values refer to :ref:`global_ibraID` table

* X_WGS84 -- WGS84 longitude of site

* Y_WGS84 -- WGS84 latitude of site

* CORDS_ELEV -- Dual field. First part of value refers to source of coordinates (“X_WGS84”, “Y_WGS84”) for the sample site ('INTP', 'ORIG', 'IPPD', or 'ND'). Second part of value refers to “ELEVATION” ('INTP', 'ORIG', 'IPPD', or 'ND'). Twelve (12) combinations possible

* ELEVATION -- Elevation above sea level. (-9999.99 = no data)

* SITENAME -- Name of the site. ('ND' = no data), ('NA' = not applicable)

* SITE_SPEC -- Further specifies information given in “SITENAME”. ('ND' = no data), ('NA' = not applicable)

* ALTNAME1 -- First alternative or additional name of the site (e.g., published under previous name etc.). ('NA' = not applicable)

* ALTNAME2 -- Second alternative or additional name of the site. ('NA' = not applicable)

* ALTNAME3 -- Third alternative or additional name of the site. ('NA' = not applicable)

* SITECODEID -- Is fkey. For available values refer to :ref:`global_SiteCode` table

* OPENCLOSED -- This field records whether the site was closed (i.e., a rockshelter, cave or other enclosed site) or open (i.e., an artefact scatter, midden on a beach etc.), and is used in the application of taphonomic techniques in time-series analysis. Please note that 'Closed' does not relate to availability or accessibility of information. Note - This field is related to the :ref:`SahulArch` collection, i.e., will not appear in any other collection view [#]_ or flat output table.

* SITE_COMMT -- Free text site comment field

* BIOMEID -- Is fkey. For available values refer to :ref:`global_biomeID` table

* CATCHSZEID -- Is fkey. For available values refer to :ref:`cabah_catchmentsizeID` table

* BASINSZEID -- Is fkey. For available values refer to :ref:`cabah_basinsizeID` table

* FLOWTYPEID -- Is fkey. For available values refer to :ref:`cabah_flowtypeID` table

* NEO_SITEID -- Is the corresponding neotoma/IPPD site ID, if applicable.

* SITEDESCR -- Free text site description field that, where applicable, stores neotoma/IPPD site descriptions.


..  _global_UnitMaster:

global_UnitMaster table
^^^^^^^^^^^^^^^^^^^^^^^
The *global_UnitMaster* table stores **collection-unit related information for all compilations**. Collection units are defined in the :ref:`cabah_unittypeID` table. In OCTOPUS data model hierarchy *global_UnitMaster* is situated between the collection-specific sample tables (subordinate) and the :ref:`global_SiteMaster` table (superordinate); (= SITEID). The *global_UnitMaster* table is exclusively used for collections with a corresponding demand, i.e., will be bypassed for any collection that does not deal with multiple samples / observations from one and the same location / site / unit (e.g. a core).

.. csv-table::
   :file: ./csv_tables/global_UnitMaster.csv
   :header-rows: 1

* UNITID -- Unique identifier (serial integer)

* SITEID -- Is fkey. Refer to :ref:`global_SiteMaster` table

* UNITNAME -- Name of the site

* UNITHANDLE -- Code name for the Collection Unit. This code may be up to 10 characters, but an effort is made to keep these to 8 characters or less. Data are frequently distributed by Collection Unit, and the Handle is used for file names. (description from (and rationale according to) neotoma database)

* UNITTYPEID -- Is fkey. For available values refer to :ref:`cabah_unittypeID` table

* COLLECTID -- Is fkey. For available values refer to :ref:`cabah_col_mtdID` table

* DEPOSITID -- Is fkey. For available values refer to :ref:`cabah_depositID` table

* COLLDATE -- Is unit collection date, if reported, at the highest possible dd/mm/yyyy level.

* WATERDEPTH -- Water depth in m. (-9999.99 = no data)

* NEO_HANDLE -- See "UNITHANDLE", but derived from Neotoma database

* UNIT_COMMT -- Free text site comment field

* COLL_SPEC -- Stores collection process specifics (if applicable)

* IS_CHAR -- Is this collection unit part of the SahulChar collection?

* IS_IPPD -- Is this collection unit part of the IPPD collection?

* IS_NEOTOMA -- Is this collection unit part of Neotoma db?

* UNIT_REF -- Primary collection unit reference. Is fkey. For available values refer to :ref:`global_RefCore` table

* NEO_UNITID -- Is Neotoma collection unit ID, serving inter-db data migration, connectivity and integrity (must never be altered nor removed)


..  _global_DataSetMaster:

global_DataSetMaster table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *global_DataSetMaster* table is the global master table that stores **dataset related information for all relevant compilations**. A Dataset is the set of samples for a particular data type, e.g. pollen,  from a certain collection unit (according to Neotoma db). Dataset types are defined in the *cabah_datasettypeID* table. In OCTOPUS data model hierarchy *global_DataSetID* is situated between the collection-specific sample tables (subordinate) and the *global_UnitMaster* table (superordinate); (= UNITID).

.. csv-table::
   :file: ./csv_tables/global_DataSetMaster.csv
   :header-rows: 1

* DATASETID -- Unique identifier (serial integer)

* UNITID -- Is fkey. For available values refer to :ref:`global_UnitMaster_Fields` table.

* DSETTYPEID -- Is fkey. For available values refer to :ref:`global_datasettypeID_Fields` table.

* NEODSETID -- Is matching Neotoma dataset ID

* NEODSETDOI -- Is matching Neotoma dataset DOI

* DSETNAME -- Is dataset name

* DSETSOURCE -- Is fkey. For available values refer to :ref:`cabah_datasourceID_Fields` table.

* DSETAGEOLD -- Is oldest dataset age

* DSETAGEYNG -- Is youngest dataset age

* DSETNOTE -- Is dataset note

.. note::

    The *global_DataSetMaster* table is exclusively used for collections with a corresponding demand, i.e., will be bypassed for any collection that does not deal with multiple samples / observations from one and the same location / site / unit (e.g. a core).

..  _global_biomeID:

global_biomeID table
^^^^^^^^^^^^^^^^^^^^
The *global_biomeID* table stores iconic biome types that allow for a coarse characterisation/classifications of sampled sites amongst Earth's major biogeographic units. *global_biomeID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/global_biomeID.csv
   :header-rows: 1

* BIOMEID -- Unique identifier (serial integer)

* BIOMETYPE -- Name of biome. For available values refer to :ref:`global_biomeID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "BIOMEID"

* BIOMEDESCR -- A concise description of "BIOMETYPE"


..  _global_ibraID:

global_ibraID table
^^^^^^^^^^^^^^^^^^^
The *global_ibraID* table stores the location code of a site within the relevant **bioregion as defined by the Interim Bio-Regionalisation of Australia (IBRA7)** framework.

.. csv-table::
   :file: ./csv_tables/global_ibraID.csv
   :header-rows: 1

* IBRAID -- Unique identifier (serial integer)

* IBRACODE -- IBRA code. For available values refer to :ref:`global_ibraID_Fields`

* IBRAREGION -- IBRA region name. For available values refer to :ref:`global_ibraID_Fields`

.. important::

    The global_ibraID table only applies to samples from Australia.


..  _global_rivID:

global_rivID table
^^^^^^^^^^^^^^^^^^
The *global_rivID* table stores the **Geofabric AHGF river name/region code** (http://www.bom.gov.au/metadata/catalogue/19115/ANZCW0503900426) of the river that drains the catchment of sample origin.

.. csv-table::
   :file: ./csv_tables/global_rivID.csv
   :header-rows: 1

* RIVID -- Unique identifier (serial integer)

* AHGFL1 -- Geofabric AHGF river region code

* AHGFL2 -- Geofabric AHGF combined river region code (“AHGLF1”) and topographic drainage division two-digit number

* RIVNAME -- Geofabric AHGF river name. For available values refer to :ref:`global_rivID_Fields`

* RIVDIV -- Geofabric AHGF river division name

.. important::

    The global_rivID table only applies to samples from Australia.


..  _global_datasettypeID:

global_datasettypeID table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *global_datasettypeID* table stores **dataset types**, e.g., pollen. To facilitate data migration where necessary, table structure, primary keys and content resemble Neotoma's datasettypes table.

.. csv-table::
   :file: ./csv_tables/global_datasettypeID.csv
   :header-rows: 1

* DSETTYPEID -- A unique identifier (auto-incrementing serial integer)

* DSETTYPE -- Name of dataset type. For available values refer to :ref:`global_datasettypeID_Fields`

* DSTYPNOTE -- Free text dataset note field


..  _spatial_ref_sys:

spatial_ref_sys table
^^^^^^^^^^^^^^^^^^^^^
The *spatial_ref_sys* table comes with PostgreSQL's PostGIS extention. As an OGC compliant database table it lists over 3000 spatial reference systems and technical details needed to transform/reproject between them. For more information see `Section 4.2.1. <https://postgis.net/docs/manual-1.4/ch04.html#spatial_ref_sys>`_ of the PostGIS online manual.

.. csv-table::
   :file: ./csv_tables/spatial_ref_sys.csv
   :header-rows: 1

* srid [#]_  -- An integer value that uniquely identifies the Spatial Referencing System (SRS) within the database

* auth_name -- The name of the standard or standards body that is being cited for this reference system. For example, "EPSG" would be a valid AUTH_NAME

* auth_srid -- The ID of the Spatial Reference System as defined by the Authority cited in the AUTH_NAME. In the case of EPSG, this is where the EPSG projection code would go.

* srtext -- The Well-Known Text representation of the Spatial Reference System

* proj4text -- PostGIS uses the Proj4 library to provide coordinate transformation capabilities. The PROJ4TEXT column contains the Proj4 coordinate definition string for a particular SRID


..  _Global_references_tables:

Global references tables
~~~~~~~~~~~~~~~~~~~~~~~~

..  _global_RefCore:

global_RefCore table
^^^^^^^^^^^^^^^^^^^^
The *global_RefCore* table stores information that allow certain **identification and citation of OCTOPUS collection data sources** according to BibTeX [#]_ referencing standards. In this context, different reference entry types require different minimum information standards, i.e., combinations of fields of which some will be *required*, some will be *optional*, and others will be *ignored* by BibTeX. Those three categories are defined in the :ref:`global_PubType_Fields` section. OCTOPUS database will always seeks to provide information beyond the minimum requirements, though with sense of proportion. As a result, for instance, language will never be captured for English publications because it is considered the communication standard.

=========== =========== ==== ======== ==================
Field       Data type   Key  Not Null Parent
=========== =========== ==== ======== ==================
REFDBID     text        pkey TRUE     
OAID        varchar(11) fkey          :ref:`global_Author`
REFDOI      text                      
AUTHORS     text                      
TITLE       text                      
PUBTYPEID   int2        fkey TRUE     :ref:`global_PubType`
JOURNALID   int2        fkey          :ref:`global_Journal`
VOLUME      text                      
NUMBER      text                      
PAGES       text                      
YEAR        int2             TRUE     
ADDRESS     text                      
NOTE        text                      
URL         text                      
BOOKTITLE   text                      
CHAPTER     text                      
EDITOR      text                      
PUBLISHER   text                      
INSTITUTION text                      
SCHOOL      text                      
=========== =========== ==== ======== ==================

* REFDBID -- A unique identifier in the format *Name<colon>YearKeyword* where *Name* is the family name of the first author, *Year* is the publication year, and *Keyword* is a catchy single word from the publication title. No whitespace or special characters are allowed. The keyword must not be numeric. 

* REFDOI -- Publication Digital Object Identifier (`DOI <https://www.doi.org/>`_), if available

* AUTHORS -- Full sequence of publication authors in the format *FamilyA, ForenameA; FamilyB, ForenameB*; ... where forenames may be abbreviated with leading capital letter in the format *FamilyA, A.; FamilyB, B.*; ...

* TITLE -- Publication title

* VOLUME -- Volume of publication medium

* NUMBER -- Number of publication medium

* PAGES -- Page range divided by double dash (e.g. 102\-\-208), running article number, or a number of pages for books, theses

* YEAR -- Year of publication

* ADDRESS -- Usually the address of the publisher or other institution

* NOTE -- Free text field for annotations

* URL -- Publication url, especially favoured when no DOI available

* BOOKTITLE -- Title of a book, part of which is being cited. In OCTOPUS, further, title of website

* CHAPTER -- A chapter, section, sequence etc. number

* EDITOR -- Name(s) of editor(s) in the format defined above

* PUBLISHER -- Publisher's name

* INSTITUTION -- Institutuion sponsoring a technical report

* SCHOOL -- Name of school where thesis was written


..  _global_RefAbstract:

global_RefAbstract table
^^^^^^^^^^^^^^^^^^^^^^^^
The *global_RefAbstract* table stores **publication abstracts** for references in :ref:`global_RefCore`.

.. csv-table::
   :file: ./csv_tables/global_RefAbstract.csv
   :header-rows: 1

* REFDBID -- Uses same "REFDBID" as :ref:`global_RefCore` table does (because is one-to-one relationship)

* ABSTRACT -- Is publication abstract, if available. Note - Very extensive abstracts have been truncated and marked as *... [_truncated_]* at their end. For available abstracts refer to :ref:`global_RefAbstract_Fields`


..  _global_Author:

global_Author table
^^^^^^^^^^^^^^^^^^^
The *global_Author* table stores information about **publication (first) authors**, which can be individuals or corporations.

.. csv-table::
   :file: ./csv_tables/global_Author.csv
   :header-rows: 1

* OAID -- A unique identifier

* AUTH -- Author family name. If the author is not an individual, but a corporation, '(Corp.)' will be added to the abbreviated corporation name, both of which will be followed by the full corporation name as for instance 'ALA (Corp.) Atlas of Living Australia (online)'. For corporations "FORENAME" : "WSCC_RESID" fields must not be populated.

* FORENAME -- Auhtor given name(s)

* INITIALS -- Given name(s) initial(s) incl. full stop and divided by space char.

* ORCID -- Open Researcher and Contributor ID (https://info.orcid.org/what-is-orcid/). ORCID is the **preferred external identifier**!

* SCOPUSID -- Scopus ID (https://www.scopus.com)

* WSCC_RESID -- Web of Science author ID (currently owned by Clarivate, https://clarivate.com/). Only relevant in case "ORCID" and "SCOPUSID" are not available

* AUTH_COMMT -- Free text comment field

* AUTH_URL -- URL field. Only used if "AUTH" is a corporation

* URL_DATE -- Date of "AUTH_URL" visit. Only applicable if "AUTH_URL" is not *NULL*


..  _global_Journal:

global_Journal table
^^^^^^^^^^^^^^^^^^^^
The *global_Journal* table stores information about **peer-reviewed scientific journals**.

.. csv-table::
   :file: ./csv_tables/global_Journal.csv
   :header-rows: 1

* JOURNALID -- A unique identifier (auto-incrementing serial integer)

* JOURNAL -- Journal title

* JOURNALABB -- Abbreviated journal name according to https://images.webofknowledge.com/images/help/WOS/A_abrvjt.html

* PRINT_ISSN -- Print ISSN according to https://portal.issn.org

* ONLIN_ISSN -- Online ISSN according to https://portal.issn.org


..  _global_PubType:

global_PubType table
^^^^^^^^^^^^^^^^^^^^
The *global_PubType* table stores **publication entry types** according to BibTeX standards.

.. csv-table::
   :file: ./csv_tables/global_PubType.csv
   :header-rows: 1

* PUBTYPEID -- A unique identifier (auto-incrementing serial integer)

* PUBTYPE -- For available values refer to :ref:`global_PubType_Fields`



..  _global_contactstatusID:

global_contactstatusID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *global_contactstatusID* table is a Neotoma-derived lookup table for compilations involving Neotoma contacts, e.g. **IPPD**. This table stores *contact statuses*.

.. csv-table::
   :file: ./csv_tables/global_contactstatusID.csv
   :header-rows: 1

* CSTATUSID -- Arbitrary identifier

* CONTSTATUS -- Contact status

* CSTATUSDSC -- Contact status description


..  _global_RefKeyword:

global_RefKeyword table
^^^^^^^^^^^^^^^^^^^^^^^

*global_RefKeyword* is thoroughly boolean and stores compilation membership keywords for observations and is part of OCTOPUS reference system (= REFDBID; one to one).


..  _global_dbDOI:

global_dbDOI table
^^^^^^^^^^^^^^^^^^
*global_dbDOI* is a lookup table that stores information about OCTOPUS (sub-)compilation versioning, preferred as digital object identifiers.

.. csv-table::
   :file: ./csv_tables/global_dbDOI.csv
   :header-rows: 1

* VERID -- A unique identifier (auto-incrementing serial integer)

* COLLDOI -- Unique identifier (Digital Object Identifier)

* COLLDESCR -- Concise (sub)Collection description

* COLLCOMMT -- (sub)Collection comment

* DBYEAR -- Publication year of database version

* INIT_DBVER -- Database version of first sub(Collection) deployment

* RUN_DBVER -- Current database version sub(Collection) deployment

* COLLVER -- (sub)Collection version

* OBSOLETES -- (sub)Collection version obsoleted by "COLLVER"

* OBSOLTD_BY -- (sub)Collection version obsoleting "COLLVER"

* DEPLOYDATE -- Date of deployment

* COLLNAME -- (sub)Collection name (if applicable)

* COLL_LEAD -- (sub)Collection lead

* REFDOI -- Digital Object Identifier of accompanying publication (if applicable)

.. note::

   For db downloads, "RUN-DBVER" (e.g. 2.2) and "COLLVER" (e.g. 3) will be concatenated yielding 'v2.2(3)'.

----

..  _Regional_tables:

Regional tables
---------------

Non-Cosmogenics tables
~~~~~~~~~~~~~~~~~~~~~~

..  _cabah_AnalysisUnit:

cabah_AnalysisUnit table
^^^^^^^^^^^^^^^^^^^^^^^^

*cabah_AnalysisUnit* is a Neotoma-derived table for compilations dealing with analysis units, e.g. **IPPD**. This table, according to Neotoma db (https://neotoma-manual.readthedocs.io/en/latest/tables_samples.html#analysisunits), stores *analysis units*, i.e., depth increments / bins that are considered analytical entities. Prior to db intake, this table has been filtered so it stores OCTOPUS relevant analysis units only. IMPORTANT NOTE: The primary key values have been migrated unaltered from Neotoma. Therefore, database relations will only work (and be updatable from the Neotoma source) if these ID stays untouched.

.. csv-table::
   :file: ./csv_tables/cabah_AnalysisUnit.csv
   :header-rows: 1

* ANLYSUNTID -- Is the original Neotoma *analysisunitid* (= arbitrary identifier)

* NEO_UNITID -- Is the original Neotoma *collectionunitid*

* AUIT_NAME -- Is the analysis unit name (if available)

* AUIT_DEPTH -- 'Optional depth of the Analysis Unit in cm. Depths are typically designated for Analysis Units from cores and for Analysis Units excavated in arbitrary (e.g. 10 cm) levels. Depths are normally the midpoints of arbitrary levels. For example, for a level excavated from 10 to 20 cm or for a core section from 10 to 15 cm, the depth is 15. Designating depths as midpoints and thicknesses facilitates calculation of ages from age models that utilize single midpoint depths for Analysis Units rather than top and bottom depths. Of course, top and bottom depths can be calculated from midpoint depths and thicknesses. For many microfossil core samples, only the midpoint depths are known or published; the diameter or width of the sampling device is often not given.' (Neotoma db documentation; 29-04-2024)

* AUIT_THICK -- 'Optional thickness of the Analysis Unit in cm. For many microfossil core samples, the depths are treated as points, and the thicknesses are not given in the publications, although 0.5 to 1.0 cm would be typical.' (Neotoma db documentation; 29-04-2024)

* FACIESID -- Sedimentary facies of the Analysis Unit

* AUIT_MIXED -- 'Indicates whether specimens in the Analysis Unit are of mixed ages, for example Pleistocene fossils occurring with late Holocene fossils. Although Analysis Units may be mixed, samples from the Analysis Unit may not be, for example individually radiocarbon dated specimens.' (Neotoma db documentation; 29-04-2024)

* AUIT_ISGN -- Is the International Geo Sample Number (if applicable)

* AUIT_NOTES -- Analysis unit notes


..  _cabah_LabCodes:

cabah_LabCodes table
^^^^^^^^^^^^^^^^^^^^
The *cabah_LabCodes* table stores information about the **lab of origin** for a certain C14 or luminescence observation, i.e., measurement. The labs have been identified automatically by their distinct labcode prefixes

.. csv-table::
   :file: ./csv_tables/cabah_LabCodes.csv
   :header-rows: 1

* LAB_ORIGID -- A unique identifier (auto-incrementing serial integer)

* LAB_PREFIX -- Lab prefix. For available values refer to :ref:`cabah_LabCodes_Fields`

* LAB_FACLTY -- Facility / institution of lab affiliation. For available values refer to :ref:`cabah_LabCodes_Fields`

* CNTRY -- Country of "LAB_FACLTY"

* LAB_ACTIVE -- Whether the lab is active or not

* LAB_MTD -- Lab method (C14, OSL, TL)

* LAB_URL -- Lab url

* LAB_SOURCE -- Source of information stored in a certain tuple. Major sources are 'Radiocarbon' (https://doi.org/10.1017/S0033822200038923) and 'RadonKiel' (https://radon.ufg.uni-kiel.de/labs).


..  _cabah_agetypeID:

cabah_agetypeID table
^^^^^^^^^^^^^^^^^^^^^
The *cabah_agetypeID* table stores the **type of time unit** used for sample age specification.

.. csv-table::
   :file: ./csv_tables/cabah_agetypeID.csv
   :header-rows: 1

* AGETYPEID -- A unique identifier (auto-incrementing serial integer)

* AGETYPE -- Unique age type name. For available values refer to :ref:`cabah_agetypeID_Fields`

* AGETDESCR -- "AGETYPE" description. For available values refer to :ref:`cabah_agetypeID_Fields`

* AGETCOMMT -- "AGETYPE" reference. For available values refer to :ref:`cabah_agetypeID_Fields`


..  _cabah_basinsizeID:

cabah_basinsizeID table
^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_basinsizeID* table, according to the Global Paleofire Database (https://www.paleofire.org/) template, stores arbitrary **water body area classes** (basin = water body itself).

.. csv-table::
   :file: ./csv_tables/cabah_basinsizeID.csv
   :header-rows: 1

* BASINSZEID -- A unique identifier (auto-incrementing serial integer)

* BASINSIZE -- Unique basin size class abbreviation. For available values refer to :ref:`cabah_basinsizeID_Fields`

* BASINAREA -- "BASINSIZE" description. For available values refer to :ref:`cabah_basinsizeID_Fields`


..  _cabah_catchmentsizeID:

cabah_catchmentsizeID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_catchmentsizeID* table, according to the Global Paleofire Database (https://www.paleofire.org/) template, stores arbitrary **catchment area classes** (catchment = area contributing to a certain basin).

.. csv-table::
   :file: ./csv_tables/cabah_catchmentsizeID.csv
   :header-rows: 1

* CATCHSZEID -- A unique identifier (auto-incrementing serial integer)

* CATCHMSIZE -- Unique catchment size class abbreviation. For available values refer to :ref:`cabah_catchmentsizeID_Fields`

* CATCHMAREA -- "CATCHSZEID" description. For available values refer to :ref:`cabah_catchmentsizeID_Fields`


..  _cabah_charmethodID:

cabah_charmethodID table
^^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_charmethodID* is a lookup table for charcoal-related compilations, i.e., SahulCHAR. This table stores the **method of charcoal quantification**.

.. csv-table::
   :file: ./csv_tables/cabah_charmethodID.csv
   :header-rows: 1

* CHARMTDID -- A unique identifier (auto-incrementing serial integer)

* CHARMETHOD -- Unique method name. For available values refer to :ref:`cabah_charmethodID_Fields`

* CHARMTDDSC -- "CHARMETHOD" description. For available values refer to :ref:`cabah_charmethodID_Fields`

* CHARMTDREF -- "CHARMETHOD" reference. For available values refer to :ref:`cabah_charmethodID_Fields`


..  _cabah_chemprepID:

cabah_chemprepID table
^^^^^^^^^^^^^^^^^^^^^^
The *cabah_chemprepID* table stores the **type of chemical pretreatment given to a sample**. Note - Methods capture the majority of methods applied in Australia. There may be considerable variation within each pretreatment code.

.. csv-table::
   :file: ./csv_tables/cabah_chemprepID.csv
   :header-rows: 1

* CHEMPREPID -- A unique identifier

* CHEMPREP -- For available values refer to :ref:`cabah_chemprepID_Fields`

* CHEMPREPAB -- For available values refer to :ref:`cabah_chemprepID_Fields`


..  _cabah_chroncontroltypeID:

cabah_chroncontroltypeID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_chroncontroltypeID* table is a Neotoma-derived table for compilations dealing with chronologies, e.g. **IPPD**. This table, according to Neotoma db (https://neotoma-manual.readthedocs.io/en/latest/tables_chron.html#chroncontroltypes), stores **chronology control types**.

.. csv-table::
   :file: ./csv_tables/cabah_chroncontroltypeID.csv
   :header-rows: 1

* CCONTRLID -- Is the original Neotoma *chroncontroltypeid*

* CCONTRLTYP -- Is the type of chronology control

* PARENTID -- Is fkey. Refers to ordinal higher ranking "CCONTRLID"

* METHODID -- Is fkey. For available values refer to :ref:`cabah_methodID_Fields`


..  _cabah_col_mtdID:

cabah_col_mtdID table
^^^^^^^^^^^^^^^^^^^^^
The *cabah_col_mtdID* table stores the **sample collection method**. *cabah_col_mtdID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/cabah_col_mtdID.csv
   :header-rows: 1

* COL_MTDID -- A unique identifier (auto-incrementing serial integer)

* COL_MTD -- For available values refer to :ref:`cabah_col_mtdID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "COL_MTDID"


..  _cabah_datasourceID:

cabah_datasourceID table
^^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_datasourceID* table stores the **way that data / information have been gathered** for database integration.

.. csv-table::
   :file: ./csv_tables/cabah_datasourceID.csv
   :header-rows: 1

* DATASRCID -- A unique identifier (auto-incrementing serial integer)

* DATASOURCE -- Unique data source name. For available values refer to :ref:`cabah_datasourceID_Fields`

* DATASRCDSC -- "DATASOURCE" description. For available values refer to :ref:`cabah_datasourceID_Fields`

* DATASRCREF -- "DATASOURCE" reference. For available values refer to :ref:`cabah_datasourceID_Fields`


..  _cabah_depositID:

cabah_depositID table
^^^^^^^^^^^^^^^^^^^^^
The *cabah_depositID* table stores the **type of deposit sampled**. *cabah_depositID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/cabah_depositID.csv
   :header-rows: 1

* DEPOSITID -- A unique identifier (auto-incrementing serial integer)

* DEPOSIT -- Unique deposit abbreviation. For available values refer to :ref:`cabah_depositID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "DEPOSITID"

* DEPOSITDSC -- "DEPOSITID" description. For available values refer to :ref:`cabah_depositID_Fields`


..  _cabah_ecolgroupID:

cabah_ecolgroupID table
^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_ecolgroupID* table is a Neotoma-derived lookup table that serves compilations dealing with taxa, e.g. IPPD. This table, according Neotoma db (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#ecolgroups), stores **ecological groups** that facilitate subsequent data handling … *Taxa are assigned to Sets of Ecological Groups. A taxon may be assigned to more than one Set of Ecological Groups, representing different schemes for organizing taxa* …

.. csv-table::
   :file: ./csv_tables/cabah_ecolgroupID.csv
   :header-rows: 1

* ECOGROUPID -- A unique identifier (auto-incrementing serial integer)

* ECOLGROUP -- Name of ecological group. For available values refer to :ref:`cabah_ecolgroupID_Fields`

* ECOGRPHNDL -- Four(4)-char ecological group handle (capitals, unique). For available values refer to :ref:`cabah_ecolgroupID_Fields`

* ECOGRPSRC -- Is fkey. For available values refer to :ref:`cabah_datasourceID_Fields`


..  _cabah_flowtypeID:

cabah_flowtypeID table
^^^^^^^^^^^^^^^^^^^^^^
The *cabah_flowtypeID* table, according to the Global Paleofire Database (https://www.paleofire.org/) template, stores **flow type descriptors** for water bodies.

.. csv-table::
   :file: ./csv_tables/cabah_flowtypeID.csv
   :header-rows: 1

* FLOWTYPEID -- A unique identifier (auto-incrementing serial integer)

* FLOWTYPE -- Unique flow type abbreviation. For available values refer to :ref:`cabah_flowtypeID_Fields`

* FLOWTYPDCR -- "FLOWTYPEID" description. For available values refer to :ref:`cabah_flowtypeID_Fields`


..  _cabah_methodID:

cabah_methodID table
^^^^^^^^^^^^^^^^^^^^
The *cabah_methodID* table stores the **type of method used in age/rate determination**. *cabah_methodID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/cabah_methodID.csv
   :header-rows: 1

* METHODID -- A unique identifier (auto-incrementing serial integer)

* METHOD -- For available values refer to :ref:`cabah_methodID_Fields`

* METHODABBR -- For available values refer to :ref:`cabah_methodID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "METHODID"

* METHODREF -- Basic method literature reference


..  _cabah_taxaID:

cabah_taxaID table
^^^^^^^^^^^^^^^^^^
The *cabah_taxaID* table is a Neotoma-derived taxa table for compilations dealing with taxa, e.g. **IPPD**. This table, according to Neotoma db (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#taxa), stores **taxa**. IMPORTANT NOTE: Primary key (and, with the exception of "TAXAGRPID", the other IDs too) have been migrated unaltered from Neotoma. Therefore, database relations will only work (and be updatable from the Neotoma source) if these IDs stay untouched.

.. csv-table::
   :file: ./csv_tables/cabah_taxaID.csv
   :header-rows: 1

* TAXONID -- Is the original Neotoma *taxonid*

* TAXONCODE -- A code for the Taxon. These codes are useful for other software or output for which the complete name is too long. Because of the very large number of taxa, codes can be duplicated for different Taxa Groups. In general, these various Taxa Groups are analyzed separately, and no duplication will occur within a dataset. However, if Taxa Groups are combined, unique codes can be generated by prefixing with the TaxaGroupID, For example, VPL:Cle (Clethra) and MAM:Cle (Clethrionomys).  [...] (Neotoma. For more detail refer to https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#taxa)

* TAXONNAME -- Name of the taxon. Most TaxonNames are biological taxa; however, some are biometric measures and some are physical parameters. In addition, some biological taxa may have parenthetic non-Latin modifers, e.g. «Betula (>20 µm)» for Betula pollen grains >20 µm in diameter. In general, the names used in Neotoma are those used by the original investigator. In particular, identifications are not changed, although Dataset notes can be added to the database regarding particular identifications. However, some corrections and synonymizations are made. [...] (Neotoma. For more detail refer to https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#taxa)

* AUTHOR -- Taxon name author(s)

* TAXONVALID -- Boolean (True/False) variable

* PARENTID -- Is fkey. Refers to ordinal higher ranking "TAXONID"

* TAXEXTINCT -- Boolean (True/False) variable. The value is True if the taxon is extinct, False if extant. (Neotoma)

* TAXAGRPID -- Is fkey. For avaiable values refer to :ref:`cabah_taxagroupID_Fields` table

* NEOTXPUBID -- Neotoma publication identification number. In Neotoma, this field links to the publications table. In OCTOPUS, however, it does NOT.

* NEOVALORID -- Is fkey. For avaiable values refer to :ref:`neo_contacts_Fields` table

* VALIDDATE -- Date of taxon validation

* TAXONNOTE -- Taxon notes


..  _cabah_taxagroupID:

cabah_taxagroupID table
^^^^^^^^^^^^^^^^^^^^^^^
The *cabah_taxagroupID* table is a Neotoma-derived lookup table for compilations dealing with taxa, e.g. IPPD. This table, according Neotoma db (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#taxa), stores **taxa groups** [...] *The TaxaGroupID facilitates rapid extraction of taxa groups that are typically grouped together for analysis. Some of these groups contain taxa in different classes or phyla* …

.. csv-table::
   :file: ./csv_tables/cabah_taxagroupID.csv
   :header-rows: 1

* TAXAGRPID -- A unique identifier (auto-incrementing serial integer)

* TAXAGROUP -- Name of taxa group. For available values refer to :ref:`cabah_taxagroupID_Fields`

* TXAGRPHDLE -- Three(3)-char taxa group handle (capitals, unique). For available values refer to :ref:`cabah_taxagroupID_Fields`

* TXAGRPSRC -- Is fkey. For available values refer to :ref:`cabah_datasourceID_Fields`


..  _cabah_unittypeID:

cabah_unittypeID table
^^^^^^^^^^^^^^^^^^^^^^
The *cabah_unittypeID* table, according to Neotoma's IPPD template, stores **collection unit types**. *cabah_unittypeID* is a lookup table for compilations that involve collection units, i.e., SahulCHAR.

.. csv-table::
   :file: ./csv_tables/cabah_unittypeID.csv
   :header-rows: 1

* UNITTYPEID -- A unique identifier (auto-incrementing serial integer)

* UNITTYPE -- For available values refer to :ref:`cabah_unittypeID_Fields`

* UNITTDESCR -- "UNITTYPE" description. For available values refer to :ref:`cabah_unittypeID_Fields`


..  _c14_calcurve:

c14_calcurve table
^^^^^^^^^^^^^^^^^^
The *c14_calcurve* table stores **calibration curves** used for radiocarbon age calibration.

.. csv-table::
   :file: ./csv_tables/c14_calcurve.csv
   :header-rows: 1

* CALCURVEID -- A unique identifier (auto-incrementing serial integer)

* CALCURVE -- Calibration curve used for C14 calibration

* CALCURVREF -- Calibration curve reference

* CALCRVNOTE -- Calibration curve note


..  _c14_calprogram:

c14_calprogram table
^^^^^^^^^^^^^^^^^^^^
The *c14_calprogram* table stores **computer programmes** -- incl. their versions -- that may be used for radiocarbon calibration. *c14_calprogram* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/c14_calprogram.csv
   :header-rows: 1

* CALPROGID -- A unique identifier (auto-incrementing serial integer)

* CALPROGRAM -- Program used for C14 calibration

* CALPROGVER -- Calibration programme version

* CALPROGREF -- Calibration programme reference

* PARENTID -- Is fkey. Refers to ordinal higher ranking "CALPROGID"

* CALPRODATE -- Calibration programme publication date

* CALPRONOTE -- Calibration programme note

.. note::

    Not the individual "CALPROGRAM" (ukey1) and "CALPROGVER" (ukey2), but only their *composite* forms the ukey.

..  _Neotoma_tables:

Neotoma tables (*neo_*)
~~~~~~~~~~~~~~~~~~~~~~~
Tables featuring the *neo_* suffix in their name have been migrated from the Neotoma db ecosystem to OCTOPUS database. *neo_* tables serve those collections that first went into Neotoma db before becoming part of OCTOPUS, as for instance **IPPD** (the latter as an effort of the Centre of Excellence for Australian Biodiversity and Heritage -- CABAH). Due to datamodel differences between Neotoma and OCTOPUS databases, migrating those unaltered *neo_* tables became a necessity. To maintain connectivity to Neotoma, primary table keys -- i.e., unique IDs that allow for definite identification of a certain tuple -- were kept and must not be altered.


..  _neo_chronologies:

neo_chronologies table
^^^^^^^^^^^^^^^^^^^^^^
The *neo_chronologies* is a Neotoma table for compilations dealing with chronologies, e.g. **IPPD**. This table, according to Neotoma db (https://neotoma-manual.readthedocs.io/en/latest/tables_chron.html#chronologies), stores *chronology data*. [...] _A Chronology refers to an explicit chronology assigned to a Collection Unit. A Chronology has Chronology Controls, the actual age-depth control points, which are stored in the ChronControls table. A Chronology is also based on an Age Model, which may be a numerical method that fits a curve to a set of age-depth control points or may simply be individually dated Analysis Units. IMPORTANT NOTE: The primary key values have been migrated unaltered from Neotoma. Therefore, database relations will only work (and be updatable from the Neotoma source) if these ID stays untouched.

.. csv-table::
   :file: ./csv_tables/neo_chronologies.csv
   :header-rows: 1

* CHRONLGYID -- Is the original Neotoma *chronologyid*

* NEO_UNITID -- Is the original Neotoma *collectionunitid*. Is fkey to :ref:`global_UnitMaster`

* AGETYPEID -- Is an fkey to :ref:`cabah_agetypeID`. IMPORTANT: values have been changed to match OCTOPUS db

* CONTACTID -- Is original Neotoma *contactid* (i.e., fkey to :ref:`neo_contacts`)

* IS_DEFAULT -- If TRUE, then chronology is the default chronology

* CHRONNAME -- Is chronology name, if available

* PREPDATE -- Date that the Chronology was prepared.

* AGEMODEL -- The age model used for the Chronology.

* AGEYOUNG -- The younger reliable age bound for the Chronology. Younger ages may be assigned to samples, but are not regarded as reliable. If the entire Chronology is considered reliable, AgeBoundYounger is assigned the youngest sample age rounded down to the nearest 10. Thus, for 72 BP, AgeBoundYounger = 70 BP; for -45 BP, AgeBoundYounger = -50 BP. (Neotoma)

* AGEOLD -- The older reliable age bound for the Chronology. Ages older than AgeOlderBound may be assigned to samples, but are not regarded as reliable. This situation is particularly true for ages extrapolated beyond the oldest Chron Control. . If the entire Chronology is considered reliable, AgeBoundOlder is assigned the oldest sample age rounded up to the nearest 10. Thus, for 12564 BP, AgeBoundOlder is 12570. (Neotoma)

* CHRONNOTE -- Chronology related note, if applicable

* UNITID -- Is fkey. For values refer to :ref:`global_UnitMaster_Fields` table.

..  _neo_contacts:

neo_contacts table
^^^^^^^^^^^^^^^^^^
The *neo_contacts* table is a Neotoma lookup table for compilations involving Neotoma contacts, e.g. **IPPD**. This table stores *contacts* of both individuals and legal entities. To preserve table usability down the database pipeline, primary key values have NOT been altered and MUST BE always identical with those from the Neotoma original.

.. csv-table::
   :file: ./csv_tables/neo_contacts.csv
   :header-rows: 1

* CONTACTID -- Is original Neotoma *contactid*

* ALIASID -- The ContactID of a person's current name. If the AliasID is different from the ContactID, the ContactID refers to the person's former name. For example, if J. L. Bouvier became J. B. Kennedy, the ContactID for J. B. Kennedy is the AliasID for J. L. Bouvier. (Neotoma)

* CONTACTNAM -- Full name of the person, last name first (e.g. «Simpson, George Gaylord») or name of organization or project (e.g. «Great Plains Flora Association»). (Neotoma)

* CSTATUSID -- Is fkey. For avaiable values refer to :ref:`global_contactstatusID_Fields` table

* FAMILYNAME -- Family or surname name of a person

* PHONE -- Phone number

* FAX -- Fax number

* EMAIL -- Email address

* URL -- URL, if applicable

* ADDRESS -- Address

* LEADINITIA -- Leading initials for given or forenames without spaces (e.g. «G.G.»)

* GIVENNAMES -- Given name(s)

* TITLE -- A person's title (e.g. «Dr.», «Prof.», «»)

* SUFFIX -- Suffix of a person's name (e.g. «Jr.», «III»)

* NOTES -- Notes, if applicable

* OAID -- Is fkey. For avaiable values refer to :ref:`global_Author_Fields` table


..  _neo_elementmaturities:

neo_elementmaturities table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *neo_elementmaturities* table is a Neotoma lookup lookup table of **Element maturities**. This table is referenced by the :ref:`neo_variableelements`.

.. csv-table::
   :file: ./csv_tables/neo_elementmaturities.csv
   :header-rows: 1

* MATURITYID -- Is the original Neotoma *maturityid*

* MATURITY -- Is the original Neotoma maturity description. For avaiable values refer to :ref:`neo_elementmaturities_Fields` table


..  _neo_elementportions:

neo_elementportions table
^^^^^^^^^^^^^^^^^^^^^^^^^
The *neo_elementportions* table is a Neotoma lookup lookup table of **Element portions**. This table is referenced by the :ref:`neo_variableelements`.

.. csv-table::
   :file: ./csv_tables/neo_elementportions.csv
   :header-rows: 1

* PORTIONID -- Is the original Neotoma *portionid*

* PORTION -- Is the original Neotoma element portion description. For avaiable values refer to :ref:`neo_elementportions_Fields` table


..  _neo_elementsymmetries:

neo_elementsymmetries table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *neo_elementsymmetries* table is a Neotoma lookup lookup table of **Element symmetries**. This table is referenced by the :ref:`neo_variableelements`.

.. csv-table::
   :file: ./csv_tables/neo_elementsymmetries.csv
   :header-rows: 1

* SYMMETRYID -- Is the original Neotoma *symmetryid*

* SYMMETRY -- Is the original Neotoma symmetry description. For avaiable values refer to :ref:`neo_elementsymmetries_Fields` table


..  _neo_elementtypes:

neo_elementtypes table
^^^^^^^^^^^^^^^^^^^^^^
The *neo_elementtypes* table is a Neotoma lookup lookup table of **Element types**. This table is refrences by the :ref:`neo_variableelements`.

.. csv-table::
   :file: ./csv_tables/neo_elementtypes.csv
   :header-rows: 1

* ELEMTYPEID -- Is the original Neotoma *elementtypeid*

* ELEMENTYPE -- Is the original Neotoma element type descriptor. For avaiable values refer to :ref:`neo_elementtypes_Fields` table

* DATASRCID -- Is an fkey to the :ref:`cabah_datasourceID`


..  _neo_keywords:

neo_keywords table
^^^^^^^^^^^^^^^^^^
The *neo_keywords* table is a Neotoma lookup table of **Keywords** referenced by the *SampleKeywords* table. The table provides a means to identify samples sharing a common attribute. For example, the keyword «modern sample» identifies modern surface samples in the database. These samples include individual surface samples, as well as core tops. Although not implemented, a «pre-European settlement» keyword would be a means to identify samples just predating European settlement. (https://neotoma-manual.readthedocs.io/en/latest/tables_samples.html#keywords)

.. csv-table::
   :file: ./csv_tables/neo_keywords.csv
   :header-rows: 1

* KEYWORDID -- Is the original Neotoma *keywordid*

* KEYWORD -- Is the original Neotoma keyword descriptor. For avaiable values refer to :ref:`neo_keywords_Fields` table


..  _neo_variablecontexts:

neo_variablecontexts table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *neo_variablecontexts* table is a Neotoma lookup lookup table of **Variable Contexts** (i.e., depositional contexts). This table is referenced by the :ref:`ippd_variables`. (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#variablecontexts)

.. csv-table::
   :file: ./csv_tables/neo_variablecontexts.csv
   :header-rows: 1

* VARCONTXID -- Is the original Neotoma *variablecontextid*

* VARCONTEXT -- Is the original Neotoma variable context descriptor. For avaiable values refer to :ref:`neo_variablecontexts_Fields` table


..  _neo_variableelements:

neo_variableelements table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *neo_variableelements* table is a Neotoma lookup lookup table of **Variable Elements**. This table is referenced by the :ref:`ippd_variables`. (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#variableelements)

.. csv-table::
   :file: ./csv_tables/neo_variableelements.csv
   :header-rows: 1

* VARELEMTID -- Is the original Neotoma *variableelementid*

* VARELEMENT -- The element, part, or organ of the taxon identified. For plants, these include pollen, spores, and various macrofossil organs, such as «seed», «twig», «cone», and «cone bract». Thus, Betula pollen and Betula seeds are two different Variables. For mammals, Elements include the bone or tooth identified, e.g. «tibia». «tibia, distal, left», «M2, lower, left». Some more unusual elements are Neotoma fecal pellets and Erethizon dorsata quills. If no element is indicated for mammalian fauna, then the genric element «bone/tooth» is assigned. Elements were not assigned in FAUNMAP, so all Variables ingested from FAUNMAP were assigned the «bone/tooth» element. Physical Variables may also have elements. For example, the Loss-on-ignition Variables have «Loss-on-ignition» as a Taxon, and temperature of analysis as an element, e.g. «500°C», «900°C». Charcoal Variables have the size fragments as elements, e.g. «75-100 µm», «100-125 µm». (Neotoma) For avaiable values refer to :ref:`neo_variableelements_Fields` table

* ELEMTYPEID -- Is fkey. For avaiable values refer to :ref:`neo_elementtypes_Fields` table

* SYMMETRYID -- Is fkey. For avaiable values refer to :ref:`neo_elementsymmetries_Fields` table

* PORTIONID -- Is fkey. For avaiable values refer to :ref:`neo_elementportions_Fields` table

* MATURITYID -- Is fkey. For avaiable values refer to :ref:`neo_elementmaturities_Fields` table


..  _neo_variableunits:

neo_variableunits table
^^^^^^^^^^^^^^^^^^^^^^^
The *neo_variableunits* table is a Neotoma lookup table of **Variable Units**. This table is referenced by the :ref:`ippd_variables`. (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#variableunits)

.. csv-table::
   :file: ./csv_tables/neo_variableunits.csv
   :header-rows: 1

* VARUNITID -- Is the original Neotoma *variableunitsid*

* VARUNIT -- The units of measurement. For fauna, these are «present/absent», «NISP» (Number of Individual Specimens), and «MNI» (Minimum Number of Individals). For pollen, these are «NISP» (pollen counts) and «percent». Units for plant macrofossils include «present/abesnt» and «NISP», as well as a number of quantitative concentration measurements and semi-quantitative abundance measurements such as «1-5 scale». Examples of charcoal measurement units are «fragments/ml» and «µm^2/ml». (Neotoma) For avaiable values refer to :ref:`neo_variableunits_Fields` table

Cosmogenics tables
~~~~~~~~~~~~~~~~~~

..  _crn_alstndID:

crn_alstndID table
^^^^^^^^^^^^^^^^^^
The *crn_alstndID* table stores **Al standards, correction factors, ratios and related information**.

.. csv-table::
   :file: ./csv_tables/crn_alstndID.csv
   :header-rows: 1

* ALSTNDID -- A unique identifier (auto-incrementing serial integer)

* ALSTND -- Al meta-standard equivalent to "ALSTND_PUB"

* ALSTND_PUB -- Published Al standard

* ALCORR -- Al correction factor

* ALSTNDRTIO -- Al standard ratio

* ALSTNDCOMT -- Al standard comment

For available values refer to :ref:`crn_alstndID_Fields`


..  _crn_bestndID:

crn_bestndID table
^^^^^^^^^^^^^^^^^^
The *crn_bestndID* table stores **Be standards, correction factors, ratios and related information**.

.. csv-table::
   :file: ./csv_tables/crn_bestndID.csv
   :header-rows: 1

* BESTNDID -- A unique identifier (auto-incrementing serial integer)

* BESTND -- Be meta-standard equivalent to "BeSTND_PUB"

* BESTND_PUB -- Published Al standard

* BECORR -- Be correction factor

* BESTNDRTIO -- Be standard ratio

* BESTNDCOMT -- Be standard comment

For available values refer to :ref:`crn_bestndID_Fields`

Luminescence tables
~~~~~~~~~~~~~~~~~~~

..  _osl-tl_agemodelID:

osl-tl_agemodelID table
^^^^^^^^^^^^^^^^^^^^^^^
The *osl-tl_agemodelID* table stores the **model used to combine individual equivalent dose estimates for age determination**.

.. csv-table::
   :file: ./csv_tables/osl-tl_agemodelID.csv
   :header-rows: 1

* AGEMODELID -- A unique identifier (auto-incrementing serial integer)

* AGEMODEL -- For available values refer to :ref:`osl-tl_agemodelID_Fields`

* AGEMODELAB -- Unique abbreviation of "AGEMODEL". For available values refer to :ref:`osl-tl_agemodelID_Fields`


..  _osl-tl_ed_procID:

osl-tl_ed_procID table
^^^^^^^^^^^^^^^^^^^^^^
The *osl-tl_ed_procID* table stores the **reported procedure used to determine sample equivalent dose for OSL and TL methods**.

.. csv-table::
   :file: ./csv_tables/osl-tl_ed_procID.csv
   :header-rows: 1

* ED_PROCID -- A unique identifier (auto-incrementing serial integer)

* ED_PROC -- For available values refer to :ref:`osl-tl_ed_procID_Fields`

* ED_PROCABR -- Unique abbreviation of "ED_PROC". For available values refer to :ref:`osl-tl_ed_procID_Fields`


..  _osl-tl_lum_matID:

osl-tl_lum_matID table
^^^^^^^^^^^^^^^^^^^^^^
The *osl-tl_lum_matID* table stores the **type of sample material used for OSL and TL dating**.

.. csv-table::
   :file: ./csv_tables/osl-tl_lum_matID.csv
   :header-rows: 1

* LUM_MATID -- A unique identifier (auto-incrementing serial integer)

* LUM_MAT -- For available values refer to :ref:`osl-tl_lum_matID_Fields`

* LUM_MATABB -- Unique abbreviation of "LUM_MAT". For available values refer to :ref:`osl-tl_lum_matID_Fields`


..  _osl-tl_mineralID:

osl-tl_mineralID table
^^^^^^^^^^^^^^^^^^^^^^
The *osl-tl_mineralID* table stores the **type of mineral used for equivalent dose determination**.

.. csv-table::
   :file: ./csv_tables/osl-tl_mineralID.csv
   :header-rows: 1

* MINERALID -- A unique identifier (auto-incrementing serial integer)

* MINERAL -- For available values refer to :ref:`osl-tl_mineralID_Fields`

* MINERALABB -- Unique abbreviation of "MINERAL". For available values refer to :ref:`osl-tl_mineralID_Fields`


..  _osl-tl_mtdID:

osl-tl_mtdID table
^^^^^^^^^^^^^^^^^^
The *osl-tl_mtdID* table stores the **method used to determine a certain element concentration of the sample** resp. the **method used to determine an external dose rate**.

.. csv-table::
   :file: ./csv_tables/osl-tl_mtdID.csv
   :header-rows: 1

* MTDID -- A unique identifier (auto-incrementing serial integer)

* MTD -- For available values refer to :ref:`osl-tl_mtdID_Fields`

* MTDAB -- Unique abbreviation of "MTDAB". For available values refer to :ref:`osl-tl_mtdID_Fields`


..  _osl_typeID:

osl_typeID table
^^^^^^^^^^^^^^^^
The *osl_typeID* table stores the **published OSL type used to determine equivalent dose**.

.. csv-table::
   :file: ./csv_tables/osl_typeID.csv
   :header-rows: 1

* OSL_TYPEID -- A unique identifier (auto-incrementing serial integer)

* OSL_TYPE -- For available values refer to :ref:`osl_typeID_Fields`

* OSL_TYPEAB -- Unique abbreviation of "OSL_TYPE". For available values refer to :ref:`osl_typeID_Fields`

----

..  _Local_tables:

Local tables
------------

CRN tables
~~~~~~~~~~

The following tables exclusively serve the :ref:`CRN`.

..  _crn_Sample:

crn_Sample table
^^^^^^^^^^^^^^^^
The *crn_Sample* table stores CRN collection sample information and is, therefore, situated between the collection-specific DataCore tables (subordinate) and the :ref:`global_SiteMaster` (superordinate; see :ref:`Semantic_data_model`).

.. csv-table::
   :file: ./csv_tables/crn_Sample.csv
   :header-rows: 1

* SMPID -- Unique sample identifier that, first and foremost, serves database operation. CRN SMPIDs have been aggregated using similarities in concatenated roundup(3) “Y_WGS84” AND roundup(3) “X_WGS84” AND "SIZEMIN” AND "SIZEMAX".

* SITEID -- Unique site identifier that, first and foremost, serves database operation. CRN SITEIDs have been aggregated using similarities in concatenated roundup(3) “Y_WGS84” AND roundup(3) “X_WGS84”, with running alphabetic letter(s) added.

* STUDYID -- Unique study identifier provided as part of the compilation

* MATERIAL -- Abbreviated type of material sampled

* SIZEMIN -- Minimum grain size sampled

* SIZEMAX -- Maximum grain size sampled

* PROJEPSGID -- EPSG projection code, used as unique identifier, of projected coordinate system used for calculations

* AREA -- Basin area as calculated from projected DEM [#]_

* ELEV_AVE -- Mean elevation of basin as calculated from projected DEM

* ELEV_STD -- Standard deviation of elevation of basin as calculated from projected DEM

* SLP_AVE -- Mean slope gradient of basin as calculated from projected DEM

* SLP_STD -- Standard deviation of slope gradient of basin as calculated from projected DEM

* SMP_DAY -- Sampling day (if published)

* SMP_MONTH -- Sampling month (if published)

* SMP_YEAR -- Sampling year (if published)

* SMP_COMMT -- Free text sample comment field.

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _crn_al_DataCore:

crn_al_DataCore table
^^^^^^^^^^^^^^^^^^^^^
The *crn_al_DataCore* table stores **Al-26 observations** (= smallest data model entity) for the :ref:`CRN` and is subordinate to the :ref:`crn_Sample`.

.. csv-table::
   :file: ./csv_tables/crn_al_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique CRN AMS measurement identifier provided as part of the compilation.

* SMPID -- Is fkey. Refers to :ref:`crn_Sample`

* OBSID2 -- Original sample identifier (as published). This is not necessarily the lab code provided by some labs, but the ID used by authors of the source publication to identify the sample.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* VERID -- ``TBA``

* REFDBID1 -- ``TBA``

* AL26NP -- Published Al-26 concentration

* AL26NP_ERR -- Published 1-sigma uncertainty in Al-26 concentration

* AL26EP -- Published Al-26 denudation rate

* AL26EP_ERR -- Published 1-sigma uncertainty in Al-26 denudation rate

* ALSTNDID -- ``TBA``

* ALAMSID -- ``TBA``

* AL26NC -- Al-26 concentration normalised to KNSTD

* AL26NC_ERR -- Uncertainty in Al-26 concentration normalised to KNSTD

* ALPROD -- CAIRN average production scaling correction for the basin

* ALTOPO -- CAIRN average topographic shielding correction for the basin

* ALSELF -- CAIRN average self shielding correction for the basin

* ALSNOW -- CAIRN average snow shielding correction for the basin

* ALTOTS -- CAIRN average combined shielding and scaling correction for the basin

* EAL_GCMYR -- CAIRN Al-26 denudation rate in mass per unit area

* ERRAL_AMS -- CAIRN Al-26 denudation rate uncertainty at 1-sigma level in mass per unit area derived from AMS uncertainty

* ERRAL_MUON -- CAIRN Al-26 denudation rate uncertainty at 1-sigma level in mass per unit area derived from muon uncertainty

* ERRAL_PROD -- CAIRN Al-26 denudation rate uncertainty at 1-sigma level in mass per unit area derived from uncertainty in the production rate

* ERRAL_TOT -- CAIRN Al-26 denudation rate uncertainty at 1-sigma level in mass per unit area that combines all uncertainties

* EAL_MMKYR -- CAIRN Al-26 denudation rate calculated assuming density of of 2650 kg.m^-3

* EAL_ERR -- CAIRN Al-26 denudation rate uncertainty at 1-sigma level calculated assuming density of 2650 kg.m^-3

* EALL -- ``TBA``

* EALL_INT -- ``TBA``

* EALL_EXT -- ``TBA``

* EALLNS -- ``TBA``

* EALLNS_INT -- ``TBA``

* EALLNS_EXT -- ``TBA``

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _crn_be_DataCore:

crn_be_DataCore table
^^^^^^^^^^^^^^^^^^^^^
The *crn_be_DataCore* table stores **Be-10 observations** (= smallest data model entity) for the :ref:`CRN` and is subordinate to the :ref:`crn_Sample`.

.. csv-table::
   :file: ./csv_tables/crn_be_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique CRN AMS measurement identifier provided as part of the compilation.

* SMPID -- Is fkey. Refers to :ref:`crn_Sample`

* OBSID2 -- Original sample identifier (as published). This is not necessarily the lab code provided by some labs, but the ID used by authors of the source publication to identify the sample.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* VERID -- ``TBA``

* REFDBID1 -- ``TBA``

* BE10NP -- Published Be-10 concentration

* BE10NP_ERR -- Published 1-sigma uncertainty in Be-10 concentration

* BE10EP -- Published Be-10 denudation rate

* BE10EP_ERR -- Published 1-sigma uncertainty in Be-10 denudation rate

* BESTNDID -- ``TBA``

* BEAMSID -- ``TBA``

* BE10NC -- Be-10 concentration normalised to 07KNSTD

* BE10NC_ERR -- Uncertainty in Be-10 concentration normalised to 07KNSTD

* BEPROD -- CAIRN average production scaling correction for the basin

* BETOPO -- CAIRN average topographic shielding correction for the basin

* BESELF -- CAIRN average self shielding correction for the basin

* BESNOW -- CAIRN average snow shielding correction for the basin

* BETOTS -- CAIRN average combined shielding and scaling correction for the basin

* EBE_GCMYR -- CAIRN Be-10 denudation rate in mass per unit area

* ERRBE_AMS -- CAIRN Be-10 denudation rate uncertainty at 1-sigma level in mass per unit area derived from AMS uncertainty

* ERRBE_MUON -- CAIRN Be-10 denudation rate uncertainty at 1-sigma level in mass per unit area derived from muon uncertainty

* ERRBE_PROD -- CAIRN Be-10 denudation rate uncertainty at 1-sigma level in mass per unit area derived from uncertainty in the production rate

* ERRBE_TOT -- CAIRN Be-10 denudation rate uncertainty at 1-sigma level in mass per unit area that combines all uncertainties

* EBE_MMKYR -- CAIRN Be-10 denudation rate calculated assuming density of 2650 kg.m^-3

* EBE_ERR -- CAIRN Be-10 denudation rate uncertainty at 1-sigma level calculated assuming density of 2650 kg.m^-3

* EBEGLA -- End-member basin-averaged denudation rate corrected for present-day glacier cover under the assumptions that (1) portions of the basin covered by glaciers contribute with sediment in proportion to their surface area and (2) the sediment are depleted in cosmogenic nuclides. 

* EBEGLA_ERR -- Uncertainty of end-member basin-averaged denudation rate corrected for present-day glacier cover.

* EBE_DIFF -- Relative difference between uncorrected (EBE_MMKYR) and glacier-cover corrected (EBEGLA) basin-averaged denudation rate.

* EBEL -- ``TBA``

* EBEL_INT -- ``TBA``

* EBEL_EXT -- ``TBA``

* EBELNS -- ``TBA``

* EBELNS_INT -- ``TBA``

* EBELNS_EXT -- ``TBA``

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _crn_amsID:

crn_amsID table
^^^^^^^^^^^^^^^
The *crn_amsID* table stores information about **Acceleration Mass Spectrometer (AMS)** facilities.

.. csv-table::
   :file: ./csv_tables/crn_amsID.csv
   :header-rows: 1

* AMSID -- A unique identifier (auto-incrementing serial integer)

* AMS -- Abbreviated AMS name. For available values refer to :ref:`crn_amsID_Fields`

* AMSORG -- Full name of AMS facility. For available values refer to :ref:`crn_amsID_Fields`

* AMSURL -- AMS url


..  _crn_projepsgID:

crn_projepsgID table
^^^^^^^^^^^^^^^^^^^^
The *crn_projepsgID* table stores **study-specific projection information** (EPSG and human readable), i.e., the particular UTM projected coordinate system used for (re)calculations.

.. csv-table::
   :file: ./csv_tables/crn_projepsgID.csv
   :header-rows: 1

* PROJEPSGID -- EPSG [#]_ projection code, used as unique identifier

* PROJECTION -- For available values refer to :ref:`crn_projepsgID_Fields`


..  _crn_studies_boundingbox:

crn_studies_boundingbox table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *crn_studies_boundingbox* table is a **CRN denudation spatial features table** (polygons, EPSG:900913) whose bounding boxes define study extents, respectively.

.. csv-table::
   :file: ./csv_tables/crn_studies_boundingbox.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT [#]_ notation of bounding box geometry

* STUDYID -- :ref:`CRN` study ID


..  _crn_v3_basins_EPSG3857:

crn_v3_basins_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *crn_v3_basins_EPSG3857* table stores **spatial features**, i.e., multipolygons of the CRN collections (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/crn_v3_basins_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation (multipolygon, 3857)

* OBSID1 -- Unique CRN AMS measurement identifier provided as part of the compilation.

* OBSID2 -- Original sample identifier (as published). This is not necessarily the lab code provided by some labs, but the ID used by authors of the source publication to identify the sample.

* STUDYID -- Unique study ID

* CRN_SUBCMP -- CRN subcompilation (Global, Australian, inPrep, XXL)

* CENTR_LAT -- The latitude of the basin centroid — as calculated by CAIRN and in WGS84 coordinate system.

* ATM_PRESS -- The atmospheric pressure needed to obtain the basin averaged production scaling. The value translates the spatially distributed production data calculated by CAIRN into one single value.

* QTZ_PCNT -- Relative basin area underlain by quartz bearing rocks (%). Source: GLiM - Global Lithological Map (Hartmann & Moosdorf, 2012)

* GLA_KM2 -- Absolute present-day glacier extent / cover of basin area (km^2). Source: GLIMS: Global Land Ice Measurements from Space (Raup et al., 2007)

* GLA_PCNT -- Relative present-day glacier extent / cover of basin area (%). Source: GLIMS: Global Land Ice Measurements from Space (Raup et al., 2007)


..  _crn_v3_outlets_EPSG3857:

crn_v3_outlets_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *crn_v3_outlets_EPSG3857* table stores **spatial features**, i.e., points of the CRN collections (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/crn_v3_outlets_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom --  WKT geometry notation (point, 3857)

* OBSID1 -- Unique CRN AMS measurement identifier provided as part of the compilation.

* OBSID2 -- Original sample identifier (as published). This is not necessarily the lab code provided by some labs, but the ID used by authors of the source publication to identify the sample.

* STUDYID -- Unique study ID

* CRN_SUBCMP -- CRN subcompilation (Global, Australian, inPrep, XXL)


SahulArch tables
~~~~~~~~~~~~~~~~

The following tables exclusively serve the :ref:`SahulArch`.

..  _arch_Sample:

arch_Sample table
^^^^^^^^^^^^^^^^^
The *arch_Sample* table stores SahulArch sample information and is, therefore, situated between the collection-specific DataCore tables (subordinate) and the :ref:`global_SiteMaster` (superordinate; see :ref:`Semantic_data_model`).

.. csv-table::
   :file: ./csv_tables/arch_Sample.csv
   :header-rows: 1

* SMPID -- Sample identifier provided as part of the compilation. The first part of the identifier (i.e., ARCH####) is linked to “SITEID”, the ID of the site. Where it is clear that two or more observations (dates/ rates) have been measured on one sample, they have the same “SMPID” but a different “OBSID1”. This also applies across methods, e.g., one sample with an OSL age and an U-series age will have the same “SMPID” but different “OBSID1” (i.e. ARCH####OSL### and ARCH####U###).

* SITEID -- Is fkey. Refers to :ref:`global_SiteMaster`

* FEATDATEID -- For available values refer to :ref:`arch_featdatedID_Fields`

* SQUARE -- Square or trench designation from where the sample is from.

* XU -- Excavation Unit or spit designation from where the sample is from.

* SMPDEPTH -- Depth below the surface (or datum) from which sample was extracted. If the published sample depth was specified as a range, then the median value for that range is reported here.

* SMPX_WGS84 -- WGS84 longitude of site. *Culturally sensitive. Coordinates not to be displayed!*

* SMPY_WGS84 -- WGS84 latitude of site. *Culturally sensitive. Coordinates not to be displayed!*

* OCCUPATION -- Is the dated sample directly related to human activity (e.g. hearth, organic artefact, burial), or was it simply part of a wider archaeological deposit. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* CONTEXT -- Was the sample collected from a stratigraphic unit that is associated with human 'Occupation' or one that was culturally 'Sterile'. |:lock:| A *predefined value set* only allows for 'Occupation', 'Sterile', or 'ND' (= no data)

* SMP_COMMT -- Free text sample comment field.


..  _arch_c14_DataCore:

arch_c14_DataCore table
^^^^^^^^^^^^^^^^^^^^^^^
The *arch_c14_DataCore* table stores stores **C14-related observations** (= smallest data model entity), i.e., ages and their associated unique lab-derived data for the :ref:`The_SahulArch_Radiocarbon_collection`.

.. csv-table::
   :file: ./csv_tables/arch_c14_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique age identifier provided as part of the compilation. The first part of the identifier (i.e., ARCH####) is linked to “SITEID”, the ID of the site. The second part of the identifier is unique to the database entry and does also include abbreviation given to the method used to produce the age. For method abbreviations see “METHOD”.

* OBSID2 -- Original sample identifier (as published). This is NOT the laboratory code provided by some labs, but the ID used by authors of the source publication to identify the sample. Samples labelled only by numbers in the literature (e.g. 1, 2, 3 etc) have had a compound prefix -- first three author name letters AND double-digit publication year -- added (e.g. 'Nan87_1' for sample 1 (Nanson 1987)).

* LABID -- Unique lab code assigned by the lab where age was determined. For radiocarbon (and for many luminescence) labs, the first part of the lab code refers to the determining facility.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* BURNT -- Whether the material dated was burnt. Note that charcoal = 'Yes'. Calcinated bone -- typically white, whilst burnt bone is black -- is different to burnt bone, and so is listed in “MATERIAL2” field. |:lock:| A *predefined value set* only allows for 'Yes' (= burnt), 'No' (= not burnt), or 'ND' (= no data)

* ARCHSPECIS -- Genus and/ or species, i.e., scientific name of animal or plant used for 14C dating

* ORGPART -- Bone element, wood part etc. -- e.g., 'Sapwood', 'Heartwood', 'Twig', 'Ring number', 'Femur' ...

* SINGULAR -- Was a single entity (e.g., a single piece of charcoal, not several pieces found close to each other) dated, or were several pieces bulked together? |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'NA' (single entities do not exist, i.e., for example sediment), or 'ND' (= no data)

* CONSERV -- Was the sample conserved? For example, was it glued or soaked in a consolidant? |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* AGEMTD -- Measurement method. Conventional includes liquid scintillation and gas proportional. |:lock:| A *predefined value set* only allows for 'AMS' (= Accelerator Mass Spectrometry), 'CONV' (= conventional), or 'ND' (= no data)

* PHYSCLEAN -- Was the sample physically cleaned? For example, was the surface removed from bone (= 'Yes'), were rootlets and sediment removed from charcoal (= 'Yes'). |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* SOLVENT1 -- Was the pretreatment preceded by a solvent extraction? |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* YIELD_MG -- Amount of material after pretreament in mg. If a range was used for a particular sample or (more commonly) all samples, the average for the range given is reported here.

* YIELD_PCT -- Amount of material after pretreament in %

* C -- mg of carbon dated

* C_ERR -- Error for measured mg carbon dated

* PCT_C -- Measured %C of the pretreated sample

* PCT_C_ERR -- Error for measured %C of the pretreated sample

* PCT_N -- Measured %N of the pretreated sample

* PCT_N_ERR -- Error for measured %N of the pretreated sample

* CN_RATIO -- Measured atomic C:N ratio of the pretreated sample

* CN_ERR -- Error for measured CN value of the pretreated sample

* C13 -- Measured δ13C of the pretreated sample. Note that δ13C value on graphite is not included as it is not equivalent to the δ13C on the pretreated material.

* C13_ERR -- Error for measured δ13C of the pretreated sample. Note that δ13C value on graphite is not included as it is not equivalent to the δ13C on the pretreated material.

* O18 -- Measured δ 18O of the of the pretreated sample

* O18_ERR -- Error for measured δ 18O of the pretreated sample

* N15 -- Measured δ15N of the of the pretreated sample

* N15_ERR -- Error for measured δ15N of the pretreated sample

* S34 -- Measured δ34S of the of the pretreated sample

* S34_ERR -- Error for measured δ34S of the of the pretreated sample.

* RECRYST -- Is secondary recrystallisation present in the pretreated carbonate sample? |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* PCT_RE_VAL -- Calcite/recrystallised mineral in the pretreated carbonate sample. Stain or microscopy methods used: 998 = presence of calcite/ recrystallization verified, or -991 = absence of calcite/ recrystallization.

* PCT_RE_ERR -- Error for measured amount of calcite/recrystallised mineral in the pretreated sample. Is -9999.99 even if “PCT_RE_VAL” = 998

* PCT_RE_MTD -- How was the presence and/or amount of calcite/recrystallisation measured in the pretreated carbonate sample. |:lock:| A *predefined value set* only allows for 'Stain' (= Fiegl's stain), 'XRD' (= X-ray diffractometry), 'FTIR' (= FT infrared spectroscopy), 'Micro' (= Microscopy), 'Other' (= other), or 'ND' (= no data)

* C14_AGE -- Conventional radiocarbon age (CRA), as defined by Stuiver and Polach (1977):

             (1) the use of the Libby half-life value of 5568 years (mean life 8033 years);
             (2) the assumption of uniformity in 14C activity throughout the biosphere in the past;
             (3) the use of oxalic acid or a secondary standard as the modern standard;
             (4) isotopic fractionation normalization of all sample activities to the base of δ13C = -25.0 per mille (relative to the 13C:12C ratio of PDB standard); and,
             (5) the use of AD 1950 as the base year, with ages given in years before present (BP) (i.e., AD 1950 = 0 BP)

.. note::

    The above "C14_AGE" definition may not be met prior to c.1980 and is unlikely to be met prior to 1977. If the database user wishes to use dates from this period, they will need to establish how the radiocarbon age was calculated.


* C14_ERRPOS -- Estimated standard error attached to an individual determination, equal to one standard deviation (1σ). Note that occasionally determinations have asymmetrical standard deviations.

* C14_ERRNEG -- Estimated standard error attached to an individual determination, equal to one standard deviation (1σ). Note that occasionally determinations have asymmetrical standard deviations.

* C14_INF -- Is the date infinite (indistinguishable from the laboratory background). This field clarifies the two previous fields, where no data may be misinterpreted as an infinite measurement. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* F14C -- Proportion of radiocarbon atoms in the sample compared to that present in the year AD 1950. “F14C” is pMC (percent modern carbon)/100.

* F14C_ERR -- Error for proportion of radiocarbon atoms in the sample compared to that present in the year AD 1950. The error for “F14C” is the error for pMC (percent modern carbon)/100.

* AGE_COMMT -- Free text age comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _arch_osl_DataCore:

arch_osl_DataCore table
^^^^^^^^^^^^^^^^^^^^^^^
The *arch_osl_DataCore* table stores **OSL-related observations** (= smallest data model entity), i.e., ages and their associated unique lab-derived data for the :ref:`The_SahulArch_OSL_collection`.

.. csv-table::
   :file: ./csv_tables/arch_osl_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique age identifier provided as part of the compilation. The first part of the identifier (i.e., ARCH####) is linked to “SITEID”, the ID of the site. The second part of the identifier is unique to the database entry and does also include abbreviation given to the method used to produce the age. For method abbreviations see “METHOD”.

* OBSID2 -- Original sample identifier (as published). This is NOT the laboratory code provided by some labs, but the ID used by authors of the source publication to identify the sample. Samples labelled only by numbers in the literature (e.g. 1, 2, 3 etc) have had a compound prefix -- first three author name letters AND double-digit publication year -- added (e.g. 'Nan87_1' for sample 1 (Nanson 1987)).

* LABID -- Unique lab code assigned by the lab where age was determined. For radiocarbon (and for many luminescence) labs, the first part of the lab code refers to the determining facility.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* SIZE_MIN -- Reported minimum grain size used for equivalent dose and environmental dose rate determination

* SIZE_MAX -- Reported maximum grain size used for equivalent dose and environmental dose rate determination

* H2O_MEAS -- Water content as measured from the sample. “H2O_MEAS” will be -9999.99 for estimated, but not measured water content. For those samples, “H2O_USED” will hold the reported estimated value. If the measured water content is given as <1% in the original publication, then 1.0 was recorded here.

* H2O_USED -- Water content used for environmental dose rate determination

* H2O_ERR -- Standard error for “H2O_USED” (1σ)

* ALIQ_TYPE -- Reported aliquot type used for equivalent dose determination. |:lock:| A *predefined value set* only allows for 'SG' (= Single Grain), 'SA' (= Single Aliquot), 'MA' (= Multipe Aliquots), or 'ND' (= no data)

* ALIQ_SIZE -- Reported size of aliquot diameter in mm

* RESCOR -- Residual dose correction was applied to the Equivalent Dose, specifically for IRSL, pIRIR, MET-pIRIR, VSL, and TT-OSL. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* DOSERECOV -- Were dose recovery test results reported in the study? |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* PH1_TEMP -- Preheat temperature applied immediately prior to measurement of either the Natural, Regenerative or Additive dose

* PH2_TEMP -- Preheat temperature applied immediately prior to measurement of test dose

* NUM_MEAS -- Number of aliquots/grains measured for the sample

* NUM_ACC -- Number of aliquots/grains accepted for equivalent dose determination

* EQUIVDOSE -- Reported equivalent dose in Gy, sometimes referred to as ED, De, palaeodose (P) or burial dose

* ED_ERR -- Published error for the equivalent dose at 1 standard error (1σ)

* ED_INF -- Natural signal projected onto the dose saturation plateau of dose response curve (De represented is a minimum value)

* OD -- Overdispersion value for equivalent dose dataset calculated as per Galbraith et al., (1999)

* OD_INF -- Overdispersion error value (at 1 standard error, 1σ) for equivalent dose data set calculated as per Galbraith et al., (1999)

* OD_TYPE -- The unit of measure for “OD” and “OD_ERR” values

* U -- Uranium content of the sample

* U_ERR -- Standard error (1σ) for the uranium content of the sample

* TH -- Thorium content of the sample

* TH_ERR -- Standard error (1σ) for the thorium content of the sample

* K -- Potassium content of the sample. N.B. K not K2O

* K_ERR -- Standard error (1σ) for the potassium content of the sample

* U238 -- 238U content from High-Resolution Gamma-ray Spectrometry (HRGS)

* U238_ERR -- Published error value for “U238”

* RA226 -- 226Ra content from High-Resolution Gamma-ray Spectrometry (HRGS)

* RA226_ERR -- Published error value for “RA226”

* PB210 -- 210Pb content from High-Resolution Gamma-ray Spectrometry (HRGS)

* PB210_ERR -- Published error value for “PB210”

* RA228 -- 228Ra content from High-Resolution Gamma-ray Spectrometry (HRGS)

* RA228_ERR -- Published error value for “RA228”

* TH228 -- 228Th content from High-Resolution Gamma-ray Spectrometry (HRGS)

* TH228_ERR -- Published error value for “TH228”

* TH232 -- 232Th content from High-Resolution Gamma-ray Spectrometry (HRGS)

* TH232_ERR -- Published error value for “TH232”

* K40 -- 40K content from High-Resolution Gamma-ray Spectrometry (HRGS)

* K40_ERR -- Published error value for “K40”

* ALPH -- External alpha dose rate (wet)

* ALPH_ERR -- 1 standard error (1σ) for external alpha dose rate

* BETA -- External beta dose rate (wet)

* BETA_ERR -- 1 standard error (1σ) for external beta dose rate

* GAMMA -- External gamma dose rate (wet)

* GAMMA_ERR -- 1 standard error (1σ) for external gamma dose rate

* COSMIC -- Cosmic dose rate (wet)

* COSMIC_ERR -- 1 standard error (1σ) for cosmic dose rate

* ALPH_I -- Internal alpha dose rate (from within grain)

* ALPH_I_ERR -- 1 standard error (1σ) for "ALPH_I"

* ALPH_I_MTD -- Was the internal alpha dose rate assumed or measured? |:lock:| A *predefined value set* only allows for 'Assumed', 'Measured', or 'ND' (= no data)

* BETA_I -- Internal beta dose rate (from within grain)

* BETA_I_ERR -- 1 standard error (1σ) for "BETA_I"

* BETA_I_MTD -- Was the internal beta dose rate assumed or measured? |:lock:| A *predefined value set* only allows for 'Assumed', 'Measured', or 'ND' (= no data)

* DIFF_DOSE -- Whether a different and/or additional method, not specified in this compilation was used to determine the dosimetry for this sample. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* DOSERATE -- Total (wet) environmental dose rate used for age determination

* DOSE_ERR -- Total (wet) environmental dose rate error at 1σ

* OSL_AGE -- Published OSL age

* OSL_RNDERR -- Published Random only “OSL_AGE” error

* OSL_ERR -- Published total “OSL_AGE” error (random + systematic)

* AGE_CI -- Published confidence interval on the age estimate. |:lock:| A *predefined value set* only allows for '1s' (= 1 standard error [1σ]), '2s' (= 2 standard error [2σ]), 'SD' (= Standard Deviation), or 'ND' (= no data)

* FADCOR -- “OSL_AGE” was corrected for fading, specifically for IRSL, pIRIR, and MET-pIRIR. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* G_VAL -- Represents the correcting approach using value of fading rate in feldspars. If reported, express as percent per decade.

* G_VAL_ERR -- Published 1σ error for the “G_VAL”

* AGE_COMMT -- Free text age comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _arch_tl_DataCore:

arch_tl_DataCore table
^^^^^^^^^^^^^^^^^^^^^^
The *arch_tl_DataCore* table stores stores **TL-related observations** (= smallest data model entity), i.e., ages and their associated unique lab-derived data for the :ref:`The_SahulArch_TL_collection`.

.. csv-table::
   :file: ./csv_tables/arch_tl_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique age identifier provided as part of the compilation. The first part of the identifier (i.e., ARCH####) is linked to “SITEID”, the ID of the site. The second part of the identifier is unique to the database entry and does also include abbreviation given to the method used to produce the age. For method abbreviations see “METHOD”.

* OBSID2 -- Original sample identifier (as published). This is NOT the laboratory code provided by some labs, but the ID used by authors of the source publication to identify the sample. Samples labelled only by numbers in the literature (e.g. 1, 2, 3 etc) have had a compound prefix -- first three author name letters AND double-digit publication year -- added (e.g. 'Nan87_1' for sample 1 (Nanson 1987)).

* LABID -- Unique lab code assigned by the lab where age was determined. For radiocarbon (and for many luminescence) labs, the first part of the lab code refers to the determining facility.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* SIZE_MIN -- Reported minimum grain size used for equivalent dose and environmental dose rate determination

* SIZE_MAX -- Reported maximum grain size used for equivalent dose and environmental dose rate determination

* H2O_MEAS -- Water content as measured from the sample. “H2O_MEAS” will be -9999.99 for estimated, but not measured water content. For those samples, “H2O_USED” will hold the reported estimated value. If the measured water content is given as <1% in the original publication, then 1.0 was recorded here.

* H2O_USED -- Water content used for environmental dose rate determination

* H2O_ERR -- Standard error for “H2O_USED” (1σ)

* ALIQ_SIZE -- Reported size of aliquot diameter in mm

* RESCOR -- Residual dose correction was applied to the Equivalent Dose, specifically for IRSL, pIRIR, MET-pIRIR, VSL, and TT-OSL. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* PLAT_REG -- Pre-heat plateau region

* AN_TEMP -- Specific temperature at which analysis is performed

* NUM_MEAS -- Number of aliquots/grains measured for the sample

* EQUIVDOSE -- Reported equivalent dose in Gy, sometimes referred to as ED, De, palaeodose (P) or burial dose

* ED_ERR -- Published error for the equivalent dose at 1 standard error (1σ)

* ED_SAT -- Equivalent dose (ED) for the saturated age

* ED_SATERR -- Published 1σ error for the saturated age

* U -- Uranium content of the sample

* U_ERR -- Standard error (1σ) for the uranium content of the sample

* TH -- Thorium content of the sample

* TH_ERR -- Standard error (1σ) for the thorium content of the sample

* U_TH -- When U and Th elemental content are reported together, rather than separate U and Th. Reported as radioactive element specific activity

* U_TH_ERR -- Published error for “U_TH” specific activity

* K -- Potassium content of the sample. N.B. K not K2O

* K_ERR -- Standard error (1σ) for the potassium content of the sample

* RB -- Rubidium (Rb) content

* U238 -- 238U content from High-Resolution Gamma-ray Spectrometry (HRGS)

* U238_ERR -- Published error value for “U238”

* RA226 -- 226Ra content from High-Resolution Gamma-ray Spectrometry (HRGS)

* RA226_ERR -- Published error value for “RA226”

* PB210 -- 210Pb content from High-Resolution Gamma-ray Spectrometry (HRGS)

* PB210_ERR -- Published error value for “PB210”

* RA228 -- 228Ra content from High-Resolution Gamma-ray Spectrometry (HRGS)

* RA228_ERR -- Published error value for “RA228”

* TH228 -- 228Th content from High-Resolution Gamma-ray Spectrometry (HRGS)

* TH228_ERR -- Published error value for “TH228”

* TH232 -- 232Th content from High-Resolution Gamma-ray Spectrometry (HRGS)

* TH232_ERR -- Published error value for “TH232”

* K40 -- 40K content from High-Resolution Gamma-ray Spectrometry (HRGS)

* K40_ERR -- Published error value for “K40”

* ALPH -- External alpha dose rate (wet)

* ALPH_ERR -- 1 standard error (1σ) for external alpha dose rate

* BETA -- External beta dose rate (wet)

* BETA_ERR -- 1 standard error (1σ) for external beta dose rate

* GAMMA -- External gamma dose rate (wet)

* GAMMA_ERR -- 1 standard error (1σ) for external gamma dose rate

* COSMIC -- Cosmic dose rate (wet)

* COSMIC_ERR -- 1 standard error (1σ) for cosmic dose rate

* ALPH_I -- Internal alpha dose rate (from within grain)

* ALPH_I_ERR -- 1 standard error (1σ) for "ALPH_I"

* ALPH_I_MTD -- Was the internal alpha dose rate assumed or measured? |:lock:| A *predefined value set* only allows for 'Assumed', 'Measured', or 'ND' (= no data)

* BETA_I -- Internal beta dose rate (from within grain)

* BETA_I_ERR -- 1 standard error (1σ) for "BETA_I"

* BETA_I_MTD -- Was the internal beta dose rate assumed or measured? |:lock:| A *predefined value set* only allows for 'Assumed', 'Measured', or 'ND' (= no data)

* DIFF_DOSE -- Whether a different and/or additional method, not specified in this compilation was used to determine the dosimetry for this sample. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* DOSERATE -- Total (wet) environmental dose rate used for age determination

* DOSE_ERR -- Total (wet) environmental dose rate error at 1σ

* TL_AGE -- Published TL age

* TL_RNDERR -- Published Random only “TL_AGE” error

* TL_ERR -- Published total “TL_AGE” error (random + systematic)

* AGE_CI -- Published confidence interval on the age estimate. |:lock:| A *predefined value set* only allows for '1s' (= 1 standard error [1σ]), '2s' (= 2 standard error [2σ]), 'SD' (= Standard Deviation), or 'ND' (= no data)

* FADCOR -- “OSL_AGE” was corrected for fading, specifically for IRSL, pIRIR, and MET-pIRIR. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* G_VAL -- Represents the correcting approach using value of fading rate in feldspars. If reported, express as percent per decade.

* G_VAL_ERR -- Published 1σ error for the “G_VAL”

* AGE_COMMT -- Free text age comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _arch_featdatedID:

arch_featdatedID table
^^^^^^^^^^^^^^^^^^^^^^
The *arch_featdatedID* table stores information about **specific features dated**.

.. csv-table::
   :file: ./csv_tables/arch_featdatedID.csv
   :header-rows: 1

* FEATDATEID -- A unique identifier (auto-incrementing serial integer)

* FEATDATED -- For available values refer to :ref:`arch_featdatedID_Fields`


..  _c13_valID:

c13_valID table
^^^^^^^^^^^^^^^
The *c13_valID* table stores information whether **delta13C was measured or assumed**.

.. csv-table::
   :file: ./csv_tables/c13_valID.csv
   :header-rows: 1

* C13_VALID -- A unique identifier (auto-incrementing serial integer)

* C13_VAL -- For available values refer to :ref:`c13_valID_Fields`


..  _c14_contamID:

c14_contamID table
^^^^^^^^^^^^^^^^^^
The *c14_contamID* table stores information about **specific contaminants that may have remained after C14 sample pretreatment**.

.. csv-table::
   :file: ./csv_tables/c14_contamID.csv
   :header-rows: 1


* CONTAMID -- A unique identifier (auto-incrementing serial integer)

* CONTAM -- For available values refer to :ref:`c14_contamID_Fields`


..  _c14_hum_modID:

c14_hum_modID table
^^^^^^^^^^^^^^^^^^^
The *c14_hum_modID* table stores information about **indications of human modification**.

.. csv-table::
   :file: ./csv_tables/c14_hum_modID.csv
   :header-rows: 1

* HUM_MODID -- A unique identifier (auto-incrementing serial integer)

* HUM_MOD -- For available values refer to :ref:`c14_hum_modID_Fields`


..  _c14_materia1ID:

c14_materia1ID table
^^^^^^^^^^^^^^^^^^^^
The *c14_materia1ID* table stores information about the **type of sample material used for 14C dating**.

.. csv-table::
   :file: ./csv_tables/c14_materia1ID.csv
   :header-rows: 1

* MATERIA1ID -- A unique identifier (auto-incrementing serial integer)

* MATERIAL1 -- For available values refer to :ref:`c14_materia1ID_Fields`

* MATERIA1AB -- For available values refer to :ref:`c14_materia1ID_Fields`


..  _c14_materia2ID:

c14_materia2ID table
^^^^^^^^^^^^^^^^^^^^
The *c14_materia2ID* table stores information about the **sub-type of sample material used for 14C dating**. *c14_materia2ID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/c14_materia2ID.csv
   :header-rows: 1

* MATERIA2ID -- A unique identifier (auto-incrementing serial integer)

* MATERIAL2 -- For available values refer to :ref:`c14_materia2ID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "MATERIA2ID"

* MAT2_DESCR -- A concise description of "MATERIAL2"


..  _c14_solvent2ID:

c14_solvent2ID table
^^^^^^^^^^^^^^^^^^^^
The *c14_solvent2ID* table stores the **solvent used** for C14 sample processing.

.. csv-table::
   :file: ./csv_tables/c14_solvent2ID.csv
   :header-rows: 1

* SOLVENT2ID -- A unique identifier (auto-incrementing serial integer)

* SOLVENT2 -- For available values refer to :ref:`c14_solvent2ID_Fields`

* SOLVENT2AB -- For available values refer to :ref:`c14_solvent2ID_Fields`


..  _c_mtdID:

c_mtdID table
^^^^^^^^^^^^^
The *c_mtdID* table stores the **method used to determine an element abundance/ ratio**.

.. csv-table::
   :file: ./csv_tables/c_mtdID.csv
   :header-rows: 1

* C_MTDID -- A unique identifier (auto-incrementing serial integer)

* C_MTD -- For available values refer to :ref:`c_mtdID_Fields`

* C_MTDAB -- For available values refer to :ref:`c_mtdID_Fields`


..  _arch_c14_polygons_EPSG3857:

arch_c14_polygons_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *arch_c14_polygons_EPSG3857* table stores **spatial features**, i.e., polygons of the SahulArch/ Radiocarbon collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/arch_c14_polygons_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


..  _arch_osl_polygons_EPSG3857:

arch_osl_polygons_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *arch_osl_polygons_EPSG3857* table stores **spatial features**, i.e., polygons of the SahulArch/ OSL collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/arch_osl_polygons_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


..  _arch_tl_polygons_EPSG3857:

arch_tl_polygons_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *arch_tl_polygons_EPSG3857* table stores **spatial features**, i.e., polygons of the SahulArch/ TL collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/arch_tl_polygons_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


SahulChar tables
~~~~~~~~~~~~~~~~

The following tables exclusively serve the :ref:`SahulChar`.

..  _char_Sample:

char_Sample table
^^^^^^^^^^^^^^^^^
The *char_Sample* table stores SahulChar sample information and is, therefore, situated between the :ref:`char_DataCore` (subordinate) and the :ref:`global_UnitMaster` (superordinate; see :ref:`Semantic_data_model`).

.. csv-table::
   :file: ./csv_tables/char_Sample.csv
   :header-rows: 1

* SMPID -- A unique identifier (auto-incrementing serial integer)

* UNITID -- Is fkey. Refer to :ref:`global_UnitMaster` table

* SMPNAME -- A human readable sample name in the form CONCAT('UNITNAME', 'SMPDEPTH')

* SMPDEPTH -- Sample depth (m, two decimals)

* SMPCOMMT -- Free text sample comment field 


..  _char_DataCore:

char_DataCore table
^^^^^^^^^^^^^^^^^^^
The *char_DataCore* table stores **charcoal / black carbon-related observations** (= smallest data model entity), i.e., ages, counts and their associated lab-derived metrics / values for the :ref:`SahulChar`.

.. csv-table::
   :file: ./csv_tables/char_DataCore.csv
   :header-rows: 1

* OBSID -- A unique identifier (auto-incrementing serial integer)

* SMPID -- Is fkey. Refer to :ref:`char_Sample` table

* OBSNAME -- A human readable observation name in the form CONCAT('SMPNAME', '_charn_n') for *count observations* resp. CONCAT('SMPNAME', '_SMPDEPTH_age') for *ages*

* LABID -- Unique lab code assigned by the lab where age was determined. For radiocarbon (and for many luminescence) labs, the first part of the lab code refers to the determining facility.

* LAB_ORIGID -- Is fkey. Refer to :ref:`cabah_LabCodes` table

* WHATAMI -- What am I - *counts* or *age*? Is fkey. Refer to :ref:`global_varunitID` table

* AGE -- Age value\* (two decimals; see below note)

* AGE_ERROR -- Age error value (two decimals)

* AGETYPEID -- Is fkey. Refer to :ref:`cabah_agetypeID` table

* AGE_SPEC -- Specifies if "AGE" should be considered a minimum / maximum age (if applicable)

* METHODID -- Is fkey. Refer to :ref:`cabah_methodID` table

* MATERIA2ID -- Is fkey. Refer to :ref:`c14_materia2ID` table

* EST_AGE -- Estimated, i.e., modelled age

* CALCURVEID -- Is fkey. Refer to :ref:`c14_calcurve` table

* CALPROGID -- Is fkey. Refer to :ref:`c14_calprogram` table

* CHARCOUNTS -- Charcoal or black carbon count

* CHARMTDID -- Is fkey. Refer to :ref:`cabah_charmethodID` table

* CHARMEASID -- Is fkey. Refer to :ref:`global_varunitID` table

* CHARMAX -- Maximum particle size

* CHARMIN -- Minimum particle size

* CHARSIZEID -- Is fkey. Refer to :ref:`global_varunitID` table

* THICKNESS -- Sample thickness (cm)

* DATASRCID -- Is fkey. Refer to :ref:`cabah_datasourceID` table

* CHARCOMMT -- Free text observation comment field 

.. note::

   \* |:nerd:| Re "AGE" -- Preference was given to uncalibrated rather than calibrated radiocarbon ages where possible, to allow for recalibration with future calibration curve updates. Ages reported in calendar years BC/AD or BCE/CE were converted to 'years BP' prior to entry or entered as AGE_UNIT = 'other' if conversion is not possible. Ages generated from dating methods that are measured as years prior to sample collection and do not require calibration, such as lead-210 or optically stimulated luminescence, were converted to 'years BP' prior to entry where possible or entered as AGE_UNIT = 'other'.


..  _IPPD_tables:

IPPD tables
~~~~~~~~~~~

..  _ippd_DataCore:

ippd_DataCore table
^^^^^^^^^^^^^^^^^^^

The *ippd_DataCore* table is an IPPD-specific Neotoma table where each occurrence of a Variable in a sample comprises a record in the Data table. "data" is the primary table in Neotoma's data model. (https://neotoma-manual.readthedocs.io/en/latest/tables_samples.html#data)

.. csv-table::
   :file: ./csv_tables/ippd_DataCore.csv
   :header-rows: 1

* DATAID -- Arbitrary identifier. Is original Neotoma *dataid*

* SAMPLEID -- Is fkey. For available values refer to :ref:`ippd_Sample_Fields` table.

* VARIABLEID -- Is fkey. For available values refer to :ref:`ippd_variables_Fields` table.

* VALUE -- Is the value of the variable


..  _ippd_Sample:

ippd_Sample table
^^^^^^^^^^^^^^^^^
The *ippd_Sample* table is an IPPD-specific Neotoma table that stores samples. In Neotoma's data model, *Samples* belong to *Analysis Units*, which belong to *Collection Units*, which belong to *Sites*. However, *Samples* also belong to a *Dataset*, and the Dataset determines the type of sample. Thus, there could be two different samples from the same Analysis Unit, one belonging to a pollen dataset, the other to a plant macrofossil dataset. (https://neotoma-manual.readthedocs.io/en/latest/tables_samples.html#samples)

.. csv-table::
   :file: ./csv_tables/ippd_Sample.csv
   :header-rows: 1

* SAMPLEID -- Arbitrary identifier. Is original Neotoma *sampleid*

* ANLYSUNTID -- Arbitrary identifier. Is original Neotoma *analysisunitid*. Is fkey to :ref:`cabah_AnalysisUnit`

* NEODSETID -- Arbitrary identifier. Is "NEODSETID", i.e., the original Neotoma *datasetid*. Is fkey to :ref:`global_DataSetMaster`

* SMPNAME -- Is sample name, if avaiable

* ANLYSDATE -- Is date of analysis, if available

* LABNUMBER -- Is lab number, if provided

* PREPMETHOD -- Is preparation method free text field

* SMPNOTE -- Is sample note, if applicable

* SMPDATE -- Is date of sampling, if provided

* TAXONID -- Is fkey to :ref:`cabah_taxaID`

* DATASETID -- Is fkey to :ref:`global_DataSetMaster`


..  _ippd_sampleages:

ippd_sampleages table
^^^^^^^^^^^^^^^^^^^^^
The *ippd_sampleages* table is an IPPD-specific Neotoma table that stores *sample ages*. In Neotoma's data model, *Ages* are assigned to a *Chronology*. Because there may be more than one *Chronology* for a *Collection Unit*, samples may be assigned different ages for different Chronologies. A simple example is one sample age in radiocarbon years and another in calibrated radiocarbon years. The age units are an attribute of the Chronology. (https://neotoma-manual.readthedocs.io/en/latest/tables_samples.html#sampleages)

.. csv-table::
   :file: ./csv_tables/ippd_sampleages.csv
   :header-rows: 1

* SMPAGEID -- Arbitrary identifier. Is original Neotoma *sampleageid*

* SAMPLEID -- Arbitrary identifier. Is original Neotoma *sampleid* (and links to :ref:`ippd_sampleages`)

* CHRONLGYID -- Arbitrary identifier. Is original Neotoma *chronologyid* (and links to :ref:`neo_chronologies`)

* AGE -- Is the age of the sample

* AGEYOUNGER -- Is the younger error estimate of the age. The definition of this estimate is an attribute of the chronology. Many ages do not have explicit error estimates assigned

* AGEOLDER -- Is the older error estimate of the age. The definition of this estimate is an attribute of the chronology. Many ages do not have explicit error estimates assigned


..  _ippd_samplekeywords:

ippd_samplekeywords table
^^^^^^^^^^^^^^^^^^^^^^^^^
The *ippd_samplekeywords* table is an IPPD-specific Neotoma table that links *keywords* to *samples*. (For example, it identifies modern pollen surface samples.)

.. csv-table::
   :file: ./csv_tables/ippd_samplekeywords.csv
   :header-rows: 1

* SAMPLEID -- Is pkey 1/2. Is fkey to :ref:`ippd_Sample`

* KEYWORDID -- Is pkey 2/2. Is fkey to :ref:`neo_keywords`

.. note::

    Not the individual "SAMPLEID" (pkey1/2) and "KEYWORDID" (pkey2/2), but only their *composite* forms the pkey.


..  _ippd_variables:

ippd_variables table
^^^^^^^^^^^^^^^^^^^^
*ippd_variables* is an IPPD-specific Neotoma table that lists **Variables**, which always consist of a *Taxon* AND *Units* of measurement. Variables can also have *Elements*, *Contexts*, and *Modifications*. Thus, the same taxon with different measurement units (e.g. present/absent, NISP, MNI) are different Variables. (https://neotoma-manual.readthedocs.io/en/latest/tables_taxa.html#variables)

.. csv-table::
   :file: ./csv_tables/ippd_variables.csv
   :header-rows: 1

* VARIABLEID -- Is the original Neotoma *variableid*

* TAXONID -- Is fkey. For available values refer to :ref:`cabah_taxaID_Fields`

* VARELEMTID -- Is fkey. For available values refer to :ref:`neo_variableelements_Fields`

* VARUNITID -- Is fkey. For available values refer to :ref:`neo_variableunits_Fields`

* VARCONTXID -- Is fkey. For available values refer to :ref:`neo_variablecontexts_Fields`


SahulSed tables
~~~~~~~~~~~~~~~

The following tables exclusively serve the :ref:`SahulSed`.

..  _sed_Sample:

sed_Sample table
^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ./csv_tables/sed_Sample.csv
   :header-rows: 1

* SMPID -- Sample identifier provided as part of the compilation. SahulSed SMPIDs have been aggregated using similarities in concatenated “X_WGS84” AND “Y_WGS84” AND “SITENAME” AND “SMPDEPTH”. Re suffixes -- '_pre' indicates that the matching age is preferred by the authors of the original publication; '_alt' tags alternatives to '_pre' ages; and '.o' indicates the existence of a corresponding TL ('.t') measurement on the same sample.

* SEDTYPE -- Sedimentary facies, referring to the main mechanism of transportation and deposition and, therefore, determining OCTOPUS/ SahulSed sub-compilation membership. |:lock:| A *predefined value set* only allows for 'AEN' (= aeolian), 'FLV' (= fluvial), or 'LAC' (= lacustrine)

* DUNEFIELD -- Name of dunefield in which the sample site located. Note -- “DUNEFIELD” field only usable if “SEDTYPE” = 'AEN', i.e., must be NULL for 'FLV' or 'LAC'. ('ND' = no data; NULL = not applicable)

* DUNTRND -- Trend, i.e., orientation of the sampled dune (in degree between 0 and 360). Note -- “DUNTRND” field only usable if “SEDTYPE” = 'AEN', i.e., must be NULL for 'FLV' or 'LAC'. (-9999 = no data; NULL = not applicable)

* DEPTHICK -- Total length of the core or height of the outcrop. (-9999 = no data; NULL = not applicable)

* SMPDEPTH -- Depth below the surface (or datum) from which sample was extracted. If the published sample depth was specified as a range, then the median value for that range is reported here. (-9999 = no data; NULL = not applicable)

* BEACHEI -- Height of the sampled beach ridge (if applicable). For beach ridges <1 m, 1 is recorded here. Note -- “BEACHEI” field only usable if “SEDTYPE” = 'LAC', i.e., must be NULL for 'AEN' or 'FLV'. (-9999 = no data; NULL = not applicable)

* BEACHAHD -- Australian Height Datum of the sampled beach ridge (if applicable). Note -- “BEACHAHD” field only usable if “SEDTYPE” = 'LAC', i.e., must be NULL for 'AEN' or 'FLV'. (-9999 = no data; NULL = not applicable)

* SMP_COMMT -- Free text sample comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _sed-osl_DataCore:

sed-osl_DataCore table
^^^^^^^^^^^^^^^^^^^^^^

The *sed-osl_DataCore* table stores stores **OSL-related observations** (= smallest data model entity), i.e., ages and their associated unique lab-derived data for the :ref:`SahulSed`, namely the :ref:`The_SahulSed_Aeolian_OSL_collection`, :ref:`The_SahulSed_Fluvial_OSL_collection`, and :ref:`The_SahulSed_Lacustrine_OSL_collection`.

.. hint::

    For information about the structure and fields of the *sed-osl_DataCore* table please refer to the :ref:`arch_osl_DataCore`. Said tables are structural identical.


..  _sed-tl_DataCore:

sed-tl_DataCore table
^^^^^^^^^^^^^^^^^^^^^

The *sed-tl_DataCore* table stores stores **TL-related observations** (= smallest data model entity), i.e., ages and their associated unique lab-derived data for the :ref:`SahulSed`, namely the :ref:`The_SahulSed_Aeolian_TL_collection`, :ref:`The_SahulSed_Fluvial_TL_collection`, and :ref:`The_SahulSed_Lacustrine_TL_collection`.

.. hint::

    For information about the structure and fields of the *sed-tl_DataCore* table please refer to the :ref:`arch_tl_DataCore`. Said tables are structural identical.


..  _sed_depconID:

sed_depconID table
^^^^^^^^^^^^^^^^^^
The *sed_depconID* table stores the **deposition context of a sampled feature**.

.. csv-table::
   :file: ./csv_tables/sed_depconID.csv
   :header-rows: 1

* DEPCONID -- A unique identifier (auto-incrementing serial integer)

* DEPCON -- For available values refer to :ref:`sed_depconID_Fields`


..  _sed_faciesID:

sed_faciesID table
^^^^^^^^^^^^^^^^^^
The *sed_faciesID* table stores the **type of sedimentological facies**.

.. csv-table::
   :file: ./csv_tables/sed_faciesID.csv
   :header-rows: 1

* FACIESID -- A unique identifier (auto-incrementing serial integer)

* FACIES -- For available values refer to :ref:`sed_faciesID_Fields`


..  _sed_geommodID:

sed_geommodID table
^^^^^^^^^^^^^^^^^^^
The *sed_geommodID* table stores the **geomorphic modifier of a sampled feature**.

.. csv-table::
   :file: ./csv_tables/sed_geommodID.csv
   :header-rows: 1

* GEOMMODID -- A unique identifier (auto-incrementing serial integer)

* GEOMMOD -- For available values refer to :ref:`sed_geommodID_Fields`


..  _sed_geotypeID:

sed_geotypeID table
^^^^^^^^^^^^^^^^^^^
The *sed_geotypeID* table stores the **geomorphological type of a sampled feature**.

.. csv-table::
   :file: ./csv_tables/sed_geotypeID.csv
   :header-rows: 1

* GEOTYPEID -- A unique identifier (auto-incrementing serial integer)

* GEOTYPE -- For available values refer to :ref:`sed_geotypeID_Fields`


..  _sed_laketypeID:

sed_laketypeID table
^^^^^^^^^^^^^^^^^^^^
The *sed_laketypeID* table stores the **type of (origin of) lake (formation)**. *sed_laketypeID* is a self-referencing table.

.. csv-table::
   :file: ./csv_tables/sed_laketypeID.csv
   :header-rows: 1

* LAKETYPEID -- A unique identifier (auto-incrementing serial integer)

* LAKETYPE -- For available values refer to :ref:`sed_laketypeID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "LAKETYPEID"


..  _sed_morphID:

sed_morphID table
^^^^^^^^^^^^^^^^^
The *sed_morphID* table stores the **morphology of a sampled feature**.

.. csv-table::
   :file: ./csv_tables/sed_morphID.csv
   :header-rows: 1

* MORPHID -- A unique identifier (auto-incrementing serial integer)

* MORPH -- For available values refer to :ref:`sed_morphID_Fields`


..  _sed_sitetypeID:

sed_sitetypeID table
^^^^^^^^^^^^^^^^^^^^
The *sed_sitetypeID* table stores the **type of the site from which samples were extracted**.

.. csv-table::
   :file: ./csv_tables/sed_sitetypeID.csv
   :header-rows: 1

* SITETYPEID -- A unique identifier (auto-incrementing serial integer)

* SITETYPE -- For available values refer to :ref:`sed_sitetypeID_Fields`


..  _sed-osl_points_EPSG3857:

sed-osl_points_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *sed-osl_points_EPSG3857* table stores **spatial features**, i.e., points of the OSL collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/sed-osl_points_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


..  _sed-tl_points_EPSG3857:

sed-tl_points_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *sed-tl_points_EPSG3857* table stores **spatial features**, i.e., points of the TL collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/sed-tl_points_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


..  _FosSahul_tables:

FosSahul tables
~~~~~~~~~~~~~~~

The following tables exclusively serve the :ref:`FosSahul`.

..  _fos_Sample:

fos_Sample table
^^^^^^^^^^^^^^^^
The *fos_Sample* table stores FosSahul collection sample information and is, therefore, situated between the collection-specific :ref:`fos_DataCore` (subordinate) and the :ref:`global_SiteMaster` (superordinate; see :ref:`Semantic_data_model`).

.. csv-table::
   :file: ./csv_tables/fos_Sample.csv
   :header-rows: 1

* SMPID -- Unique sample identifier that, first and foremost, serves database operation. FosSahul SMPIDs have been aggregated using similarities in concatenated “X_WGS84” AND “Y_WGS84” AND “SITENAME” AND “OBSID2”.

* STRAT_TAPH -- |:lock:| A *predefined value set* covers wheter stratigraphic ('Strat'), taphonomic ('Taph') or even both ('Both') information are available in source publication; 'ND' (= no data), 'NA' (= not applicable). “REFDOI” references link to secondary literature containing “STRAT_TAPH” information, so for example 'Strat, REFDOI2' would refer to secondary stratigraphy linked to “REFDBID2”. 

* SPEC_ABUND -- Wheter relative species abundances are given in source publication. |:lock:| A *predefined value set* only allows for 'No' (= Species abundances unavailable), 'Yes' (= Species abundances available), 'Yes, SupplMat' (= Species abundances available in Supplementary Material of original Publication), 'ND' (= no data), 'NA' (= not applicable)

* SQUARE_XU -- Square or trench designation and/ or excavation unit or spit designation from where the sample is from. Recurrent nomenclature abbreviated as described in 'Values' to the left; abbreviations are not upper/ lower case sensitive. **AHD** -- Australian Height Datum, **abv.** -- above, **analyt.** -- analytical, **arch.** -- archaeological, **bel.** -- below, **brec.** -- breccia, **catal.** -- catalogue, **class.** -- classic, **cult.** -- cultural, **dat.** -- datum, **dep.** -- deposit, **excav.** -- excavated/ -ion, **geom.** -- geomorphological, **hozn.** -- horizon, **in.** -- inch(es), **lay.** -- layer, **low.** -- lower, **meas.** -- measured, **mega.** -- megafauna(l), **no.** -- number, **pleist.** -- Pleistocene, **overl.** -- overlying, **rel.** -- relative, **sect.** -- section, **sed.** -- sediment/s, **shelt.** -- shelter, **sqre.** -- square, **strat.** -- stratigraphic, **strm.** -- stratum, **surf.** -- surface, **trch.** -- trench(es), **underl.** -- underlying, **u.** -- unit, **up.** -- upper

* SMP_COMMT -- Free text sample comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _fos_DataCore:

fos_DataCore table
^^^^^^^^^^^^^^^^^^
The *fos_DataCore* table stores **observations** (= smallest data model entity) for the :ref:`FosSahul` and is subordinate to the :ref:`fos_Sample`.

.. csv-table::
   :file: ./csv_tables/fos_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique sample identifier provided as part of the compilation. Serves as back reference to parent FosSahul fork (https://doi.org/10.1038/s41597-019-0267-3), with the prefix 'FOS' and wildcard zero(s) added to the original ID.

* OBSID2 -- Original sample identifier (as published). This is NOT the laboratory code provided by some labs, but the ID used by authors of the source publication to identify the sample. Samples labelled only by numbers in the literature (e.g., 1, 2, 3 etc) have had a compound prefix -- first three author name letters AND double-digit publication year -- added (e.g. 'Nan87_1' for sample 1 (Nanson 1987)).

* LABID -- Unique lab code assigned by the lab where age was determined. For radiocarbon (and for many luminescence) labs, the first part of the lab code refers to the determining facility.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* STATUS -- Most updated status. |:lock:| A *predefined value set* only allows for 'Extant', 'Extinct', 'ND' (= no data), or 'NA' (= not applicable)

* MEGAFAUNA -- 'Yes' if species weight > 44 kg, otherwise 'No', 'ND' for no data

* C14_CALIB -- Whether the published radiocarbon age is calibrated or uncalibrated. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* PHYSCLEAN -- Was the sample physically cleaned? For example, was the surface removed from bone (= 'Yes'), were rootlets and sediment removed from charcoal (= 'Yes'). |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* CONTAM -- Whether the study authors suggest a contaminant may have occurred. |:lock:| A *predefined value set* only allows for 'Likely' (= contamination likely), 'Possible' (= contamination possible), 'No' (= not contaminated), or 'Yes' (= indication for contamination), 'ND' (= no data), or 'NA' (= not applicable)

* XTR_PROBLEM -- Whether the study authors reported extraction problems. |:lock:| A *predefined value set* only allows for 'Yes', 'No', or 'ND' (= no data)

* CN_RATIO -- Measured atomic C:N ratio of the pretreated sample

* PCT_N -- Measured %N of the pretreated sample

* C14_XRDIFF -- For corals/shells only: Indicates if X-ray diffraction shows that recrystallisation is insignificant. |:lock:| A *predefined value set* only allows for 'No', 'ND' (= no data), or 'NA' (= not applicable)

* AAR_T_HIST -- Thermal history of the sample. Based on the established quality rating criteria (Rodríguez-Rey et al. 2015): is the thermal history of the sample unknown or were materials burnt (i.e., is “AAR_T_HIST” not 'Fine'), then rating will be 'C'. |:lock:| A *predefined value set* only allows for 'Fine', 'ND' (= no data), or 'NA' (= not applicable)

* AAR_CLOSD -- Whether the material has demonstrated closed-system behaviour. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* AAR_UNCERT -- Whether multiple analyses were replicated with low uncertainties. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* AAR_INCAL -- Whether reliable calibration was done using independent dating techniques. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* U_TH_PRE -- Short description of pretreatment

* U_TH_CLOSD -- Uranium-series ages for teeth (dentine) and bone: whether closed-system behaviour has been demonstrated by U-series profiling and modelling based on continuous profiles or spot sampling using laser ablation. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* U_TH_DCORR -- Uranium-series ages for closed-system of no body remains (e.g., speleothems, corals, calcite within bones etc): Whether a correction was made for detrital thorium contamination. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* ESR_I_DR10 -- ESR ages: Whether the internal dose rate is less/ greater 10%. |:lock:| A *predefined value set* only allows for '<10' (= less than 10%), '>10' (= greater than 10%), 'ND' (= no data), or 'NA' (= not applicable)

* ESR_GAMMA -- ESR ages: Whether the gamma dose rate was measured 'In_situ' or was 'Assumed'. |:lock:| A *predefined value set* only allows for 'In_situ', 'Assumed', 'ND' (= no data), or 'NA' (= not applicable)

* ALIQ_TYPE -- Reported aliquot type used for equivalent dose determination. |:lock:| A *predefined value set* only allows for 'MA' (= Multi Aliquot), 'SA' (= Single Aliquot), 'SG' (= Single Grain), 'ND' (= no data), or 'NA' (= not applicable)

* BLEACH_STS -- Luminescence bleaching status. |:lock:| A *predefined value set* only allows for 'Adequately', 'Partially', 'ND' (= no data), or 'NA' (= not applicable)

* AGEMD_TRUE -- Luminescence single grain equivalent dose model. Whether the luminescence age can be modelled. |:lock:| A *predefined value set* only allows for 'Yes', 'No', 'ND' (= no data), or 'NA' (= not applicable)

* AGE -- Published age

* AGE_ERR -- Published total age error

* AGE_TYPE -- Temporal quality of published age estimate. |:lock:| A *predefined value set* only allows for 'Min' (= Minimum age), 'Max' (= Maximum age), 'Exact' (= Exact age), 'ND' (= no data), or 'NA' (= not applicable)

* AGE_CI -- Published confidence interval on the age estimate. |:lock:| A *predefined value set* only allows for '1SD' (= 1 Standard deviation), '2SD' (= 2 Standard deviations), or 'ND' (= no data)

* AGE_PREQ -- Quality rating of dating protocol (see Rodríguez-Rey, M. et al. 2015. Quat Geochronol 30. Fig. 1). |:lock:| A *predefined value set* only allows for 'm*' (= Highest reliability), 'm' (= High reliability), 'B' (= Low reliability), 'C' (= Lowest reliability), or 'ND' (= no data)

* AGE_Q -- Reliability rating of fossil age (see Rodríguez-Rey, M. et al. , 2015). |:lock:| A *predefined value set* only allows for 'A*' (= Highly reliable), 'A' (= Reliable), 'B' (= Unreliable), C (= Highly unreliable), 'ND' (= no data)

* AGE_SUBQ -- Sub-category of “AGE_Q”, if reliable by association (see Rodríguez-Rey, M. et al. , 2015). |:lock:| A *predefined value set* only allows for 'a' (= above), 'w' (= within), 'b' (= below), 'ND' (= no data), or 'NA' (= not applicable)

* AGE_ASSOC1 -- 'Direct' age estimates have been derived from vertebrate parts of the target species itself. 'Indirect' ages are not based on taget species body parts, but still can be used based on association, i.e., the relationship between the target fossil and the dated structure/ material. |:lock:| A *predefined value set* only allows for 'Direct', 'Indirect', or 'ND' (= no data)

* AGE_ASSOC2 -- Applicable if “AGE_ASSOC1” = 'Indirect'. Additional descriptor for the quality of the association between the dated structure/ material and the target specimen. Is NA if “AGE_ASSOC1” = 'Direct'. |:lock:| A *predefined value set* only allows for 'Yes' (= clear association), 'No' (= association not clear), 'Uncertain' (= association uncertain), 'NA' ("AGE_ASSOC1" = 'Direct'), or 'ND' (= no data)

* AGE_PREQ_R -- Reason for “AGE_PREQ” value

* AGE_Q_R -- Reason for “AGE_Q” value

* AGE_COMMT -- Free text age comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _fos_TaxRank1_classID:

fos_TaxRank1_classID table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank1_classID* table stores the most updated **vertebrata class** name.

.. csv-table::
   :file: ./csv_tables/fos_TaxRank1_classID.csv
   :header-rows: 1

* CLASSID -- A unique identifier (auto-incrementing serial integer)

* CLASS -- The most updated **vertebrata class** name. For available values refer to :ref:`fos_TaxRank1_classID_Fields`


..  _fos_TaxRank2_infraclaID:

fos_TaxRank2_infraclaID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank2_infraclaID* table stores the most updated **vertebrata infraclass** name.

.. csv-table::
   :file: ./csv_tables/fos_TaxRank2_infraclaID.csv
   :header-rows: 1

* INFRACLAID -- A unique identifier (auto-incrementing serial integer)

* INFRACLASS -- The most updated **vertebrata infraclass** name. For available values refer to :ref:`fos_TaxRank2_infraclaID_Fields`


..  _fos_TaxRank3_ordrID:

fos_TaxRank3_ordrID table
^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank3_ordrID* table stores the most updated **vertebrata order** name.

.. csv-table::
   :file: ./csv_tables/fos_TaxRank3_ordrID.csv
   :header-rows: 1

* ORDRID -- A unique identifier (auto-incrementing serial integer)

* ORDR -- The most updated **vertebrata order** name. For available values refer to :ref:`fos_TaxRank3_ordrID_Fields`


..  _fos_TaxRank4_familyID:

fos_TaxRank4_familyID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank4_familyID* table stores the most updated **vertebrata family** name.

.. csv-table::
   :file: ./csv_tables/fos_TaxRank4_familyID.csv
   :header-rows: 1

* FAMILYID -- A unique identifier (auto-incrementing serial integer)

* FAMILY -- The most updated **vertebrata family** name. For available values refer to :ref:`fos_TaxRank4_familyID_Fields`


..  _fos_TaxRank5_genusID:

fos_TaxRank5_genusID table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank5_genusID* table stores the most updated **vertebrata genus** name.

.. csv-table::
   :file: ./csv_tables/fos_TaxRank5_genusID.csv
   :header-rows: 1

* GENUSID -- A unique identifier (auto-incrementing serial integer)

* GENUS -- The most updated **vertebrata genus** name. For available values refer to :ref:`fos_TaxRank5_genusID_Fields`


..  _fos_TaxRank6_speciesID:

fos_TaxRank6_speciesID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank6_speciesID* table stores the most updated **vertebrata species** name.

.. csv-table::
   :file: ./csv_tables/fos_TaxRank6_speciesID.csv
   :header-rows: 1

* SPECIESID -- A unique identifier (auto-incrementing serial integer)

* SPECIES -- The most updated **vertebrata species** name. For available values refer to :ref:`fos_TaxRank6_speciesID_Fields`


..  _fos_chemtypeID:

fos_chemtypeID table
^^^^^^^^^^^^^^^^^^^^
The *fos_chemtypeID* table stores the **type of chemical pretreatment given to the sample** as described in the original publication. There may be considerable variation within each pretreatment code.

.. csv-table::
   :file: ./csv_tables/fos_chemtypeID.csv
   :header-rows: 1

* CHEMTYPEID -- A unique identifier (auto-incrementing serial integer)

* CHEMTYPE -- For available values refer to :ref:`fos_chemtypeID_Fields`

* CHEMTYPEAB -- For available values refer to :ref:`fos_chemtypeID_Fields`


..  _fos_fosmat1ID:

fos_fosmat1ID table
^^^^^^^^^^^^^^^^^^^
The *fos_fosmat1ID* table stores the **type of dated remain**.

.. csv-table::
   :file: ./csv_tables/fos_fosmat1ID.csv
   :header-rows: 1

* FOSMAT1IDd -- A unique identifier (auto-incrementing serial integer)

* FOSMAT1 -- For available values refer to :ref:`fos_fosmat1ID_Fields`

* FOSMAT1ABB -- For available values refer to :ref:`fos_fosmat1ID_Fields`


..  _fos_fosmat2ID:

fos_fosmat2ID table
^^^^^^^^^^^^^^^^^^^
The *fos_fosmat2ID* table stores the **type of dated material**.

.. csv-table::
   :file: ./csv_tables/fos_fosmat2ID.csv
   :header-rows: 1

* FOSMAT2ID -- A unique identifier (auto-incrementing serial integer)

* FOSMAT2 -- For available values refer to :ref:`fos_fosmat2ID_Fields`

* FOSMAT2ABB -- For available values refer to :ref:`fos_fosmat2ID_Fields`


..  _fos_mtdsID:

fos_mtdsID table
^^^^^^^^^^^^^^^^
The *fos_mtdsID* table stores the type of **method used in age determination**.

.. csv-table::
   :file: ./csv_tables/fos_mtdsID.csv
   :header-rows: 1

* FOS_MTDSID -- A unique identifier (auto-incrementing serial integer)

* FOS_MTDSUB -- For available values refer to :ref:`fos_mtdsID_Fields`

* FOS_MTDSAB -- For available values refer to :ref:`fos_mtdsID_Fields`


..  _fos_polygons_EPSG3857:

fos_polygons_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_polygons_EPSG3857* table stores **spatial features**, i.e., polygons of the FosSahul partner collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/fos_polygons_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


..  _expage_tables:

ExpAge tables
~~~~~~~~~~~~~

The following tables exclusively serve the :ref:`expage`.

..  _expage_Sample:

expage_Sample table
^^^^^^^^^^^^^^^^^^^
The *expage_Sample* table stores :ref:`expage` sample information and is, therefore, situated between the collection-specific :ref:`expage_DataCore` (subordinate) and the :ref:`global_SiteMaster` (superordinate; see :ref:`Semantic_data_model`).

.. csv-table::
   :file: ./csv_tables/expage_Sample.csv
   :header-rows: 1

* SMPID -- Unique sample identifier that serves database operation

* THICKNESS -- Sample thickness

* DENSITY -- Sample density. When information is not provided in original publication, 2.65 g/cm^3 is assumed

* SHIELDING -- Topographic / geometric shielding of the sample

* SMP_YR -- Year of sample collection. Generally assumed to be two years before publication if not indicated.

* SMP_COMMT -- Free text sample comment field

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _expage_DataCore:

expage_DataCore table
^^^^^^^^^^^^^^^^^^^^^
The *expage_DataCore* table stores **observations** (= smallest data model entity) for the :ref:`expage` and is subordinate to the :ref:`expage_Sample`.

.. csv-table::
   :file: ./csv_tables/expage_DataCore.csv
   :header-rows: 1

* OBSID1 -- Unique age identifier provided as part of the compilation. Serves as back reference to parent ExpAge fork (https://expage.github.io), with running alphabetic letter(s) added to the original “Sample ID”.

* OBSID2 -- Original sample identifier (as published). This is NOT the laboratory code provided by some labs, but the ID used by authors of the source publication to identify the sample.

* IGSNID -- Placeholder for International Geo Sample Number unique ID

* BE10NP -- Published Be-10 concentration. (-9999 = no data)

* BE10NP_ERR -- Published 1-sigma uncertainty in Be-10 concentration. (-9999 = no data)

* BE10AP -- Published Be-10 exposure age. (-9999 = no data)

* BE10AP_ERR -- Published Be-10 exposure age. (-9999 = no data)

* AL26NP -- Published Al-26 concentration. (-9999 = no data)

* AL26NP_ERR -- Published 1-sigma uncertainty in Al-26 concentration. (-9999 = no data)

* AL26AP -- Published Al-26 exposure age. (-9999 = no data)

* AL26AP_ERR -- Published Al-26 exposure age. (-9999 = no data)

* ABE_YR -- Recalculated zero erosion Be-10 exposure age. (-9999.99 = no data)

* ABE_ERREXT -- External uncertainty for “ABE_YR”. (-9999.99 = no data) For detailed information see Balco et al. 2008 [#]_

* ABE_ERRINT -- External uncertainty for “ABE_YR”. (-9999.99 = no data) For detailed information see Balco et al. 2008

* AAL_YR -- Recalculated zero erosion Al-26 exposure age. (-9999.99 = no data)

* AAL_ERREXT -- External uncertainty for “AAL_YR”. (-9999.99 = no data) For detailed information see Balco et al. 2008

* AAL_ERRINT -- Internal uncertainty for “AAL_YR”. (-9999.99 = no data) For detailed information see Balco et al. 2008

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _expage_points_EPSG3857:

expage_points_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *expage_points_EPSG3857* table stores spatial features, i.e., points of the ExpAge partner collection (EPSG:900913).

.. csv-table::
   :file: ./csv_tables/expage_points_EPSG3857.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available


.. rubric:: Footnotes

.. [#] `Primary key <https://www.postgresql.org/docs/15/ddl-constraints.html#DDL-CONSTRAINTS-PRIMARY-KEYS>`_
.. [#] `Unique key <https://www.postgresql.org/docs/15/ddl-constraints.html#DDL-CONSTRAINTS-UNIQUE-CONSTRAINTS>`_
.. [#] `Foreign key <https://www.postgresql.org/docs/15/ddl-constraints.html#DDL-CONSTRAINTS-FK>`_
.. [#] This self-referencing table is both parent and child at the same time - a table design that was chosen for the representation of nested hierarchies. 
.. [#] PostgreSQL view: `https://www.postgresql.org/docs/current/sql-createview.html <https://www.postgresql.org/docs/current/sql-createview.html>`_
.. [#] Field descriptions unaltered taken from `https://postgis.net/ <https://postgis.net/>`_
.. [#] `https://www.ctan.org/pkg/bibtex <https://www.ctan.org/pkg/bibtex>`_
.. [#] Digital Elevation Model, i.e., a digital representation of elevation data / terrain
.. [#] dimensionless
.. [#] https://epsg.org/
.. [#] Well Known Text (https://postgis.net/docs/manual-1.4/ch04.html#id417971)
.. [#] Balco et al. 2008 (https://doi.org/10.1016/j.quageo.2007.12.001)
