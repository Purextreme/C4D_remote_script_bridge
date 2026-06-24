import math

import c4d


PREFIX = "Remote_Demo_"


def iter_objects(root):
    obj = root
    while obj is not None:
        yield obj
        child = obj.GetDown()
        if child is not None:
            for child_obj in iter_objects(child):
                yield child_obj
        obj = obj.GetNext()


def remove_existing(doc):
    objects = list(iter_objects(doc.GetFirstObject()))
    for obj in objects:
        if obj.GetName().startswith(PREFIX):
            obj.Remove()

    mat = doc.GetFirstMaterial()
    while mat is not None:
        next_mat = mat.GetNext()
        if mat.GetName().startswith(PREFIX):
            mat.Remove()
        mat = next_mat


def make_material(doc, name, color):
    mat = c4d.BaseMaterial(c4d.Mmaterial)
    mat.SetName(PREFIX + name)
    mat[c4d.MATERIAL_COLOR_COLOR] = color
    doc.InsertMaterial(mat)
    return mat


def add_texture_tag(obj, mat):
    tag = c4d.TextureTag()
    tag.SetMaterial(mat)
    obj.InsertTag(tag)


def add_object(doc, type_id, name, pos, scale, mat):
    obj = c4d.BaseObject(type_id)
    obj.SetName(PREFIX + name)
    obj.SetAbsPos(pos)
    obj.SetAbsScale(scale)
    add_texture_tag(obj, mat)
    doc.InsertObject(obj)
    return obj


doc = c4d.documents.GetActiveDocument()
remove_existing(doc)

red = make_material(doc, "Red", c4d.Vector(1.0, 0.12, 0.08))
blue = make_material(doc, "Blue", c4d.Vector(0.08, 0.28, 1.0))
green = make_material(doc, "Green", c4d.Vector(0.1, 0.75, 0.25))
yellow = make_material(doc, "Yellow", c4d.Vector(1.0, 0.78, 0.08))

add_object(
    doc,
    c4d.Ocube,
    "Cube",
    c4d.Vector(-220, 0, 0),
    c4d.Vector(1.2, 1.2, 1.2),
    red,
)
add_object(
    doc,
    c4d.Osphere,
    "Sphere",
    c4d.Vector(0, 0, 0),
    c4d.Vector(1.1, 1.1, 1.1),
    blue,
)
add_object(
    doc,
    c4d.Ocone,
    "Cone",
    c4d.Vector(220, 0, 0),
    c4d.Vector(1.0, 1.35, 1.0),
    green,
)

floor = add_object(
    doc,
    c4d.Oplane,
    "Plane",
    c4d.Vector(0, -105, 0),
    c4d.Vector(5.0, 1.0, 2.8),
    yellow,
)
floor[c4d.PRIM_PLANE_WIDTH] = 520
floor[c4d.PRIM_PLANE_HEIGHT] = 300

light = c4d.BaseObject(c4d.Olight)
light.SetName(PREFIX + "Key_Light")
light.SetAbsPos(c4d.Vector(-300, 420, -250))
doc.InsertObject(light)

camera = c4d.BaseObject(c4d.Ocamera)
camera.SetName(PREFIX + "Camera")
camera.SetAbsPos(c4d.Vector(0, 230, -650))
camera.SetAbsRot(c4d.Vector(math.radians(-20), 0, 0))
doc.InsertObject(camera)
doc.SetActiveObject(camera)

bd = doc.GetActiveBaseDraw()
if bd is not None:
    bd.SetSceneCamera(camera)

c4d.EventAdd()
