import traceback

import c4d


def _line(message):
    print("[verify_layers] %s" % message)


def main():
    doc = c4d.documents.GetActiveDocument()
    obj = None
    layer = None

    doc.StartUndo()
    try:
        root = doc.GetLayerObjectRoot()
        _line("GetLayerObjectRoot success=%s type=%s" % (root is not None, type(root).__name__ if root else None))

        layer = c4d.documents.LayerObject()
        layer.SetName("VERIFY_TMP_Layer")
        layer.InsertUnder(root)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, layer)
        _line("LayerObject created type=%s name=%s has_parent=%s" % (type(layer).__name__, layer.GetName(), layer.GetUp() is not None))

        obj = c4d.BaseObject(c4d.Ocube)
        obj.SetName("VERIFY_TMP_Layer_Cube")
        doc.InsertObject(obj)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)

        has_set_layer = hasattr(obj, "SetLayerObject")
        _line("obj.SetLayerObject hasattr=%s" % has_set_layer)
        if has_set_layer:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
            result = obj.SetLayerObject(layer)
            got = obj.GetLayerObject(doc) if hasattr(obj, "GetLayerObject") else None
            _line("SetLayerObject result=%s assigned_layer_name=%s" % (result, got.GetName() if got else None))
    except Exception as exc:
        _line("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
        if obj is not None and obj.GetDocument() is not None:
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
            obj.Remove()
            _line("cleanup object=removed")
        if layer is not None:
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, layer)
            layer.Remove()
            _line("cleanup layer=removed")
        doc.EndUndo()
        c4d.EventAdd()


try:
    main()
except Exception as exc:
    _line("FATAL %s: %s" % (type(exc).__name__, exc))
    print(traceback.format_exc())
