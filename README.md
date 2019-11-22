fields2fdf
==========

* Read `pdftk dump_data_fields` dump of pdf fields
* Extract name-value pairs from the dump
* Generate fdf file ignoring duplicated field values

Why?
----

This is one of two steps aimed at fixing PDFs with forms corrupted by OS X Preview.app.

See details on the issue: http://kb2.adobe.com/community/publishing/885/cpsid_88564.html

See the script assembling the solution for linux using pdftk dump/restore trick: https://github.com/vindex10/shorties/blob/master/fixpdffields
