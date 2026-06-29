import traceback

import c4d


PREFIX = "Verified_Demo_"


def log(message):
    print("[create_verified_cheatsheet_demo] %s" % message)


def make_material(doc, name):
    mat = c4d.BaseMaterial(c4d.Mmaterial)
    mat.SetName(PREFIX + name)
    doc.InsertMaterial(mat)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, mat)
    return mat


def make_layer(doc, name):
    root = doc.GetLayerObjectRoot()
    layer = c4d.documents.LayerObject()
    layer.SetName(PREFIX + name)
    layer.InsertUnder(root)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, layer)
    return layer


def make_object(doc, obj_type, name, pos, parent, mat, layer):
    obj = c4d.BaseObject(obj_type)
    obj.SetName(PREFIX + name)
    obj.SetRelPos(pos)
    doc.InsertObject(obj, parent)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)

    tag = c4d.BaseTag(c4d.Ttexture)
    tag.SetMaterial(mat)
    obj.InsertTag(tag)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, tag)

    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
    obj.SetLayerObject(layer)
    return obj


def main():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    try:
        layer_geo = make_layer(doc, "Layer_Geometry")
        layer_round = make_layer(doc, "Layer_Round_Objects")

        mat_a = make_material(doc, "Material_A")
        mat_b = make_material(doc, "Material_B")

        group = c4d.BaseObject(c4d.Onull)
        group.SetName(PREFIX + "Group_Null")
        doc.InsertObject(group)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, group)
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, group)
        group.SetLayerObject(layer_geo)

        created = [
            make_object(doc, c4d.Ocube, "Cube", c4d.Vector(-300, 0, 0), group, mat_a, layer_geo),
            make_object(doc, c4d.Oplane, "Plane", c4d.Vector(0, -120, 0), group, mat_a, layer_geo),
            make_object(doc, c4d.Ocylinder, "Cylinder", c4d.Vector(300, 0, 0), group, mat_a, layer_geo),
            make_object(doc, c4d.Osphere, "Sphere", c4d.Vector(-150, 180, 0), group, mat_b, layer_round),
            make_object(doc, c4d.Otorus, "Torus", c4d.Vector(150, 180, 0), group, mat_b, layer_round),
        ]

        doc.SetActiveObject(group, c4d.SELECTION_NEW)
        log("created group=%s" % group.GetName())
        log("created objects=%s" % [obj.GetName() for obj in created])
        log("created materials=%s" % [mat_a.GetName(), mat_b.GetName()])
        log("created layers=%s" % [layer_geo.GetName(), layer_round.GetName()])
    except Exception as exc:
        log("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
        raise
    finally:
        doc.EndUndo()
        c4d.EventAdd()


main()
