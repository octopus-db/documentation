===========
Data tables
===========

Global tables
-------------

Global lookup tables
~~~~~~~~~~~~~~~~~~~~

global_GrainSize
^^^^^^^^^^^^^^^^

Global georeferencing tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

global_MetaSite
^^^^^^^^^^^^^^^

global_SiteCode
^^^^^^^^^^^^^^^

global_SiteMaster
^^^^^^^^^^^^^^^^^

global_dbDOI
^^^^^^^^^^^^

global_ibraID
^^^^^^^^^^^^^

global_rivID
^^^^^^^^^^^^

spatial_ref_sys
^^^^^^^^^^^^^^

Global reference tables
~~~~~~~~~~~~~~~~~~~~~~~

..  _global_RefCore:

global_RefCore
^^^^^^^^^^^^^^

Minimum set of information defined by type of publication (REF)

=========== =========== ==== ==== ======== ==================
Field       Data type   Unit Key  Not Null Reference
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

* ADDRESS -- Publisher address

* NOTE -- free text field for annotations

* URL -- Publication url, especially favoured when no DOI available

* BOOKTITLE -- Title of book, website, 

* CHAPTER -- Book chapter

* EDITOR -- 

* PUBLISHER -- Publisher

* INSTITUTION -- 

* SCHOOL -- 

..  _global_RefAbstract:

global_RefAbstract
^^^^^^^^^^^^^^^^^^

..  _global_Author:

global_Author
^^^^^^^^^^^^^

..  _global_Journal:

global_Journal
^^^^^^^^^^^^^^

..  _global_PubType:

global_PubType
^^^^^^^^^^^^^^

Information standard defined by BibTex

========= ========= ==== ==== ======== =========
Field     Data type Unit Key  Nullable Reference
========= ========= ==== ==== ======== =========
PUBTYPEID int2           pkey FALSE    
PUBTYPE   text                         
========= ========= ==== ==== ======== =========

* PUBTYPEID -- Unique identifier (auto-incrementing serial integer)

* PUBTYPE -- Name of reference entry type according to BibTeX standards

..  _global_RefKeyword:

global_RefKeyword
^^^^^^^^^^^^^^^^^

----

Regional tables
---------------

Non-Cosmogenics tables
~~~~~~~~~~~~~~~~~~~~~~

cabah_LabCodes
^^^^^^^^^^^^^^

cabah_chemprepID
^^^^^^^^^^^^^^^^

cabah_col_mtdID
^^^^^^^^^^^^^^^

cabah_methodID
^^^^^^^^^^^^^^

Cosmogenics tables
~~~~~~~~~~~~~~~~~~

crn_alstndID
^^^^^^^^^^^^

crn_bestndID
^^^^^^^^^^^^

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

Collection specific tables
--------------------------

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

**arch_c14_polygons_EPSG3857

**arch_osl_polygons_EPSG3857

**arch_tl_polygons_EPSG3857

SahulSed tables
~~~~~~~~~~~~~~~
**sed_depconID**

**sed_faciesID**

**sed_geommodID**

**sed_geotypeID**

**sed_laketypeID**

**sed_morphID**

**sed_sitetypeID**

**sed-osl_points_EPSG3857**

**sed-tl_points_EPSG3857**

FosSahul tables
~~~~~~~~~~~~~~~

**fos_TaxRank1_classID**

**fos_TaxRank2_infraclaID**

**fos_TaxRank3_ordrID**

**fos_TaxRank4_familyID**

**fos_TaxRank5_genusID**

**fos_TaxRank6_speciesID**

**fos_chemtypeID**

**fos_fosmat1ID**

**fos_fosmat2ID**

**fos_mtdsID**

**fos_polygons_EPSG3857**

expage tables
~~~~~~~~~~~~~
**expage_points_EPSG3857**
