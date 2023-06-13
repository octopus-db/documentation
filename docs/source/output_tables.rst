============================
Output table fields & values
============================

To serve the data collected in the OCTOPUS database as geospatial layers via an interactive map :ref:`Web_interface` and to allow for data manipulation via the :ref:`Web_Feature_Service` protocol, each data sub-collection is served to GeoServer as a flat data table. The deployed version of GeoServer does not accept dynamically generated PostgreSQL virtual tables (knows as “views”); therefore, the generation of static flat data tables was required to serve the purpose of a view. Newer versions of GeoServer, however, accept materialised views, and an upgrade would present a possible improvement in the database by eliminating the need to store duplicate data. When downloading data from OCTOPUS, users are presented with point or polygon geospatial data files with associated attribute tables. Direct connections to the PostgreSQL/PostGIS database are possible upon request. Munack and Codilean (`2022 <https://doi.org/10.5281/zenodo.7352807>`_) provide a complete documentation of the relational database, including a detailed database model diagram and searchable HTML documentation generated using SchemaSpy (https://schemaspy.org, last access: 04 May 2023).

.. note::

  The above section is a modified version of Section 3 from `Codilean et al. 2022 <https://doi.org/10.5194/essd-14-3695-2022>`_

CRN output
----------

+------------+-------------+-------------------+-------------------+
| Field Name | Unit        | Example           | Origin (Alias)    |
+============+=============+===================+===================+
| OBSID1     |             | \*Kier2014-3a\*   | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| OBSID2     |             | \*DR-2A\*         | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| IGSNID     |             | \*NA\*            | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| DBDOI      |             | \*expage_Odbv.    | :ref              |
|            |             | 2_no_DOI_minted\* | :\`global_dbDOI\` |
|            |             |                   | (gdd)             |
+------------+-------------+-------------------+-------------------+
| DBVERNO    |             | \*2\*             | :ref              |
|            |             |                   | :\`global_dbDOI\` |
|            |             |                   | (gdd)             |
+------------+-------------+-------------------+-------------------+
| SMPID      |             | \                 | :ref:             |
|            |             | *Kier2014-3.den\* | \`expage_Sample\` |
|            |             |                   | (es)              |
+------------+-------------+-------------------+-------------------+
| SITEID     |             | \*Kier2014-A.z\*  | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| METASITEID |             | \*Kier2014-A\*    | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| CNTRY      |             | \*AUS\*           | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| REGION_INT |             | \*Lake Rhona\*    | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| REGION_REG |             | \*AUS\*           | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| DIV_ADMIN  |             | \*AU-TAS\*        | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| DIV_OTHER  |             | \*NA\*            | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| ISL_NAME   |             | \*Tasmania\*      | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| BASIN      |             | \*Gordon River\*  | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| AHGFL1     |             | \*TAS\*           | :ref              |
|            |             |                   | :\`global_rivID\` |
|            |             |                   | (grid)            |
+------------+-------------+-------------------+-------------------+
| AHGFL2     |             | \*TAS_08\*        | :ref              |
|            |             |                   | :\`global_rivID\` |
|            |             |                   | (grid)            |
+------------+-------------+-------------------+-------------------+
| RIVNAME    |             | \*Gordon River\*  | :ref              |
|            |             |                   | :\`global_rivID\` |
|            |             |                   | (grid)            |
+------------+-------------+-------------------+-------------------+
| RIVDIV     |             | \*Tasmania\*      | :ref              |
|            |             |                   | :\`global_rivID\` |
|            |             |                   | (grid)            |
+------------+-------------+-------------------+-------------------+
| IBRACODE   |             | \*TWE\*           | :ref:\`ibraID\`   |
|            |             |                   | (giid)            |
+------------+-------------+-------------------+-------------------+
| IBRAREGION |             | \*Tasmanian       | :ref:\`ibraID\`   |
|            |             | West\*            | (giid)            |
+------------+-------------+-------------------+-------------------+
| X_WGS84    | decimal deg | \*146.29\*        | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| Y_WGS84    | decimal deg | \*-42.55\*        | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| CORDS_ELEV |             | \*INTP_ND\*       | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| ELEVATION  | m           | \*908\*           | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| SITE_COMMT |             | \*NA\*            | :ref:\`gl         |
|            |             |                   | obal_SiteMaster\` |
|            |             |                   | (gsm)             |
+------------+-------------+-------------------+-------------------+
| REFDBID1   |             | \*Kier            | :ref:\`           |
|            |             | nan:2014denison\* | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| OAID1      |             | \*OAID-000303\*   | :ref:\            |
|            |             |                   | `global_RefCore\` |
|            |             |                   | (grc1)            |
+------------+-------------+-------------------+-------------------+
| AUTHOR1    |             | \*Kiernan\*       | :ref              |
|            |             |                   | :\`global_Author' |
|            |             |                   | (ga1)             |
+------------+-------------+-------------------+-------------------+
| PUBYEAR1   |             | \*2014\*          | :ref:\            |
|            |             |                   | `global_RefCore\` |
|            |             |                   | (grc1)            |
+------------+-------------+-------------------+-------------------+
| REFID1     |             | \*Quater          | :ref:\            |
|            |             | nary_Sci_Rev_97\* | `global_RefCore\` |
|            |             |                   | (grc1)            |
+------------+-------------+-------------------+-------------------+
| REFDOI1    |             | \                 | :ref:\            |
|            |             | *10.1016/j.quasci | `global_RefCore\` |
|            |             | rev.2014.05.008\* | (grc1)            |
+------------+-------------+-------------------+-------------------+
| REFDBID2   |             |                   | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| ...        |             | ...               | ...               |
+------------+-------------+-------------------+-------------------+
| REFDOI4    |             |                   | :ref:\            |
|            |             |                   | `global_RefCore\` |
|            |             |                   | (grc4)            |
+------------+-------------+-------------------+-------------------+
| MATERIAL   |             | \*Boulder\*       | :ref:             |
|            |             |                   | \`expage_Sample\` |
|            |             |                   | (es)              |
+------------+-------------+-------------------+-------------------+
| THICKNESS  | cm          | \*3.5\*           | :ref:             |
|            |             |                   | \`expage_Sample\` |
|            |             |                   | (es)              |
+------------+-------------+-------------------+-------------------+
| DENSITY    | g.cm^-3     | \*2.7\*           | :ref:             |
|            |             |                   | \`expage_Sample\` |
|            |             |                   | (es)              |
+------------+-------------+-------------------+-------------------+
| SHIELDING  |             | \*0.978\*         | :ref:             |
|            |             |                   | \`expage_Sample\` |
|            |             |                   | (es)              |
+------------+-------------+-------------------+-------------------+
| SMP_YR     |             | \*2012\*          | :ref:             |
|            |             |                   | \`expage_Sample\` |
|            |             |                   | (es)              |
+------------+-------------+-------------------+-------------------+
| SMP_COMMT  |             | \*Latitudes and \ | :ref:             |
|            |             | longitudes based\ | \`expage_Sample\` |
|            |             | on map figures\   | (es)              |
|            |             | and Google Earth.\|                   |
|            |             | Sample thickness\ |                   |
|            |             | back-calculated\  |                   |
|            |             | from depth\       |                   |
|            |             | correction values\|                   |
|            |             | in Table 1.\      |                   |
|            |             | Sampling year\    |                   |
|            |             | assumed to be\    |                   |
|            |             | 2012. Group ID\   |                   |
|            |             | based on\         |                   |
|            |             | publication\      |                   |
|            |             | (Table 1).\*      |                   |
+------------+-------------+-------------------+-------------------+
| BE10NP     | atoms.g^-1  | \*141000\*        | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| BE10NP_ERR | atoms.g^-1  | \*7000\*          | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| BESTND     |             | \*07KNSTD\*       | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| BECORR     |             | \*1\*             | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| BE10AP     | kyr         | \*18.3\*          | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| BE10AP_ERR | kyr         | \*1\*             | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AL26NP     | atoms.g^-1  | \*930000\*        | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AL26NP_ERR | atoms.g^-1  | \*118000\*        | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| ALSTND     |             | \*KNSTD\*         | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| ALCORR     |             | \*1\*             | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AL26AP     | kyr         | \*18\*            | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AL26AP_ERR | kyr         | \*2.7\*           | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| ABE_YR     | kyr         | \*17.719\*        | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| ABE_ERREXT | kyr         | \*1.322\*         | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| ABE_ERRINT | kyr         | \*0.884\*         | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AAL_YR     | kyr         | \*16.607\*        | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AAL_ERREXT | kyr         | \*2.401\*         | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+
| AAL_ERRINT | kyr         | \*2.124\*         | :ref:\`           |
|            |             |                   | expage_DataCore\` |
|            |             |                   | (edc)             |
+------------+-------------+-------------------+-------------------+



SahulArch output
----------------

SahulSed output
---------------

FosSahul output
---------------

expage output
-------------