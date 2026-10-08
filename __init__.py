from kapitan.inputs.kadet import BaseObj, inventory


def main(input_params=None):
    params = inventory().parameters.get("sample", {})
    obj = BaseObj()
    obj.root.configmap = {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {"name": params.get("name", "sample")},
        "data": dict(params.get("data", {})),
    }
    return obj
