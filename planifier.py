from flow_mlops import reentrainement


if __name__ == "__main__":
    reentrainement.serve(name="hebdomadaire", cron="0 6 * * 1")
