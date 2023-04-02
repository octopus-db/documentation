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

========= ============================= ========== ========== ==========
GRNSIZEID GRNSIZE                       GRNSIZEABB GRNSIZEMIN GRNSIZEMAX
========= ============================= ========== ========== ==========
-9999     ND                            ND                    
1         Sand                          Sa         0.063      2
2         Silt                          Si         0.002      0.063
3         Clay                          Cl                    0.002
4         Large boulder                 LBo        630        
5         Boulder                       Bo         200        630
6         Cobble                        Co         63         200
7         Gravel                        Gr         2          63
12        Silty Sand                    SiSa       0.002      2
13        Clayey Sand                   ClSa                  2
14        Mix of Sand and Large boulder SaLBo      0.063      
15        Mix of Sand and Boulder       SaBo       0.063      630
16        Mix of Sand and Cobble        SaCo       0.063      200
17        Mix of Sand and Gravel        SaGr       0.063      63
21        Coarse silt                   CSi        0.02       0.063
22        Medium silt                   MSi        0.0063     0.02
23        Fine silt                     FSi        0.002      0.0063
31        Coarse sand                   CSa        0.63       2
32        Medium sand                   MSa        0.2        0.63
33        Fine sand                     FSa        0.063      0.2
50        Pebble                        Pe         4          64
56        Mix of Boulders and Cobbles   BoCo       63         630
65        Mix of Cobbles and Boulders   CoBo       63         630
71        Coarse gravel                 CGr        20         63
72        Medium gravel                 MGr        6.3        20
73        Fine gravel                   FGr        2          6.3
80        Sediment (unspecified)        Sed                   
81        Loam                          Lo                    2
100       Bedrock                       Bed                   
========= ============================= ========== ========== ==========

* -- "GRNSIZEMIN" and "GRNSIZEMAX" unit is *mm*.

..  _global_SiteCode_Fields:

global_SiteCode Fields
~~~~~~~~~~~~~~~~~~~~

========== ========================
SITECODEID SITECODE
========== ========================
-9999      no data
1          Stone artefact deposit
2          Burial (animal)
3          Burial (human)
4          Cemetery
5          Earth mound
6          Hearth (isolated)
7          Shell midden
8          Open site
9          Quarry
10         Rock art
11         Rockshelter or cave
12         Culturally modified tree
13         Stone structure
19         Other
========== ========================

.. note::

   The dominant attribute of a site will override any other. So, for example, burials in a rockshelter with lots of occupation deposit would be classified as a Rockshelter, not a Cemetery.

..  _global_biomeID_Fields:

global_biomeID Fields
~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

