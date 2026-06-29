import traceback

import c4d


def _line(message):
    print("[verify_stop_all_threads] %s" % message)


def _create_and_remove(doc, name, call_stop_all_threads):
    obj = None
    if call_stop_all_threads:
        c4d.StopAllThreads()
    obj = c4d.BaseObject(c4d.Ocube)
    obj.SetName(name)
    doc.InsertObject(obj)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)
    inserted = obj.GetDocument() is not None
    doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
    obj.Remove()
    return inserted


def main():
    doc = c4d.documents.GetActiveDocument()
    _line("StopAllThreads hasattr=%s" % hasattr(c4d, "StopAllThreads"))

    doc.StartUndo()
    try:
        without_stop = _create_and_remove(doc, "VERIFY_TMP_NoStopAllThreads", False)
        _line("create/remove without StopAllThreads inserted=%s" % without_stop)

        if hasattr(c4d, "StopAllThreads"):
            with_stop = _create_and_remove(doc, "VERIFY_TMP_WithStopAllThreads", True)
            _line("create/remove with StopAllThreads inserted=%s" % with_stop)
    except Exception as exc:
        _line("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
        doc.EndUndo()
        c4d.EventAdd()


try:
    main()
except Exception as exc:
    _line("FATAL %s: %s" % (type(exc).__name__, exc))
    print(traceback.format_exc())
