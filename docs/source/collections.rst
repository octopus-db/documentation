================
Data collections
================
OCTOPUS database knows two levels of sub-collection integration - *core* collections and *partner* collections. Though, like core collections, being fully integrated into OCTOPUS database, partner collections are not maintained nor officially supported by the OCTOPUS project, meaning that more up to date (albeit less rich in auxiliary data) versions may exist elsewhere.

Core collections
----------------

CRN
~~~
OCTOPUS CRN branch features collections of published **cosmogenic Be-10 and Al-26 concentrations from modern river sediment and basin-averaged denudation rates** inferred from these data. Ancillary spatial data includes: sample site location (point), basin outline (polygon), digital elevation model (raster), D8 flow direction and flow accumulation grids (raster), topographic gradient (raster), atmospheric pressure (raster), and cosmogenic nuclide production scaling factor and topographic shielding grids (raster). The vector spatial data uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system. The raster data uses the WGS84/UTM projected coordinate reference system, UTM zones depending on the extent and location of each data package. Sample metadata is comprehensive and includes all necessary information and input files for the recalculation of denudation rates using the `CAIRN model <https://github.com/LSDtopotools/LSDTopoTools_CRNBasinwide>`_. **All denudation rates were recalculated and harmonised** using CAIRN.

CRN Australia
"""""""""""""
| *Collection of Australian basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances*
| **Publisher, Year**
| University of Wollongong, 2021
| **Spatial, temporal data extent**
| Australia, 1998-2021
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370399 Geochemistry not elsewhere classified, 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Codilean A.T., Munack H., 2021, OCTOPUS Database v.2: The CRN Denudation Australian collection. Basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances.
| **DOI**
| http://dx.doi.org/10.25900/mpr9-yn15

CRN International
"""""""""""""""""
| *Global collection of basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances, excluding Australia*
| **Publisher, Year**
| University of Wollongong, 2021
| **Spatial, temporal data extent**
| Global (excl. Australia), 1995-2021
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370399 Geochemistry not elsewhere classified, 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Codilean A.T., Munack H., 2021, OCTOPUS Database v.2: The CRN Denudation Global collection. Basin-averaged denudation rates from cosmogenic Be-10 and Al-26 abundances.
| **DOI**
| http://dx.doi.org/10.25900/g76f-0h45

CRN XXL
"""""""
| description to appear here...

CRN inprep
""""""""""
| description to appear here...

SahulArch
~~~~~~~~~
SahulArch is a collection triplet of published **radiometric ages for archaeological records from Sahul**. Sample locations were obfuscated within a radius of 25 km and spatial data includes sample locations as circular polygons. The data uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system. Sample metadata is comprehensive and includes bibliographic, contextual, and sample preparation and measurement related information.

The SahulArch Radiocarbon collection
""""""""""""""""""""""""""""""""""""
| *Database of published radiocarbon ages for archaeological records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH), 2022
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1961-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370905 Quaternary environments, 430103 Archaeology of Australia (excl. Aboriginal and Torres Strait Islander)
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Saktura W.M., Rehn E., Linnenlucke L., Munack H., Wood R., Petchey F., Codilean A.T., Jacobs Z., Williams A., Ulm S., 2022, The SahulArch Radiocarbon collection. Sahul-wide database of published archaeological records with radiometric ages (v.2).
| **DOI**
| https://doi.org/10.25900/gpvr-ay04

