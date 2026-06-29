import traceback

import c4d


def _line(message):
    print("[verify_document_methods] %s" % message)


def main():
    doc = c4d.documents.GetActiveDocument()
    mats = []

    doc.StartUndo()
    try:
        exists = hasattr(doc, "GetMaterials")
        _line("doc.GetMaterials hasattr=%s" % exists)

        for index in range(2):
            mat = c4d.BaseMaterial(c4d.Mmaterial)
            mat.SetName("VERIFY_TMP_DocMaterial_%d" % (index + 1))
            doc.InsertMaterial(mat)
            doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, mat)
            mats.append(mat)

        if exists:
            all_mats = doc.GetMaterials()
            _line("GetMaterials type=%s len=%d" % (type(all_mats).__name__, len(all_mats)))
            result_names = [mat.GetName() for mat in all_mats]
            temp_names = [mat.GetName() for mat in mats]
            _line("contains temp mats=%s" % all(name in result_names for name in temp_names))
            _line("temp names in result=%s" % [name for name in result_names if name in temp_names])

        first = doc.GetFirstMaterial()
        traversed = []
        while first is not None:
            traversed.append(first)
            first = first.GetNext()
        traversed_names = [mat.GetName() for mat in traversed]
        temp_names = [mat.GetName() for mat in mats]
        _line("GetFirstMaterial traversal len=%d contains temp mats=%s" % (len(traversed), all(name in traversed_names for name in temp_names)))
    except Exception as exc:
        _line("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
        for mat in list(mats):
            if mat is not None and mat.GetDocument() is not None:
                doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, mat)
                mat.Remove()
        doc.EndUndo()
        c4d.EventAdd()
        _line("cleanup materials=removed")


try:
    main()
except Exception as exc:
    _line("FATAL %s: %s" % (type(exc).__name__, exc))
    print(traceback.format_exc())
