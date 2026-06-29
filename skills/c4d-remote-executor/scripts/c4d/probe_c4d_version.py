import json

import c4d


def _call_optional(name):
    func = getattr(c4d, name, None)
    if func is None:
        return None
    try:
        return func()
    except Exception as exc:
        return "ERROR: %s" % exc


def _parse_version(raw):
    if not isinstance(raw, int):
        return None

    text = str(raw)
    if text.startswith("20") and len(text) >= 5:
        major = int(text[:4])
        minor = int(text[4]) if len(text) >= 5 else 0
        return "%d.%d" % (major, minor)

    return None


def _sdk_hint(version):
    if not version:
        return "https://developers.maxon.net/docs/py/"

    major = version.split(".", 1)[0]
    if major == "2024":
        return "https://developers.maxon.net/docs/py/2024_4_0a/index.html"

    return "https://developers.maxon.net/docs/py/"


raw_version = _call_optional("GetC4DVersion")
version = _parse_version(raw_version)
payload = {
    "c4d_version_raw": raw_version,
    "c4d_version": version,
    "version_type": _call_optional("GeGetVersionType"),
    "sdk_docs_hint": _sdk_hint(version),
}

print(json.dumps(payload, indent=2, sort_keys=True))
