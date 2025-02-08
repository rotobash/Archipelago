
import json
import pkgutil


def load_check_json(is_location, filename):
    if is_location:
        fp = f"locations/{filename}"
    else:
        fp = f"items/{filename}"

    data = pkgutil.get_data(__name__, "data/" + fp).decode("utf-8-sig")
    return json.loads(data)

def load_region_json(filename):
    data = pkgutil.get_data(__name__, "data/" + filename).decode("utf-8-sig")
    return json.loads(data)