The SahulArch OSL collection
""""""""""""""""""""""""""""
| *Database of published optically stimulated luminescence (OSL) ages for archaeological records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH), 2022
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1990-2022
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370905 Quaternary environments, 430103 Archaeology of Australia (excl. Aboriginal and Torres Strait Islander)
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Saktura W.M., Rehn E., Munack H., Codilean A.T., Jacobs Z., Williams A., Ulm S., 2022, The SahulArch OSL collection. Sahul-wide database of published archaeological records with radiometric ages (v.2).
| **DOI**
| https://doi.org/10.25900/9y07-4j77

The SahulArch TL collection
"""""""""""""""""""""""""""
| *Database of published thermoluminescence (TL) ages for archaeological records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH), 2022
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1972-2022
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370905 Quaternary environments, 430103 Archaeology of Australia (excl. Aboriginal and Torres Strait Islander)
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Saktura W.M., Rehn E., Munack H., Codilean A.T., Jacobs Z., Williams A., Ulm S., 2022, The SahulArch TL collection. Sahul-wide database of published archaeological records with radiometric ages (v.2).
| **DOI**
| https://doi.org/10.25900/af67-kh16

SahulSed
~~~~~~~~
OCTOPUS collection set of published **optically stimulated luminescence (OSL) ages for fluvial sedimentary records from Sahul**. Spatial data includes sample locations (point) and uses the WGS84/Pseudo-Mercator (EPSG: 3857) projected coordinate reference system. Sample metadata is comprehensive and includes bibliographic, contextual, and sample preparation and measurement related information.

The SahulSed Aeolian OSL collection
"""""""""""""""""""""""""""""""""""
| *Database of published optically stimulated luminescence (OSL) ages for aeolian sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1993-2019
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Hesse P., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Aeolian OSL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/5jcw-tn50

The SahulSed Aeolian TL collection
""""""""""""""""""""""""""""""""""
| *Database of published thermoluminescence (TL) ages for aeolian sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1987-2018
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Hesse P., Price D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Aeolian TL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/a2k9-kj43

The SahulSed Fluvial OSL collection
"""""""""""""""""""""""""""""""""""
| *Database of published optically stimulated luminescence (OSL) ages for fluvial sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1997-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Saktura W.M., Jansen J.D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Fluvial OSL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/p5ye-rn35

The SahulSed Fluvial TL collection
""""""""""""""""""""""""""""""""""
| *Database of published thermoluminescence (TL) ages for fluvial sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1986-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Saktura W.M., Jansen J.D., Price D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Fluvial TL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/2a76-vw55

The SahulSed Lacustrine OSL collection
""""""""""""""""""""""""""""""""""""""
| *Database of published optically stimulated luminescence (OSL) ages for lacustrine sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1997-2020
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Lacustrine OSL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/6hmv-zz61

The SahulSed Lacustrine TL collection
"""""""""""""""""""""""""""""""""""""
| *Database of published thermoluminescence (TL) ages for lacustrine sedimentary records from Sahul*
| **Publisher, Year**
| ARC Centre of Excellence for Australian Biodiversity and Heritage (CABAH); University of Wollongong, 2021
| **Spatial, temporal data extent**
| Sahul (mainland Australia, Tasmania, New Guinea, and neighbouring islands), 1991-2015
| **Software Required**
| any web browser (OCTOPUS web interface), any GIS, or any Web Feature Service (WFS) compliant application (see :ref:`Data access` section)
| **FoR codes (2020) [#f1]_**
| 370502 Geochronology, 370901 Geomorphology and earth surface processes, 370905 Quaternary environments
| **Creative Commons License**
| Creative Commons Attribution 4.0 International License (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_)
| **Recommended citation**
| Cohen T.J., Fu X., Price D., Rui X., Saktura R.B.K., Munack H., Codilean A.T., 2021, OCTOPUS Database v.2: The SahulSed Lacustrine TL collection. Sahul-wide database of published sedimentary records with radiometric ages.
| **DOI**
| https://doi.org/10.25900/32de-mj32

Partner collections
-------------------

FosSahul
~~~~~~~~
| description to appear here...

expage
~~~~~~
| description to appear here...

.. rubric:: Footnotes

.. [#f1] `https://www.arc.gov.au/manage-your-grant/classification-codes-rfcd-seo-and-anzsic-codes <https://www.arc.gov.au/manage-your-grant/classification-codes-rfcd-seo-and-anzsic-codes>`_
