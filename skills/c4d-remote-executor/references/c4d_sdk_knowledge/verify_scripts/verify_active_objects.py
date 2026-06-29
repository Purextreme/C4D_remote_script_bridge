import traceback

import c4d


def _line(message):
    print("[verify_active_objects] %s" % message)


def main():
    doc = c4d.documents.GetActiveDocument()
    created = []

    doc.StartUndo()
    try:
        flag_exists = hasattr(c4d, "GETACTIVEOBJECTFLAGS_0")
        _line("GETACTIVEOBJECTFLAGS_0 hasattr=%s" % flag_exists)
        flags = c4d.GETACTIVEOBJECTFLAGS_0 if flag_exists else 0
        _line("flags value=%s" % flags)

        for index, x in enumerate((-200, 0, 200), 1):
            obj = c4d.BaseObject(c4d.Ocube)
            obj.SetName("VERIFY_TMP_Selected_%d" % index)
            obj.SetRelPos(c4d.Vector(x, 0, 0))
            doc.InsertObject(obj)
            doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)
            created.append(obj)

        doc.SetActiveObject(None, c4d.SELECTION_NEW)
        for obj in created:
            doc.SetActiveObject(obj, c4d.SELECTION_ADD)

        selected = doc.GetActiveObjects(flags)
        _line("selected type=%s count=%d" % (type(selected).__name__, len(selected)))
        _line("selected names=%s" % [obj.GetName() for obj in selected])
        selected_names = set(obj.GetName() for obj in selected)
        created_names = set(obj.GetName() for obj in created)
        _line("expected all selected=%s" % (selected_names == created_names))
    except Exception as exc:
        _line("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
        for obj in list(created):
            if obj is not None and obj.GetDocument() is not None:
                doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
                obj.Remove()
        doc.EndUndo()
        c4d.EventAdd()
        _line("cleanup objects=removed")


try:
    main()
except Exception as exc:
    _line("FATAL %s: %s" % (type(exc).__name__, exc))
    print(traceback.format_exc())
