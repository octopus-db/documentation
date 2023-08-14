================
Data collections
================
OCTOPUS database knows two levels of sub-collection integration - :ref:`core collections <Core collections>` and :ref:`partner collections <Partner collections>`. Though, like core collections, being fully integrated into OCTOPUS database, partner collections are not maintained nor officially supported by the OCTOPUS project, meaning that more up to date (albeit less rich in auxiliary data) versions may exist elsewhere.

..  _Core_collections:

Core collections
----------------

..  _CRN:

CRN collections
~~~~~~~~~~~~~~~
| OCTOPUS CRN branch features collections of published **cosmogenic Be-10 and Al-26 concentrations from modern river sediment and basin-averaged denudation rates** inferred from these data. The vector spatial data -- sample site location (point), basin outline (polygon) --  uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system.
| :ref:`CRN_ancillary_data` includes: digital elevation model (raster), D8 flow direction and flow accumulation grids (raster), topographic gradient (raster), atmospheric pressure (raster), and cosmogenic nuclide production scaling factor and topographic shielding grids (raster). The raster data uses the WGS84/UTM projected coordinate reference system, UTM zones depending on the extent and location of each data package. Sample metadata is comprehensive and includes all necessary information and input files (see :ref:`CSV_folder`) for the recalculation of denudation rates using the CAIRN model [#]_. 

.. important::
   **All denudation rates were recalculated and harmonised** using CAIRN.

..  _CRN_Australia:

CRN Australia
"""""""""""""
| *A collection of Australian basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances*
| **Publisher, Year**
| University of Wollongong, 2021
| **Spatial extent, Publication period**
| Australia, 1998-2021
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)** [#]_
| 370399 Geochemistry not elsewhere classified, 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Codilean A.T., Munack H., 2021, OCTOPUS Database v.2: The CRN Denudation Australian collection. Basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances.
| **DOI**
| http://dx.doi.org/10.25900/mpr9-yn15


..  _CRN_International:

CRN International
"""""""""""""""""
| *A global collection of basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances, excluding Australia*
| **Publisher, Year**
| University of Wollongong, 2021
| **Spatial extent, Publication period**
| Global (excl. Australia), 1995-2021
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370399 Geochemistry not elsewhere classified, 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Codilean A.T., Munack H., 2021, OCTOPUS Database v.2: The CRN Denudation Global collection. Basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances.
| **DOI**
| http://dx.doi.org/10.25900/g76f-0h45


..  _CRN_Large_Basins:

CRN Large Basins
"""""""""""""""""
| *A global collection of catchment polygons for extra large river basins for which Be-10 and Al-26 abundances have been published*
| **Publisher, Year**
| University of Wollongong, 2021
| **Spatial extent, Publication period**
| Global, 2006-2017
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370399 Geochemistry not elsewhere classified, 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Codilean A.T., Munack H., 2021, OCTOPUS Database v.2: The CRN Large Basins collection. (Online via https://octopusdata.org. Accessed DD-MM-YYYY)
| **DOI**
| not applicable

----

..  _SahulArch:

SahulArch collections
~~~~~~~~~~~~~~~~~~~~~
SahulArch is a collection triplet of published **radiometric ages for archaeological records from Sahul**. Sample locations were obfuscated within a radius of 25 km and spatial data includes sample locations as circular polygons. The data uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system. Sample metadata is comprehensive and includes bibliographic, contextual, and sample preparation and measurement related information. For more detailed information refer to `Saktura et al. 2023 <https://doi.org/10.1080/03122417.2022.2159751>`_.


..  _The_SahulArch_Radiocarbon_collection:

The SahulArch Radiocarbon collection
""""""""""""""""""""""""""""""""""""
| *A database of published radiocarbon ages for archaeological records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH), 2022
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1961-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370905 Quaternary environments, 430103 Archaeology of Australia (excl. Aboriginal and Torres Strait Islander)
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Saktura W.M., Rehn E., Linnenlucke L., Munack H., Wood R., Petchey F., Codilean A.T., Jacobs Z., Williams A., Ulm S., 2022, The SahulArch Radiocarbon collection. Sahul-wide database of published archaeological records with radiometric ages (v.2).
| **DOI**
| https://doi.org/10.25900/gpvr-ay04


..  _The_SahulArch_OSL_collection:

The SahulArch OSL collection
""""""""""""""""""""""""""""
| *A database of published optically stimulated luminescence (OSL) ages for archaeological records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH), 2022
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1990-2022
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370905 Quaternary environments, 430103 Archaeology of Australia (excl. Aboriginal and Torres Strait Islander)
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Saktura W.M., Rehn E., Munack H., Codilean A.T., Jacobs Z., Williams A., Ulm S., 2022, The SahulArch OSL collection. Sahul-wide database of published archaeological records with radiometric ages (v.2).
| **DOI**
| https://doi.org/10.25900/9y07-4j77


..  _The_SahulArch_TL_collection:

The SahulArch TL collection
"""""""""""""""""""""""""""
| *A database of published thermoluminescence (TL) ages for archaeological records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH), 2022
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1972-2022
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370905 Quaternary environments, 430103 Archaeology of Australia (excl. Aboriginal and Torres Strait Islander)
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Saktura W.M., Rehn E., Munack H., Codilean A.T., Jacobs Z., Williams A., Ulm S., 2022, The SahulArch TL collection. Sahul-wide database of published archaeological records with radiometric ages (v.2).
| **DOI**
| https://doi.org/10.25900/af67-kh16

