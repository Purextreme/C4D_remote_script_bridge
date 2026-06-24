import c4d


doc = c4d.documents.GetActiveDocument()
cube = c4d.BaseObject(c4d.Ocube)
cube.SetName("Remote_Test_Cube")
doc.InsertObject(cube)
c4d.EventAdd()
