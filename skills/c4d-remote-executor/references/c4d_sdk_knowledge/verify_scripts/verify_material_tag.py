import traceback

import c4d


def _line(message):
    print("[verify_material_tag] %s" % message)


def _constant(name):
    exists = hasattr(c4d, name)
    _line("%s hasattr=%s" % (name, exists))
    if not exists:
        return None
    value = getattr(c4d, name)
    _line("%s value=%s" % (name, value))
    return value


def main():
    doc = c4d.documents.GetActiveDocument()
    mat = None
    obj = None
    tex_tag = None
    phong_tag = None

    doc.StartUndo()
    try:
        material_type = _constant("Mmaterial")
        texture_tag_type = _constant("Ttexture")
        phong_tag_type = _constant("Tphong")

        if material_type is not None:
            mat = c4d.BaseMaterial(material_type)
            _line("BaseMaterial(Mmaterial) success=%s type=%s" % (mat is not None, mat.GetType() if mat else None))
            if mat is not None:
                mat.SetName("VERIFY_TMP_Material")
                doc.InsertMaterial(mat)
                doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, mat)
                _line("InsertMaterial valid=%s name=%s" % (mat.GetDocument() is not None, mat.GetName()))

        if texture_tag_type is not None:
            tex_tag = c4d.BaseTag(texture_tag_type)
            _line("BaseTag(Ttexture) success=%s type=%s" % (tex_tag is not None, tex_tag.GetType() if tex_tag else None))

        if phong_tag_type is not None:
            phong_tag = c4d.BaseTag(phong_tag_type)
            _line("BaseTag(Tphong) success=%s type=%s" % (phong_tag is not None, phong_tag.GetType() if phong_tag else None))

        obj = c4d.BaseObject(c4d.Ocube)
        obj.SetName("VERIFY_TMP_MaterialTag_Cube")
        doc.InsertObject(obj)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)

        if mat is not None and tex_tag is not None:
            tex_tag.SetMaterial(mat)
            obj.InsertTag(tex_tag)
            doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, tex_tag)
            _line("TextureTag inserted=%s material_name=%s" % (tex_tag.GetObject() is not None, tex_tag.GetMaterial().GetName() if tex_tag.GetMaterial() else None))
            tex_tag = None

        if phong_tag is not None:
            obj.InsertTag(phong_tag)
            doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, phong_tag)
            _line("PhongTag inserted=%s" % (phong_tag.GetObject() is not None))
            phong_tag = None
    except Exception as exc:
        _line("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
        if obj is not None and obj.GetDocument() is not None:
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
            obj.Remove()
            _line("cleanup object=removed")
        if mat is not None and mat.GetDocument() is not None:
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, mat)
            mat.Remove()
            _line("cleanup material=removed")
        doc.EndUndo()
        c4d.EventAdd()


try:
    main()
except Exception as exc:
    _line("FATAL %s: %s" % (type(exc).__name__, exc))
    print(traceback.format_exc())
