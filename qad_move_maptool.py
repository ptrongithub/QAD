# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QAD Quantum Aided Design plugin

 classe per gestire il map tool in ambito del comando move
 
                              -------------------
        begin                : 2013-09-27
        copyright            : iiiii
        email                : hhhhh
        developers           : bbbbb aaaaa ggggg
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import math


import qad_utils
from qad_snapper import *
from qad_snappointsdisplaymanager import *
from qad_variables import *
from qad_getpoint import *
from qad_rubberband import QadRubberBand
from qad_dim import *


#===============================================================================
# Qad_move_maptool_ModeEnum class.
#===============================================================================
class Qad_move_maptool_ModeEnum():
   # noto niente si richiede il punto base
   NONE_KNOWN_ASK_FOR_BASE_PT = 1     
   # noto il punto base si richiede il secondo punto per lo spostamento
   BASE_PT_KNOWN_ASK_FOR_MOVE_PT = 2     


#===============================================================================
# Qad_move_maptool class
#===============================================================================
class Qad_move_maptool(QadGetPoint):
    
   def __init__(self, plugIn):
      QadGetPoint.__init__(self, plugIn)
                        
      self.basePt = None
      self.entitySet = QadEntitySet()
      self.__rubberBand = QadRubberBand(self.canvas)

   def hidePointMapToolMarkers(self):
      QadGetPoint.hidePointMapToolMarkers(self)
      self.__rubberBand.hide()

   def showPointMapToolMarkers(self):
      QadGetPoint.showPointMapToolMarkers(self)
      self.__rubberBand.show()
                             
   def clear(self):
      QadGetPoint.clear(self)
      self.__rubberBand.reset()
      self.mode = None    

   
   #============================================================================
   # move
   #============================================================================
   def move(self, entity, offSetX, offSetY):
      # verifico se l'entità appartiene ad uno stile di quotatura
      if entity.whatIs() == "ENTITY":
         # sposto l'entità
         movedGeom = qad_utils.moveQgsGeometry(entity.getGeometry(), offSetX, offSetY)
         if movedGeom is not None:
            self.__rubberBand.addGeometry(movedGeom, entity.layer)
      else:
         # sposto la quota
         entity.move(offSetX, offSetY)
         self.__rubberBand.addGeometry(entity.textualFeature.geometry(), entity.getTextualLayer())
         self.__rubberBand.addGeometries(entity.getLinearGeometryCollection(), entity.getLinearLayer())
         self.__rubberBand.addGeometries(entity.getSymbolGeometryCollection(), entity.getSymbolLayer())

   
   def addMovedGeometries(self, newPt):
      self.__rubberBand.reset()            

      dimElaboratedList = [] # lista delle quotature già elaborate
      entity = QadEntity()
      
      for layerEntitySet in self.entitySet.layerEntitySetList:
         layer = layerEntitySet.layer
         
         transformedBasePt = self.canvas.mapRenderer().mapToLayerCoordinates(layer, self.basePt)
         transformedNewPt = self.canvas.mapRenderer().mapToLayerCoordinates(layer, newPt)
         offSetX = transformedNewPt.x() - transformedBasePt.x()
         offSetY = transformedNewPt.y() - transformedBasePt.y()

         for featureId in layerEntitySet.featureIds:
            # verifico se l'entità appartiene ad uno stile di quotatura
            dimEntity = self.plugIn.dimStyles.getDimEntity(layer, featureId)  
            if dimEntity is None:
               entity.set(layer, featureId)
               f = layerEntitySet.getFeature(featureId)
               self.move(entity, offSetX, offSetY)
            else:            
               found = False
               for dimElaborated in dimElaboratedList:
                  if dimElaborated == dimEntity:
                     found = True
               if found == False: # quota non ancora elaborata
                  dimElaboratedList.append(dimEntity)
                  self.stretch(dimEntity, offSetX, offSetY)


   def canvasMoveEvent(self, event):
      QadGetPoint.canvasMoveEvent(self, event)
                     
      # noto il punto base si richiede il secondo punto
      if self.mode == Qad_move_maptool_ModeEnum.BASE_PT_KNOWN_ASK_FOR_MOVE_PT:
         self.addMovedGeometries(self.tmpPoint)                           
         
    
   def activate(self):
      QadGetPoint.activate(self)            
      self.__rubberBand.show()          

   def deactivate(self):
      try: # necessario perché se si chiude QGIS parte questo evento nonostante non ci sia più l'oggetto maptool !
         QadGetPoint.deactivate(self)
         self.__rubberBand.hide()
      except:
         pass

   def setMode(self, mode):
      self.mode = mode
      # noto niente si richiede il punto base
      if self.mode == Qad_move_maptool_ModeEnum.NONE_KNOWN_ASK_FOR_BASE_PT:
         self.setSelectionMode(QadGetPointSelectionModeEnum.POINT_SELECTION)
         self.setDrawMode(QadGetPointDrawModeEnum.NONE)
         self.__rubberBand.reset()
      # noto il punto base si richiede il secondo punto
      elif self.mode == Qad_move_maptool_ModeEnum.BASE_PT_KNOWN_ASK_FOR_MOVE_PT:
         self.setDrawMode(QadGetPointDrawModeEnum.ELASTIC_LINE)
         self.setStartPoint(self.basePt)