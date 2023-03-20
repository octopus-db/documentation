=============
Field indices
=============

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

..  _cabah_chemprepID_Fields:

cabah_chemprepID Fields
~~~~~~~~~~~~~~~~~~~~~~~

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

..  _cabah_col_mtdID_Fields:

cabah_col_mtdID Fields
~~~~~~~~~~~~~~~~~~~~~~

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

======== ==================================== ==========
METHODID METHOD                               METHODABBR
======== ==================================== ==========
-9999    not applicable                       NA
1        Amino Acid Racemization              AAR
2        Radiocarbon Dating                   C14
3        Cation Ratio Dating                  CRD
4        Electron Spin Resonance              ESR
5        Oxidisable Carbon Ratio              OCR
6        Optically Stimulated Luminescence    OSL
7        Thermoluminescence                   TL
8        Uranium-Series                       U
9        Closed-system U-Series and ESR model CSU-ESR
10       Stratigraphic correlation            Strat
11       Coupled U-ESR model                  U-ESR
======== ==================================== ==========


.. rubric:: Footnotes

.. [#] Entry type descriptions taken from `http://newton.ex.ac.uk/tex/pack/bibtex/btxdoc/ <http://newton.ex.ac.uk/tex/pack/bibtex/btxdoc/>`_
