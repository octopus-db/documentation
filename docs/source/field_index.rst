=============================
Table fields and their values
=============================

Data table fields
-----------------

Lookup table fields
-------------------

..  _global_GrainSize_Fields:

global_GrainSize Fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_GrainSize_FIELDS.csv
   :header-rows: 1

The unit for both fields "GRNSIZEMIN" and "GRNSIZEMAX" is *mm*.

..  _global_SiteCode_Fields:

global_SiteCode Fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_SiteCode_FIELDS.csv
   :header-rows: 1

.. note::

   The dominant attribute of a site will override any other. So, for example, burials in a rockshelter with lots of occupation deposit would be classified as a Rockshelter, not a Cemetery.

..  _global_biomeID_Fields:

global_biomeID Fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_biomeID_FIELDS.csv
   :header-rows: 1

Classification of biomes on the basis of Prentice et al. (1992), Forseth (2010), and GPD [#]_.

..  _global_ibraID_Fields:

global_ibraID Fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_ibraID_FIELDS.csv
   :header-rows: 1

Detailed information about Australia's bioregions classification rationale and model can be found at `https://www.dcceew.gov.au/environment/land/nrs/science/ibra <https://www.dcceew.gov.au/environment/land/nrs/science/ibra>`_.

.. warning::

   The *global_ibraID* table only applies to samples from Australia.

..  _global_rivID_Fields:

global_rivID Fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_rivID_FIELDS.csv
   :header-rows: 1

Detailed information about the Australian Hydrological Geospatial Fabric (Geofabric) classification rationale and model can be found at  `http://www.bom.gov.au/water/geofabric/ <http://www.bom.gov.au/water/geofabric/>`_.

.. warning::

   The *global_rivID* table only applies to samples from Australia.

..  _global_varunitID_Fields:

global_varunitID Fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_varunitID_FIELDS.csv
   :header-rows: 1

..  _global_PubType_Fields:

global_PubType Fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_PubType_FIELDS.csv
   :header-rows: 1

* **article** [#]_ -- An article from a journal or magazine. *Required fields*: author, title, journal, year. *Optional fields*: volume, number, pages, month, note.

* **book** -- A book with an explicit publisher. *Required fields*: author or editor, title, publisher, year. *Optional fields*: volume or number, series, address, edition, month, note.

* **booklet** -- A work that is printed and bound, but without a named publisher or sponsoring institution. *Required field*: title. *Optional fields*: author, howpublished, address, month, year, note.

* **conference** -- The same as INPROCEEDINGS, included for Scribe compatibility.

* **inbook** -- A part of a book, which may be a chapter (or section or whatever) and/or a range of pages. *Required fields*: author or editor, title, chapter and/or pages, publisher, year. *Optional fields*: volume or number, series, type, address, edition, month, note.

* **incollection** -- A part of a book having its own title. *Required fields*: author, title, booktitle, publisher, year. *Optional fields*: editor, volume or number, series, type, chapter, pages, address, edition, month, note.

* **inproceedings** -- An article in a conference proceedings. *Required fields*: author, title, booktitle, year. *Optional fields*: editor, volume or number, series, pages, address, month, organization, publisher, note.

* **manual** -- Technical documentation. *Required field*: title. *Optional fields*: author, organization, address, edition, month, year, note.

* **mastersthesis** -- A Master's thesis. *Required fields*: author, title, school, year. *Optional fields*: type, address, month, note.

* **misc** -- Use this type when nothing else fits. *Required fields*: none. *Optional fields*: author, title, howpublished, month, year, note.

* **phdthesis** -- A PhD thesis. *Required fields*: author, title, school, year. *Optional fields*: type, address, month, note.

* **proceedings** -- The proceedings of a conference. *Required fields*: title, year. *Optional fields*: editor, volume or number, series, address, month, organization, publisher, note.

* **techreport** -- A report published by a school or other institution, usually numbered within a series. *Required fields*: author, title, institution, year. *Optional fields*: type, number, address, month, note.

* **unpublished** -- A document having an author and title, but not formally published. *Required fields*: author, title, note. *Optional fields*: month, year.

* **pers_comm** -- Personal communication. *Required fields*: author

* **online** -- Internet source. *Required fields*: title, url, urldate (in "NOTE" field)

----

..  _cabah_chemprepID_Fields:

cabah_chemprepID Fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/cabah_chemprepID_FIELDS.csv
   :header-rows: 1

* ABA -- Acid-base-acid is equivalent to *AAA* (acid-alkali-acid)

* ABOx-SC -- Acid-base-oxidation-stepped-combustion

* HyPy -- Hydrogen pyrolysis

* Acid-gelatinisation -- The Longin method

* CARDS -- Carbonate Density Separation

* XAD -- Resin used to clean amino acids. Note that *XAD* flag overwrites potential other pretreatment

* Plasma oxidation and potassium permanganate methods refer to methods which aim to convert a specific portion of the sample to CO2 and may involve a variety of other steps.

* Bulk -- Several fragments dated together

* SC -- Stepped combustion

* Ultra -- Ultrafiltration

* Longin -- Modified Longing method

* Gelatin -- Gelatinisation

* Coll -- Collagen


..  _cabah_col_mtdID_Fields:

cabah_col_mtdID Fields
~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/cabah_col_mtdID_FIELDS.csv
   :header-rows: 1

..  _cabah_methodID_Fields:

cabah_methodID Fields
~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------+------------+----------+----------------+
| METHODID | METHOD         | METHODABBR | PARENTID | METHODREF      |
+==========+================+============+==========+================+
| 1        | Amino Acid     | AAR        | 63       | Hare, P .E. &  |
|          | Racemization   |            |          | Abelson, P .H. |
|          | (AAR)          |            |          | (1968).        |
|          |                |            |          | Racemization   |
|          |                |            |          | of amino acids |
|          |                |            |          | in fossil      |
|          |                |            |          | shells.        |
|          |                |            |          | Carnegie       |
|          |                |            |          | Institution of |
|          |                |            |          | Washington     |
|          |                |            |          | Yearbook, 66,  |
|          |                |            |          | 516--528.      |
+----------+----------------+------------+----------+----------------+
| 2        | Radiocarbon    | C14        | 14       | Anderson,      |
|          | Dating         |            |          | Libby,         |
|          |                |            |          | Weinhouse,     |
|          |                |            |          | Reid,          |
|          |                |            |          | Kirshenbaum &  |
|          |                |            |          | Grosse (1947)  |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 3        | Cation Ratio   | CRD        | 3        | Dorn (1983)    |
|          | Dating         |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 4        | Electron Spin  | ESR        | 47       | Zeller, E.J.;  |
|          | Resonance      |            |          | Levy, P.W.; &  |
|          |                |            |          | Mattern, P.L.  |
|          |                |            |          | (1             |
|          |                |            |          | 967). Geologic |
|          |                |            |          | dating by      |
|          |                |            |          | electron spin  |
|          |                |            |          | resonance.     |
|          |                |            |          | International  |
|          |                |            |          | Atomic Energy  |
|          |                |            |          | Agency (IAEA). |
+----------+----------------+------------+----------+----------------+
| 5        | Oxidisable     | OCR        | 5        | Frink (1996)   |
|          | Carbon Ratio   |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 6        | Optically      | OSL        | 47       | Huntley,       |
|          | Stimulated     |            |          | Godfrey-Smith  |
|          | Luminescence   |            |          | & Thewalt      |
|          |                |            |          | (1985) [#]_    |
+----------+----------------+------------+----------+----------------+
| 7        | Thermo\        | TL         | 47       | Daniels, Boyd  |
|          | luminescence   |            |          | & Saunders     |
|          |                |            |          | (1953) [#]_    |
+----------+----------------+------------+----------+----------------+
| 8        | Uranium-Series | U          | 42       | NULL           |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 9        | Closed-system  | CSU-ESR    | 83       | NULL           |
|          | U-Series and   |            |          |                |
|          | ESR model      |            |          |                |
|          | (CSU-ESR)      |            |          |                |
+----------+----------------+------------+----------+----------------+
| 10       | Stratigraphic  | Strat      | 68       | NULL           |
|          | correlation    |            |          |                |
+----------+----------------+------------+----------+----------------+
| 11       | Coupled U-ESR  | U-ESR      | 83       | NULL           |
|          | model (U-ESR)  |            |          |                |
+----------+----------------+------------+----------+----------------+
| 12       | Chronometric   | ChronMet   | 12       | NULL           |
|          | dating         |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 13       | Radiometric    | RadioMet   | 12       | NULL           |
|          | dating         |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 14       | Cosmogenic     | CRN        | 13       | NULL           |
|          | Radionuclides  |            |          |                |
+----------+----------------+------------+----------+----------------+
| 15       | C13 date       | C13        | 2        | NULL           |
+----------+----------------+------------+----------+----------------+
| 16       | C14 date       | C14-uncorr | 2        | NULL           |
|          | (uncorrected)  |            |          |                |
+----------+----------------+------------+----------+----------------+
| 17       | C14 date       | C14-corr   | 2        | NULL           |
|          | (corrected)    |            |          |                |
+----------+----------------+------------+----------+----------------+
| 18       | Tritium/Helium | 3H/3He     | 14       | Kaufmann &     |
|          |                |            |          | Libby (1954)   |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 19       | Beryllium-10   | Be-10      | 14       | Arnold (1956)  |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 20       | Aluminium-26   | Al-26      | 14       | Tanaka, S.;    |
|          |                |            |          | Sakamoto, K. & |
|          |                |            |          | Tschuchimoto,  |
|          |                |            |          | M. (1964).     |
|          |                |            |          | Experimental   |
|          |                |            |          | proposal on    |
|          |                |            |          | search for     |
|          |                |            |          | 26Al induced   |
|          |                |            |          | by cosmic-ray  |
|          |                |            |          | myons in       |
|          |                |            |          | terrestrial    |
|          |                |            |          | rocks. Inst.   |
|          |                |            |          | Nuclear Study, |
|          |                |            |          | Univ. Tokyo,   |
|          |                |            |          | INS-19.        |
+----------+----------------+------------+----------+----------------+
| 21       | Silicon-32     | Si-32      | 14       | Lal, Goldberg  |
|          |                |            |          | & Koide (1960) |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 22       | Chlorine-36    | Cl-36      | 14       | Davis &        |
|          |                |            |          | Schaeffer      |
|          |                |            |          | (1955) [#]_    |
+----------+----------------+------------+----------+----------------+
| 23       | Argon-39       | Ar-39      | 14       | Loosli &       |
|          |                |            |          | Oeschger       |
|          |                |            |          | (1968) [#]_    |
+----------+----------------+------------+----------+----------------+
| 24       | Calcium-41     | Ca-41      | 14       | Raisbeck &     |
|          |                |            |          | Yiou (1979)    |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 25       | Manganese-53   | Mg-53      | 14       | Wilkinson &    |
|          |                |            |          | Sheline (1955) |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 26       | Krypton-81     | Kr-81      | 14       | Marti (1967)   |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 27       | Iodine-129     | I-129      | 14       | Takagi, Hampel |
|          |                |            |          | & Kirsten      |
|          |                |            |          | (1974) [#]_    |
+----------+----------------+------------+----------+----------------+
| 28       | Radionuclide   | RN         | 13       | NULL           |
|          | dating         |            |          |                |
+----------+----------------+------------+----------+----------------+
| 29       | Radionuclides  | RN-long    | 28       | NULL           |
|          | (long-lived)   |            |          |                |
+----------+----------------+------------+----------+----------------+
| 30       | Argon-Isotope  | Ar         | 29       | NULL           |
|          | dating         |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 31       | 40K/40Ar       | K/Ar       | 30       | Smits &        |
|          |                |            |          | Gentner (1950) |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 32       | 39Ar(K)/40Ar   | Ar/Ar      | 30       | Sigurgeirsson, |
|          |                |            |          | Thorbjörn      |
|          |                |            |          | (1962). Dating |
|          |                |            |          | recent basalt  |
|          |                |            |          | by the         |
|          |                |            |          | potassium      |
|          |                |            |          | argon method.  |
|          |                |            |          | (in Icelandic) |
|          |                |            |          | Rept. Physical |
|          |                |            |          | Laboratory of  |
|          |                |            |          | the Univ.      |
|          |                |            |          | Iceland, p. 9  |
+----------+----------------+------------+----------+----------------+
| 33       | 87Rb/Sr87      | Rb/Sr      | 29       | Hahn,          |
|          |                |            |          | Strassmann &   |
|          |                |            |          | Walling (1937) |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 34       | 147Sm/143Nd    | Sm/Nd      | 29       | Lugmair, G. W. |
|          |                |            |          | (1974). Sm-Nd  |
|          |                |            |          | ages: a new    |
|          |                |            |          | dating method. |
|          |                |            |          | Meteoritics,   |
|          |                |            |          | 9, 369.        |
+----------+----------------+------------+----------+----------------+
| 35       | 176Lu/176Hf    | Lu/Hf      | 29       | Herr, Merz,    |
|          |                |            |          | Eberhardt &    |
|          |                |            |          | Signer (1958)  |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 36       | 187Re/187Os    | Re/Os      | 29       | Herr & Merz    |
|          |                |            |          | (1955) [#]_    |
+----------+----------------+------------+----------+----------------+
| 37       | U/Th/Pb        | U/Th/Pb    | 29       | Holmes (1911)  |
|          | (non-specific) |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 38       | 207Pb/206Pb    | Pb/Pb      | 29       | Houtermans, F. |
|          |                |            |          | G. (1946). The |
|          |                |            |          | isotope ratios |
|          |                |            |          | in natural     |
|          |                |            |          | lead and the   |
|          |                |            |          | age of         |
|          |                |            |          | uranium.       |
|          |                |            |          | Naturwissen-   |
|          |                |            |          | schaften,      |
|          |                |            |          | 33, 185--186.  |
+----------+----------------+------------+----------+----------------+
| 39       | Radionuclides  | RN-short   | 28       | NULL           |
|          | (short-lived)  |            |          |                |
+----------+----------------+------------+----------+----------------+
| 40       | Lead-210       | 210Pb      | 39       | Goldberg, E.   |
|          |                |            |          | D. (1963).     |
|          |                |            |          | Geochronology  |
|          |                |            |          | with 210Pb.    |
|          |                |            |          | In:            |
|          |                |            |          | Radioactive    |
|          |                |            |          | Dating,        |
|          |                |            |          | I.A.E.A.,      |
|          |                |            |          | Vienna:        |
|          |                |            |          | 121--131.      |
+----------+----------------+------------+----------+----------------+
| 41       | Caesium-137    | 137Cs      | 39       | Williams       |
|          |                |            |          | (1995) [#]_    |
+----------+----------------+------------+----------+----------------+
| 42       | Parent         | PD-Disequ  | 13       | NULL           |
|          | daughter       |            |          |                |
|          | disequilibrium |            |          |                |
+----------+----------------+------------+----------+----------------+
| 43       | 230Th/U        | Th/U       | 8        | Barnes, Lang & |
|          |                |            |          | Potratz (1956) |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 44       | 234U/238U      | U/U        | 8        | Thurber (1962) |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 45       | 230Th_exc      | Th_exc     | 42       | Petterson, H.  |
|          |                |            |          | (1937). Das    |
|          |                |            |          | Verhaltnis     |
|          |                |            |          | Thorium zu     |
|          |                |            |          | Uran in dem    |
|          |                |            |          | Gestein und im |
|          |                |            |          | Meer. (in      |
|          |                |            |          | German) Anz.   |
|          |                |            |          | Akad. Wiss.    |
|          |                |            |          | Wien Math.     |
|          |                |            |          | Naturwiss. Kl. |
|          |                |            |          | 127.           |
+----------+----------------+------------+----------+----------------+
| 46       | 210Pb (free)   | 210Pb_free | 42       | Goldberg, F.   |
|          |                |            |          | D. (1963).     |
|          |                |            |          | Geochronology  |
|          |                |            |          | with lead-210. |
|          |                |            |          | In:            |
|          |                |            |          | Radioactive    |
|          |                |            |          | Dating,        |
|          |                |            |          | 121--131, IAEA |
|          |                |            |          | Wien.          |
+----------+----------------+------------+----------+----------------+
| 47       | Radiation      | RadEx      | 13       | NULL           |
|          | exposure       |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 48       | Luminescence   | LUM        | 47       | NULL           |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 49       | Infrared       | IR-PL      | 47       | Prasad,        |
|          | Photo\         |            |          | Poolton, Kook  |
|          | luminescence   |            |          | & Jain (2017)  |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 50       | Infrared       | IR-RF      | 47       | Trautmann,     |
|          | Radio\         |            |          | Krbetschek,    |
|          | fluorescence   |            |          | Dietrich &     |
|          |                |            |          | Stolz (1998)   |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 51       | Infrared       | IRSL       | 47       | Hütt, Jaek &   |
|          | Stimulated     |            |          | Tchonka (1988) |
|          | Luminescence   |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 52       | Alpha-recoil   | ART        | 47       | Huang & Walker |
|          | track dating   |            |          | (1967) [#]_    |
+----------+----------------+------------+----------+----------------+
| 53       | (Uranium+T     | (U+Th)/He  | 47       | Fanale &       |
|          | horium)/Helium |            |          | Schaeffer      |
|          |                |            |          | (1965) [#]_    |
+----------+----------------+------------+----------+----------------+
| 54       | Fission track  | FT         | 47       | Price & Walker |
|          |                |            |          | (1962) [#]_    |
+----------+----------------+------------+----------+----------------+
| 55       | Banded records | Banded     | 12       | NULL           |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 56       | Dendro\        | Dendro     | 55       | NULL           |
|          | chronology     |            |          |                |
+----------+----------------+------------+----------+----------------+
| 57       | Varve          | Varve      | 55       | NULL           |
|          | chronology     |            |          |                |
+----------+----------------+------------+----------+----------------+
| 58       | Annual layers  | Ice        | 55       | NULL           |
|          | in glacier ice |            |          |                |
+----------+----------------+------------+----------+----------------+
| 59       | Lichenometry   | Lichen     | 55       | NULL           |
+----------+----------------+------------+----------+----------------+
| 60       | Speleothem     | Speleo     | 55       | NULL           |
|          | bands          |            |          |                |
+----------+----------------+------------+----------+----------------+
| 61       | Coral bands    | Coral      | 55       | NULL           |
+----------+----------------+------------+----------+----------------+
| 62       | Mollusc bands  | Mollusc    | 55       | NULL           |
+----------+----------------+------------+----------+----------------+
| 63       | Relative       | RelDat     | 63       | NULL           |
|          | dating method  |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 64       | Rock surface   | RSurf      | 63       | NULL           |
|          | weathering     |            |          |                |
+----------+----------------+------------+----------+----------------+
| 65       | Obsidian       | Obsid      | 63       | Friedman &     |
|          | hydration      |            |          | Smith (1960)   |
|          | dating         |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 66       | Pedogenesis    | Pedogen    | 63       | NULL           |
+----------+----------------+------------+----------+----------------+
| 67       | Relative       | FUn        | 63       | Oakley, K.     |
|          | dating of      |            |          | (1949). The    |
|          | fossile bone   |            |          | fluorine-      |
|          |                |            |          | dating         |
|          |                |            |          | method.        |
|          |                |            |          | Yearbook of    |
|          |                |            |          | Physical       |
|          |                |            |          | Anthropology,  |
|          |                |            |          | 5, 44.         |
+----------+----------------+------------+----------+----------------+
| 68       | Age            | AgeEquiv   | 68       | NULL           |
|          | equivalence    |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 69       | Oxygen isotope | Oxygen     | 68       | Emiliani       |
|          | chrono-        |            |          | (1954) [#]_    |
|          | stratigraphy   |            |          |                |
+----------+----------------+------------+----------+----------------+
| 70       | Tephro\        | Tephra     | 68       | Thorarinsson,  |
|          | chronology     |            |          | Sigurdur       |
|          |                |            |          | (1944).        |
|          |                |            |          | Tef            |
|          |                |            |          | rokronologiska |
|          |                |            |          | studier på     |
|          |                |            |          | Island :       |
|          |                |            |          | Þjórsárdalur   |
|          |                |            |          | och dess       |
|          |                |            |          | förödelse.     |
|          |                |            |          | Thesis         |
|          |                |            |          | (doctoral).    |
|          |                |            |          | Stockholms     |
|          |                |            |          | Högskola. 217  |
|          |                |            |          | pp             |
+----------+----------------+------------+----------+----------------+
| 71       | European       | Horizon    | 68       | NULL           |
|          | settlement     |            |          |                |
|          | horizon        |            |          |                |
+----------+----------------+------------+----------+----------------+
| 72       | Known fire     | Fire       | 68       | NULL           |
+----------+----------------+------------+----------+----------------+
| 73       | Magneto\       | Magnet     | 68       | NULL           |
|          | stratigraphy   |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 74       | Archaeo\       | A-Magnet   | 73       | Harold (1960)  |
|          | magnetic       |            |          | [#]_           |
|          | dating         |            |          |                |
+----------+----------------+------------+----------+----------------+
| 75       | Geomagnetic    | G-Magnet   | 73       | Thellier, E.   |
|          | dating         |            |          | (1938). Sur    |
|          |                |            |          | l'aimantation  |
|          |                |            |          | des terres     |
|          |                |            |          | cuites et ses  |
|          |                |            |          | applications   |
|          |                |            |          | géophysiques.  |
|          |                |            |          | Ann. Inst.     |
|          |                |            |          | Phys. Globe,   |
|          |                |            |          | 16, pp.        |
|          |                |            |          | 157--302       |
+----------+----------------+------------+----------+----------------+
| 76       | Palaeomagnetic | P-Magnet   | 73       | Irving, E.     |
|          | dating         |            |          | (1964).        |
|          |                |            |          | Paleomagnetism |
|          |                |            |          | and its        |
|          |                |            |          | application to |
|          |                |            |          | geological and |
|          |                |            |          | geophysical    |
|          |                |            |          | problems. John |
|          |                |            |          | Wiley & Sons,  |
|          |                |            |          | Inc, New York. |
+----------+----------------+------------+----------+----------------+
| 77       | Palaeosol      | Psol       | 68       | Catt, J. A.    |
|          |                |            |          | (1986). Soils  |
|          |                |            |          | and Quaternary |
|          |                |            |          | geology: a     |
|          |                |            |          | handbook for   |
|          |                |            |          | field          |
|          |                |            |          | scientists.    |
|          |                |            |          | 267 pp.        |
+----------+----------------+------------+----------+----------------+
| 78       | Marker horizon | Marker     | 68       | NULL           |
+----------+----------------+------------+----------+----------------+
| 79       | Fossil         | Fossil     | 78       | NULL           |
|          | assemblage     |            |          |                |
+----------+----------------+------------+----------+----------------+
| 80       | Pollen         | Pollen     | 68       | NULL           |
|          | correlation    |            |          |                |
+----------+----------------+------------+----------+----------------+
| 81       | Top of core    | Core-hi    | 68       | NULL           |
+----------+----------------+------------+----------+----------------+
| 82       | Bottom of core | Core-lo    | 68       | NULL           |
+----------+----------------+------------+----------+----------------+
| 83       | Method         | Combi      | 83       | NULL           |
|          | combination    |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 84       | Statistical    | Stats      | 84       | NULL           |
|          | approach       |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 85       | Estimated      | Estimate   | 84       | NULL           |
+----------+----------------+------------+----------+----------------+
| 86       | Extrapolation  | Extrap     | 84       | NULL           |
+----------+----------------+------------+----------+----------------+
| 87       | Interpolation  | Interp     | 84       | NULL           |
+----------+----------------+------------+----------+----------------+
| 88       | Measurement    | MeasApp    | 88       | NULL           |
|          | technique      |            |          |                |
+----------+----------------+------------+----------+----------------+
| 89       | Liquid         | LSC        | 88       | Birks, J.B.    |
|          | Scintillation  |            |          | (1964). The    |
|          | Counting       |            |          | Theory and     |
|          | (non-specific) |            |          | Practice of    |
|          |                |            |          | Scintillation  |
|          |                |            |          | Counting.      |
|          |                |            |          | Pergammon      |
|          |                |            |          | Press, Oxford, |
|          |                |            |          | UK.            |
+----------+----------------+------------+----------+----------------+
| 90       | Cherenkov      | LSC-C      | 88       | Rengan (1983)  |
|          | Counting       |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 91       | Accelerator    | AMS        | 88       | Fifield (1999) |
|          | Mass           |            |          | [#]_           |
|          | Spectrometry   |            |          |                |
|          | (non-specific) |            |          |                |
+----------+----------------+------------+----------+----------------+
| 92       | SHRIMP         | SHRIMP     | 88       | NULL           |
+----------+----------------+------------+----------+----------------+

Classification and selection of methods on the basis of Geyh (2005), and Walker (2005).

----

..  _crn_alstndID_Fields:

crn_alstndID Fields
~~~~~~~~~~~~~~~~~~~

======== ====== ================== ====== ==========
ALSTNDID ALSTND ALSTND_PUB         ALCORR ALSTNDRTIO
======== ====== ================== ====== ==========
-9999    NA     NA                 0      
1        ZAL94  AL09               0.9134 1.19E-09
2        ZAL94  AL09-Assumed       0.9134 1.19E-09
3        KNSTD  KN-4-2             1      3.096E-11
4        KNSTD  KN-4-2-Assumed     1      3.096E-11
5        KNSTD  KN01-X-Y           1      
6        KNSTD  KN01-X-Y-Assumed   1      
7        KNSTD  KNSTD              1      
8        KNSTD  KNSTD-Assumed      1      
9        KNSTD  KNSTD10650         1      1.065E-11
10       KNSTD  KNSTD10650-Assumed 1      1.065E-11
11       KNSTD  KNSTD30960         1      3.096E-11
12       KNSTD  KNSTD30960-Assumed 1      3.096E-11
13       KNSTD  NBS                1      
14       KNSTD  NBS-Assumed        1      
15       SMAL11 SMAL11             1.021  7.401E-12
16       SMAL11 SMAL11-Assumed     1.021  7.401E-12
17       KNSTD  Z92-0222           1      4.11E-11
18       KNSTD  Z92-0222-Assumed   1      4.11E-11
19       KNSTD  Z93-0221           1      1.68E-11
20       KNSTD  Z93-0221-Assumed   1      1.68E-11
21       ZAL94  ZAL94              0.9134 5.26E-10
22       ZAL94  ZAL94-Assumed      0.9134 5.26E-10
23       ZAL94N ZAL94N             1      4.9E-10
24       ZAL94N ZAL94N-Assumed     1      4.9E-10
25       ND     ND                 0      
======== ====== ================== ====== ==========

Values for crn_alstndID.**"ALSTNDCOMT"** field as follows ...

* IDs 1, 2	-- ETH-Zurich standard, former Cologne standard, equivalent to ZAL94
* IDs 3, 4	-- ANSTO, equivalent to KNSTD
* IDs 5, 6	-- Cologne, equivalent to KNSTD
* IDs 7, 8	-- Nishiizumi, 2004
* IDs 9, 10	-- LLNL-CAMS, equivalent to KNSTD
* IDs 11, 12	-- LLNL-CAMS, PRIME-Lab, equivalent to KNSTD
* IDs 13, 14 -- ASTER in-house standard
* IDs 15, 16	-- PRIME Lab standard, equivalent to KNSTD
* IDs 17, 18	-- PRIME Lab standard, ANSTO, ANSTO-Assumed, equivalent to KNSTD
* IDs 19, 20	-- ETH-Zurich standard used prior to 1 Apr 2010, Kubik and Christl, 2010
* IDs 21, 22 -- ETH-Zurich standard, equivalent to KNSTD, effective 1 Apr 2010, Kubik and Christl, 2010

..  _crn_amsID_Fields:

crn_amsID Fields
~~~~~~~~~~~~~~~~

+-------+------------------------+-----------------------------+
| AMSID | AMS                    | AMSORG                      |
+=======+========================+=============================+
| -9999 | NA                     | not applicable              |
+-------+------------------------+-----------------------------+
| 1     | ANSTO                  | Australian Nuclear Science  |
|       |                        | and Technology Organisation |
|       |                        | ANSTO                       |
+-------+------------------------+-----------------------------+
| 2     | ANSTO-Assumed          | Australian Nuclear Science  |
|       |                        | and Technology Organisation |
|       |                        | ANSTO                       |
+-------+------------------------+-----------------------------+
| 3     | ANU                    | Australian National         |
|       |                        | University ANU              |
+-------+------------------------+-----------------------------+
| 4     | ANU-Assumed            | Australian National         |
|       |                        | University ANU              |
+-------+------------------------+-----------------------------+
| 5     | ASTER                  | Centre for Research and     |
|       |                        | Teaching in Environmental   |
|       |                        | Geoscience CEREGE           |
+-------+------------------------+-----------------------------+
| 6     | ASTER-Assumed          | Centre for Research and     |
|       |                        | Teaching in Environmental   |
|       |                        | Geoscience CEREGE           |
+-------+------------------------+-----------------------------+
| 7     | Cologne                | University of Cologne       |
+-------+------------------------+-----------------------------+
| 8     | Cologne-Assumed        | University of Cologne       |
+-------+------------------------+-----------------------------+
| 9     | DREAMS                 | Helmholtz-Zentrum           |
|       |                        | Dresden-Rossendorf HZDR     |
+-------+------------------------+-----------------------------+
| 10    | DREAMS-Assumed         | Helmholtz-Zentrum           |
|       |                        | Dresden-Rossendorf HZDR     |
+-------+------------------------+-----------------------------+
| 11    | ETH-Zurich             | Swiss Federal Institute of  |
|       |                        | Technology in Zurich        |
|       |                        | ETH-Zurich                  |
+-------+------------------------+-----------------------------+
| 12    | ETH-Zurich-Assumed     | Swiss Federal Institute of  |
|       |                        | Technology in Zurich        |
|       |                        | ETH-Zurich                  |
+-------+------------------------+-----------------------------+
| 13    | Gif-sur-Yvette         | Climate and Environment     |
|       |                        | Sciences Laboratory LSCE,   |
|       |                        | Pierre Simon Laplace        |
|       |                        | Institute                   |
+-------+------------------------+-----------------------------+
| 14    | Gif-sur-Yvette-Assumed | Climate and Environment     |
|       |                        | Sciences Laboratory LSCE,   |
|       |                        | Pierre Simon Laplace        |
|       |                        | Institute                   |
+-------+------------------------+-----------------------------+
| 15    | KIGAM AMS              | Korea Institute of          |
|       |                        | Geoscience and Mineral      |
|       |                        | Resources KIGAM             |
+-------+------------------------+-----------------------------+
| 16    | KIGAM AMS-Assumed      | Korea Institute of          |
|       |                        | Geoscience and Mineral      |
|       |                        | Resources KIGAM             |
+-------+------------------------+-----------------------------+
| 17    | KIST Seoul             | Korea Institute of Science  |
|       |                        | and Technology              |
+-------+------------------------+-----------------------------+
| 18    | KIST Seoul-Assumed     | Korea Institute of Science  |
|       |                        | and Technology              |
+-------+------------------------+-----------------------------+
| 19    | LLNL-CAMS              | Lawrence Livermore National |
|       |                        | Laboratory LLNL, Center for |
|       |                        | Accelerator Mass            |
|       |                        | Spectrometry                |
+-------+------------------------+-----------------------------+
| 20    | LLNL-CAMS-Assumed      | Lawrence Livermore National |
|       |                        | Laboratory LLNL, Center for |
|       |                        | Accelerator Mass            |
|       |                        | Spectrometry                |
+-------+------------------------+-----------------------------+
| 21    | MALT Tokyo AMS         | Micro                       |
|       |                        | Analysis Laboratory, Tandem |
|       |                        | accelerator MALT, The       |
|       |                        | University of Tokyo         |
+-------+------------------------+-----------------------------+
| 22    | MALT Tokyo AMS-Assumed | Micro                       |
|       |                        | Analysis Laboratory, Tandem |
|       |                        | accelerator MALT, The       |
|       |                        | University of Tokyo         |
+-------+------------------------+-----------------------------+
| 23    | PRIME-Lab              | Purdue Rare Isotope         |
|       |                        | Measurement Laboratory      |
|       |                        | PRIME                       |
+-------+------------------------+-----------------------------+
| 24    | PRIME-Lab-Assumed      | Purdue Rare Isotope         |
|       |                        | Measurement Laboratory      |
|       |                        | PRIME                       |
+-------+------------------------+-----------------------------+
| 25    | SUERC                  | Scottish Universities       |
|       |                        | Environmental Research      |
|       |                        | Centre                      |
+-------+------------------------+-----------------------------+
| 26    | SUERC-Assumed          | Scottish Universities       |
|       |                        | Environmental Research      |
|       |                        | Centre                      |
+-------+------------------------+-----------------------------+
| 27    | Uppsala                | Uppsala University, Tandem  |
|       |                        | Laboratory                  |
+-------+------------------------+-----------------------------+
| 28    | Uppsala-Assumed        | Uppsala University, Tandem  |
|       |                        | Laboratory                  |
+-------+------------------------+-----------------------------+
| 29    | XCAMS (GNS)            | Compact AMS, GNS New        |
|       |                        | Zealand                     |
+-------+------------------------+-----------------------------+
| 30    | XCAMS (GNS)-Assumed    | Compact AMS, GNS New        |
|       |                        | Zealand                     |
+-------+------------------------+-----------------------------+
| 31    | XAAMS                  | Xi’an AMS Center, China     |
+-------+------------------------+-----------------------------+
| 32    | XAAMS-Assumed          | Xi’an AMS Center, China     |
+-------+------------------------+-----------------------------+
| 33    | iThemba LABS           | iThemba Laboratory for      |
|       |                        | Accelerator Based Sciences  |
+-------+------------------------+-----------------------------+
| 34    | iThemba LABS-Assumed   | iThemba Laboratory for      |
|       |                        | Accelerator Based Sciences  |
+-------+------------------------+-----------------------------+
| 35    | Tianjin                | Inst. of Surface-Earth      |
|       |                        | System Sci., School of      |
|       |                        | Earth System Sci., Tianjin  |
|       |                        | University (CHN)            |
+-------+------------------------+-----------------------------+
| 36    | Tianjin-Assumed        | Inst. of Surface-Earth      |
|       |                        | System Sci., School of      |
|       |                        | Earth System Sci., Tianjin  |
|       |                        | University (CHN)            |
+-------+------------------------+-----------------------------+

Values for crn_amsID.**"AMSURL"** field as follows ...

* IDs 1, 2	-- https://www.ansto.gov.au/accelerator-mass-spectrometry
* IDs 3, 4	-- https://physics.anu.edu.au/nuclear/research/ams/
* IDs 5, 6	-- https://www.cerege.fr
* IDs 7, 8	-- https://cologneams.uni-koeln.de
* IDs 9, 10	-- https://www.hzdr.de
* IDs 11, 12	-- https://ams.ethz.ch
* IDs 13, 14 -- https://www.lsce.ipsl.fr
* IDs 15, 16	-- https://www.kigam.re.kr
* IDs 17, 18	-- https://eng.kist.re.kr
* IDs 19, 20	-- https://cams.llnl.gov
* IDs 21, 22 -- http://malt.um.u-tokyo.ac.jp
* IDs 23, 24 -- https://www.physics.purdue.edu/primelab/
* IDs 25, 26 -- https://www.gla.ac.uk/research/az/suerc/researchthemes/ams/
* IDs 27, 28 -- https://www.tandemlab.uu.se
* IDs 29, 30 -- https://www.gns.cri.nz
* IDs 31, 32 -- http://www.xaams.cn
* IDs 33, 34 -- https://tlabs.ac.za
* IDs 35, 36 -- http://earth.tju.edu.cn/en/

..  _crn_bestndID_Fields:

crn_bestndID Fields
~~~~~~~~~~~~~~~~~~~

======== ============== ====================== ====== ==========
BESTNDID BESTND         BESTND_PUB             BECORR BESTNDRTIO
======== ============== ====================== ====== ==========
-9999    NA             NA                     0      
1        07KNSTD        07KNSTD                1      
2        07KNSTD        07KNSTD-Assumed        1      
3        07KNSTD        07KNSTD3110            1      2.85E-12
4        07KNSTD        07KNSTD3110-Assumed    1      2.85E-12
5        BEST433        BEST433                0.9124 9.31E-11
6        BEST433        BEST433-Assumed        0.9124 9.31E-11
7        BEST433N       BEST433N               1      8.33E-11
8        BEST433N       BEST433N-Assumed       1      8.33E-11
9        07KNSTD        ICN                    1      
10       07KNSTD        ICN-Assumed            1      
11       07KNSTD        ICN 01-5-2             1      8.558E-12
12       07KNSTD        ICN 01-5-2-Assumed     1      8.558E-12
13       07KNSTD        KN01-6-2               1      5.349E-13
14       07KNSTD        KN01-6-2-Assumed       1      5.349E-13
15       KNSTD          KNSTD                  0.9042 
16       KNSTD          KNSTD-Assumed          0.9042 
17       07KNSTD        KNSTD3110              1      2.85E-12
18       07KNSTD        KNSTD3110-Assumed      1      2.85E-12
19       LLNL1000       LLNL1000               0.9313 1E-12
20       LLNL1000       LLNL1000-Assumed       0.9313 1E-12
21       LLNL10000      LLNL10000              0.9042 1E-11
22       LLNL10000      LLNL10000-Assumed      0.9042 1E-11
23       LLNL300        LLNL300                0.8562 3E-13
24       LLNL300        LLNL300-Assumed        0.8562 3E-13
25       LLNL3000       LLNL3000               0.8644 3E-12
26       LLNL3000       LLNL3000-Assumed       0.8644 3E-12
27       LLNL31000      LLNL31000              0.8761 3.1E-11
28       LLNL31000      LLNL31000-Assumed      0.8761 3.1E-11
29       07KNSTD        NIST SRM-4325          1      2.79E-11
30       07KNSTD        NIST SRM-4325-Assumed  1      2.79E-11
31       07KNSTD        NIST_27900             1      2.79E-11
32       07KNSTD        NIST_27900-Assumed     1      2.79E-11
33       NIST_30000     NIST_30000             0.9313 3E-11
34       NIST_30000     NIST_30000-Assumed     0.9313 3E-11
35       NIST_30200     NIST_30200             0.9251 3.02E-11
36       NIST_30200     NIST_30200-Assumed     0.9251 3.02E-11
37       NIST_30300     NIST_30300             0.9221 3.03E-11
38       NIST_30300     NIST_30300-Assumed     0.9221 3.03E-11
39       NIST_30600     NIST_30600             0.913  3.06E-11
40       NIST_30600     NIST_30600-Assumed     0.913  3.06E-11
41       NIST_Certified NIST_Certified         1.0425 2.68E-11
42       NIST_Certified NIST_Certified-Assumed 1.0425 2.68E-11
43       S2007          S2007                  0.9124 3.08E-11
44       S2007          S2007-Assumed          0.9124 3.08E-11
45       S2007N         S2007N                 1      2.81E-11
46       S2007N         S2007N-Assumed         1      2.81E-11
47       S555           S555                   0.9124 9.55E-11
48       S555           S555-Assumed           0.9124 9.55E-11
49       S555N          S555N                  1      8.71E-11
50       S555N          S555N-Assumed          1      8.71E-11
51       07KNSTD        SMD-Be-12              1      1.704E-12
52       07KNSTD        SMD-Be-12-Assumed      1      1.704E-12
53       07KNSTD        SRM KN-5-2             1      8.558E-12
54       07KNSTD        SRM KN-5-2-Assumed     1      8.558E-12
55       07KNSTD        STD-11                 1      1.191E-11
56       07KNSTD        STD-11-Assumed         1      1.191E-11
57       NIST_30500     NIST_30500             0.9124 3.05E-11
58       NIST_30500     NIST_30500-Assumed     0.9124 3.05E-11
59       ND             ND                     0      
======== ============== ====================== ====== ==========

Values for crn_bestndID.**"BESTNDCOMT"** as follows ...

* IDs 1, 2	-- Nishiizumi et al, 2007 (NIM-B v. 258, p. 403)
* IDs 3, 4	-- Standard used at PRIME, equivalent to 07KNSTD
* IDs 5, 6	-- ETH-Zurich standard used prior to 1 Apr 2010, Kubik and Christl, 2010
* IDs 7, 8	-- ETH-Zurich standard, equivalent to 07KNSTD, effective 1 Apr 2010, Kubik and Christl, 2010
* IDs 9, 10	-- S130 and S142, Nishiizumi e al., 2007, equivalent to 07KNSTD
* IDs 11, 12	-- S145, Nishiizumi e al., 2007, equivalent to 07KNSTD
* IDs 13, 14 -- S109, Nishiizumi e al., 2007, measured in Cologne, equivalent to 07KNSTD
* IDs 15, 16	-- Nishiizumi standards assuming old 10Be half life
* IDs 17, 18	-- S154, primary LLNL standard (01-5-4), Rood et al., 2013
* IDs 19, 20	-- LLNL-CAMS in-house standard, cf. Balco, 2016
* IDs 21, 22 -- LLNL-CAMS in-house standard, cf. Balco, 2016
* IDs 23, 24 -- LLNL-CAMS in-house standard, cf. Balco, 2016
* IDs 25, 26 -- LLNL-CAMS in-house standard, cf. Balco, 2016
* IDs 27, 28 -- LLNL-CAMS in-house standard, cf. Balco, 2016
* IDs 29, 30 -- equivalent to 07KNSTD
* IDs 31, 32 -- NIST SRM-4325, but with differing assumed isotope ratio, equivalent to 07KNSTD
* IDs 33, 34 -- NIST SRM-4325, but with differing assumed isotope ratio
* IDs 35, 36 -- NIST SRM-4325, but with differing assumed isotope ratio
* IDs 37, 38 -- NIST SRM-4325, but with differing assumed isotope ratio
* IDs 39, 40 -- NIST SRM-4325, but with differing assumed isotope ratio
* IDs 41, 42 -- used at PRIME Lab prior to 12 Jan 2005, cf. Balco 2016
* IDs 43, 44 -- ETH-Zurich standard used prior to 1 Apr 2010, Kubik and Christl, 2010
* IDs 45, 46 -- ETH-Zurich standard, equivalent to 07KNSTD, effective 1 Apr 2010, Kubik and Christl, 2010
* IDs 47, 48 -- ETH-Zurich standard used prior to 1 Apr 2010, Kubik and Christl, 2010
* IDs 49, 50 -- ETH-Zurich standard, equivalent to 07KNSTD, effective 1 Apr 2010, Kubik and Christl, 2010
* IDs 51, 52 -- S225, DREAMS, equivalent to 07KNSTD
* IDs 53, 54 -- various ANSTO runs, equivalent to 07KNSTD
* IDs 55, 56 -- ASTER standard, equivalent to NIST_27900 and 07KNSTD
* IDs 57, 58 -- NIST SRM-4325, but with differing assumed isotope ratio

----

..  _arch_featdatedID_Fields:

arch_featdatedID Fields
~~~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ========================
FEATDATEID FEATDATED
========== ========================
-9999      no data
1          Hearth
2          Burial (animal)
3          Burial (human)
4          Mud wasp nest
5          Rock art
9          Other
999        not related to a feature
========== ========================

..  _c13_valID_Fields:

c13_valID Fields
~~~~~~~~~~~~~~~~

``Draft`` -- 

========= ========================
C13_VALID C13_VAL
========= ========================
-9999     no data
1         Measured by AMS
2         Measured by IRMS or CRDS
3         Assumed
========= ========================

..  _c14_contamID_Fields:

c14_contamID Fields
~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

======== =======================
CONTAMID CONTAM
======== =======================
-9999    ND
1        Glue
2        Conservative
3        Rootlets
4        Sediment
5        Recrystallised material
9        Other
======== =======================

..  _c14_hum_modID_Fields:

c14_hum_modID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========= ==============
HUM_MODID HUM_MOD
========= ==============
-9999     ND
1         Yes
2         No
10        Artefact
11        Cut marked
19        Other
100       Bead
101       String
102       Boomerang
103       Point
104       Hook
109       Other artefact
========= ==============

..  _c14_materia1ID_Fields:

c14_materia1ID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== =================== ==========
MATERIA1ID MATERIAL1           MATERIA1AB
========== =================== ==========
-9999      no data             ND
1          Biogenic Carbonate  CarbBio
2          Inorganic Carbonate CarbInorg
3          Charred Plant       Charred
4          Faunal              Faunal
5          Oxalate             Oxalate
6          Paint               Paint
7          Plant               Plant
8          Sediment            Sediment
9          Other               Other
10         Mix of materials    Bulk
========== =================== ==========

..  _c14_materia2ID_Fields:

c14_materia2ID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ======================
MATERIA2ID MATERIAL2
========== ======================
29         Bulk
1          Bark
2          Beeswax
3          Binder
4          Bone
5          Calcined bone
6          Calcium soil carbonate
7          Celtis seed
8          Coral
9          Dentine
10         Egg shell
11         Enamel
12         Foraminifera
13         Freshwater shell
14         Hair
15         Marine shell
16         Nut
17         Otolith
18         Peat
19         Pigment
20         Pollen
21         Resin
22         Seed
23         Speleothem
24         Terrestrial snail
25         Tooth dentine
26         Tooth enamel
27         Tufa
28         Wood
99         Other
-9999      ND
========== ======================

..  _c14_solvent2ID_Fields:

c14_solvent2ID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ========================= ==========
SOLVENT2ID SOLVENT2                  SOLVENT2AB
========== ========================= ==========
-9999      no data                   ND
1          Methanol                  Met
2          Ethanol                   Eth
3          Chloroform                Chl
4          Dichloromethane           Dic
5          Toluene                   Tol
6          Hexane                    Hex
7          Chloroform: Methanol      Chl:Met
8          Dichloromethane: Methanol Dic:Met
9          Other                     Other
========== ========================= ==========

..  _c_mtdID_Fields:

c_mtdID Fields
~~~~~~~~~~~~~~

``Draft`` -- 

======= ==================== =======
C_MTDID C_MTD                C_MTDAB
======= ==================== =======
-9999   ND                   ND
1       IR mass spectrometry IRMS
2       Elemental analyser   Elemt
3       CRD spectroscopy     CRDS
4       Volumetric           Vol
5       Other                Other
======= ==================== =======

----

..  _sed_depconID_Fields:

sed_depconID Fields
~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

======== ==========================
DEPCONID DEPCON
======== ==========================
-9999    ND
1        Isolated dune
2        Dunefield
3        Aeolian cap on beach ridge
4        Sandsheet
5        Coastal shoreline
======== ==========================

..  _sed_faciesID_Fields:

sed_faciesID Fields
~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

======== ================================
FACIESID FACIES
======== ================================
-9999    ND
1        Channel
2        Overbank
3        Beach / Shoreline
4        Deep-water lacustrine
5        Shallow-water lacustrine
6        Near-shore lacustrine
7        Lacustrine (water depth unclear)
8        Playa
9        Calcareous deposits
======== ================================

..  _sed_geommodID_Fields:

sed_geommodID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========= ================================
GEOMMODID GEOMMOD
========= ================================
-9999     ND
0         No modifier, i.e., 'normal' dune
1         Lacustrine source bordering
2         Lakefloor
3         Fluvial source bordering
4         Obstacle
5         Coastal
6         Blowout
========= ================================

..  _sed_geotypeID_Fields:

sed_geotypeID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========= ===================
GEOTYPEID GEOTYPE
========= ===================
-9999     ND
1         Terrace
2         Floodplain
3         Alluvial fan
4         Bench
5         Island
6         Slack water deposit
7         Levee
8         Dune
9         Sandsheet
10        Beach / Shoreline
11        Nearshore deposit
12        Lake floor
13        Lakeshore terrace
14        Deflated cliff
15        Bar
========= ===================

..  _sed_laketypeID_Fields:

sed_laketypeID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ================================ ========
LAKETYPEID LAKETYPE                         PARENTID
========== ================================ ========
-9999      ND                               -9999
1          Tectonic lake                    11
2          Landslide lake                   11
3          Crater lake (volcanic)           15
4          Oxbow lake                       31
5          Playa lake                       11
6          Fen                              50
7          Swamp                            50
8          Lagoon                           11
9          Lake (unknown origin)            10
10         Lake (non-specific)              10
11         Natural lake                     10
12         Natural lake (unknown origin)    11
13         Artificial lake                  10
14         Artificial lake (unknown origin) 13
15         Volcanic lake                    11
16         Caldera lake                     15
17         Lava flow dammed lake            15
18         Glacial lake                     11
19         Glacial meltwater channel lake   18
20         Glacial scour lake               18
21         Kettle lake                      18
22         Cirque lake                      18
23         Proglacial lake                  18
24         Subglacial lake                  18
25         Finger lake                      18
26         Valley glacier lake              18
27         Glacial outburst flood lake      18
28         Ice thrust lake                  18
29         Moraine dammed lake              18
30         Drift filled valley lake         18
31         Fluvial lake                     11
32         Meander lake                     31
33         Fluviatile dam lake              31
34         Lateral lake                     31
35         Floodplain lake                  31
36         Plunge pool lake                 31
37         Alluvial fan dammed lake         31
38         Flood scour lake                 31
39         Fluvial terrace lake             31
40         Drained lake                     11
41         Backwater lake                   31
42         Solution lake                    11
43         Karst pond                       42
44         Underground lake                 42
45         Aeolian lake                     11
46         Deflation basin lake             45
47         Dune dammed lake                 45
48         Interdunal lake                  45
49         Shoreline lake                   11
50         Organic lake                     11
51         Lake marginal fen                50
52         Anthropogenic lake               13
53         Reservoir                        13
54         Meteorite impact lake            11
55         Peat lake                        50
56         Periglacial lake                 11
57         Thermokarst lake                 56
========== ================================ ========

..  _sed_morphID_Fields:

sed_morphID Fields
~~~~~~~~~~~~~~~~~~

``Draft`` -- 

======= ====================
MORPHID MORPH
======= ====================
-9999   ND
0       no modifier
1       Climbing
2       Falling
3       Foredune
4       Longitudinal
5       Lunette
6       Nebkha
7       Network
8       Parabolic
9       Sand sheet
10      Transverse
11      Transverse shoreline
======= ====================

..  _sed_sitetypeID_Fields:

sed_sitetypeID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ==============================
SITETYPEID SITETYPE
========== ==============================
-9999      ND
1          Outcrop
2          Core
3          Auger hole
4          Pit or Quarry
5          Artificial excavation (trench)
========== ==============================

----

..  _fos_chemtypeID_Fields:

fos_chemtypeID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ====================================== ==============
CHEMTYPEID CHEMTYPE                               CHEMTYPEAB
========== ====================================== ==============
-9999      no data                                ND
-9991      not applicable                         NA
1          Acid-alkali-acid and decalcification   AAA_decal
2          ABA_BC technique                       ABA-BC
3          Acid-base-oxidation stepped combustion ABOx-SC
4          Acetic acid treatment                  Acetic
5          Alkali wash                            Alkali_wash
6          Etching                                Etch
7          Filtration                             Filtration
8          Gelatinisation                         Gelatinisation
9          Hydrochloric acid etching              HCl_etch
10         Hydrocloric acid wash                  HCl_wash
11         Treatment with HCl and NaOH            HCl,NaOH
12         Leaching                               Leach
13         Boiling in saturated NaCl solution     NaCl_boil
14         no treatment                           No
15         not reported                           Not_rep
16         Ultrafiltration                        Ultra
17         Wash                                   Wash
18         for other treatment (see attachment)   Other
========== ====================================== ==============


..  _fos_fosmat1ID_Fields:

fos_fosmat1ID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========= ======================================== ============
FOSMAT1ID FOSMAT1                                  FOSMAT1ABB
========= ======================================== ============
-9999     no data                                  ND
-9991     not applicable                           NA
1         Bone                                     Bone
2         Bulk bone                                Bone_bulk
3         Multiple bones                           Bone_mult
4         Calcite filling in bone                  Calc_bone
5         Calcite straw (reworked in bone breccia) Calc_straw
6         Calcite within tooth                     Calc_tooth
7         Carcass remains                          Carcass
8         Calcite cement                           Cement
9         Charcoal                                 Charcoal
10        Diprotodon crop content                  Dipto_crop
11        Eggshell                                 Eggshell
12        Fireplace                                Fireplace
13        Fish otolith                             Fish_olth
14        Flowstone                                Flow
15        Flowstone (oldest)                       Flow_old
16        Flowstone straw                          Flow_straw
17        Flowstone (youngest)                     Flow_young
18        Gut content                              Gut
19        Sarcophilus hair                         Hair_sarco
20        Midden                                   Midden
21        Carbonate nodule                         Nodule
22        Plant remains                            Plant
23        Post-depositional formation              Post-deposit
24        Sediment                                 Sed
25        Shell                                    Shell
26        Marine shell                             Shell_mare
27        Skull                                    Skull
28        Skull (dentary)                          Skull_dnty
29        Skull (maxilla)                          Skull_max
30        Snail shell                              Snail
31        Speleothem                               Speleo
32        Coralline speleothem                     Speleo_coral
33        Tooth                                    Tooth
34        Wood                                     Wood
35        for other                                Other
========= ======================================== ============


..  _fos_fosmat2ID_Fields:

fos_fosmat2ID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

========= ================================= =================
FOSMAT2ID FOSMAT2                           FOSMAT2ABB
========= ================================= =================
-9999     no data                           ND
-9991     not applicable                    NA
1         Apatite                           Apatite
2         Bone                              Bone
3         Multiple bones                    Bone_mult
4         Burnt bone                        Bone_burnt
5         Calcite                           Calcite
6         Carbonate                         Carb
7         Charcoal                          Charcoal
8         Cellulose                         Cellulose
9         Collagen                          Collagen
10        Dentine                           Dentine
11        Dentine/Enamel                    Dentine/Enamel
12        Eggshell                          Eggshell
13        Enamel                            Enamel
14        Flesh                             Flesh
15        Gelatine extract                  Gelatine_extr
16        Gelatine fraction                 Gelatine_frac
17        Hair                              Hair
18        Acid and alkali insoluble residue Insoble
19        Acid insoluble fraction           Insoble_acid_frac
20        Acid insoluble residue            Insoble_acid_res
21        Molar                             Molar
22        Organic band                      Organic_layer
23        Organic carbon residue            Organic_carb
24        Organic fraction                  Organic_frac
25        Organic material                  Organic_mat
26        Otolith                           Otolith
27        Peat                              Peat
28        Carbonaceous pellet               Pellet_carb
29        Leaf, seed and stem fragments     Plant
30        Quartz                            Quartz
31        Celtis seed                       Seed_celtis
32        Shell                             Shell
33        Shell (Velesunio ambiguous)       Shell_veles
34        Bulk soil organics                Soil
35        Marine shell                      Shell_mare
36        Speleothem                        Speleo
37        Straw stalactite                  Stalactite
38        Tooth                             Tooth
39        Tooth from breccia                Tooth_breccia
40        Wood                              Wood
41        Burnt wood                        Wood_burnt
42        Carbonised wood                   Wood_carb
43        for other                         Other
44        Charcoal (assumed)                Charcoal?
45        Sediment                          Sed
========= ================================= =================


..  _fos_mtdsID_Fields:

fos_mtdsID Fields
~~~~~~~~~~~~~~~~~

``Draft`` -- 

========== ============================================ ==========
FOS_MTDSID FOS_MTDSUB                                   FOS_MTDSAB
========== ============================================ ==========
-9999      ND                                           ND
-9991      NA                                           NA
1          Accelerator Mass Spectroscopy                AMS
2          C13 adjusted                                 C13_adj
3          Early uptake ESR                             EU
4          Inductively Coupled Plasma Mass Spectrometry ICP-MS
5          Linear uptake ESR                            LU
6          Multicollector ICP-MS                        MC-ICP-MS
7          Thermal Ionization Mass Spectrometry         TIMS
8          Thermally-transferred                        TT
========== ============================================ ==========


.. rubric:: Footnotes

.. [#] Global Palaeofire Database (`https://www.paleofire.org <https://www.paleofire.org>`_)
.. [#] Entry type descriptions taken from `http://newton.ex.ac.uk/tex/pack/bibtex/btxdoc/ <http://newton.ex.ac.uk/tex/pack/bibtex/btxdoc/>`_
.. [#] Anderson, Libby, Weinhouse, Reid, Kirshenbaum & Grosse (1947) DOI: `10.1103/PhysRev.72.931 <https://doi.org/10.1103/PhysRev.72.931>`_
.. [#] Dorn (1983) DOI: `10.1016/0033-5894(83)90065-0 <https://doi.org/10.1016/0033-5894(83)90065-0>`_
.. [#] Frink (1996) DOI: `10.2136/sssaspecpub44.c6 <https://doi.org/10.2136/sssaspecpub44.c6>`_
.. [#] Huntley, Godfrey-Smith & Thewalt (1985) DOI: `10.1038/313105a0 <https://doi.org/10.1038/313105a0>`_
.. [#] Daniels, Boyd & Saunders (1953) DOI: `10.1126/science.117.3040.343 <https://doi.org/10.1126/science.117.3040.343>`_
.. [#] Kaufmann & Libby (1954) DOI: `10.1103/PhysRev.93.1337 <https://doi.org/10.1103/PhysRev.93.1337>`_
.. [#] Arnold (1956) DOI: `10.1126/science.124.3222.584 <https://doi.org/10.1126/science.124.3222.584>`_
.. [#] Lal, Goldberg & Koide (1960) DOI: `10.1126/science.131.3397.332 <https://doi.org/10.1126/science.131.3397.332>`_
.. [#] Davis & Schaeffer (1955) DOI: `10.1111/j.1749-6632.1955.tb35368.x <https://doi.org/10.1111/j.1749-6632.1955.tb35368.x>`_
.. [#] Loosli & Oeschger (1968) DOI: `10.1016/S0012-821X(68)80039-1 <https://doi.org/10.1016/S0012-821X(68)80039-1>`_
.. [#] Raisbeck & Yiou (1979) DOI: `10.1038/277042a0 <https://doi.org/10.1038/277042a0>`_
.. [#] Wilkinson & Sheline (1955) DOI: `10.1103/PhysRev.99.752 <https://doi.org/10.1103/PhysRev.99.752>`_
.. [#] Marti (1967) DOI: `10.1103/PhysRevLett.18.264 <https://doi.org/10.1103/PhysRevLett.18.264>`_
.. [#] Takagi, Hampel & Kirsten (1974) DOI: `10.1016/0012-821X(74)90019-3 <https://doi.org/10.1016/0012-821X(74)90019-3>`_
.. [#] Smits & Gentner (1950) DOI: `10.1016/0016-7037(50)90005-6 <https://doi.org/10.1016/0016-7037(50)90005-6>`_
.. [#] Hahn, Strassmann & Walling (1937) DOI: `10.1007/BF01492269 <https://doi.org/10.1007/BF01492269>`_
.. [#] Herr, Merz, Eberhardt & Signer (1958) DOI: `10.1515/zna-1958-0404 <https://doi.org/10.1515/zna-1958-0404>`_
.. [#] Herr & Merz (1955) DOI: `10.1515/zna-1955-0804 <https://doi.org/10.1515/zna-1955-0804>`_
.. [#] Holmes (1911) DOI: `10.1098/rspa.1911.0036 <https://doi.org/10.1098/rspa.1911.0036>`_
.. [#] Williams (1995) DOI: `10.1007/BF00768738 <https://doi.org/10.1007/BF00768738>`_
.. [#] Barnes, Lang & Potratz (1956) DOI: `10.1126/science.124.3213.175.b <https://doi.org/10.1126/science.124.3213.175.b>`_
.. [#] Thurber (1962) DOI: `10.1029/JZ067i011p04518 <https://doi.org/10.1029/JZ067i011p04518>`_
.. [#] Prasad, Poolton, Kook & Jain (2017) DOI: `10.1038/s41598-017-10174-8 <https://doi.org/10.1038/s41598-017-10174-8>`_
.. [#] Trautmann, Krbetschek, Dietrich & Stolz (1998) DOI: `10.1016/S1350-4487(98)00012-2 <https://doi.org/10.1016/S1350-4487(98)00012-2>`_
.. [#] Hütt, Jaek & Tchonka (1988) DOI: `10.1016/0277-3791(88)90033-9 <https://doi.org/10.1016/0277-3791(88)90033-9>`_
.. [#] Huang & Walker (1967) DOI: `10.1126/science.155.3766.1103 <https://doi.org/10.1126/science.155.3766.1103>`_
.. [#] Fanale & Schaeffer (1965) DOI: `10.1126/science.149.3681.312 <https://doi.org/10.1126/science.149.3681.312>`_
.. [#] Price & Walker (1962) DOI: `10.1038/196732a0 <https://doi.org/10.1038/196732a0>`_
.. [#] Friedman & Smith (1960) DOI: `10.2307/276634 <https://doi.org/10.2307/276634>`_
.. [#] Emiliani (1954) DOI: `10.1126/science.119.3103.853 <https://doi.org/10.1126/science.119.3103.853>`_
.. [#] Harold (1960) DOI: `10.1111/j.1475-4754.1960.tb00518.x <https://doi.org/10.1111/j.1475-4754.1960.tb00518.x>`_
.. [#] Rengan (1983) DOI: `10.1021%2Fed060p682 <https://doi.org/10.1021%2Fed060p682>`_
.. [#] Fifield (1999) DOI: `10.1088/0034-4885/62/8/202 <https://doi.org/10.1088/0034-4885/62/8/202>`_