----

..  _SahulSed:

SahulSed collections
~~~~~~~~~~~~~~~~~~~~
OCTOPUS collection set of published **optically stimulated luminescence (OSL) ages for fluvial sedimentary records from Sahul**. Spatial data includes sample locations (point) and uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system. Sample metadata is comprehensive and includes bibliographic, contextual, and sample preparation and measurement related information.


..  _The_SahulSed_Aeolian_OSL_collection:

The SahulSed Aeolian OSL collection
"""""""""""""""""""""""""""""""""""
| *A database of published optically stimulated luminescence (OSL) ages for aeolian sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1993-2019
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Hesse P., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Aeolian OSL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/5jcw-tn50


..  _The_SahulSed_Aeolian_TL_collection:

The SahulSed Aeolian TL collection
""""""""""""""""""""""""""""""""""
| *A database of published thermoluminescence (TL) ages for aeolian sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1987-2018
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Hesse P., Price D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Aeolian TL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/a2k9-kj43


..  _The_SahulSed_Fluvial_OSL_collection:

The SahulSed Fluvial OSL collection
"""""""""""""""""""""""""""""""""""
| *A database of published optically stimulated luminescence (OSL) ages for fluvial sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1997-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Saktura W.M., Jansen J.D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Fluvial OSL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/p5ye-rn35


..  _The_SahulSed_Fluvial_TL_collection:

The SahulSed Fluvial TL collection
""""""""""""""""""""""""""""""""""
| *A database of published thermoluminescence (TL) ages for fluvial sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1986-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Saktura W.M., Jansen J.D., Price D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Fluvial TL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/2a76-vw55


..  _The_SahulSed_Lacustrine_OSL_collection:

The SahulSed Lacustrine OSL collection
""""""""""""""""""""""""""""""""""""""
| *A database of published optically stimulated luminescence (OSL) ages for lacustrine sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1997-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Lacustrine OSL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/6hmv-zz61


..  _The_SahulSed_Lacustrine_TL_collection:

The SahulSed Lacustrine TL collection
"""""""""""""""""""""""""""""""""""""
| *A database of published thermoluminescence (TL) ages for lacustrine sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1991-2015
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Price D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Lacustrine TL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/32de-mj32

..  _Partner_collections:

Partner collections
-------------------


..  _FosSahul:

FosSahul collection
~~~~~~~~~~~~~~~~~~~
| *A database of quality-rated dates from Late Quaternary non-human vertebrate fossil records published up to 2018*
| **Publisher, Year**
| OCTOPUS database, 2021
| **Spatial extent, Publication period**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1955-2018
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 310306 Palaecology, 370502 Geochronology, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Peters, Katharina J.; Saltré, Frédérik; Friedrich, Tobias; Jacobs, Zenobia; Wood, Rachel; McDowell, Matthew; Ulm, Sean; Bradshaw, Corey J. A. (2019). FosSahul 2.0, an updated database for the Late Quaternary fossil records of Sahul. Sci Data 6, 272. (Online via https://octopusdata.org. Accessed DD-MM-YYYY)
| **DOI**
| https://doi.org/10.1038/s41597-019-0267-3


..  _expage:

ExpAge collection
~~~~~~~~~~~~~~~~~
| *A global database of published 10Be and 26Al data from glacial samples*
| **Publisher, Year**
| OCTOPUS database, 2021
| **Spatial extent, Publication period**
| Global, 1989-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020)**
| 370502 Geochronology, 370902 Glaciology, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Heyman, Jakob (2021) ExpAge -- A global compilation of glacial 10Be and 26Al data. https://expage.github.io (Online via https://octopusdata.org. Accessed DD-MM-YYYY)
| **DOI**
| not applicable
|

.. rubric:: Footnotes

.. [#] `https://github.com/LSDtopotools/LSDTopoTools_CRNBasinwide <https://github.com/LSDtopotools/LSDTopoTools_CRNBasinwide>`_
.. [#] `https://www.arc.gov.au/manage-your-grant/classification-codes-rfcd-seo-and-anzsic-codes <https://www.arc.gov.au/manage-your-grant/classification-codes-rfcd-seo-and-anzsic-codes>`_