+---------+---------------------------------+----------+------------+
| BIOMEID | BIOMETYPE                       | PARENTID | BIOMEDESCR |
+=========+=================================+==========+============+
| -9999   | no data                         | -9999    | no data    |
+---------+---------------------------------+----------+------------+
| 1       | Terrestrial                     | 1        |            |
+---------+---------------------------------+----------+------------+
| 2       | Aquatic                         | 2        |            |
+---------+---------------------------------+----------+------------+
| 3       | Tidal                           | 3        |            |
+---------+---------------------------------+----------+------------+
| 4       | Freshwater                      | 4        |            |
+---------+---------------------------------+----------+------------+
| 5       | Marine                          | 5        |            |
+---------+---------------------------------+----------+------------+
| 6       | Tropical forest                 | 1        |            |
+---------+---------------------------------+----------+------------+
| 7       | Tropical rainforest             | 6        |            |
+---------+---------------------------------+----------+------------+
| 8       | Tropical seasonal forest        | 6        |            |
+---------+---------------------------------+----------+------------+
| 9       | Tropical dry forest             | 6        |            |
+---------+---------------------------------+----------+------------+
| 10      | Tropical deciduous broadleaf    | 6        |            |
|         | forest and woodland             |          |            |
+---------+---------------------------------+----------+------------+
| 11      | Tropical evergreen broadleaf    | 6        |            |
+---------+---------------------------------+----------+------------+
| 12      | Tropical semi-evergreen         | 6        |            |
|         | broadleaf                       |          |            |
+---------+---------------------------------+----------+------------+
| 13      | Tropical xerophytic shrubland   | 6        |            |
+---------+---------------------------------+----------+------------+
| 14      | Savanna                         | 1        |            |
+---------+---------------------------------+----------+------------+
| 15      | Tropical savanna                | 14       |            |
+---------+---------------------------------+----------+------------+
| 16      | Subtropical savanna             | 14       |            |
+---------+---------------------------------+----------+------------+
| 17      | Temperate savanna               | 14       |            |
+---------+---------------------------------+----------+------------+
| 18      | Temperate deciduous broadleaf   | 14       |            |
|         | savanna                         |          |            |
+---------+---------------------------------+----------+------------+
| 19      | Mediterranean savanna           | 14       |            |
+---------+---------------------------------+----------+------------+
| 20      | Flooded savanna                 | 14       |            |
+---------+---------------------------------+----------+------------+
| 21      | Temperate forest                | 1        |            |
+---------+---------------------------------+----------+------------+
| 22      | Temperate deciduous broadleaf   | 21       |            |
|         | forest                          |          |            |
+---------+---------------------------------+----------+------------+
| 23      | Temperate evergreen needleleaf  | 21       |            |
|         | forest                          |          |            |
+---------+---------------------------------+----------+------------+
| 24      | Temperate evergreen needleleaf  | 21       |            |
|         | open woodland                   |          |            |
+---------+---------------------------------+----------+------------+
| 25      | Temperate sclerophyll woodland  | 21       |            |
|         | and shrubland                   |          |            |
+---------+---------------------------------+----------+------------+
| 26      | Temperate xerophytic shrubland  | 21       |            |
+---------+---------------------------------+----------+------------+
| 27      | Warm-temperate evergreen        | 21       |            |
|         | broadleaf and mixed             |          |            |
+---------+---------------------------------+----------+------------+
| 28      | Cool / cold forest              | 1        |            |
+---------+---------------------------------+----------+------------+
| 29      | Cool mixed forest               | 28       |            |
+---------+---------------------------------+----------+------------+
| 30      | Cool conifer forest             | 28       |            |
+---------+---------------------------------+----------+------------+
| 31      | Cool-temperate evergreen        | 28       |            |
|         | needleleaf forest               |          |            |
+---------+---------------------------------+----------+------------+
| 32      | Cool evergreen needleleaf       | 28       |            |
|         | forest                          |          |            |
+---------+---------------------------------+----------+------------+
| 33      | Taiga (Boreal forest)           | 28       |            |
+---------+---------------------------------+----------+------------+
| 34      | Cold mixed forest               | 28       |            |
+---------+---------------------------------+----------+------------+
| 35      | Cold deciduous forest           | 28       |            |
+---------+---------------------------------+----------+------------+
| 36      | Cold evergreen needleleaf       | 28       |            |
|         | forest                          |          |            |
+---------+---------------------------------+----------+------------+
| 37      | Cold parkland                   | 28       |            |
+---------+---------------------------------+----------+------------+
| 38      | Grassland                       | 1        |            |
+---------+---------------------------------+----------+------------+
| 39      | Warm grass- / shrubland         | 38       |            |
+---------+---------------------------------+----------+------------+
| 40      | Cool grass- / shrubland         | 38       |            |
+---------+---------------------------------+----------+------------+
| 41      | Tundra                          | 1        |            |
+---------+---------------------------------+----------+------------+
| 42      | Arctic tundra                   | 41       |            |
+---------+---------------------------------+----------+------------+
| 43      | Cushion-forb tundra             | 42       |            |
+---------+---------------------------------+----------+------------+
| 44      | Erect dwarf shrub tundra        | 42       |            |
+---------+---------------------------------+----------+------------+
| 45      | Graminoid and forb tundra       | 42       |            |
+---------+---------------------------------+----------+------------+
| 46      | Low and high shrub tundra       | 42       |            |
+---------+---------------------------------+----------+------------+
| 47      | Prostrate dwarf shrub tundra    | 42       |            |
+---------+---------------------------------+----------+------------+
| 48      | Mediterranean                   | 1        |            |
+---------+---------------------------------+----------+------------+
| 49      | Chaparral                       | 48       |            |
+---------+---------------------------------+----------+------------+
| 50      | Xerophytic woods / scrub        | 48       |            |
+---------+---------------------------------+----------+------------+
| 51      | Desert                          | 1        |            |
+---------+---------------------------------+----------+------------+
| 52      | Hot desert                      | 51       |            |
+---------+---------------------------------+----------+------------+
| 53      | Semidesert                      | 51       |            |
+---------+---------------------------------+----------+------------+
| 54      | Ice / polar desert              | 51       |            |
+---------+---------------------------------+----------+------------+
| 55      | High-altitude desert            | 51       |            |
+---------+---------------------------------+----------+------------+
| 56      | Altitudinal                     | 1        |            |
+---------+---------------------------------+----------+------------+
| 57      | Nival barrens                   | 56       |            |
+---------+---------------------------------+----------+------------+
| 58      | Alpine tundra                   | 56       |            |
+---------+---------------------------------+----------+------------+
| 59      | Sub-nival tundra                | 58       |            |
+---------+---------------------------------+----------+------------+
| 60      | Low-alpine tundra               | 58       |            |
+---------+---------------------------------+----------+------------+
| 61      | Subalpine (montane) woodland    | 56       |            |
+---------+---------------------------------+----------+------------+
| 63      | Barren                          | 1        |            |
+---------+---------------------------------+----------+------------+

