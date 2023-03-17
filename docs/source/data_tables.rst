===========
Data tables
===========
| OCTOPUS data tables, using a spatial allegory, can be grouped into a *global*, a *regional*, and a *local* level. While a :ref:`Global_tables` can serve any database relation, :ref:`Regional_tables` should be seen as a thematic tables not matching certain sub-collections. Finally, :ref:`Local_tables` are collection specific tables with a high degree of specialisation compared to the two aforementioned higher-level table groups.

| ``DRAFT`` --> data type abbreviations, key abbreviations, not null, parent (link to https://www.postgresql.org/docs/11/datatype.html)
| ``DRAFT`` --> "CREATED_AT" (Is record timestamp with timezone based on UTC), "UPDATED_AT" (Is timestamp of record update with timezone based on UTC)

..  _Global_tables:

Global tables
-------------

..  _Global_lookup_tables:

Global lookup tables
~~~~~~~~~~~~~~~~~~~~

..  _global_GrainSize:

global_GrainSize
^^^^^^^^^^^^^^^^
``DRAFT`` This table stores the *type of material sampled* (= "MATERIAL" in CRN denudation and expage tables, = "SED_MAT" in SahulSed tables).

========== ============= ==== ==== ======== ======
Field      Data type     Unit Key  Not Null Parent
========== ============= ==== ==== ======== ======
GRNSIZEID  int2               pkey TRUE     
GRNSIZE    text                    TRUE     
GRNSIZEABB varchar(6)                      
GRNSIZEMIN numeric(7, 4) mm                 
GRNSIZEMAX numeric(7, 4) mm                 
========== ============= ==== ==== ======== ======

* GRNSIZEID -- Unique identifier (auto-incrementing serial integer)

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
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
SITECODEID int2           pkey TRUE     
SITECODE   text                TRUE     
========== ========= ==== ==== ======== ======

* SITECODEID -- Unique identifier (auto-incrementing serial integer)

* SITECODE -- 

..  _global_SiteMaster:

global_SiteMaster
^^^^^^^^^^^^^^^^^

``DRAFT`` This table

========== ============== ========== ==== ======== ======================
Field      Data type      Unit       Key  Not Null Parent
========== ============== ========== ==== ======== ======================
SITEID     text                      pkey TRUE     
METASITEID text                      fkey          :ref:`global_MetaSite`
CNTRY      varchar(3)                     TRUE     
REGION_INT text                                    
REGION_REG varchar(3)                              
DIV_ADMIN  varchar(7)                              
DIV_OTHER  text                                    
ISL_NAME   text                                    
LAKE       text                                    
BASIN      text                                    
RIVID      int2                      fkey          :ref:`global_rivID`
IBRAID     int2                      fkey          :ref:`global_ibraID`
X_WGS84    numeric(10, 6) dec degree               
Y_WGS84    numeric(10, 6) dec degree               
CORDS_ELEV varchar(9)                     TRUE     
ELEVATION  numeric(6, 2)  m a.s.l.                 
SITENAME   text                                    
SITE_SPEC  text                                    
ALTNAME1   text                                    
ALTNAME2   text                                    
ALTNAME3   text                                    
SITECODEID int2                      fkey          :ref:`global_SiteCode`
OPENCLOSED varchar(6)                              
SITE_COMMT text                                    
========== ============== ========== ==== ======== ======================

* SITEID -- 

* METASITEID -- 

* CNTRY -- 

* REGION_INT -- 

* REGION_REG -- 

* DIV_ADMIN -- 

* DIV_OTHER -- 

* ISL_NAME -- 

* LAKE -- 

* BASIN -- 

* RIVID -- 

* IBRAID -- 

* X_WGS84 -- 

* Y_WGS84 -- 

* CORDS_ELEV -- 

* ELEVATION -- 

* SITE_SPEC -- 

* ALTNAME1 -- 

* ALTNAME2 -- 

* ALTNAME3 -- 

* SITECODEID -- 

* OPENCLOSED -- 

* SITECODE -- 

* SITE_COMMT -- 

..  _global_dbDOI:

global_dbDOI
^^^^^^^^^^^^

..  _global_ibraID:

global_ibraID
^^^^^^^^^^^^^
``DRAFT`` This table

========== ========== ==== ==== ======== ======
Field      Data type  Unit Key  Not Null Parent
========== ========== ==== ==== ======== ======
IBRAID     int2            pkey TRUE     
IBRACODE   varchar(3)           TRUE     
IBRAREGION text                          
========== ========== ==== ==== ======== ======

* IBRAID -- 

* IBRACODE -- 

* IBRAREGION -- 

..  _global_rivID:

global_rivID
^^^^^^^^^^^^
``DRAFT`` This table

======= ========== ==== ==== ======== ======
Field   Data type  Unit Key  Not Null Parent
======= ========== ==== ==== ======== ======
RIVID   int2            pkey TRUE     
AHGFL1  varchar(3)                    
AHGFL2  varchar(6)                    
RIVNAME text                          
RIVDIV  text                          
======= ========== ==== ==== ======== ======

* RIVID -- 

* AHGFL1 -- 

* AHGFL2 -- 

* RIVNAME -- 

* RIVDIV -- 

..  _spatial_ref_sys:

spatial_ref_sys
^^^^^^^^^^^^^^^
The spatial_ref_sys table that comes with PostgreSQL's PostGIS extention. As an OGC compliant database table it lists over 3000 spatial reference systems and technical details needed to transform/reproject between them. For more information see `Section 4.2.1.<https://postgis.net/docs/manual-1.4/ch04.html#spatial_ref_sys>`_ of the PostGIS online manual.

========= ============= ==== ==== ======== ======
Field     Data type     Unit Key  Not Null Parent
========= ============= ==== ==== ======== ======
srid      int4               pkey TRUE     
auth_name varchar(256)                     
auth_srid int4                             
srtext    varchar(2048)                    
proj4text varchar(2048)                    
========= ============= ==== ==== ======== ======

* srid -- 

* auth_name -- 

* auth_srid -- 

* srtext -- 

* proj4text -- 

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
CREATED_AT  timestamptz           TRUE     
UPDATED_AT  timestamptz                    
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

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
REFDBID   text           pkey TRUE     
ABSTRACT  text                         
========= ========= ==== ==== ======== ======

* REFDBID -- Uses same "REFDBID" as :ref:`global_RefCore` table does (because is one-to-one relationship)

* ABSTRACT -- Is publication abstract, if available. Note - Very extensive abstracts have been truncated and marked as *... [_truncated_]* at their end.

..  _global_Author:

global_Author
^^^^^^^^^^^^^
``DRAFT`` This table 

========== ============ ==== ==== ======== ======
Field      Data type    Unit Key  Not Null Parent
========== ============ ==== ==== ======== ======
OAID       varchar(11)       pkey TRUE     
AUTH       text                   TRUE     
FORENAME   text                            
INITIALS   text                            
ORCID      #varchar(19)                    
SCOPUSID   text                            
WSCC_RESID text                            
AUTH_COMMT text                            
AUTH_URL   text                            
URL_DATE   date                            
========== ============ ==== ==== ======== ======

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

========== ========== ==== ==== ======== ======
Field      Data type  Unit Key  Not Null Parent
========== ========== ==== ==== ======== ======
JOURNALID  int2            pkey TRUE     
JOURNAL    text                 TRUE     
JOURNALABB text                 TRUE     
PRINT_ISSN varchar(9)                    
ONLIN_ISSN varchar(9)                    
========== ========== ==== ==== ======== ======

* JOURNALID -- Unique identifier (auto-incrementing serial integer)

* JOURNAL -- 

* JOURNALABB -- Abbreviated journal name according to https://images.webofknowledge.com/images/help/WOS/A_abrvjt.html

* PRINT_ISSN -- 

* ONLIN_ISSN -- 

..  _global_PubType:

global_PubType
^^^^^^^^^^^^^^
``DRAFT`` Information standard defined by BibTex

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
PUBTYPEID int2           pkey TRUE     
PUBTYPE   text                         
========= ========= ==== ==== ======== ======

* PUBTYPEID -- Unique identifier (auto-incrementing serial integer)

* PUBTYPE -- Name of publication entry type according to BibTeX standards. For selectable values see :ref:`global_PubType_Fields`

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

========== ========== ==== ==== ======== ======
Field      Data type  Unit Key  Not Null Parent
========== ========== ==== ==== ======== ======
LAB_ORIGID int2            pkey TRUE     
LAB_PREFIX text                          
LAB_FACLTY text                          
CNTRY      varchar(3)                    
LAB_ACTIVE bool                          
LAB_MTD    varchar(3)                    
LAB_URL    text                          
LAB_SOURCE text                          
========== ========== ==== ==== ======== ======

* LAB_ORIGID -- Unique identifier (auto-incrementing serial integer)

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
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
CHEMPREPID int2           pkey TRUE     
CHEMPREP   text                TRUE     
CHEMPREPAB text                         
========== ========= ==== ==== ======== ======

* CHEMPREPID -- Unique identifier (auto-incrementing serial integer)

* CHEMPREP -- 

* CHEMPREPAB -- 

..  _cabah_col_mtdID:

cabah_col_mtdID
^^^^^^^^^^^^^^^
``DRAFT`` This table 

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
COL_MTDID int2           pkey TRUE     
COL_MTD   text                TRUE     
========= ========= ==== ==== ======== ======

* COL_MTDID -- Unique identifier (auto-incrementing serial integer)

* COL_MTD -- 

..  _cabah_methodID:

cabah_methodID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
METHODID   int2           pkey TRUE     
METHOD     text                TRUE     
METHODABBR text                TRUE     
========== ========= ==== ==== ======== ======

* METHODID -- Unique identifier (auto-incrementing serial integer)

* METHOD -- 

* METHODABBR -- 

Cosmogenics tables
~~~~~~~~~~~~~~~~~~

..  _crn_alstndID:

crn_alstndID
^^^^^^^^^^^^
``DRAFT`` This table 

========== ============= ==== ==== ======== ======
Field      Data type     Unit Key  Not Null Parent
========== ============= ==== ==== ======== ======
ALSTNDID   int2               pkey TRUE     
ALSTND     text                    TRUE     
ALSTND_PUB text                             
ALCORR     numeric(5, 4)                    
ALSTNDRTIO numeric                          
ALSTNDCOMT text                             
========== ============= ==== ==== ======== ======

* ALSTNDID -- Unique identifier (auto-incrementing serial integer)

* ALSTND -- 

* ALSTND_PUB -- 

* ALCORR -- 

* ALSTNDRTIO -- 

* ALSTNDCOMT -- 

..  _crn_bestndID:

crn_bestndID
^^^^^^^^^^^^
``DRAFT`` This table 

========== ============= ==== ==== ======== ======
Field      Data type     Unit Key  Not Null Parent
========== ============= ==== ==== ======== ======
BESTNDID   int2               pkey TRUE     
BESTND     text                    TRUE     
BESTND_PUB text                             
BECORR     numeric(5, 4)                    
BESTNDRTIO numeric                          
BESTNDCOMT text                             
========== ============= ==== ==== ======== ======

* BESTNDID -- Unique identifier (auto-incrementing serial integer)

* BESTND -- 

* BESTND_PUB -- 

* BECORR -- 

* BESTNDRTIO -- 

* BESTNDCOMT -- 

Luminescence tables
~~~~~~~~~~~~~~~~~~~

..  _osl-tl_agemodelID:

osl-tl_agemodelID
^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
AGEMODELID int2           pkey TRUE     
AGEMODEL   text                TRUE     
AGEMODELAB text                         
========== ========= ==== ==== ======== ======

* AGEMODELID -- Unique identifier (auto-incrementing serial integer)

* AGEMODEL -- 

* AGEMODELAB -- 

..  _osl-tl_ed_procID:

osl-tl_ed_procID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
ED_PROCID  int2           pkey TRUE     
ED_PROC    text                TRUE     
ED_PROCABR text                         
========== ========= ==== ==== ======== ======

* ED_PROCID -- Unique identifier (auto-incrementing serial integer)

* ED_PROC -- 

* ED_PROCABR -- 

..  _osl-tl_lum_matID:

osl-tl_lum_matID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
LUM_MATID  int2           pkey TRUE     
LUM_MAT    text                TRUE     
LUM_MATABB text                         
========== ========= ==== ==== ======== ======

* LUM_MATID -- Unique identifier (auto-incrementing serial integer)

* LUM_MAT -- 

* LUM_MATABB -- 

..  _osl-tl_mineralID:

osl-tl_mineralID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
MINERALID  int2           pkey TRUE     
MINERAL    text                TRUE     
MINERALABB text                         
========== ========= ==== ==== ======== ======

* MINERALID -- Unique identifier (auto-incrementing serial integer)

* MINERAL -- 

* MINERALABB -- 

..  _osl-tl_mtdID:

osl-tl_mtdID
^^^^^^^^^^^^
``DRAFT`` This table 

===== ========= ==== ==== ======== ======
Field Data type Unit Key  Not Null Parent
===== ========= ==== ==== ======== ======
MTDID int2           pkey TRUE     
MTD   text                TRUE     
MTDAB text                         
===== ========= ==== ==== ======== ======

* MTDID -- Unique identifier (auto-incrementing serial integer)

* MTD -- 

* MTDAB -- 

..  _osl_typeID:

osl_typeID
^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
OSL_TYPEID int2           pkey TRUE     
OSL_TYPE   text                TRUE     
OSL_TYPEAB text                         
========== ========= ==== ==== ======== ======

* OSL_TYPEID -- Unique identifier (auto-incrementing serial integer)

* OSL_TYPE -- 

* OSL_TYPEAB -- 

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

====== ========= ==== ==== ======== ======
Field  Data type Unit Key  Not Null Parent
====== ========= ==== ==== ======== ======
AMSID  int2           pkey TRUE     
AMS    text                TRUE     
AMSORG text                         
AMSURL text                         
====== ========= ==== ==== ======== ======

* AMSID -- Unique identifier (auto-incrementing serial integer)

* AMS -- 

* AMSORG -- 

* AMSURL --

..  _crn_projepsgID:

crn_projepsgID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== =========== ==== ==== ======== ======
Field      Data type   Unit Key  Not Null Parent
========== =========== ==== ==== ======== ======
PROJEPSGID int2             pkey TRUE     
PROJECTION varchar(13)           TRUE     
========== =========== ==== ==== ======== ======

* PROJEPSGID -- Unique identifier (auto-incrementing serial integer)

* PROJECTION -- 

..  _crn_projepsgID:

crn_studies_boundingbox
^^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

======= ========== ==== ==== ======== ======
Field   Data type  Unit Key  Not Null Parent
======= ========== ==== ==== ======== ======
id      serial4         pkey TRUE     
geom    geometry                      
STUDYID varchar(5)      ukey TRUE     
======= ========== ==== ==== ======== ======

* id -- Unique identifier (auto-incrementing serial integer)

* geom -- 

* STUDYID -- 

SahulArch tables
~~~~~~~~~~~~~~~~

..  _arch_featdatedID:

arch_featdatedID
^^^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
FEATDATEID           int2 pkey TRUE     
FEATDATED            text      TRUE     
========== ========= ==== ==== ======== ======

* FEATDATEID -- Unique identifier (auto-incrementing serial integer)

* FEATDATED -- 

..  _c13_valID:

c13_valID
^^^^^^^^^
``DRAFT`` This table 

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
C13_VALID int2           pkey TRUE     
C13_VAL   text                TRUE     
========= ========= ==== ==== ======== ======

* C13_VALID -- Unique identifier (auto-incrementing serial integer)

* C13_VAL -- 

..  _c14_contamID:

c14_contamID
^^^^^^^^^^^^
``DRAFT`` This table 

======== ========= ==== ==== ======== ======
Field    Data type Unit Key  Not Null Parent
======== ========= ==== ==== ======== ======
CONTAMID int2           pkey TRUE     
CONTAM   text                TRUE     
======== ========= ==== ==== ======== ======

* CONTAMID -- Unique identifier (auto-incrementing serial integer)

* CONTAM -- 

..  _c14_hum_modID:

c14_hum_modID
^^^^^^^^^^^^^
``DRAFT`` This table 

========= ========= ==== ==== ======== ======
Field     Data type Unit Key  Not Null Parent
========= ========= ==== ==== ======== ======
HUM_MODID int2           pkey TRUE     
HUM_MOD   text                TRUE     
========= ========= ==== ==== ======== ======

* HUM_MODID -- Unique identifier (auto-incrementing serial integer)

* HUM_MOD -- 

..  _c14_materia1ID:

c14_materia1ID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
MATERIA1ID int2           pkey TRUE     
MATERIAL1  text                TRUE     
MATERIA1AB text                         
========== ========= ==== ==== ======== ======

* MATERIA1ID -- Unique identifier (auto-incrementing serial integer)

* MATERIAL1 -- 

* MATERIA1AB -- 

..  _c14_materia2ID:

c14_materia2ID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
MATERIA2ID int2           pkey TRUE     
MATERIAL2  text                TRUE     
========== ========= ==== ==== ======== ======

* MATERIA2ID -- Unique identifier (auto-incrementing serial integer)

* MATERIAL2 -- 

..  _c14_solvent2ID:

c14_solvent2ID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
SOLVENT2ID int2           pkey TRUE     
SOLVENT2   text                TRUE     
SOLVENT2AB text                         
========== ========= ==== ==== ======== ======

* SOLVENT2ID -- Unique identifier (auto-incrementing serial integer)

* SOLVENT2 -- 

* SOLVENT2AB -- 

..  _c_mtdID:

c_mtdID
^^^^^^^
``DRAFT`` This table 

======= ========= ==== ==== ======== ======
Field   Data type Unit Key  Not Null Parent
======= ========= ==== ==== ======== ======
C_MTDID int2           pkey TRUE     
C_MTD   text                TRUE     
C_MTDAB text                         
======= ========= ==== ==== ======== ======

* C_MTDID -- Unique identifier (auto-incrementing serial integer)

* C_MTD -- 

* C_MTDAB -- 

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

* id -- Unique identifier (auto-incrementing serial integer)

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

* id -- Unique identifier (auto-incrementing serial integer)

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

* id -- Unique identifier (auto-incrementing serial integer)

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

* DEPCONID -- Unique identifier (auto-incrementing serial integer)

* DEPCON -- 

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

* FACIESID -- Unique identifier (auto-incrementing serial integer)

* FACIES -- 

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

* GEOMMODID -- Unique identifier (auto-incrementing serial integer)

* GEOMMOD -- 

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

* GEOTYPEID -- Unique identifier (auto-incrementing serial integer)

* GEOTYPE -- 

..  _sed_laketypeID:

sed_laketypeID
^^^^^^^^^^^^^^
``DRAFT`` This table 

========== ========= ==== ==== ======== ======
Field      Data type Unit Key  Not Null Parent
========== ========= ==== ==== ======== ======
LAKETYPEID int2           pkey TRUE     
LAKETYPE   text                TRUE     
========== ========= ==== ==== ======== ======

* LAKETYPEID -- Unique identifier (auto-incrementing serial integer)

* LAKETYPE -- 

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

* MORPHID -- Unique identifier (auto-incrementing serial integer)

* MORPH -- 

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

* SITETYPEID -- Unique identifier (auto-incrementing serial integer)

* SITETYPE -- 

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

* id -- Unique identifier (auto-incrementing serial integer)

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

* id -- Unique identifier (auto-incrementing serial integer)

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
``DRAFT`` This table 

fos_fosmat1ID
^^^^^^^^^^^^^
``DRAFT`` This table 

fos_fosmat2ID
^^^^^^^^^^^^^
``DRAFT`` This table 

fos_mtdsID
^^^^^^^^^^
``DRAFT`` This table 

fos_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

expage tables
~~~~~~~~~~~~~

expage_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^
``DRAFT`` This table 

.. rubric:: Footnotes

.. [#] `https://www.ctan.org/pkg/bibtex <https://www.ctan.org/pkg/bibtex>`_
