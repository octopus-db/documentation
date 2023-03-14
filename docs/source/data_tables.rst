===========
Data tables
===========

Global tables
-------------
**global_GrainSize**

**global_MetaSite**

**global_SiteCode**

**global_SiteMaster**

**global_dbDOI**

**global_ibraID**

**global_rivID**

**spatial_ref_sys**

Reference tables
~~~~~~~~~~~~~~~~
**global_RefCore**

=========== =========== ==== ==== ======== ==================
Field       Data type   Unit Key  Not Null Parent
=========== =========== ==== ==== ======== ==================
REFDBID     text             pkey TRUE     
OAID        varchar(11)      fkey          global_Author
REFDOI      text                           
AUTHORS     text                           
TITLE       text                           
PUBTYPEID   int2             fkey TRUE     global_Publication
JOURNALID   int2             fkey          global_Journal
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

* REFDBID

* REFDOI

* AUTHORS

* TITLE

* VOLUME

* NUMBER

* PAGES

* YEAR

* ADDRESS

* NOTE

* URL

* BOOKTITLE

* CHAPTER

* EDITOR

* PUBLISHER

* INSTITUTION

* SCHOOL

**global_RefAbstract**

**global_Author**

**global_Journal**

**global_Journal**

**global_RefKeyword**

----

Regional tables
---------------
Non-Cosmogenics
~~~~~~~~~~~~~~~
**cabah_LabCodes**

**cabah_chemprepID**

**cabah_col_mtdID**

**cabah_methodID**

Cosmogenics
~~~~~~~~~~~
**crn_alstndID**

**crn_bestndID**

Luminescence
~~~~~~~~~~~~
**osl-tl_agemodelID**

**osl-tl_ed_procID**

**osl-tl_lum_matID**

**osl-tl_mineralID**

**osl-tl_mtdID**

**osl_typeID**

----

Collection specific tables
--------------------------

CRN
~~~~
**crn_amsID**

**crn_projepsgID**

**crn_studies_boundingbox**

SahulArch
~~~~~~~~~
**arch_featdatedID**

**c13_valID**

**c14_contamID**

**c14_hum_modID**

**c14_materia1ID**

**c14_materia2ID**

**c14_solvent2ID**

**c_mtdID**

**arch_c14_polygons_EPSG3857**

**arch_osl_polygons_EPSG3857**

**arch_tl_polygons_EPSG3857**

SahulSed
~~~~~~~~
**sed_depconID**

**sed_faciesID**

**sed_geommodID**

**sed_geotypeID**

**sed_laketypeID**

**sed_morphID**

**sed_sitetypeID**

**sed-osl_points_EPSG3857**

**sed-tl_points_EPSG3857**

FosSahul
~~~~~~~~

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

expage
~~~~~~
**expage_points_EPSG3857**