Classification of biomes on the basis of Prentice et al. (1992), Forseth (2010), and GPD [#]_.

..  _global_ibraID_Fields:

global_ibraID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- `https://www.dcceew.gov.au/environment/land/nrs/science/ibra/ibra7-codes <https://www.dcceew.gov.au/environment/land/nrs/science/ibra/ibra7-codes>`_

====== ======== =============================
IBRAID IBRACODE IBRAREGION
====== ======== =============================
-9999  NA       NA
1      ARC      Arnhem Coast
2      ARP      Arnhem Plateau
3      AUA      Australian Alps
4      AVW      Avon Wheatbelt
5      BBN      Brigalow Belt North
6      BBS      Brigalow Belt South
7      BEL      Ben Lomond
8      BHC      Broken Hill Complex
9      BRT      Burt Plain
10     CAR      Carnarvon
11     CEA      Central Arnhem
12     CEK      Central Kimberley
13     CER      Central Ranges
14     CHC      Channel Country
15     CMC      Central Mackay Coast
16     COO      Coolgardie
17     COP      Cobar Peneplain
18     COS      Coral Sea
19     CYP      Cape York Peninsula
20     DAB      Daly Basin
21     DAC      Darwin Coastal
22     DAL      Dampierland
23     DEU      Desert Uplands
24     DMR      Davenport Murchison Ranges
25     DRP      Darling Riverine Plains
26     EIU      Einasleigh Uplands
27     ESP      Esperance Plains
28     EYB      Eyre Yorke Block
29     FIN      Finke
30     FLB      Flinders Lofty Block
31     FUR      Furneaux
32     GAS      Gascoyne
33     GAW      Gawler
34     GES      Geraldton Sandplains
35     GFU      Gulf Fall and Uplands
36     GID      Gibson Desert
37     GSD      Great Sandy Desert
38     GUC      Gulf Coastal
39     GUP      Gulf Plains
40     GVD      Great Victoria Desert
41     HAM      Hampton
42     ITI      Indian Tropical Islands
43     JAF      Jarrah Forest
44     KAN      Kanmantoo
45     KIN      King
46     LSD      Little Sandy Desert
47     MAC      MacDonnell Ranges
48     MAL      Mallee
49     MDD      Murray Darling Depression
50     MGD      Mitchell Grass Downs
51     MII      Mount Isa Inlier
52     MUL      Mulga Lands
53     MUR      Murchison
54     NAN      Nandewar
55     NCP      Naracoorte Coastal Plain
56     NET      New England Tablelands
57     NNC      NSW North Coast
58     NOK      Northern Kimberley
59     NSS      NSW South Western Slopes
60     NUL      Nullarbor
61     OVP      Ord Victoria Plain
62     PCK      Pine Creek
63     PIL      Pilbara
64     PSI      Pacific Subtropical Islands
65     RIV      Riverina
66     SAI      Subantarctic Islands
67     SCP      South East Coastal Plain
68     SEC      South East Corner
69     SEH      South Eastern Highlands
70     SEQ      South Eastern Queensland
71     SSD      Simpson Strzelecki Dunefields
72     STP      Stony Plains
73     STU      Sturt Plateau
74     SVP      Southern Volcanic Plain
75     SWA      Swan Coastal Plain
76     SYB      Sydney Basin
77     TAN      Tanami
78     TCH      Tasmanian Central Highlands
79     TIW      Tiwi Cobourg
80     TNM      Tasmanian Northern Midlands
81     TNS      Tasmanian Northern Slopes
82     TSE      Tasmanian South East
83     TSR      Tasmanian Southern Ranges
84     TWE      Tasmanian West
85     VIB      Victoria Bonaparte
86     VIM      Victorian Midlands
87     WAR      Warren
88     WET      Wet Tropics
89     YAL      Yalgoo
====== ======== =============================

.. note::

   The *global_ibraID* table only applies to samples from Australia.

..  _global_rivID_Fields:

global_rivID Fields
~~~~~~~~~~~~~~~~~~~~

``Draft`` -- `http://www.bom.gov.au/metadata/catalogue/19115/ANZCW0503900426 <http://www.bom.gov.au/metadata/catalogue/19115/ANZCW0503900426>`_

+-------+--------+--------+---------------------+---------------------+
| RIVID | AHGFL1 | AHGFL2 | RIVNAME             | RIVDIV              |
+=======+========+========+=====================+=====================+
| -9999 | NA     | NA     | NA                  | NA                  |
+-------+--------+--------+---------------------+---------------------+
| 1     | CC     | CC_01  | Koolatong River     | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 2     | CC     | CC_02  | Walker River        | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 3     | CC     | CC_03  | Groote Eylandt      | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 4     | CC     | CC_04  | Roper River         | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 5     | CC     | CC_05  | Towns River         | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 6     | CC     | CC_06  | Limmen Bight River  | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 7     | CC     | CC_07  | Rosie River         | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 8     | CC     | CC_08  | Mcarthur River      | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 9     | CC     | CC_09  | Robinson River      | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 10    | CC     | CC_10  | Calvert River       | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 11    | CC     | CC_11  | Settlement Creek    | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 12    | CC     | CC_12  | Mornington Island   | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 13    | CC     | CC_13  | Nicholson           | Carpentaria Coast   |
|       |        |        | -Leichhardt Rivers  |                     |
+-------+--------+--------+---------------------+---------------------+
| 14    | CC     | CC_14  | Morning Inlet       | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 15    | CC     | CC_15  | Flinders-Norman     | Carpentaria Coast   |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 16    | CC     | CC_16  | Mitchell-Coleman    | Carpentaria Coast   |
|       |        |        | Rivers (QLD)        |                     |
+-------+--------+--------+---------------------+---------------------+
| 17    | CC     | CC_17  | Holroyd River       | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 18    | CC     | CC_18  | Archer-Watson       | Carpentaria Coast   |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 19    | CC     | CC_19  | Ward River          | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 20    | CC     | CC_20  | Embley River        | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 21    | CC     | CC_21  | Wenlock River       | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 22    | CC     | CC_22  | Ducie River         | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 23    | CC     | CC_23  | Jardine River       | Carpentaria Coast   |
+-------+--------+--------+---------------------+---------------------+
| 24    | CC     | CC_24  | Torres Strait       | Carpentaria Coast   |
|       |        |        | Islands             |                     |
+-------+--------+--------+---------------------+---------------------+
| 25    | LEB    | LEB_01 | Cooper Creek-Bulloo | Lake Eyre Basin     |
|       |        |        | River               |                     |
+-------+--------+--------+---------------------+---------------------+
| 26    | LEB    | LEB_02 | Diamantina-Georgina | Lake Eyre Basin     |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 27    | LEB    | LEB_03 | Lake Eyre           | Lake Eyre Basin     |
+-------+--------+--------+---------------------+---------------------+
| 28    | MDB    | MDB_01 | Upper Murray River  | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 29    | MDB    | MDB_02 | Kiewa River         | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 30    | MDB    | MDB_03 | Ovens River         | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 31    | MDB    | MDB_04 | Broken River        | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 32    | MDB    | MDB_05 | Goulburn River      | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 33    | MDB    | MDB_06 | Campaspe River      | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 34    | MDB    | MDB_07 | Loddon River        | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 35    | MDB    | MDB_08 | Avoca River         | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 36    | MDB    | MDB_09 | Avon River-Tyrell   | Murray-Darling      |
|       |        |        | Lake                | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 37    | MDB    | MDB_10 | Murray Riverina     | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 38    | MDB    | MDB_11 | Billabong-Yanco     | Murray-Darling      |
|       |        |        | Creeks              | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 39    | MDB    | MDB_12 | Murrumbidgee River  | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 40    | MDB    | MDB_13 | Lachlan River       | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 41    | MDB    | MDB_14 | Benanee-Willandra   | Murray-Darling      |
|       |        |        | Creek               | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 42    | MDB    | MDB_15 | Wimmera River       | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 43    | MDB    | MDB_16 | Upper Mallee        | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 44    | MDB    | MDB_17 | Border Rivers       | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 45    | MDB    | MDB_18 | Moonie River        | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 46    | MDB    | MDB_19 | Gwydir River        | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 47    | MDB    | MDB_20 | Namoi River         | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 48    | MDB    | MDB_21 | Castlereagh River   | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 49    | MDB    | MDB_22 | Macquarie-Bogan     | Murray-Darling      |
|       |        |        | Rivers              | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 50    | MDB    | MDB_23 | Condamine-Culgoa    | Murray-Darling      |
|       |        |        | Rivers              | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 51    | MDB    | MDB_24 | Warrego River       | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 52    | MDB    | MDB_25 | Paroo River         | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 53    | MDB    | MDB_26 | Darling River       | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 54    | MDB    | MDB_27 | Lower Mallee        | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 55    | MDB    | MDB_28 | Lower Murray River  | Murray-Darling      |
|       |        |        |                     | Basin               |
+-------+--------+--------+---------------------+---------------------+
| 56    | NEC    | NEC_01 | Jacky Jacky Creek   | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 57    | NEC    | NEC_02 | Olive-Pascoe Rivers | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 58    | NEC    | NEC_03 | Lockhart River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 59    | NEC    | NEC_04 | Stewart River       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 60    | NEC    | NEC_05 | Normanby River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 61    | NEC    | NEC_06 | Jeannie River       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 62    | NEC    | NEC_07 | Endeavour River     | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 63    | NEC    | NEC_08 | Daintree River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 64    | NEC    | NEC_09 | Mossman River       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 65    | NEC    | NEC_10 | Barron River        | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 66    | NEC    | NEC_11 | Mulgrave-Russell    | North East Coast    |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 67    | NEC    | NEC_12 | Johnstone River     | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 68    | NEC    | NEC_13 | Tully-Murray Rivers | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 69    | NEC    | NEC_14 | Cardwell Coast      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 70    | NEC    | NEC_15 | Hinchinbrook Island | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 71    | NEC    | NEC_16 | Herbert River       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 72    | NEC    | NEC_17 | Black River         | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 73    | NEC    | NEC_18 | Ross River          | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 74    | NEC    | NEC_19 | Haughton River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 75    | NEC    | NEC_20 | Burdekin River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 76    | NEC    | NEC_21 | Don River           | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 77    | NEC    | NEC_22 | Proserpine River    | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 78    | NEC    | NEC_23 | Whitsunday Islands  | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 79    | NEC    | NEC_24 | O'connell River     | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 80    | NEC    | NEC_25 | Pioneer River       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 81    | NEC    | NEC_26 | Plane Creek         | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 82    | NEC    | NEC_27 | Styx River          | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 83    | NEC    | NEC_28 | Shoalwater Creek    | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 84    | NEC    | NEC_29 | Water Park Creek    | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 85    | NEC    | NEC_30 | Fitzroy River (QLD) | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 86    | NEC    | NEC_31 | Calliope River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 87    | NEC    | NEC_32 | Curtis Island       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 88    | NEC    | NEC_33 | Boyne River         | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 89    | NEC    | NEC_34 | Baffle Creek        | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 90    | NEC    | NEC_35 | Kolan River         | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 91    | NEC    | NEC_36 | Burnett River       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 92    | NEC    | NEC_37 | Burrum River        | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 93    | NEC    | NEC_38 | Mary River (QLD)    | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 94    | NEC    | NEC_39 | Fraser Island       | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 95    | NEC    | NEC_40 | Noosa River         | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 96    | NEC    | NEC_41 | Maroochy River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 97    | NEC    | NEC_42 | Pine River          | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 98    | NEC    | NEC_43 | Brisbane River      | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 99    | NEC    | NEC_44 | Stradbroke Island   | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 100   | NEC    | NEC_45 | Logan-Albert Rivers | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 101   | NEC    | NEC_46 | South Coast         | North East Coast    |
+-------+--------+--------+---------------------+---------------------+
| 102   | NWP    | NWP_01 | De Grey River       | North Western       |
|       |        |        |                     | Plateau             |
+-------+--------+--------+---------------------+---------------------+
| 103   | NWP    | NWP_02 | Sandy Desert        | North Western       |
|       |        |        |                     | Plateau             |
+-------+--------+--------+---------------------+---------------------+
| 104   | PG     | PG_01  | Greenough River     | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 105   | PG     | PG_02  | Murchison River     | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 106   | PG     | PG_03  | Wooramel River      | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 107   | PG     | PG_04  | Gascoyne River      | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 108   | PG     | PG_05  | Yannarie River      | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 109   | PG     | PG_06  | Ashburton River     | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 110   | PG     | PG_07  | Onslow Coast        | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 111   | PG     | PG_08  | Fortescue River     | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 112   | PG     | PG_09  | Port Hedland Coast  | Pilbara-Gascoyne    |
+-------+--------+--------+---------------------+---------------------+
| 113   | SAG    | SAG_01 | Fleurieu Peninsula  | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 114   | SAG    | SAG_02 | Myponga River       | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 115   | SAG    | SAG_03 | Onkaparinga River   | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 116   | SAG    | SAG_04 | Torrens River       | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 117   | SAG    | SAG_05 | Gawler River        | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 118   | SAG    | SAG_06 | Wakefield River     | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 119   | SAG    | SAG_07 | Broughton River     | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 120   | SAG    | SAG_08 | Lake                | South Australian    |
|       |        |        | Torrens-Mambray     | Gulf                |
|       |        |        | Coast               |                     |
+-------+--------+--------+---------------------+---------------------+
| 121   | SAG    | SAG_09 | Spencer Gulf        | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 122   | SAG    | SAG_10 | Eyre Peninsula      | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 123   | SAG    | SAG_11 | Kangaroo Island     | South Australian    |
|       |        |        |                     | Gulf                |
+-------+--------+--------+---------------------+---------------------+
| 124   | SEN    | SEN_01 | Tweed River         | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 125   | SEN    | SEN_02 | Brunswick River     | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 126   | SEN    | SEN_03 | Richmond River      | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 127   | SEN    | SEN_04 | Clarence River      | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 128   | SEN    | SEN_05 | Bellinger River     | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 129   | SEN    | SEN_06 | Macleay River       | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 130   | SEN    | SEN_07 | Hastings River      | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 131   | SEN    | SEN_08 | Manning River       | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 132   | SEN    | SEN_09 | Karuah River        | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 133   | SEN    | SEN_10 | Hunter River        | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 134   | SEN    | SEN_11 | Macquarie-Tuggerah  | South East Coast    |
|       |        |        | Lakes               | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 135   | SEN    | SEN_12 | Hawkesbury River    | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 136   | SEN    | SEN_13 | Sydney              | South East Coast    |
|       |        |        | Coast-Georges River | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 137   | SEN    | SEN_14 | Wollongong Coast    | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 138   | SEN    | SEN_15 | Shoalhaven River    | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 139   | SEN    | SEN_16 | Clyde River-Jervis  | South East Coast    |
|       |        |        | Bay                 | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 140   | SEN    | SEN_17 | Moruya River        | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 141   | SEN    | SEN_18 | Tuross River        | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 142   | SEN    | SEN_19 | Bega River          | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 143   | SEN    | SEN_20 | Towamba River       | South East Coast    |
|       |        |        |                     | (NSW)               |
+-------+--------+--------+---------------------+---------------------+
| 144   | SEV    | SEV_01 | East Gippsland      | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 145   | SEV    | SEV_02 | Snowy River         | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 146   | SEV    | SEV_03 | Mitchell-Thomson    | South East Coast    |
|       |        |        | Rivers              | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 147   | SEV    | SEV_04 | South Gippsland     | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 148   | SEV    | SEV_05 | Bunyip River        | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 149   | SEV    | SEV_06 | Yarra River         | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 150   | SEV    | SEV_07 | Werribee River      | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 151   | SEV    | SEV_08 | Little River        | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 152   | SEV    | SEV_09 | Barwon River-Lake   | South East Coast    |
|       |        |        | Corangamite         | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 153   | SEV    | SEV_10 | Otway Coast         | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 154   | SEV    | SEV_11 | Hopkins River       | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 155   | SEV    | SEV_12 | Portland Coast      | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 156   | SEV    | SEV_13 | Glenelg River       | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 157   | SEV    | SEV_14 | Millicent Coast     | South East Coast    |
|       |        |        |                     | (Victoria)          |
+-------+--------+--------+---------------------+---------------------+
| 158   | SWC    | SWC_01 | Esperance Coast     | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 159   | SWC    | SWC_02 | Albany Coast        | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 160   | SWC    | SWC_03 | Denmark River       | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 161   | SWC    | SWC_04 | Kent River          | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 162   | SWC    | SWC_05 | Frankland-Deep      | South West Coast    |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 163   | SWC    | SWC_06 | Shannon River       | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 164   | SWC    | SWC_07 | Warren River        | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 165   | SWC    | SWC_08 | Donnelly River      | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 166   | SWC    | SWC_09 | Blackwood River     | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 167   | SWC    | SWC_10 | Busselton Coast     | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 168   | SWC    | SWC_11 | Collie-Preston      | South West Coast    |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 169   | SWC    | SWC_12 | Murray River (WA)   | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 170   | SWC    | SWC_13 | Swan Coast-Avon     | South West Coast    |
|       |        |        | River               |                     |
+-------+--------+--------+---------------------+---------------------+
| 171   | SWC    | SWC_14 | Moore-Hill Rivers   | South West Coast    |
+-------+--------+--------+---------------------+---------------------+
| 172   | SWP    | SWP_01 | Gairdner            | South Western       |
|       |        |        |                     | Plateau             |
+-------+--------+--------+---------------------+---------------------+
| 173   | SWP    | SWP_02 | Nullarbor           | South Western       |
|       |        |        |                     | Plateau             |
+-------+--------+--------+---------------------+---------------------+
| 174   | SWP    | SWP_03 | Salt Lake           | South Western       |
|       |        |        |                     | Plateau             |
+-------+--------+--------+---------------------+---------------------+
| 175   | TAS    | TAS_01 | Flinders-Cape       | Tasmania            |
|       |        |        | Barren Islands      |                     |
+-------+--------+--------+---------------------+---------------------+
| 176   | TAS    | TAS_02 | East Coast          | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 177   | TAS    | TAS_03 | Coal River          | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 178   | TAS    | TAS_04 | Derwent River       | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 179   | TAS    | TAS_05 | Kingston Coast      | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 180   | TAS    | TAS_06 | Huon River          | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 181   | TAS    | TAS_07 | South-West Coast    | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 182   | TAS    | TAS_08 | Gordon River        | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 183   | TAS    | TAS_09 | King-Henty Rivers   | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 184   | TAS    | TAS_10 | Pieman River        | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 185   | TAS    | TAS_11 | Sandy Cape Coast    | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 186   | TAS    | TAS_12 | Arthur River        | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 187   | TAS    | TAS_13 | King Island         | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 188   | TAS    | TAS_14 | Smithton-Burnie     | Tasmania            |
|       |        |        | Coast               |                     |
+-------+--------+--------+---------------------+---------------------+
| 189   | TAS    | TAS_15 | Forth River         | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 190   | TAS    | TAS_16 | Mersey River        | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 191   | TAS    | TAS_17 | Rubicon River       | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 192   | TAS    | TAS_18 | Tamar River         | Tasmania            |
+-------+--------+--------+---------------------+---------------------+
| 193   | TAS    | TAS_19 | Piper-Ringarooma    | Tasmania            |
|       |        |        | Rivers              |                     |
+-------+--------+--------+---------------------+---------------------+
| 194   | TTS    | TTS_01 | Cape Leveque Coast  | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 195   | TTS    | TTS_02 | Fitzroy River (WA)  | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 196   | TTS    | TTS_03 | Lennard River       | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 197   | TTS    | TTS_04 | Isdell River        | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 198   | TTS    | TTS_05 | Prince Regent River | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 199   | TTS    | TTS_06 | King Edward River   | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 200   | TTS    | TTS_07 | Drysdale River      | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 201   | TTS    | TTS_08 | Ord-Pentecost       | Tanami-Timor Sea    |
|       |        |        | Rivers              | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 202   | TTS    | TTS_09 | Keep River          | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 203   | TTS    | TTS_10 | Victoria River-wiso | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 204   | TTS    | TTS_11 | Fitzmaurice River   | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 205   | TTS    | TTS_12 | Moyle River         | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 206   | TTS    | TTS_13 | Daly River          | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 207   | TTS    | TTS_14 | Finniss River       | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 208   | TTS    | TTS_15 | Bathurst-Melville   | Tanami-Timor Sea    |
|       |        |        | Islands             | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 209   | TTS    | TTS_16 | Adelaide River      | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 210   | TTS    | TTS_17 | Mary River (NT)     | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 211   | TTS    | TTS_18 | Wildman River       | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 212   | TTS    | TTS_19 | South Alligator     | Tanami-Timor Sea    |
|       |        |        | River               | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 213   | TTS    | TTS_20 | East Alligator      | Tanami-Timor Sea    |
|       |        |        | River               | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 214   | TTS    | TTS_21 | Goomadeer River     | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 215   | TTS    | TTS_22 | Liverpool River     | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 216   | TTS    | TTS_23 | Blyth River         | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 217   | TTS    | TTS_24 | Goyder River        | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+
| 218   | TTS    | TTS_25 | Buckingham River    | Tanami-Timor Sea    |
|       |        |        |                     | Coast               |
+-------+--------+--------+---------------------+---------------------+

.. note::

   The *global_rivID* table only applies to samples from Australia.

..  _global_PubType_Fields:

global_PubType Fields
~~~~~~~~~~~~~~~~~~~~~

========= =============
PUBTYPEID PUBTYPE
========= =============
1         article
2         book
3         booklet
4         conference
5         inbook
6         incollection
7         inproceedings
8         manual
9         mastersthesis
10        misc
11        phdthesis
12        proceedings
13        techreport
14        unpublished
15        pers_comm
16        online
========= =============

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

``Draft`` -- 

+------------+---------------------------+---------------------------+
| CHEMPREPID | CHEMPREP                  | CHEMPREPAB                |
+============+===========================+===========================+
| -9999      | no data                   | ND                        |
+------------+---------------------------+---------------------------+
| -9991      | not applicable            | NA                        |
+------------+---------------------------+---------------------------+
| 1          | Acid-Base-Acid            | ABA                       |
+------------+---------------------------+---------------------------+
| 2          | ABA (base soluble)        | ABA (base soluble)        |
+------------+---------------------------+---------------------------+
| 3          | ABA and bleach            | ABA and bleach            |
+------------+---------------------------+---------------------------+
| 4          | ABA and bleach-Stepped    | ABA and bleach-SC         |
|            | Combustion                |                           |
+------------+---------------------------+---------------------------+
| 5          | Acid-Base-Acid Stepped    | ABA-SC                    |
|            | Combustion                |                           |
+------------+---------------------------+---------------------------+
| 6          | Acid-Base Oxidation       | ABOx                      |
+------------+---------------------------+---------------------------+
| 7          | Acid-Base Oxidation       | ABOx-SC                   |
|            | Stepped Combustion        |                           |
+------------+---------------------------+---------------------------+
| 8          | Acid treatment            | Acid                      |
+------------+---------------------------+---------------------------+
| 9          | Acid (to extract apatite) | Acid (to extract apatite) |
+------------+---------------------------+---------------------------+
| 10         | Acid or ABA               | Acid or ABA               |
|            | gelatinisation            | gelatinisation            |
|            | -ultrafiltration          | -ultrafiltration          |
+------------+---------------------------+---------------------------+
| 11         | Acid or                   | Acid or                   |
|            | ABA-gelatinisation        | ABA-gelatinisation        |
+------------+---------------------------+---------------------------+
| 12         | Alpha cellulose           | Alpha cellulose           |
+------------+---------------------------+---------------------------+
| 13         | Alpha cellulose-SC        | Alpha cellulose-SC        |
+------------+---------------------------+---------------------------+
| 14         | AOx                       | AOx                       |
+------------+---------------------------+---------------------------+
| 15         | AOx-SC                    | AOx-SC                    |
+------------+---------------------------+---------------------------+
| 16         | Carbonate Density         | CARDS                     |
|            | Separation                |                           |
+------------+---------------------------+---------------------------+
| 17         | CARDS + acid              | CARDS + acid              |
+------------+---------------------------+---------------------------+
| 18         | Hydroxyproline            | Hydroxyproline            |
+------------+---------------------------+---------------------------+
| 19         | Hydrogen Pyrolysis        | HyPy                      |
+------------+---------------------------+---------------------------+
| 20         | Plasma Oxidation          | Plasma Oxidation          |
+------------+---------------------------+---------------------------+
| 21         | Potassium permanganate    | Potassium permanganate    |
|            | (to extract oxalate)      | (to extract oxalate)      |
+------------+---------------------------+---------------------------+
| 22         | Stepped hydrolysis        | Stepped hydrolysis        |
+------------+---------------------------+---------------------------+
| 23         | Resin used to clean amino | XAD                       |
|            | acids                     |                           |
+------------+---------------------------+---------------------------+
| 24         | Acid-Alkali-Acid          | AAA                       |
+------------+---------------------------+---------------------------+
| 25         | AAA or ABA                | AAA/ABA                   |
+------------+---------------------------+---------------------------+
| 26         | AAA or ABA or Acid wash   | AAA/ABA/Acid              |
+------------+---------------------------+---------------------------+
| 27         | ABA + Ultrafiltration     | ABAu                      |
+------------+---------------------------+---------------------------+
| 28         | Several fragments dated   | Bulk                      |
|            | together                  |                           |
+------------+---------------------------+---------------------------+
| 29         | Collagen Stepped          | Coll_SC                   |
|            | Combustion                |                           |
+------------+---------------------------+---------------------------+
| 30         | Collagen ultrafiltration  | Coll_ultra                |
+------------+---------------------------+---------------------------+
| 31         | Gelatinisation            | Gelatin                   |
+------------+---------------------------+---------------------------+
| 32         | Modified Longin method    | Longin                    |
+------------+---------------------------+---------------------------+
| 33         | no treatment              | No                        |
+------------+---------------------------+---------------------------+
| 34         | Ultrafiltration           | Ultra                     |
+------------+---------------------------+---------------------------+
| 99         | for other method          | Other                     |
+------------+---------------------------+---------------------------+

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

``Draft`` -- 

========= =============
COL_MTDID COL_MTD
========= =============
-9999     ND
1         Auger
2         Block
3         Core
4         Downhole Tube
5         Excavated
6         Tube
7         Other
8         InSitu
9         Sieve
========= =============

..  _cabah_methodID_Fields:

cabah_methodID Fields
~~~~~~~~~~~~~~~~~~~~~~

``Draft`` -- 

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
|          | Photo-         |            |          | Poolton, Kook  |
|          | luminescence   |            |          | & Jain (2017)  |
|          |                |            |          | [#]_           |
+----------+----------------+------------+----------+----------------+
| 50       | Infrared       | IR-RF      | 47       | Trautmann,     |
|          | Radio-         |            |          | Krbetschek,    |
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

``Draft`` -- 

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

crn_alstndID **"ALSTNDCOMT"**

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

``Draft`` -- 

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

crn_amsID **"AMSURL"**

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

``Draft`` -- 

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

crn_bestndID **"BESTNDCOMT"**

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
.. [#] Anderson, Libby, Weinhouse, Reid, Kirshenbaum & Grosse (1947)`DOI:10.1103/PhysRev.72.931 <https://doi.org/10.1103/PhysRev.72.931>`_
.. [#] Dorn (1983)`DOI: 10.1016/0033-5894(83)90065-0 <https://doi.org/10.1016/0033-5894(83)90065-0>`_
.. [#] Frink (1996)`DOI: 10.2136/sssaspecpub44.c6 <https://doi.org/10.2136/sssaspecpub44.c6>`_
.. [#] Huntley, Godfrey-Smith & Thewalt (1985)`DOI: 10.1038/313105a0 <https://doi.org/10.1038/313105a0>`_
.. [#] Daniels, Boyd & Saunders (1953)`DOI: 10.1126/science.117.3040.343 <https://doi.org/10.1126/science.117.3040.343>`_
.. [#] Kaufmann & Libby (1954)`DOI: 10.1103/PhysRev.93.1337 <https://doi.org/10.1103/PhysRev.93.1337>`_
.. [#] Arnold (1956)`DOI: 10.1126/science.124.3222.584 <https://doi.org/10.1126/science.124.3222.584>`_
.. [#] Lal, Goldberg & Koide (1960)`DOI: 10.1126/science.131.3397.332 <https://doi.org/10.1126/science.131.3397.332>`_
.. [#] Davis & Schaeffer (1955)`DOI: 10.1111/j.1749-6632.1955.tb35368.x <https://doi.org/10.1111/j.1749-6632.1955.tb35368.x>`_
.. [#] Loosli & Oeschger (1968)`DOI: 10.1016/S0012-821X(68)80039-1 <https://doi.org/10.1016/S0012-821X(68)80039-1>`_
.. [#] Raisbeck & Yiou (1979)`DOI: 10.1038/277042a0 <https://doi.org/10.1038/277042a0>`_
.. [#] Wilkinson & Sheline (1955)`DOI: 10.1103/PhysRev.99.752 <https://doi.org/10.1103/PhysRev.99.752>`_
.. [#] Marti (1967)`DOI: 10.1103/PhysRevLett.18.264 <https://doi.org/10.1103/PhysRevLett.18.264>`_
.. [#] Takagi, Hampel & Kirsten (1974)`DOI: 10.1016/0012-821X(74)90019-3 <https://doi.org/10.1016/0012-821X(74)90019-3>`_
.. [#] Smits & Gentner (1950)`DOI: 10.1016/0016-7037(50)90005-6 <https://doi.org/10.1016/0016-7037(50)90005-6>`_
.. [#] Hahn, Strassmann & Walling (1937)`DOI: 10.1007/BF01492269 <https://doi.org/10.1007/BF01492269>`_
.. [#] Herr, Merz, Eberhardt & Signer (1958)`DOI: 10.1515/zna-1958-0404 <https://doi.org/10.1515/zna-1958-0404>`_
.. [#] Herr & Merz (1955)`DOI: 10.1515/zna-1955-0804 <https://doi.org/10.1515/zna-1955-0804>`_
.. [#] Holmes (1911) `DOI: 10.1098/rspa.1911.0036 <https://doi.org/10.1098/rspa.1911.0036>`_
.. [#] Williams (1995)`DOI: 10.1007/BF00768738 <https://doi.org/10.1007/BF00768738>`_
.. [#] Barnes, Lang & Potratz (1956)`DOI: 10.1126/science.124.3213.175.b <https://doi.org/10.1126/science.124.3213.175.b>`_
.. [#] Thurber (1962)`DOI: 10.1029/JZ067i011p04518 <https://doi.org/10.1029/JZ067i011p04518>`_
.. [#] Prasad, Poolton, Kook & Jain (2017)`DOI: 10.1038/s41598-017-10174-8 <https://doi.org/10.1038/s41598-017-10174-8>`_
.. [#] Trautmann, Krbetschek, Dietrich & Stolz (1998)`DOI: 10.1016/S1350-4487(98)00012-2 <https://doi.org/10.1016/S1350-4487(98)00012-2>`_
.. [#] Hütt, Jaek & Tchonka (1988)`DOI: 10.1016/0277-3791(88)90033-9 <https://doi.org/10.1016/0277-3791(88)90033-9>`_
.. [#] Huang & Walker (1967)`DOI: 10.1126/science.155.3766.1103 <https://doi.org/10.1126/science.155.3766.1103>`_
.. [#] Fanale & Schaeffer (1965)`DOI: 10.1126/science.149.3681.312 <https://doi.org/10.1126/science.149.3681.312>`_
.. [#] Price & Walker (1962)`DOI: 10.1038/196732a0 <https://doi.org/10.1038/196732a0>`_
.. [#] Friedman & Smith (1960)`DOI: 10.2307/276634 <https://doi.org/10.2307/276634>`_
.. [#] Emiliani (1954)`DOI: 10.1126/science.119.3103.853 <https://doi.org/10.1126/science.119.3103.853>`_
.. [#] Harold (1960)`DOI: 10.1111/j.1475-4754.1960.tb00518.x <https://doi.org/10.1111/j.1475-4754.1960.tb00518.x>`_
.. [#] Rengan (1983)`DOI: 10.1021%2Fed060p682 <https://doi.org/10.1021%2Fed060p682>`_
.. [#] Fifield (1999)`DOI: 10.1088/0034-4885/62/8/202 <https://doi.org/10.1088/0034-4885/62/8/202>`_
