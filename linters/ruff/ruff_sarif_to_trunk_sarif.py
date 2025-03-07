#!/usr/bin/env python3

import json
import sys

results = []
for run in json.load(sys.stdin).get("runs", []):
    for result in run.get("results", []):
        # Ruff will set code to null for syntax errors
        if result["ruleId"] is None:
            result["ruleId"] = "E999"
        results.append(result)

sarif = {
    "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
    "version": "2.1.0",
    "runs": [{"results": results}],
}

print(json.dumps(sarif, indent=2))
