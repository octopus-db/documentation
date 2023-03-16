===========
Data tables
===========
| OCTOPUS data tables, using a spatial allegory, can be grouped into a *global*, a *regional*, and a *local* level. While a :ref:`Global_tables` can serve any database relation, :ref:`Regional_tables` should be seen as a thematic tables not matching certain sub-collections. Finally, :ref:`Local_tables` are collection specific tables with a high degree of specialisation compared to the two aforementioned higher-level table groups.

| ``DRAFT`` --> data type abbreviations, key abbreviations, not null, parent (link to https://www.postgresql.org/docs/11/datatype.html)
| ``DRAFT`` --> "CREATED_AT", "UPDATED_AT"

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

========== ============ ==== ==== ======== ======
Field      Data type    Unit Key  Not Null Parent
========== ============ ==== ==== ======== ======
GRNSIZEID  int2              pkey TRUE     
GRNSIZE    text                   TRUE     
GRNSIZEABB varchar(6)                      
GRNSIZEMIN numeric(7,4) mm                 
GRNSIZEMAX numeric(7,4) mm                 
========== ============ ==== ==== ======== ======

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
^^^^^^^^^^^^^^

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
osl-tl_agemodelID
^^^^^^^^^^^^^^^^^

osl-tl_ed_procID
^^^^^^^^^^^^^^^^

osl-tl_lum_matID
^^^^^^^^^^^^^^^^

osl-tl_mineralID
^^^^^^^^^^^^^^^^

osl-tl_mtdID
^^^^^^^^^^^^

osl_typeID
^^^^^^^^^^

----

..  _Local_tables:

Local tables
------------

CRN tables
~~~~~~~~~~

crn_amsID
^^^^^^^^^

crn_projepsgID
^^^^^^^^^^^^^^

crn_studies_boundingbox
^^^^^^^^^^^^^^^^^^^^^^^

SahulArch tables
~~~~~~~~~~~~~~~~

arch_featdatedID
^^^^^^^^^^^^^^^^

c13_valID
^^^^^^^^^

c14_contamID
^^^^^^^^^^^^

c14_hum_modID
^^^^^^^^^^^^^

c14_materia1ID
^^^^^^^^^^^^^^

c14_materia2ID
^^^^^^^^^^^^^^

c14_solvent2ID
^^^^^^^^^^^^^^

c_mtdID
^^^^^^^

arch_c14_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^^

arch_c14_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^^

arch_c14_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^^

arch_osl_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^^

arch_tl_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^^^

SahulSed tables
~~~~~~~~~~~~~~~

sed_depconID
^^^^^^^^^^^^

sed_faciesID
^^^^^^^^^^^^

sed_geommodID
^^^^^^^^^^^^^

sed_geotypeID
^^^^^^^^^^^^^

sed_laketypeID
^^^^^^^^^^^^^^

sed_morphID
^^^^^^^^^^^

sed_sitetypeID
^^^^^^^^^^^^^^

sed-osl_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^^

sed-tl_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^

FosSahul tables
~~~~~~~~~~~~~~~

fos_TaxRank1_classID
^^^^^^^^^^^^^^^^^^^^

fos_TaxRank2_infraclaID
^^^^^^^^^^^^^^^^^^^^^^^

fos_TaxRank3_ordrID
^^^^^^^^^^^^^^^^^^^

fos_TaxRank4_familyID
^^^^^^^^^^^^^^^^^^^^^

fos_TaxRank5_genusID
^^^^^^^^^^^^^^^^^^^^

fos_TaxRank6_speciesID
^^^^^^^^^^^^^^^^^^^^^^

fos_chemtypeID
^^^^^^^^^^^^^^

fos_fosmat1ID
^^^^^^^^^^^^^

fos_fosmat2ID
^^^^^^^^^^^^^

fos_mtdsID
^^^^^^^^^^

fos_polygons_EPSG3857
^^^^^^^^^^^^^^^^^^^^^

expage tables
~~~~~~~~~~~~~

expage_points_EPSG3857
^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Footnotes

.. [#] `https://www.ctan.org/pkg/bibtex <https://www.ctan.org/pkg/bibtex>`_
