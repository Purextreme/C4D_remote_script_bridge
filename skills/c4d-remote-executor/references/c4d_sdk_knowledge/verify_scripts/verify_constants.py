import traceback

import c4d


def _line(message):
    print("[verify_constants] %s" % message)


def _verify_object_constant(doc, name):
    exists = hasattr(c4d, name)
    _line("%s hasattr=%s" % (name, exists))
    if not exists:
        return

    value = getattr(c4d, name)
    _line("%s value=%s" % (name, value))

    obj = None
    try:
        obj = c4d.BaseObject(value)
        _line("%s BaseObject success=%s type=%s" % (name, obj is not None, obj.GetType() if obj else None))
        if obj is None:
            return

        obj.SetName("VERIFY_TMP_%s" % name)
        doc.InsertObject(obj)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)
        _line("%s inserted valid=%s name=%s" % (name, obj.GetDocument() is not None, obj.GetName()))
    except Exception as exc:
        _line("%s ERROR %s: %s" % (name, type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
        if obj is not None and obj.GetDocument() is not None:
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
            obj.Remove()
            _line("%s cleanup=removed" % name)


def main():
    doc = c4d.documents.GetActiveDocument()
    names = ["Oplane", "Osphere", "Ocube", "Ocylinder", "Otorus", "Onull"]

    doc.StartUndo()
    try:
        for name in names:
            _verify_object_constant(doc, name)
    finally:
        doc.EndUndo()
        c4d.EventAdd()


try:
    main()
except Exception as exc:
    _line("FATAL %s: %s" % (type(exc).__name__, exc))
    print(traceback.format_exc())
