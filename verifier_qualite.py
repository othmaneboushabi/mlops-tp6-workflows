import json
import sys

import yaml


with open("reports/metrics.json", encoding="utf-8") as file:
    f1 = json.load(file)["f1"]
with open("params.yaml", encoding="utf-8") as file:
    seuil = yaml.safe_load(file)["validation"]["seuil_f1"]

print(f"F1 = {f1} | seuil = {seuil}")
if f1 < seuil:
    print("ECHEC : modele refuse")
    sys.exit(1)
print("OK : modele accepte")
