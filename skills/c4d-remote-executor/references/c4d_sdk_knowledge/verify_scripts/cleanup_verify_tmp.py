import traceback

import c4d


PREFIX = "VERIFY_TMP_"


def _line(message):
    print("[cleanup_verify_tmp] %s" % message)


def _walk_objects(root):
    current = root
    while current is not None:
        next_obj = current.GetNext()
        child = current.GetDown()
        yield current
        if child is not None:
            for item in _walk_objects(child):
                yield item
        current = next_obj


def _remove_named_chain(doc, first, label):
    removed = 0
    node = first
    while node is not None:
        next_node = node.GetNext()
        if node.GetName().startswith(PREFIX):
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, node)
            node.Remove()
            removed += 1
        node = next_node
    _line("%s removed=%d" % (label, removed))


def main():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    try:
        removed_objects = 0
        for obj in list(_walk_objects(doc.GetFirstObject())):
            if obj.GetName().startswith(PREFIX):
                doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
                obj.Remove()
                removed_objects += 1
        _line("objects removed=%d" % removed_objects)

        _remove_named_chain(doc, doc.GetFirstMaterial(), "materials")

        root = doc.GetLayerObjectRoot()
        _remove_named_chain(doc, root.GetDown() if root else None, "layers")
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
