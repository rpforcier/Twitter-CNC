#!/usr/bin/env python
"""
Twitter CNC Project Code from Hershey Text Extension for Inkscape
Passes Tweet Text into InkScape
"""

"""
Hershey Text - renders a line of text using "Hershey" fonts for plotters

Copyright 2011, Windell H. Oskay, www.evilmadscientist.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import inkex
from simplestyle import *
import hersheydata          
import simplestyle
from simpletransform import computePointInNode

def draw_svg_text(char, face, offset, vertoffset, parent, scale):
    style = { 'stroke': '#000000', 'fill': 'none' }
    pathString = face[char]
    splitString = pathString.split()  
    midpoint = offset - int(splitString[0]) 
    pathString = pathString[pathString.find("M"):] #portion after first move
    trans = 'translate(' + str(midpoint) + ',' + str(vertoffset) + ')' 
    text_attribs = {'style':simplestyle.formatStyle(style), 'd':pathString, 'transform':trans}
    inkex.etree.SubElement(parent, inkex.addNS('path','svg'), text_attribs) 
    return midpoint + int(splitString[1])   #new offset value

class TwitterCNCEffect(inkex.Effect):
    
    def __init__(self):
        
        inkex.Effect.__init__(self)
        
        self.OptionParser.add_option('--name', action = 'store',
            type = 'string', dest = 'name', default='')
          
        self.OptionParser.add_option('--date', action = 'store',
            type = 'string', dest = 'date', default='')
        
        self.OptionParser.add_option('--body1', action = 'store',
            type = 'string', dest = 'body1', default='')

        self.OptionParser.add_option('--body2', action = 'store',
            type = 'string', dest = 'body2', default='')

        self.OptionParser.add_option('--body3', action = 'store',
            type = 'string', dest = 'body3', default='')

        self.OptionParser.add_option('--body4', action = 'store',
            type = 'string', dest = 'body4', default='')
        
        self.OptionParser.add_option('--body5', action = 'store',
            type = 'string', dest = 'body5', default='')
        
    def effect(self):
        
        #Pull Data from Inx File
        date = self.options.date
        name = self.options.name
        body1 = self.options.body1
	body2 = self.options.body2
	body3 = self.options.body3
	body4 = self.options.body4
	body5 = self.options.body5
	
	#Letter Intro, Outro, and Reference Mark
        intro = 'Dearest Everyone,'
        outro = 'Yours Most Sincerly,'
        reference = '.'
        
        #Set Layer and Scale
        g = self.current_layer
        scale = self.unittouu('1.5px')
        
        #Set Font  
        font = eval('hersheydata.' + 'cursive')
        clearfont = hersheydata.futural
        
        def DrawSvgWords(text, vertPos):
            
            spacing = 3 
            w = 15
            letterVals = [ord(q) - 32 for q in text]
            
            for q in letterVals:
                if (q < 0) or (q > 95):
                    w += 2*spacing
                else:
                    w = draw_svg_text(q, font, w, vertPos, g, scale)
                    
        #Create Paths for Date, Greeting, Ending, Body, and Name
        DrawSvgWords(intro, 250)
                 
        if body2 == '' and body3 == '' and body4 == '' and body5 == '':
            DrawSvgWords(date, 160)
            DrawSvgWords(body1, 300)
            DrawSvgWords(outro, 500)
            DrawSvgWords(name, 550)
            DrawSvgWords(reference, 551)
        elif body3 == '' and body4 == '' and body5 == '':
            DrawSvgWords(date, 160)
            DrawSvgWords(body1, 300)
            DrawSvgWords(body2, 350)
            DrawSvgWords(outro, 500)
            DrawSvgWords(name, 550)
            DrawSvgWords(reference, 551)
        elif body4 == '' and body5 == '':
            DrawSvgWords(date, 185)
            DrawSvgWords(body1, 300)
            DrawSvgWords(body2, 350)
            DrawSvgWords(body3, 400)
            DrawSvgWords(outro, 560)
            DrawSvgWords(name, 610)
            DrawSvgWords(reference, 611)
        elif body5 == '':
            DrawSvgWords(date, 185)
            DrawSvgWords(body1, 300)
            DrawSvgWords(body2, 350)
            DrawSvgWords(body3, 400)
            DrawSvgWords(body4, 450)
            DrawSvgWords(outro, 560)
            DrawSvgWords(name, 610)
            DrawSvgWords(reference, 611)
        else:
            DrawSvgWords(date, 185)
            DrawSvgWords(body1, 300)
            DrawSvgWords(body2, 350)
            DrawSvgWords(body3, 400)
            DrawSvgWords(body4, 450)
            DrawSvgWords(body5, 500)
            DrawSvgWords(outro, 560)
            DrawSvgWords(name, 610)
            DrawSvgWords(reference, 611)
             
        t = ' scale(' + str(scale) + ')'
        g.set('transform',t)
            		
# Create Effect Instance and Apply It.
e = TwitterCNCEffect()
e.affect()