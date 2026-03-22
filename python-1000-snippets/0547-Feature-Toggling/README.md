# Feature Toggling

## Description
Demonstrates runtime feature flag checks and state persistence.

## Samples
- `SAMPLES/sample1.py`: return enabled/disabled for flags.
- `SAMPLES/sample2.py`: toggle value at runtime and then query.
- `SAMPLES/sample3.py`: log toggle updates to `temp/0547_toggle_status.txt`.

## Output
- `sample1.py`: flag states for both features.
- `sample2.py`: updated flag status change.
- `sample3.py`: file write and content output.

## Explanation
Feature toggles enable safe deployments and gradual rollout by turning features on/off in config.
