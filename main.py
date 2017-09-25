import Rhino
import clr
from System.Collections.Generic import List
#clr.AddReference(
#clr.AddReferenceByName("geom")
#clr.Reference("geom")
#geom = Rhino.Geometry.GeometryBase()
#List<Rhino.Geometry.GeometryBase> geom = new List<Rhino.Geometry.GeometryBase>()

filter = Rhino.DocObjects.ObjectType.Brep

objref = clr.Reference[Rhino.DocObjects.ObjRef]()
object = Rhino.Input.RhinoGet.GetOneObject("Get It!", False, filter, objref)

viewport = Rhino.Display.RhinoViewport()
print "git test"
options = Rhino.Geometry.HiddenLineDrawingParameters()
options.SetViewport(viewport)
options.AddGeometry(objref.Geometry(),"")

drawing = Rhino.Geometry.HiddenLineDrawing.Compute(options, True)

print drawing
