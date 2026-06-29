import traceback
import os
import tempfile

import c4d


def _line(message):
    print("[verify_bitmap_shader] %s" % message)


def main():
    doc = c4d.documents.GetActiveDocument()
    mat = None
    shader = None

    doc.StartUndo()
    try:
        xbitmap_exists = hasattr(c4d, "Xbitmap")
        filename_exists = hasattr(c4d, "BITMAPSHADER_FILENAME")
        _line("Xbitmap hasattr=%s" % xbitmap_exists)
        if xbitmap_exists:
            _line("Xbitmap value=%s" % c4d.Xbitmap)
        _line("BITMAPSHADER_FILENAME hasattr=%s" % filename_exists)
        if filename_exists:
            _line("BITMAPSHADER_FILENAME value=%s" % c4d.BITMAPSHADER_FILENAME)

        mat = c4d.BaseMaterial(c4d.Mmaterial)
        mat.SetName("VERIFY_TMP_BitmapShader_Material")
        doc.InsertMaterial(mat)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, mat)

        shader = c4d.BaseShader(c4d.Xbitmap)
        shader.SetName("VERIFY_TMP_BitmapShader")
        mat.InsertShader(shader)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, shader)

        test_path_1 = os.path.join(tempfile.gettempdir(), "VERIFY_TMP_texture_a.png")
        test_path_2 = os.path.join(tempfile.gettempdir(), "VERIFY_TMP_texture_b.png")
        shader[c4d.BITMAPSHADER_FILENAME] = test_path_1
        mat[c4d.MATERIAL_COLOR_SHADER] = shader
        mat.SetChannelState(c4d.CHANNEL_COLOR, True)
        mat.Message(c4d.MSG_UPDATE)
        mat.Update(True, True)

        first = mat.GetFirstShader()
        _line("mat.GetFirstShader success=%s type=%s name=%s" % (first is not None, first.GetType() if first else None, first.GetName() if first else None))
        _line("first matches inserted shader=%s" % (first is not None and first.GetName() == shader.GetName()))
        _line("filename readback=%s" % shader[c4d.BITMAPSHADER_FILENAME])

        found = None
        current = mat.GetFirstShader()
        while current is not None:
            _line("walk shader name=%s type=%s" % (current.GetName(), current.GetType()))
            if current.GetType() == c4d.Xbitmap:
                found = current
                break
            current = current.GetNext()

        if found is not None:
            found[c4d.BITMAPSHADER_FILENAME] = test_path_2
            found.Message(c4d.MSG_UPDATE)
            mat.Message(c4d.MSG_UPDATE)
            mat.Update(True, True)
            _line("replacement readback=%s" % found[c4d.BITMAPSHADER_FILENAME])
    except Exception as exc:
        _line("ERROR %s: %s" % (type(exc).__name__, exc))
        print(traceback.format_exc())
    finally:
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
