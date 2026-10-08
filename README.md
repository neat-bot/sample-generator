# sample-generator

A minimal kadet generator used to test the kadet-hub/registry gate. It renders
one ConfigMap from `parameters.sample`.

```yaml
parameters:
  sample:
    name: demo
    data:
      key: value
  kapitan:
    compile:
      - output_path: manifests
        input_type: kadet
        input_paths:
          - lib/sample-generator
        output_type: yaml
```
