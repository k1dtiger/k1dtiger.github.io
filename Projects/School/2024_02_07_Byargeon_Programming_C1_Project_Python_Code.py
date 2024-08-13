import arcpy
#define project, maps, and layers
aprx = arcpy.mp.ArcGISProject("CURRENT")
maps = aprx.listMaps("Map")[0]
lyr = maps.listLayers("Points")[0]

#set field name to EventType and length to 20 then create new field
fieldname = "EventType"
fieldlength = 20
arcpy.AddField_management(lyr, fieldname,"TEXT",field_length=fieldlength)

#set field name to EventDest and create new field
fieldname = "EventDest"
arcpy.AddField_management(lyr, fieldname,"TEXT",field_length=fieldlength)

#define the event types and destruction ranges
Tevent='"Tsunami"'
Eevent='"Earthquake"'
Vevent='"VolcanicEruption"'
L1='"unknown"'
L2='"(1-50)"'
L3='"(51-100)"'
L4='"(101-1,000)"'
L5='"(Over 1,000)"'

#Select layer by attribute and calculate fields
#Point 0
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 0", None)
arcpy.management.CalculateField('hazards_NOAA_2024\\Points', 'EventType',Tevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2024\\Points', 'EventDest',L4, 'PYTHON3')

#Point 1
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 1", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Tevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L1, 'PYTHON3')
#Point 2
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 2", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Tevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L5, 'PYTHON3')
#Point 3
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 3", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Tevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L3, 'PYTHON3')
#Point 4
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 4", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Tevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L2, 'PYTHON3')
#Point 8
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 8", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Eevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L1, 'PYTHON3')
#Point 9
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 9", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Eevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L2, 'PYTHON3')
#Point 10
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 10", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Eevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L4, 'PYTHON3')
#Point 11
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID =11", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Eevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L5, 'PYTHON3')
#Point 12
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 12", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Eevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L3, 'PYTHON3')
#Point 13
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 13", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Vevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L1, 'PYTHON3')
#Point 14
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 14", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Vevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L4, 'PYTHON3')
#Point 15
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 15", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Vevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L2, 'PYTHON3')
#Point 16
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 16", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Vevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L5, 'PYTHON3')
#Point 17
arcpy.management.SelectLayerByAttribute('hazards_NOAA_2021\\Points', 'NEW_SELECTION', "SymbolID = 17", None)
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventType',Vevent, 'PYTHON3')
arcpy.management.CalculateField('hazards_NOAA_2021\\Points', 'EventDest',L3, 'PYTHON3')

#Create definition layer for Tsunami
lyr.definitionQuery="EventType = 'Tsunami'"
lyr.name="Tsunami"


3A: Update Layouts
#define layout variable as entry 0 in the Layouts list
lyt=aprx.listLayouts("HazardsLayout")[0]
#create list of text elements within selected layout, store the element names in a list called "eleList"
eleList=lyt.listElements("TEXT_ELEMENT")
#For each element in eleList, update the Title element text to read "Natural Hazards"
for ele in eleList:
	if ele.text=="Title";
		ele.text="Natural Hazards"
#For each element called "Subtitle" in eleList, update the text to read "Tsunami"
for ele in eleList:
	if ele.text=="Subtitle":
		ele.text="Tsunami
for ele in eleList:
    if ele.text=="Paragraph Text":
        ele.text="Tsunamis are giant waves usually caused by earthquakes or volcanic eruptions under the sea.  Their waves do not dramatically increase in height until reaching the shore, which makes forecasting their impact elusive."
lyt.exportToPDF("Z:\\ACC PC\\ACC GIS\\Projects\\GISC_2435_Programming\\P1_Global_Natural_Hazards\\10_Deliverables\\2024_01_27_Byargeon_Programming_C1_Layout_Tsunami")

for ele in eleList:
     if ele.text=="Tsunamis are giant waves usually caused by earthquakes or volcanic eruptions under the sea.  Their waves do not dramatically increase in height until reaching the shore, which makes forecasting their impact elusive.":
      ele.text="An earthquake is the shaking of the Earth's surface caused by energy releases in the lithosphere.  These energy releases usually occur along fault lines, when adjacent plates move relative to each other. The type of fault can determine the severity of the earthquake."
lyt.exportToPDF("Z:\\ACC PC\\ACC GIS\\Projects\\GISC_2435_Programming\\P1_Global_Natural_Hazards\\10_Deliverables\\2024_01_27_Byargeon_Programming_C1_Layout_Tsunami")
lyr.definitionQuery="EventType = 'Earthquake'"
lyr.name="Earthquake"

#define layout variable as entry 0 in the Layouts list
lyt=aprx.listLayouts("HazardsLayout")[0]
#create list of text elements within selected layout, store the element names in a list called "eleList"
eleList=lyt.listElements("TEXT_ELEMENT")

#For each element in eleList, update the Title element text to read "Natural Hazards"
for ele in eleList:
	if ele.text=="Title":
		ele.text="Natural Hazards"
for ele in eleList:
    if ele.text=="Earthquake":
        ele.text="Volcano"
for ele in eleList:
     if ele.text=="An earthquake is the shaking of the Earth's surface caused by energy releases in the lithosphere.  These energy releases usually occur along fault lines, when adjacent plates move relative to each other. The type of fault can determine the severity of the earthquake.":
      ele.text="Volcanos are openings in the Earth's surface that allow magma, volcanic ash, and gases to escape.  Sometimes the release of volcanic materials occurs suddenly, which can result in violent eruptions."
lyt.exportToPDF("Z:\\ACC PC\\ACC GIS\\Projects\\GISC_2435_Programming\\P1_Global_Natural_Hazards\\10_Deliverables\\2024_01_27_Byargeon_Programming_C1_Layout_Volcano")
# Create and Export Layout for Earthquakes
for ele in eleList:
    if ele.text=="Volcano":
        ele.text="Earthquake"
for ele in eleList:
     if ele.text=="Volcanos are openings in the Earth's surface that allow magma, volcanic ash, and gases to escape.  Sometimes the release of volcanic materials occurs suddenly, which can result in violent eruptions.":
      ele.text="An earthquake is the shaking of the Earth's surface caused by energy releases in the lithosphere.  These energy releases usually occur along fault lines, when adjacent plates move relative to each other. The type of fault can determine the severity of the earthquake."
lyt.exportToPDF("Z:\\ACC PC\\ACC GIS\\Projects\\GISC_2435_Programming\\P1_Global_Natural_Hazards\\10_Deliverables\\2024_01_27_Byargeon_Programming_C1_Layout_Earthquake")
for ele in eleList:
    if ele.text=="Earthquake":
        ele.text="Landslide"
for ele in eleList:
     if ele.text=="An earthquake is the shaking of the Earth's surface caused by energy releases in the lithosphere.  These energy releases usually occur along fault lines, when adjacent plates move relative to each other. The type of fault can determine the severity of the earthquake.":
      ele.text="Landslides are the mass movement of rock, debris, or earth down a slope. Most landslides occur for multiple reasons, but are often related to increased loads up-slope coupled with structural degredation down-slope.  Earthquakes can initiate land-slides, and submarine landslides can initiate tsunamis."
lyt.exportToPDF("Z:\\ACC PC\\ACC GIS\\Projects\\GISC_2435_Programming\\P1_Global_Natural_Hazards\\10_Deliverables\\2024_01_27_Byargeon_Programming_C1_Layout_Land_Slide")