#!/usr/bin/env python

#    Inkscape Multi-Bool extension for Inkscape 0.91
#    Copyright (C) 2014  Ryan Lerch (multiple difference)
#                  2016  Maren Hachmann <marenhachmannATyahoo.com> (refactoring, extend to multibool)
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
This extension takes a selection of paths, and applies a division
between the top shape in the z-order, and each of the shapes underneath.
"""
import inkex, os, csv, math
from subprocess import Popen, PIPE
from lxml import etree
from shutil import copy2

class MultipleDivision(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

    def effect(self):
    
        file = self.args[-1]
        tempfile = os.path.splitext(file)[0] + "-multidiv.svg"

        p = Popen('inkscape --query-all '+file, shell=True, stdout=PIPE, stderr=PIPE)
        err = p.stderr
        f = p.communicate()[0]
        lines=csv.reader(f.split(os.linesep))
        err.close() 

        copy2(file, tempfile)

        documentobjects = []
        for line in lines:
            if len(line) > 0:
                documentobjects.append(line[0])

        commandstring="inkscape "
        first = True
        toppath=""
        selecteditems = self.selected
                
        documentobjects.reverse()
        if len(selecteditems) > 1:
            for o in documentobjects:
                if o in selecteditems:
                    if first:
                        toppath=o
                        first = False
                    else:
                        commandstring = commandstring + "--select="+toppath+" --verb=EditDuplicate --select="+o+" --verb=SelectionDivide --verb=EditDeselect "
            
            commandstring += "--verb=FileSave --verb=FileQuit "
            p = Popen(commandstring+tempfile, shell=True, stdout=PIPE, stderr=PIPE)
            err = p.stderr
            f = p.communicate()[0]
            err.close()
            
            self.document = etree.parse(tempfile)
            
if __name__ == '__main__':
    e = MultipleDivision()
    e.affect()
