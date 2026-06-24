import c4d


def has_selected_ancestor(obj, selected):
    parent = obj.GetUp()
    while parent is not None:
        if parent in selected:
            return True
        parent = parent.GetUp()
    return False


doc = c4d.documents.GetActiveDocument()
selected = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
selected_set = set(selected)
roots = [obj for obj in selected if not has_selected_ancestor(obj, selected_set)]

if roots:
    doc.StartUndo()
    try:
        for obj in roots:
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
            obj.Remove()
    finally:
        doc.EndUndo()

c4d.EventAdd()
print("Deleted %d selected object(s)." % len(roots))
