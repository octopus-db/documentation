=============
Field indices
=============

Data table fields
-----------------



Lookup table fields
-------------------

..  _global_GrainSize_Fields:

global_GrainSize Fields
~~~~~~~~~~~~~~~~~~~~~

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

* **article** -- An article from a journal or magazine. *Required fields*: author, title, journal, year. *Optional fields*: volume, number, pages, month, note.

* **book** [#]_ -- A book with an explicit publisher. *Required fields*: author or editor, title, publisher, year. *Optional fields*: volume or number, series, address, edition, month, note.

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

.. rubric:: Footnotes

.. [#] Entry type descriptions taken from `http://newton.ex.ac.uk/tex/pack/bibtex/btxdoc/ <http://newton.ex.ac.uk/tex/pack/bibtex/btxdoc/>`_
