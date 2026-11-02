import json
import subprocess
import sys

import yaml
from prefect import flow, get_run_logger, task


@task(retries=2, retry_delay_seconds=10)
def rejouer_pipeline():
    result = subprocess.run(
        [sys.executable, "-m", "dvc", "repro"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    logger = get_run_logger()
    logger.info(result.stdout[-1500:])
    if result.returncode != 0:
        raise RuntimeError(result.stderr[-800:])
    return "pipeline rejoue"


@task
def lire_metriques():
    with open("reports/metrics.json", encoding="utf-8") as file:
        return json.load(file)


@task
def valider(metrics):
    with open("params.yaml", encoding="utf-8") as file:
        seuil = yaml.safe_load(file)["validation"]["seuil_f1"]
    if metrics["f1"] < seuil:
        raise ValueError(f"F1 {metrics['f1']} < seuil {seuil} : modele refuse")
    get_run_logger().info(
        f"F1 {metrics['f1']} >= seuil {seuil} : modele accepte"
    )
    return True


@task
def notifier(metrics):
    get_run_logger().info(
        f"NOTIFICATION equipe : nouveau modele valide, F1 = {metrics['f1']}"
    )


@flow(name="reentrainement-fraude", log_prints=True)
def reentrainement():
    rejouer_pipeline()
    metrics = lire_metriques()
    valider(metrics)
    notifier(metrics)


if __name__ == "__main__":
    reentrainement()
