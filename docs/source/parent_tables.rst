============================
Parent table fields & values
============================


..  _global_parent_tables:

Global parent tables
--------------------

..  _global_GrainSize_Fields:

global_GrainSize fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_GrainSize_FIELDS.csv
   :header-rows: 1

| The unit for both fields "GRNSIZEMIN" and "GRNSIZEMAX" is *mm*.
| The latest *global_GrainSize* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_GrainSize__202305230906.csv>`_ |:chipmunk:|

..  _global_SiteCode_Fields:

global_SiteCode fields
~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_SiteCode_FIELDS.csv
   :header-rows: 1

| The latest *global_SiteCode* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_SiteCode__202305230906.csv>`_ |:chipmunk:|

.. note::

   The dominant attribute of a site will override any other. So, for example, burials in a rockshelter with lots of occupation deposit would be classified as a Rockshelter, not a Cemetery.

..  _global_biomeID_Fields:

global_biomeID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_biomeID_FIELDS.csv
   :header-rows: 1

| Classification of biomes on the basis of Prentice et al. (1992), Forseth (2010), and GPD [#]_.
| The latest *global_biomeID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_biomeID__202305230906.csv>`_ |:chipmunk:|

..  _global_ibraID_Fields:

global_ibraID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_ibraID_FIELDS_trunc.csv
   :header-rows: 1

| The latest full *global_ibraID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_ibraID__202305221532.csv>`_ |:chipmunk:|
| Detailed information about Australia's bioregions classification rationale and model can be found at `https://www.dcceew.gov.au/environment/land/nrs/science/ibra <https://www.dcceew.gov.au/environment/land/nrs/science/ibra>`_.

.. important::

   The *global_ibraID* table only applies to samples from Australia.

..  _global_rivID_Fields:

global_rivID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_rivID_FIELDS_trunc.csv
   :header-rows: 1

| The latest full *global_rivID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_rivID__202305221533.csv>`_ |:chipmunk:|
| Detailed information about the Australian Hydrological Geospatial Fabric (Geofabric) classification rationale and model can be found at  `http://www.bom.gov.au/water/geofabric/ <http://www.bom.gov.au/water/geofabric/>`_.

.. important::

   The *global_rivID* table only applies to samples from Australia.

..  _global_varunitID_Fields:

global_varunitID fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_varunitID_FIELDS.csv
   :header-rows: 1

| The latest *global_varunitID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_varunitID__202305230906.csv>`_ |:chipmunk:|


..  _global_RefCore_Fields:

global_RefCore fields
~~~~~~~~~~~~~~~~~~~~~

| The latest *global_RefCore* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_RefCore__202305230906.csv>`_ |:chipmunk:|


..  _global_RefAbstract_Fields:

global_RefAbstract fields
~~~~~~~~~~~~~~~~~~~~~

| The latest *global_RefAbstract* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_RefAbstract__202305230906.csv>`_ |:chipmunk:|


..  _global_Author_Fields:

global_Author fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_Author_FIELDS_trunc.csv
   :header-rows: 1

| The latest *global_Author* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_Author__202305230906.csv>`_ |:chipmunk:|

..  _global_Journal_Fields:

global_Journal fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_Journal_FIELDS_trunc.csv
   :header-rows: 1

| The latest *global_Journal* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_Journal__202305230906.csv>`_ |:chipmunk:|

..  _global_PubType_Fields:

global_PubType fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/global_PubType_FIELDS.csv
   :header-rows: 1

* **article** [#]_ -- An article from a journal or magazine. *Required fields*: author, title, journal, year. *Optional fields*: volume, number, pages, month, note.

* **book** -- A book with an explicit publisher. *Required fields*: author or editor, title, publisher, year. *Optional fields*: volume or number, series, address, edition, month, note.

* **booklet** -- A work that is printed and bound, but without a named publisher or sponsoring institution. *Required field*: title. *Optional fields*: author, howpublished, address, month, year, note.

* **conference** -- The same as inproceedings, included for Scribe compatibility.

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

The latest *global_PubType* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_PubType__202305230906.csv>`_ |:chipmunk:|

----

..  _regional_parent_tables:

Regional parent tables
----------------------

..  _cabah_LabCodes_Fields:

cabah_LabCodes fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/cabah_LabCodes_FIELDS_trunc.csv
   :header-rows: 1

The latest *cabah_LabCodes* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_global_PubType__202305230906.csv>`_ |:chipmunk:|

..  _cabah_chemprepID_Fields:

cabah_chemprepID fields
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

The latest *cabah_chemprepID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_cabah_chemprepID__202305230904.csv>`_ |:chipmunk:|

..  _cabah_col_mtdID_Fields:

cabah_col_mtdID fields
~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/cabah_col_mtdID_FIELDS.csv
   :header-rows: 1

The latest *cabah_col_mtdID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_cabah_col_mtdID__202305230904.csv>`_ |:chipmunk:|

..  _cabah_methodID_Fields:

cabah_methodID fields
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

| Classification and selection of methods on the basis of Geyh (2005), and Walker (2005).
| The latest *cabah_methodID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_cabah_methodID__202305230904.csv>`_ |:chipmunk:|


----


..  _local_parent_tables:

Local parent tables
-------------------

..  _crn_alstndID_Fields:

crn_alstndID fields
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

Values for crn_alstndID."ALSTNDCOMT" field as follows ...

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

| The latest *crn_alstndID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_crn_alstndID__202305230906.csv>`_ |:chipmunk:|

..  _crn_amsID_Fields:

crn_amsID fields
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

Values for crn_amsID."AMSURL" field as follows ...

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

| The latest *crn_amsID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_crn_amsID__202305230906.csv>`_ |:chipmunk:|

..  _crn_projepsgID_Fields:

crn_projepsgID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/crn_projepsgID_FIELDS_trunc.csv
   :header-rows: 1

The latest full *crn_projepsgID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_crn_projepsgID__202305221534.csv>`_ |:chipmunk:|

..  _crn_bestndID_Fields:

crn_bestndID fields
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

Values for crn_bestndID."BESTNDCOMT" as follows ...

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

The latest full *crn_bestndID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_crn_bestndID__202305230906.csv>`_ |:chipmunk:|

----

..  _arch_featdatedID_Fields:

arch_featdatedID fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/arch_featdatedID_FIELDS.csv
   :header-rows: 1

The latest *arch_featdatedID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_arch_featdatedID__202305230904.csv>`_ |:chipmunk:|

..  _c13_valID_Fields:

c13_valID fields
~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c13_valID_FIELDS.csv
   :header-rows: 1

The latest *c13_valID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_c13_valID__202305230904.csv>`_ |:chipmunk:|

..  _c14_contamID_Fields:

c14_contamID fields
~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c14_contamID_FIELDS.csv
   :header-rows: 1

The latest *c14_contamID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_c14_contamID__202305230904.csv>`_ |:chipmunk:|

..  _c14_hum_modID_Fields:

c14_hum_modID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c14_hum_modID_FIELDS.csv
   :header-rows: 1

..  _c14_materia1ID_Fields:

c14_materia1ID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c14_materia1ID_FIELDS.csv
   :header-rows: 1

..  _c14_materia2ID_Fields:

c14_materia2ID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c14_materia2ID_FIELDS.csv
   :header-rows: 1

The latest *c14_materia2ID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_c14_materia2ID__202305230904.csv>`_ |:chipmunk:|

..  _c14_solvent2ID_Fields:

c14_solvent2ID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c14_solvent2ID_FIELDS.csv
   :header-rows: 1

..  _c_mtdID_Fields:

c_mtdID fields
~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/c_mtdID_FIELDS.csv
   :header-rows: 1

----

..  _osl-tl_agemodelID_Fields:

osl-tl_agemodelID fields
~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/osl-tl_agemodelID_FIELDS.csv
   :header-rows: 1

The latest *osl-tl_agemodelID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_osl_tl_agemodelID__202305230906.csv>`_ |:chipmunk:|

..  _osl-tl_ed_procID_Fields:

osl-tl_ed_procID fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/osl-tl_ed_procID_FIELDS.csv
   :header-rows: 1

..  _osl-tl_lum_matID_Fields:

osl-tl_lum_matID fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/osl-tl_lum_matID_FIELDS.csv
   :header-rows: 1

..  _osl-tl_mineralID_Fields:

osl-tl_mineralID fields
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/osl-tl_mineralID_FIELDS.csv
   :header-rows: 1

..  _osl-tl_mtdID_Fields:

osl-tl_mtdID fields
~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/osl-tl_mtdID_FIELDS.csv
   :header-rows: 1

The latest *osl-tl_mtdID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_osl_tl_mtdID__202305230906.csv>`_ |:chipmunk:|

..  _osl_typeID_Fields:

osl_typeID fields
~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/osl_typeID_FIELDS.csv
   :header-rows: 1

----

..  _sed_depconID_Fields:

sed_depconID fields
~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_depconID_FIELDS.csv
   :header-rows: 1

..  _sed_faciesID_Fields:

sed_faciesID fields
~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_faciesID_FIELDS.csv
   :header-rows: 1

..  _sed_geommodID_Fields:

sed_geommodID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_geommodID_FIELDS.csv
   :header-rows: 1

..  _sed_geotypeID_Fields:

sed_geotypeID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_geotypeID_FIELDS.csv
   :header-rows: 1

..  _sed_laketypeID_Fields:

sed_laketypeID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_laketypeID_FIELDS.csv
   :header-rows: 1

| The latest *sed_laketypeID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_sed_laketypeID__202305230906.csv>`_ |:chipmunk:|

..  _sed_morphID_Fields:

sed_morphID fields
~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_morphID_FIELDS.csv
   :header-rows: 1

..  _sed_sitetypeID_Fields:

sed_sitetypeID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/sed_sitetypeID_FIELDS.csv
   :header-rows: 1

----

..  _fos_TaxRank1_classID_Fields:

fos_TaxRank1_classID fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_TaxRank1_classID_FIELDS.csv
   :header-rows: 1


..  _fos_TaxRank2_infraclaID_Fields:

fos_TaxRank2_infraclaID fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_TaxRank2_infraclaID_FIELDS_trunc.csv
   :header-rows: 1

The latest full *fos_TaxRank2_infraclaID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_TaxRank2_infraclaID__202305221536.csv>`_ |:chipmunk:|


..  _fos_TaxRank3_ordrID_Fields:

fos_TaxRank3_ordrID fields
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_TaxRank3_ordrID_FIELDS_trunc.csv
   :header-rows: 1

The latest full *fos_TaxRank3_ordrID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_TaxRank3_ordrID__202305221536.csv>`_ |:chipmunk:|


..  _fos_TaxRank4_familyID_Fields:

fos_TaxRank4_familyID fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_TaxRank4_familyID_FIELDS_trunc.csv
   :header-rows: 1

The latest full *fos_TaxRank4_familyID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_TaxRank4_familyID__202305221535.csv>`_ |:chipmunk:|


..  _fos_TaxRank5_genusID_Fields:

fos_TaxRank5_genusID fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_TaxRank5_genusID_FIELDS_trunc.csv
   :header-rows: 1

The latest full *fos_TaxRank5_genusID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_TaxRank5_genusID__202305221535.csv>`_ |:chipmunk:|


..  _fos_TaxRank6_speciesID_Fields:

fos_TaxRank6_speciesID fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_TaxRank6_speciesID_FIELDS_trunc.csv
   :header-rows: 1

The latest full *fos_TaxRank6_speciesID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_TaxRank6_speciesID__202305221535.csv>`_ |:chipmunk:|


..  _fos_chemtypeID_Fields:

fos_chemtypeID fields
~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_chemtypeID_FIELDS.csv
   :header-rows: 1

The latest full *fos_chemtypeID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_chemtypeID__202305230906.csv>`_ |:chipmunk:|

..  _fos_fosmat1ID_Fields:

fos_fosmat1ID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_fosmat1ID_FIELDS.csv
   :header-rows: 1

The latest full *fos_fosmat1ID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_fosmat1ID__202305230906.csv>`_ |:chipmunk:|

..  _fos_fosmat2ID_Fields:

fos_fosmat2ID fields
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_fosmat2ID_FIELDS.csv
   :header-rows: 1

The latest full *fos_fosmat2ID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_fosmat2ID__202305230906.csv>`_ |:chipmunk:|

..  _fos_mtdsID_Fields:

fos_mtdsID fields
~~~~~~~~~~~~~~~~~

.. csv-table::
   :file: ./csv_tables/fos_mtdsID_FIELDS.csv
   :header-rows: 1

The latest full *fos_mtdsID* table version can be downloaded `here <https://github.com/hmunack/OCTOPUS/blob/main/docs/source/storage/_fos_mtdsID__202305230906.csv>`_ |:chipmunk:|

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
