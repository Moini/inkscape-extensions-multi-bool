inkscape-extension-multi-bool
=============================

**Moved to [GitLab](https://gitlab.com/Moini/inkscape-extensions-multi-bool/)!**

*This is an archived version of the extension. For the current one, visit [the new repository](https://gitlab.com/Moini/inkscape-extensions-multi-bool/).*

-------

Fork of Ryan Lerch's [multiple-difference Inkscape extension](https://github.com/ryanlerch/inkscape-extension-multiple-difference).

A set of three inkscape extensions to apply

-    Path -> Difference
-    Path -> Cut Path
-    Path -> Division

on multiple selected paths or shapes at once.

The topmost object is used to cut / divide / do a difference on each selected object below.

In contrast to the standard operations, it keeps the topmost object.

Installation
============

Copy the *.py and *.inx files into the directory indicated in Edit -> Preferences -> System: User extensions 

Usage
=====

Select all objects (paths or shapes only!) that you want to use the extension with, then go to Extensions -> Boolean -> Multiple Cut / Multiple Difference / Multiple Division. Done!

Known Issues:
=============

-   Does not give any error messages.
-   Does not recurse into groups.
-   Is probably slow on large files, as it replaces the file's contents by the contents of an edited temporary file.

Licence:
========
GPLv2 or later (see https://github.com/ryanlerch/inkscape-extension-multiple-difference/issues/1#issuecomment-178285798)
