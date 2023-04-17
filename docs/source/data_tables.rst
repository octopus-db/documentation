============================
Data tables and their fields
============================
| OCTOPUS data tables, using a spatial allegory, can be grouped into a *global*, a *regional*, and a *local* level. While a :ref:`Global_tables` can serve any database relation, :ref:`Regional_tables` should be seen as a thematic tables not matching certain sub-collections. Finally, :ref:`Local_tables` are collection specific tables with a high degree of specialisation compared to the two aforementioned higher-level table groups.

| ``DRAFT`` --> data type abbreviations, key abbreviations, not null, parent (link to https://www.postgresql.org/docs/11/datatype.html)
| ``DRAFT`` --> "CREATED_AT" (Is record timestamp with timezone based on UTC), "UPDATED_AT" (Is timestamp of record update with timezone based on UTC)

..  _Global_tables:

Global tables
-------------

..  _Global_lookup_tables:

Global lookup tables
~~~~~~~~~~~~~~~~~~~~

..  _global_varunitID:

global_varunitID
^^^^^^^^^^^^^^^^
``DRAFT`` This table ... :ref:`global_varunitID_Fields`

.. csv-table::
   :file: ./csv_tables/global_varunitID.csv
   :header-rows: 1

..  _global_GrainSize:

global_GrainSize
^^^^^^^^^^^^^^^^
| ``DRAFT`` This table stores the *type of material sampled* (= "MATERIAL" in CRN denudation and expage tables, = "SED_MAT" in SahulSed tables).
| ... ... :ref:`global_GrainSize_Fields`

.. csv-table::
   :file: ./csv_tables/global_GrainSize.csv
   :header-rows: 1

* GRNSIZEID -- A unique identifier (auto-incrementing serial integer)

* GRNSIZE -- Name of grain size fraction / material

* GRNSIZEABB -- Unique abbreviation of "GRNSIZE"

* GRNSIZEMIN -- Lower grainsize fraction limit, if applicable

* GRNSIZEMAX -- Upper grain size fraction limit, if applicable

Global georeferencing tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  _global_MetaSite:

global_MetaSite
^^^^^^^^^^^^^^^

..  _global_SiteCode:

global_SiteCode
^^^^^^^^^^^^^^^
The *global_SiteCode* table stores **site types characterising the dominant attribute of a site**

.. csv-table::
   :file: ./csv_tables/global_SiteCode.csv
   :header-rows: 1

* SITECODEID -- A unique identifier (auto-incrementing serial integer)

* SITECODE -- For available values refer to :ref:`global_SiteCode_Fields`

..  _global_SiteMaster:

global_SiteMaster
^^^^^^^^^^^^^^^^^

``DRAFT`` This table

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

* SITEID -- 

* METASITEID -- Is fkey. Refer to :ref:`global_MetaSite` table

* CNTRY -- `ISO 3166 Alpha-3 country code <https://www.iso.org/obp/ui/#search>`_

* REGION_INT -- Region where the study site is located

* REGION_REG -- Refers to Sahul region. Same as “CNTRY” but needed to accommodate for ‘TSI’

* DIV_ADMIN -- ISO 3166 code of the administrative region where the study site is located

* DIV_OTHER -- Geographical region in ‘PNG’ and ‘TSI’ where study site is located

* ISL_NAME -- Name of island where study site is located

* LAKE -- Name of lake where study site is located

* BASIN -- Name of river basin where study site is located

* RIVID -- Is fkey. Refer to :ref:`global_rivID` table

* IBRAID -- Is fkey. Refer to :ref:`global_ibraID` table

* X_WGS84 -- WGS84 longitude of site

* Y_WGS84 -- WGS84 latitude of site

* CORDS_ELEV -- Dual field. First part of value refers to source of coordinates (“X_WGS84”, “Y_WGS84”) for the sample site ('INTP', or 'ORIG', or 'ND'). Second part of value refers to “ELEVATION” ('INTP', or 'ORIG', or 'ND'). Nine (9) combinations possible

* ELEVATION -- Elevation above sea level of the sample

* SITENAME -- Name of the site

* SITE_SPEC -- Further specifies information given in “SITENAME”

* ALTNAME1 -- First alternative or additional name of the site (e.g., published under previous name etc.)

* ALTNAME2 -- Second alternative or additional name of the site

* ALTNAME3 -- Second alternative or additional name of the site

* SITECODEID -- Is fkey. Refer to :ref:`global_SiteCode` table

* OPENCLOSED -- This field records whether the site was closed (i.e., a rockshelter, cave or other enclosed site) or open (i.e., an artefact scatter, midden on a beach etc.), and is used in the application of taphonomic techniques in time-series analysis. Please note that ‘Closed’ does not relate to availability or accessibility of information. Note - this field is related to the :ref:`SahulArch` collection, i.e., will not appear in any other collection view [#]_ or flat output table.

* SITE_COMMT -- Free text site comment field

..  _global_biomeID:

global_biomeID
^^^^^^^^^^^^^^
``DRAFT`` -- 

.. csv-table::
   :file: ./csv_tables/global_biomeID.csv
   :header-rows: 1

* BIOMEID -- Unique identifier (serial integer)

* BIOMETYPE -- Name of biome

* PARENTID -- Is fkey. Refers to ordinally higher ranking "BIOMEID"

* BIOMEDESCR -- A concise description of "BIOMETYPE"

For available values refer to :ref:`global_biomeID_Fields`

..  _global_dbDOI:

global_dbDOI
^^^^^^^^^^^^

..  _global_ibraID:

global_ibraID
^^^^^^^^^^^^^
``DRAFT`` This table ... :ref:`global_ibraID_Fields`

.. csv-table::
   :file: ./csv_tables/global_ibraID.csv
   :header-rows: 1

* IBRAID -- Unique identifier (serial integer)

* IBRACODE -- The location code of the site within the relevant bioregion as defined by the Interim Bio-Regionalisation of Australia (IBRA7) framework. *Only used for data from Australia*

* IBRAREGION -- The location of the site within the relevant bioregion as defined by the Interim Bio-Regionalisation of Australia (IBRA7) framework. *Only used for data from Australia*

For available values refer to :ref:`global_ibraID_Fields`

..  _global_rivID:

global_rivID
^^^^^^^^^^^^
``DRAFT`` This table ... :ref:`global_rivID_Fields`

.. csv-table::
   :file: ./csv_tables/global_rivID.csv
   :header-rows: 1

* RIVID -- Unique identifier (serial integer)

* AHGFL1 -- Geofabric AHGF river region code. *Only used for data from Australia*

* AHGFL2 -- Geofabric AHGF combined river region code (“AHGLF1”) and topographic drainage division two-digit number. *Only used for data from Australia*

* RIVNAME -- Geofabric AHGF river name. *Only used for data from Australia*. A full list of AHGF river names and codes is available at: http://www.bom.gov.au/metadata/catalogue/19115/ANZCW0503900426

* RIVDIV -- Geofabric AHGF river division name. *Only used for data from Australia*

For available values refer to :ref:`global_rivID_Fields`

..  _spatial_ref_sys:

spatial_ref_sys
^^^^^^^^^^^^^^^
The spatial_ref_sys table that comes with PostgreSQL's PostGIS extention. As an OGC compliant database table it lists over 3000 spatial reference systems and technical details needed to transform/reproject between them. For more information see `Section 4.2.1. <https://postgis.net/docs/manual-1.4/ch04.html#spatial_ref_sys>`_ of the PostGIS online manual.

.. csv-table::
   :file: ./csv_tables/spatial_ref_sys.csv
   :header-rows: 1

* srid [#]_  -- An integer value that uniquely identifies the Spatial Referencing System (SRS) within the database

* auth_name -- The name of the standard or standards body that is being cited for this reference system. For example, "EPSG" would be a valid AUTH_NAME

* auth_srid -- The ID of the Spatial Reference System as defined by the Authority cited in the AUTH_NAME. In the case of EPSG, this is where the EPSG projection code would go.

* srtext -- The Well-Known Text representation of the Spatial Reference System

* proj4text -- PostGIS uses the Proj4 library to provide coordinate transformation capabilities. The PROJ4TEXT column contains the Proj4 coordinate definition string for a particular SRID

Global references tables
~~~~~~~~~~~~~~~~~~~~~~~~

..  _global_RefCore:

global_RefCore
^^^^^^^^^^^^^^
This table stores information that allow certain identification and citation of OCTOPUS collection data sources according to BibTeX [#]_ referencing standards. In this context, different reference entry types require different minimum information standards, i.e., combinations of fields of which some will be *required*, some will be *optional*, and others will be *ignored* by BibTeX. Those three categories are defined in the :ref:`global_PubType_Fields` section. OCTOPUS database will always seeks to provide information beyond the minimum requirements, though with sense of proportion. As a result, for instance, language will never be captured for English publications because it is considered the communication standard.

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

global_RefAbstract
^^^^^^^^^^^^^^^^^^
``DRAFT`` This table stores publication abstracts for references in :ref:`global_RefCore`.

.. csv-table::
   :file: ./csv_tables/global_RefAbstract.csv
   :header-rows: 1

* REFDBID -- Uses same "REFDBID" as :ref:`global_RefCore` table does (because is one-to-one relationship)

* ABSTRACT -- Is publication abstract, if available. Note - Very extensive abstracts have been truncated and marked as *... [_truncated_]* at their end.

..  _global_Author:

global_Author
^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/global_Author.csv
   :header-rows: 1

* OAID -- 

* AUTH -- 

* FORENAME -- 

* INITIALS -- 

* ORCID -- 

* SCOPUSID -- 

* WSCC_RESID -- 

* AUTH_COMMT -- 

* AUTH_URL -- ... if "AUTH" is a corporation

* URL_DATE -- ... only applicable if "AUTH_URL" is not null

..  _global_Journal:

global_Journal
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/global_Journal.csv
   :header-rows: 1

* JOURNALID -- A unique identifier (auto-incrementing serial integer)

* JOURNAL -- 

* JOURNALABB -- Abbreviated journal name according to https://images.webofknowledge.com/images/help/WOS/A_abrvjt.html

* PRINT_ISSN -- 

* ONLIN_ISSN -- 

..  _global_PubType:

global_PubType
^^^^^^^^^^^^^^
The *global_PubType* table stores **publication entry types according to BibTeX standards**.

.. csv-table::
   :file: ./csv_tables/global_PubType.csv
   :header-rows: 1

* PUBTYPEID -- A unique identifier (auto-incrementing serial integer)

* PUBTYPE -- For available values refer to :ref:`global_PubType_Fields`

..  _global_RefKeyword:

global_RefKeyword
^^^^^^^^^^^^^^^^^

----

..  _Regional_tables:

Regional tables
---------------

Non-Cosmogenics tables
~~~~~~~~~~~~~~~~~~~~~~

..  _cabah_LabCodes:

cabah_LabCodes
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/cabah_LabCodes.csv
   :header-rows: 1

* LAB_ORIGID -- A unique identifier (auto-incrementing serial integer)

* LAB_PREFIX -- 

* LAB_FACLTY -- 

* CNTRY -- 

* LAB_ACTIVE -- 

* LAB_MTD -- 

* LAB_URL -- 

* LAB_SOURCE -- 

..  _cabah_chemprepID:

cabah_chemprepID
^^^^^^^^^^^^^^^^
The stores the **type of chemical pretreatment given to a sample**. Note -- methods capture the majority of methods applied in Australia. There may be considerable variation within each pretreatment code.

.. csv-table::
   :file: ./csv_tables/cabah_chemprepID.csv
   :header-rows: 1

* CHEMPREPID -- A unique identifier (auto-incrementing serial integer)

* CHEMPREP -- For available values refer to :ref:`cabah_chemprepID_Fields`

* CHEMPREPAB -- For available values refer to :ref:`cabah_chemprepID_Fields`

..  _cabah_col_mtdID:

cabah_col_mtdID
^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/cabah_col_mtdID.csv
   :header-rows: 1

* COL_MTDID -- A unique identifier (auto-incrementing serial integer)

* COL_MTD -- For available values refer to :ref:`cabah_col_mtdID_Fields`

..  _cabah_methodID:

cabah_methodID
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/cabah_methodID.csv
   :header-rows: 1

* METHODID -- A unique identifier (auto-incrementing serial integer)

* METHOD -- For available values refer to :ref:`cabah_methodID_Fields`

* METHODABBR -- For available values refer to :ref:`cabah_methodID_Fields`

* PARENTID -- Is fkey. Refers to ordinally higher ranking "METHODID"

* METHODREF -- Basic method literature reference

Cosmogenics tables
~~~~~~~~~~~~~~~~~~

..  _crn_alstndID:

crn_alstndID
^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/crn_alstndID.csv
   :header-rows: 1

* ALSTNDID -- A unique identifier (auto-incrementing serial integer)

* ALSTND -- 

* ALSTND_PUB -- 

* ALCORR -- 

* ALSTNDRTIO -- 

* ALSTNDCOMT -- 

For available values refer to :ref:`crn_alstndID_Fields`

..  _crn_bestndID:

crn_bestndID
^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/crn_bestndID.csv
   :header-rows: 1

* BESTNDID -- A unique identifier (auto-incrementing serial integer)

* BESTND -- 

* BESTND_PUB -- 

* BECORR -- 

* BESTNDRTIO -- 

* BESTNDCOMT -- 

For available values refer to :ref:`crn_bestndID_Fields`

Luminescence tables
~~~~~~~~~~~~~~~~~~~

..  _osl-tl_agemodelID:

osl-tl_agemodelID
^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/osl-tl_agemodelID.csv
   :header-rows: 1

* AGEMODELID -- A unique identifier (auto-incrementing serial integer)

* AGEMODEL -- For available values refer to :ref:`osl-tl_agemodelID_Fields`

* AGEMODELAB -- For available values refer to :ref:`osl-tl_agemodelID_Fields`

..  _osl-tl_ed_procID:

osl-tl_ed_procID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/osl-tl_ed_procID.csv
   :header-rows: 1

* ED_PROCID -- A unique identifier (auto-incrementing serial integer)

* ED_PROC -- For available values refer to :ref:`osl-tl_ed_procID_Fields`

* ED_PROCABR -- For available values refer to :ref:`osl-tl_ed_procID_Fields`

..  _osl-tl_lum_matID:

osl-tl_lum_matID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/osl-tl_lum_matID.csv
   :header-rows: 1

* LUM_MATID -- A unique identifier (auto-incrementing serial integer)

* LUM_MAT -- For available values refer to :ref:`osl-tl_lum_matID_Fields`

* LUM_MATABB -- For available values refer to :ref:`osl-tl_lum_matID_Fields`

..  _osl-tl_mineralID:

osl-tl_mineralID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/osl-tl_mineralID.csv
   :header-rows: 1

* MINERALID -- A unique identifier (auto-incrementing serial integer)

* MINERAL -- For available values refer to :ref:`osl-tl_mineralID_Fields`

* MINERALABB -- For available values refer to :ref:`osl-tl_mineralID_Fields`

..  _osl-tl_mtdID:

osl-tl_mtdID
^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/osl-tl_mtdID.csv
   :header-rows: 1

* MTDID -- A unique identifier (auto-incrementing serial integer)

* MTD -- For available values refer to :ref:`osl-tl_mtdID_Fields`

* MTDAB -- For available values refer to :ref:`osl-tl_mtdID_Fields`

..  _osl_typeID:

osl_typeID
^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/osl_typeID.csv
   :header-rows: 1

* OSL_TYPEID -- A unique identifier (auto-incrementing serial integer)

* OSL_TYPE -- For available values refer to :ref:`osl_typeID_Fields`

* OSL_TYPEAB -- For available values refer to :ref:`osl_typeID_Fields`

----

..  _Local_tables:

Local tables
------------

CRN tables
~~~~~~~~~~

..  _crn_amsID:

crn_amsID
^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/crn_amsID.csv
   :header-rows: 1

* AMSID -- A unique identifier (auto-incrementing serial integer)

* AMS -- 

* AMSORG -- 

* AMSURL --

..  _crn_projepsgID:

crn_projepsgID
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/crn_projepsgID.csv
   :header-rows: 1

* PROJEPSGID -- A unique identifier (auto-incrementing serial integer)

* PROJECTION -- For available values refer to :ref:`crn_projepsgID_Fields`

..  _crn_projepsgID:

crn_studies_boundingbox
^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/crn_studies_boundingbox.csv
   :header-rows: 1

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- 

* STUDYID -- 

SahulArch tables
~~~~~~~~~~~~~~~~

..  _arch_featdatedID:

arch_featdatedID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/arch_featdatedID.csv
   :header-rows: 1

* FEATDATEID -- A unique identifier (auto-incrementing serial integer)

* FEATDATED -- For available values refer to :ref:`arch_featdatedID_Fields`

..  _c13_valID:

c13_valID
^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c13_valID.csv
   :header-rows: 1

* C13_VALID -- A unique identifier (auto-incrementing serial integer)

* C13_VAL -- For available values refer to :ref:`c13_valID_Fields`

..  _c14_contamID:

c14_contamID
^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c14_contamID.csv
   :header-rows: 1


* CONTAMID -- A unique identifier (auto-incrementing serial integer)

* CONTAM -- For available values refer to :ref:`c14_contamID_Fields`

..  _c14_hum_modID:

c14_hum_modID
^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c14_hum_modID.csv
   :header-rows: 1

* HUM_MODID -- A unique identifier (auto-incrementing serial integer)

* HUM_MOD -- For available values refer to :ref:`c14_hum_modID_Fields`

..  _c14_materia1ID:

c14_materia1ID
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c14_materia1ID.csv
   :header-rows: 1

* MATERIA1ID -- A unique identifier (auto-incrementing serial integer)

* MATERIAL1 -- For available values refer to :ref:`c14_materia1ID_Fields`

* MATERIA1AB -- For available values refer to :ref:`c14_materia1ID_Fields`

..  _c14_materia2ID:

c14_materia2ID
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c14_materia2ID.csv
   :header-rows: 1

* MATERIA2ID -- A unique identifier (auto-incrementing serial integer)

* MATERIAL2 -- For available values refer to :ref:`c14_materia2ID_Fields`

..  _c14_solvent2ID:

c14_solvent2ID
^^^^^^^^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c14_solvent2ID.csv
   :header-rows: 1

* SOLVENT2ID -- A unique identifier (auto-incrementing serial integer)

* SOLVENT2 -- For available values refer to :ref:`c14_solvent2ID_Fields`

* SOLVENT2AB -- For available values refer to :ref:`c14_solvent2ID_Fields`

..  _c_mtdID:

c_mtdID
^^^^^^^
``DRAFT`` This table 

.. csv-table::
   :file: ./csv_tables/c_mtdID.csv
   :header-rows: 1

* C_MTDID -- A unique identifier (auto-incrementing serial integer)

* C_MTD -- For available values refer to :ref:`c_mtdID_Fields`

* C_MTDAB -- For available values refer to :ref:`c_mtdID_Fields`

..  _arch_c14_polygons_EPSG3857:

arch_c14_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

====== ============ ==== ==== ======== ======
Field  Data type    Unit Key  Not Null Parent
====== ============ ==== ==== ======== ======
id     serial4           pkey TRUE     
geom   geometry(mp)                    
OBSID1 text              ukey TRUE     
OBSID2 text                            
====== ============ ==== ==== ======== ======

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- 

* OBSID1 -- 

* OBSID2 -- 

..  _arch_osl_polygons_EPSG3857:

arch_osl_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

====== ============ ==== ==== ======== ======
Field  Data type    Unit Key  Not Null Parent
====== ============ ==== ==== ======== ======
id     serial4           pkey TRUE     
geom   geometry(mp)                    
OBSID1 text              ukey TRUE     
OBSID2 text                            
====== ============ ==== ==== ======== ======

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- 

* OBSID1 -- 

* OBSID2 -- 

..  _arch_tl_polygons_EPSG3857:

arch_tl_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

====== ============ ==== ==== ======== ======
Field  Data type    Unit Key  Not Null Parent
====== ============ ==== ==== ======== ======
id     serial4           pkey TRUE     
geom   geometry(mp)                    
OBSID1 text              ukey TRUE     
OBSID2 text                            
====== ============ ==== ==== ======== ======

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- 

* OBSID1 -- 

* OBSID2 -- 

SahulSed tables
~~~~~~~~~~~~~~~

..  _sed_depconID:

sed_depconID
^^^^^^^^^^^^
``DRAFT`` This table 

======== ========= ==== ==== ======== ======
Field    Data type Unit Key  Not Null Parent
======== ========= ==== ==== ======== ======
DEPCONID int2           pkey TRUE     
DEPCON   text                TRUE     
======== ========= ==== ==== ======== ======

* DEPCONID -- A unique identifier (auto-incrementing serial integer)

* DEPCON -- For available values refer to :ref:`sed_depconID_Fields`

..  _sed_faciesID:

sed_faciesID
^^^^^^^^^^^^
``DRAFT`` This table 

======== ========= ==== ==== ======== ======
Field    Data type Unit Key  Not Null Parent
======== ========= ==== ==== ======== ======
FACIESID int2           pkey TRUE     
FACIES   text                TRUE     
======== ========= ==== ==== ======== ======

* FACIESID -- A unique identifier (auto-incrementing serial integer)

* FACIES -- For available values refer to :ref:`sed_faciesID_Fields`

..  _sed_geommodID:

sed_geommodID
^^^^^^^^^^^^^
``DRAFT`` This table 

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
GEOMMODID int2           pkey TRUE     
GEOMMOD   text                TRUE     
========= ========= ==== ==== ======== ======

* GEOMMODID -- A unique identifier (auto-incrementing serial integer)

* GEOMMOD -- For available values refer to :ref:`sed_geommodID_Fields`

..  _sed_geotypeID:

sed_geotypeID
^^^^^^^^^^^^^
``DRAFT`` This table 

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
GEOTYPEID int2           pkey TRUE     
GEOTYPE   text                TRUE     
========= ========= ==== ==== ======== ======

* GEOTYPEID -- A unique identifier (auto-incrementing serial integer)

* GEOTYPE -- For available values refer to :ref:`sed_geotypeID_Fields`

..  _sed_laketypeID:

sed_laketypeID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
LAKETYPEID int2           pkey TRUE     
LAKETYPE   text                TRUE     
PARENTID   int2           fkey
========== ========= ==== ==== ======== ======

* LAKETYPEID -- A unique identifier (auto-incrementing serial integer)

* LAKETYPE -- For available values refer to :ref:`sed_laketypeID_Fields`

* PARENTID -- Is fkey. Refers to ordinally higher ranking "LAKETYPEID"

..  _sed_morphID:

sed_morphID
^^^^^^^^^^^
``DRAFT`` This table 

======= ========= ==== ==== ======== ======
Field   Data type Unit Key  Not Null Parent
======= ========= ==== ==== ======== ======
MORPHID int2           pkey TRUE     
MORPH   text                TRUE     
======= ========= ==== ==== ======== ======

* MORPHID -- A unique identifier (auto-incrementing serial integer)

* MORPH -- For available values refer to :ref:`sed_morphID_Fields`

..  _sed_sitetypeID:

sed_sitetypeID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
SITETYPEID int2           pkey TRUE     
SITETYPE   text                TRUE     
========== ========= ==== ==== ======== ======

* SITETYPEID -- A unique identifier (auto-incrementing serial integer)

* SITETYPE -- For available values refer to :ref:`sed_sitetypeID_Fields`

..  _sed-osl_points_EPSG3857:

sed-osl_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

====== ============ ==== ==== ======== ======
Field  Data type    Unit Key  Not Null Parent
====== ============ ==== ==== ======== ======
id     serial4           pkey TRUE     
geom   geometry(pt)                    
OBSID1 text              ukey TRUE     
OBSID2 text                            
====== ============ ==== ==== ======== ======

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- 

* OBSID1 -- 

* OBSID2 -- 

..  _sed-tl_points_EPSG3857:

sed-tl_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

====== ============ ==== ==== ======== ======
Field  Data type    Unit Key  Not Null Parent
====== ============ ==== ==== ======== ======
id     serial4           pkey TRUE     
geom   geometry(pt)                    
OBSID1 text              ukey TRUE     
OBSID2 text                            
====== ============ ==== ==== ======== ======

* id -- A unique identifier (auto-incrementing serial integer)

* geom -- 

* OBSID1 -- 

* OBSID2 -- 

FosSahul tables
~~~~~~~~~~~~~~~

fos_TaxRank1_classID
^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

fos_TaxRank2_infraclaID
^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

fos_TaxRank3_ordrID
^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

fos_TaxRank4_familyID
^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

fos_TaxRank5_genusID
^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

fos_TaxRank6_speciesID
^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

fos_chemtypeID
^^^^^^^^^^^^^^
The *fos_chemtypeID* table stores the **type of chemical pretreatment given to the sample** as described in the original publication. There may be considerable variation within each pretreatment code.

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
CHEMTYPEID int2           pkey TRUE     
CHEMTYPE   text                TRUE     
CHEMTYPEAB text                         
========== ========= ==== ==== ======== ======

* CHEMTYPEID -- A unique identifier (auto-incrementing serial integer)

* CHEMTYPE -- For available values refer to :ref:`fos_chemtypeID_Fields`

* CHEMTYPEAB -- For available values refer to :ref:`fos_chemtypeID_Fields`

fos_fosmat1ID
^^^^^^^^^^^^^
The *fos_fosmat1ID* table stores the **type of dated remain**.

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
FOSMAT1ID  int2           pkey TRUE     
FOSMAT1    text                TRUE     
FOSMAT1ABB text                         
========== ========= ==== ==== ======== ======

* FOSMAT1IDd -- A unique identifier (auto-incrementing serial integer)

* FOSMAT1 -- For available values refer to :ref:`fos_fosmat1ID_Fields`

* FOSMAT1ABB -- For available values refer to :ref:`fos_fosmat1ID_Fields`

fos_fosmat2ID
^^^^^^^^^^^^^
The *fos_fosmat2ID* table stores the **type of dated material**.

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
FOSMAT2ID  int2           pkey TRUE     
FOSMAT2    text                TRUE     
FOSMAT2ABB text                         
========== ========= ==== ==== ======== ======

* FOSMAT2ID -- A unique identifier (auto-incrementing serial integer)

* FOSMAT2 -- For available values refer to :ref:`fos_fosmat2ID_Fields`

* FOSMAT2ABB -- For available values refer to :ref:`fos_fosmat2ID_Fields`

fos_mtdsID
^^^^^^^^^^
The *fos_mtdsID* table stores the type of **method used in age determination**.

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
FOS_MTDSID int2           pkey TRUE     
FOS_MTDSUB text                TRUE     
FOS_MTDSAB text                         
========== ========= ==== ==== ======== ======

* FOS_MTDSID -- A unique identifier (auto-incrementing serial integer)

* FOS_MTDSUB -- For available values refer to :ref:`fos_mtdsID_Fields`

* FOS_MTDSAB -- For available values refer to :ref:`fos_mtdsID_Fields`

fos_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

expage tables
~~~~~~~~~~~~~

expage_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. rubric:: Footnotes

.. [#] PostgreSQL view: `https://www.postgresql.org/docs/current/sql-createview.html <https://www.postgresql.org/docs/current/sql-createview.html>`_
.. [#] Field descriptions unaltered taken from `https://postgis.net/ <https://postgis.net/>`_
.. [#] `https://www.ctan.org/pkg/bibtex <https://www.ctan.org/pkg/bibtex>`_
