============================
Data tables and their fields
============================
OCTOPUS data tables, using a spatial allegory, can be grouped into a *global*, a *regional*, and a *local* level. While :ref:`Global_tables` can serve any database relation, :ref:`Regional_tables` should be seen as thematic tables matching certain sub-collections. Finally, :ref:`Local_tables` are collection specific tables with a high degree of specialisation compared to the two aforementioned higher-level table groups.

PostgreSQL data types, constraints, and foreign key principles are comprehensibly described in the PostgreSQL online documentation (https://www.postgresql.org/docs/15/datatype.html). Another excellent, more introductory read is Michael J. Hernandez' *Database design for Mere Mortals - A Hands-On Guide to Relational Database Design*.

.. note::

    To ensure database integrity, any OCTOPUS db relation features a "CREATED_AT" (= *record timestamp* with timezone based on UTC) and a "UPDATED_AT" (= *timestamp of record update* with timezone based on UTC) field, respectively. These fields are automatically populated upon db trigger, however, are not displayed as part of this documentation for the sake of readability.

..  _Global_tables:

Global tables
-------------
This section features information about :ref:`Global_lookup_tables` (i.e., indexed arrays of certain data recurring across the entire database), :ref:`Global_georeferencing_tables` (i.e., tables that store information about the spatial context of an observation), and :ref:`Global_references_tables`. The latter relations form the part of OCTOPUS db that allows for definite identification of data sources resp. publications.

..  _Global_lookup_tables:

Global lookup tables
~~~~~~~~~~~~~~~~~~~~

..  _global_varunitID:

global_varunitID table
^^^^^^^^^^^^^^^^^^^^^^
The *global_varunitID* table stores **variable units** for those compilations whose values involve different units of measurement. Data tables with invariant variable units, however, do not feature explicit units fields. 

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
``DRAFT`` The *global_MetaSite* table ...

..  _global_SiteCode:

global_SiteCode table
^^^^^^^^^^^^^^^^^^^^^
The *global_SiteCode* table stores **site types characterising the dominant attribute of a site**.

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

========== ============== =========== ==== ======== ======================
Field      Data type      Unit        Key  Not Null Parent
========== ============== =========== ==== ======== ======================
SITEID     text                       pkey TRUE     
METASITEID text                       fkey          :ref:`global_MetaSite`
CNTRY      varchar(3)                      TRUE     
REGION_INT text                                    
REGION_REG varchar(3)                              
DIV_ADMIN  varchar(7)                              
DIV_OTHER  text                                    
ISL_NAME   text                                    
LAKE       text                                    
BASIN      text                                    
RIVID      int2                       fkey          :ref:`global_rivID`
IBRAID     int2                       fkey          :ref:`global_ibraID`
X_WGS84    numeric(10, 6) decimal deg               
Y_WGS84    numeric(10, 6) decimal deg               
CORDS_ELEV varchar(9)                      TRUE     
ELEVATION  numeric(6, 2)  m                 
SITENAME   text                                    
SITE_SPEC  text                                    
ALTNAME1   text                                    
ALTNAME2   text                                    
ALTNAME3   text                                    
SITECODEID int2                       fkey          :ref:`global_SiteCode`
OPENCLOSED varchar(6)                              
SITE_COMMT text                                    
========== ============== =========== ==== ======== ======================

* SITEID -- A unique site identifier provided as part of the compilation

* METASITEID -- Is fkey. Refer to :ref:`global_MetaSite` table

* CNTRY -- `ISO 3166 Alpha-3 country code <https://www.iso.org/obp/ui/#search>`_

* REGION_INT -- Region where the study site is located

* REGION_REG -- Refers to Sahul region. Same as “CNTRY” but needed to accommodate for 'TSI'

* DIV_ADMIN -- ISO 3166 code of the administrative region where the study site is located

* DIV_OTHER -- Geographical region in 'PNG' and 'TSI' where study site is located

* ISL_NAME -- Name of island where study site is located

* LAKE -- Name of lake where study site is located

* BASIN -- Name of river basin where study site is located

* RIVID -- Is fkey. For available values refer to :ref:`global_rivID` table

* IBRAID -- Is fkey. For available values refer to :ref:`global_ibraID` table

* X_WGS84 -- WGS84 longitude of site

* Y_WGS84 -- WGS84 latitude of site

* CORDS_ELEV -- Dual field. First part of value refers to source of coordinates (“X_WGS84”, “Y_WGS84”) for the sample site ('INTP', or 'ORIG', or 'ND'). Second part of value refers to “ELEVATION” ('INTP', or 'ORIG', or 'ND'). Nine (9) combinations possible

* ELEVATION -- Elevation above sea level

* SITENAME -- Name of the site

* SITE_SPEC -- Further specifies information given in “SITENAME”

* ALTNAME1 -- First alternative or additional name of the site (e.g., published under previous name etc.)

* ALTNAME2 -- Second alternative or additional name of the site

* ALTNAME3 -- Third alternative or additional name of the site

* SITECODEID -- Is fkey. For available values refer to :ref:`global_SiteCode` table

* OPENCLOSED -- This field records whether the site was closed (i.e., a rockshelter, cave or other enclosed site) or open (i.e., an artefact scatter, midden on a beach etc.), and is used in the application of taphonomic techniques in time-series analysis. Please note that 'Closed' does not relate to availability or accessibility of information. Note - This field is related to the :ref:`SahulArch` collection, i.e., will not appear in any other collection view [#]_ or flat output table.

* SITE_COMMT -- Free text site comment field

..  _global_biomeID:

global_biomeID table
^^^^^^^^^^^^^^^^^^^^
The *global_biomeID* table stores iconic biome types that allow for a coarse characterisation/classifications of sampled sites amongst Earth's major biogeographic units. 

.. csv-table::
   :file: ./csv_tables/global_biomeID.csv
   :header-rows: 1

* BIOMEID -- Unique identifier (serial integer)

* BIOMETYPE -- Name of biome. For available values refer to :ref:`global_biomeID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "BIOMEID"

* BIOMEDESCR -- A concise description of "BIOMETYPE"

..  _global_dbDOI:

global_dbDOI table
^^^^^^^^^^^^^^^^^^
``DRAFT`` The *global_dbDOI* table ...

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

.. warning::

    The global_ibraID table only applies to samples from Australia.

..  _global_rivID:

global_rivID_table
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

.. warning::

    The global_rivID table only applies to samples from Australia.

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

=========== =========== ==== ==== ======== ==================
Field       Data type   Unit Key  Not Null Parent
=========== =========== ==== ==== ======== ==================
REFDBID     text             pkey TRUE     
OAID        varchar(11)      fkey          :ref:`global_Author`
REFDOI      text                           
AUTHORS     text                           
TITLE       text                           
PUBTYPEID   int2             fkey TRUE     :ref:`global_PubType`
JOURNALID   int2             fkey          :ref:`global_Journal`
VOLUME      text                           
NUMBER      text                           
PAGES       text                           
YEAR        int2                  TRUE     
ADDRESS     text                           
NOTE        text                           
URL         text                           
BOOKTITLE   text                           
CHAPTER     text                           
EDITOR      text                           
PUBLISHER   text                           
INSTITUTION text                           
SCHOOL      text                           
=========== =========== ==== ==== ======== ==================

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

* ABSTRACT -- Is publication abstract, if available. Note - Very extensive abstracts have been truncated and marked as *... [_truncated_]* at their end.

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

..  _global_RefKeyword:

global_RefKeyword table
^^^^^^^^^^^^^^^^^^^^^^^

``DRAFT`` The *global_RefKeyword* table ...

----

..  _Regional_tables:

Regional tables
---------------

Non-Cosmogenics tables
~~~~~~~~~~~~~~~~~~~~~~

..  _cabah_LabCodes:

cabah_LabCodes table
^^^^^^^^^^^^^^^^^^^^
The *cabah_LabCodes* table stores information about the **lab of origin** for a certain C14 or luminescence observation, i.e., measurement. The labs have been identified automatically by their distinct labcode prefixes

.. csv-table::
   :file: ./csv_tables/cabah_LabCodes.csv
   :header-rows: 1

* LAB_ORIGID -- A unique identifier (auto-incrementing serial integer)

* LAB_PREFIX -- Lab prefix

* LAB_FACLTY -- Facility / institution of lab affiliation

* CNTRY -- Country of "LAB_FACLTY"

* LAB_ACTIVE -- Whether the lab is active or not

* LAB_MTD -- Lab method (C14, OSL, TL)

* LAB_URL -- Lab url

* LAB_SOURCE -- Source of information stored in a certain tuple. Major yources are 'Radiocarbon' (https://doi.org/10.1017/S0033822200038923) and 'RadonKiel' (https://radon.ufg.uni-kiel.de/labs).

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

..  _cabah_col_mtdID:

cabah_col_mtdID table
^^^^^^^^^^^^^^^^^^^^^
The *cabah_col_mtdID* table stores the **sample collection method**.

.. csv-table::
   :file: ./csv_tables/cabah_col_mtdID.csv
   :header-rows: 1

* COL_MTDID -- A unique identifier (auto-incrementing serial integer)

* COL_MTD -- For available values refer to :ref:`cabah_col_mtdID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking “COL_MTDID”

..  _cabah_methodID:

cabah_methodID table
^^^^^^^^^^^^^^^^^^^^
The *cabah_methodID* table stores the **type of method used in age/rate determination**.

.. csv-table::
   :file: ./csv_tables/cabah_methodID.csv
   :header-rows: 1

* METHODID -- A unique identifier (auto-incrementing serial integer)

* METHOD -- For available values refer to :ref:`cabah_methodID_Fields`

* METHODABBR -- For available values refer to :ref:`cabah_methodID_Fields`

* PARENTID -- Is fkey. Refers to ordinal higher ranking "METHODID"

* METHODREF -- Basic method literature reference

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


SahulArch tables
~~~~~~~~~~~~~~~~

..  _arch_Sample:

arch_Sample table
^^^^^^^^^^^^^^^^^
The *arch_Sample* table stores SahulArch sample (see :ref:`Semantic_data_mode`) and is, therefore, situated between the collection-specific DataCore tables (subordinate) and the `global_SiteMaster` (superordinate).

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

* OCCUPATION -- Is the dated sample directly related to human activity (e.g. hearth, organic artefact, burial), or was it simply part of a wider archaeological deposit. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* CONTEXT -- Was the sample collected from a stratigraphic unit that is associated with human 'Occupation' or one that was culturally 'Sterile'. A **predefined value set** only allows for 'Occupation', 'Sterile', or 'ND' (= 'no data')

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

* BURNT -- Whether the material dated was burnt. Note that charcoal = 'Yes'. Calcinated bone -- typically white, whilst burnt bone is black -- is different to burnt bone, and so is listed in “MATERIAL2” field. A **predefined value set** only allows for 'Yes' (= burnt), 'No' (= not burnt), or 'ND' (= 'no data')

* ARCHSPECIS -- Genus and/ or species, i.e., scientific name of animal or plant used for 14C dating

* ORGPART -- Bone element, wood part etc. -- e.g., 'Sapwood', 'Heartwood', 'Twig', 'Ring number', 'Femur' ...

* SINGULAR -- Was a single entity (e.g., a single piece of charcoal, not several pieces found close to each other) dated, or were several pieces bulked together? A **predefined value set** only allows for 'Yes', 'No', 'NA' (single entities do not exist, i.e., for example sediment), or 'ND' (= 'no data')

* CONSERV -- Was the sample conserved? For example, was it glued or soaked in a consolidant? A **predefined value set** only allows for 'Yes', 'No', 'ND' (= 'no data'), or 'NA' (= not applicable)

* AGEMTD -- Measurement method. Conventional includes liquid scintillation and gas proportional. A **predefined value set** only allows for 'AMS' (= Accelerator Mass Spectrometry), 'CONV' (= conventional), or 'ND' (= 'no data')

* PHYSCLEAN -- Was the sample physically cleaned? For example, was the surface removed from bone (= 'Yes'), were rootlets and sediment removed from charcoal (= 'Yes'). A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* SOLVENT1 -- Was the pretreatment preceded by a solvent extraction? A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

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

* RECRYST -- Is secondary recrystallisation present in the pretreated carbonate sample? A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* PCT_RE_VAL -- Calcite/recrystallised mineral in the pretreated carbonate sample. Stain or microscopy methods used: 998 = presence of calcite/ recrystallization verified, or -991 = absence of calcite/ recrystallization.

* PCT_RE_ERR -- Error for measured amount of calcite/recrystallised mineral in the pretreated sample. Is -9999.99 even if “PCT_RE_VAL” = 998

* PCT_RE_MTD -- How was the presence and/or amount of calcite/recrystallisation measured in the pretreated carbonate sample. A **predefined value set** only allows for 'Stain' (= Fiegl's stain), 'XRD' (= X-ray diffractometry), 'FTIR' (= FT infrared spectroscopy), 'Micro' (= Microscopy), 'Other' (= other), or 'ND' (= 'no data')

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

* C14_INF -- Is the date infinite (indistinguishable from the laboratory background). This field clarifies the two previous fields, where no data may be misinterpreted as an infinite measurement. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* F14C -- Proportion of radiocarbon atoms in the sample compared to that present in the year AD 1950. “F14C” is pMC (percent modern carbon)/100.

* F14C_ERR -- Error for proportion of radiocarbon atoms in the sample compared to that present in the year AD 1950. The error for “F14C” is the error for pMC (percent modern carbon)/100.

* AGE_COMMT -- Free text age comment field.


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

* ALIQ_TYPE -- Reported aliquot type used for equivalent dose determination. A **predefined value set** only allows for 'SG' (= Single Grain), 'SA' (= Single Aliquot), 'MA' (= Multipe Aliquots), or 'ND' (= 'no data')

* ALIQ_SIZE -- Reported size of aliquot diameter in mm

* ED_PROCID -- Abbreviated reported procedure used to determine sample equivalent dose for OSL and TL methods

* RESCOR -- Residual dose correction was applied to the Equivalent Dose, specifically for IRSL, pIRIR, MET-pIRIR, VSL, and TT-OSL. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* DOSERECOV -- Were dose recovery test results reported in the study? A **predefined value set** only allows for 'Yes', 'No', 'ND' (= 'no data'), or 'NA' (= not applicable)

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

* ALPH_I_MTD -- Was the internal alpha dose rate assumed or measured? A **predefined value set** only allows for 'Assumed', 'Measured', or 'ND' (= 'no data')

* BETA_I -- Internal beta dose rate (from within grain)

* BETA_I_ERR -- 1 standard error (1σ) for "BETA_I"

* BETA_I_MTD -- Was the internal beta dose rate assumed or measured? A **predefined value set** only allows for 'Assumed', 'Measured', or 'ND' (= 'no data')

* DIFF_DOSE -- Whether a different and/or additional method, not specified in this compilation was used to determine the dosimetry for this sample. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* DOSERATE -- Total (wet) environmental dose rate used for age determination

* DOSE_ERR -- Total (wet) environmental dose rate error at 1σ

* OSL_AGE -- Published OSL age

* OSL_RNDERR -- Published Random only “OSL_AGE” error

* OSL_ERR -- Published total “OSL_AGE” error (random + systematic)

* AGE_CI -- Published confidence interval on the age estimate. A **predefined value set** only allows for '1s' (= 1 standard error [1σ]), '2s' (= 2 standard error [2σ]), 'SD' (= Standard Deviation), or 'ND' (= 'no data')

* FADCOR -- “OSL_AGE” was corrected for fading, specifically for IRSL, pIRIR, and MET-pIRIR. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* G_VAL -- Represents the correcting approach using value of fading rate in feldspars. If reported, express as percent per decade.

* G_VAL_ERR -- Published 1σ error for the “G_VAL”

* AGE_COMMT -- Free text age comment field.

.. note::

    Fkey fields are decribed elsewhere, i.e., within the scope of their tables of origin.


..  _arch_tl_DataCore:

arch_tl_DataCore table
^^^^^^^^^^^^^^^^^^^^^^^
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

* ED_PROCID -- Abbreviated reported procedure used to determine sample equivalent dose for OSL and TL methods

* RESCOR -- Residual dose correction was applied to the Equivalent Dose, specifically for IRSL, pIRIR, MET-pIRIR, VSL, and TT-OSL. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

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

* ALPH_I_MTD -- Was the internal alpha dose rate assumed or measured? A **predefined value set** only allows for 'Assumed', 'Measured', or 'ND' (= 'no data')

* BETA_I -- Internal beta dose rate (from within grain)

* BETA_I_ERR -- 1 standard error (1σ) for "BETA_I"

* BETA_I_MTD -- Was the internal beta dose rate assumed or measured? A **predefined value set** only allows for 'Assumed', 'Measured', or 'ND' (= 'no data')

* DIFF_DOSE -- Whether a different and/or additional method, not specified in this compilation was used to determine the dosimetry for this sample. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* DOSERATE -- Total (wet) environmental dose rate used for age determination

* DOSE_ERR -- Total (wet) environmental dose rate error at 1σ

* TL_AGE -- Published TL age

* TL_RNDERR -- Published Random only “TL_AGE” error

* TL_ERR -- Published total “TL_AGE” error (random + systematic)

* AGE_CI -- Published confidence interval on the age estimate. A **predefined value set** only allows for '1s' (= 1 standard error [1σ]), '2s' (= 2 standard error [2σ]), 'SD' (= Standard Deviation), or 'ND' (= 'no data')

* FADCOR -- “OSL_AGE” was corrected for fading, specifically for IRSL, pIRIR, and MET-pIRIR. A **predefined value set** only allows for 'Yes', 'No', or 'ND' (= 'no data')

* G_VAL -- Represents the correcting approach using value of fading rate in feldspars. If reported, express as percent per decade.

* G_VAL_ERR -- Published 1σ error for the “G_VAL”

* AGE_COMMT -- Free text age comment field.

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
The *c14_materia2ID* table stores information about the **sub-type of sample material used for 14C dating**.

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

SahulSed tables
~~~~~~~~~~~~~~~

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
The *sed_laketypeID* table stores the **type of (origin of) lake (formation)**.

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

FosSahul tables
~~~~~~~~~~~~~~~

fos_TaxRank1_classID
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank1_classID* table stores the most updated **vertebrata class** name.

``Table to come``

fos_TaxRank2_infraclaID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank2_infraclaID* table stores the most updated **vertebrata infraclass** name.

``Table to come``

fos_TaxRank3_ordrID table
^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank3_ordrID* table stores the most updated **vertebrata order** name.

``Table to come``

fos_TaxRank4_familyID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank4_familyID* table stores the most updated **vertebrata family** name.

``Table to come``

fos_TaxRank5_genusID table
^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank5_genusID* table stores the most updated **vertebrata genus** name.

``Table to come``

fos_TaxRank6_speciesID table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_TaxRank6_speciesID* table stores the most updated **vertebrata species** name.

``Table to come``

fos_chemtypeID table
^^^^^^^^^^^^^^^^^^^^
The *fos_chemtypeID* table stores the **type of chemical pretreatment given to the sample** as described in the original publication. There may be considerable variation within each pretreatment code.

.. csv-table::
   :file: ./csv_tables/fos_chemtypeID.csv
   :header-rows: 1

* CHEMTYPEID -- A unique identifier (auto-incrementing serial integer)

* CHEMTYPE -- For available values refer to :ref:`fos_chemtypeID_Fields`

* CHEMTYPEAB -- For available values refer to :ref:`fos_chemtypeID_Fields`

fos_fosmat1ID table
^^^^^^^^^^^^^^^^^^^
The *fos_fosmat1ID* table stores the **type of dated remain**.

.. csv-table::
   :file: ./csv_tables/fos_fosmat1ID.csv
   :header-rows: 1

* FOSMAT1IDd -- A unique identifier (auto-incrementing serial integer)

* FOSMAT1 -- For available values refer to :ref:`fos_fosmat1ID_Fields`

* FOSMAT1ABB -- For available values refer to :ref:`fos_fosmat1ID_Fields`

fos_fosmat2ID table
^^^^^^^^^^^^^^^^^^^
The *fos_fosmat2ID* table stores the **type of dated material**.

.. csv-table::
   :file: ./csv_tables/fos_fosmat2ID.csv
   :header-rows: 1

* FOSMAT2ID -- A unique identifier (auto-incrementing serial integer)

* FOSMAT2 -- For available values refer to :ref:`fos_fosmat2ID_Fields`

* FOSMAT2ABB -- For available values refer to :ref:`fos_fosmat2ID_Fields`

fos_mtdsID table
^^^^^^^^^^^^^^^^
The *fos_mtdsID* table stores the type of **method used in age determination**.

.. csv-table::
   :file: ./csv_tables/fos_mtdsID.csv
   :header-rows: 1

* FOS_MTDSID -- A unique identifier (auto-incrementing serial integer)

* FOS_MTDSUB -- For available values refer to :ref:`fos_mtdsID_Fields`

* FOS_MTDSAB -- For available values refer to :ref:`fos_mtdsID_Fields`

fos_polygons_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *fos_polygons_EPSG3857* table stores **spatial features**, i.e., polygons of the FosSahul partner collection (EPSG:900913).

``Table to come``

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- WKT geometry notation

* OBSID1 -- A unique identifier and one-to-one reference to a certain observation

* OBSID2 -- The original sample identifier (as published), if available

expage tables
~~~~~~~~~~~~~

expage_points_EPSG3857 table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *expage_points_EPSG3857* table stores spatial features, i.e., points of the expage partner collection (EPSG:900913).

``Table to come``

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
.. [#] https://epsg.org/
.. [#] Well Known Text (https://postgis.net/docs/manual-1.4/ch04.html#id417971)
