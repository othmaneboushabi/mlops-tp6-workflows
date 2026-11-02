# Orchestrateur ou intégration continue ? (TP06)

| Critère | Prefect (orchestrateur) | GitHub Actions (CI) |
|---|---|---|
| Ce qui déclenche l'exécution | Planning hebdomadaire, interface ou API | Push Git ou bouton `Run workflow` |
| Où s'exécute le traitement | Machine locale via serveur, serve ou worker | Runner Linux éphémère de GitHub |
| Qui surveille, et où | Équipe via l'interface Prefect | Équipe via l'onglet Actions |
| Ce qui se passe en cas d'échec | Le flow passe en échec et les tâches suivantes sont arrêtées | Le job passe en rouge et les étapes suivantes sont arrêtées |
| Type de tâche adapté | Réentraînement et exécution planifiée | Vérification automatique avant intégration |
| Ce qui est versionné dans Git | Code du flow et configuration du déploiement | Code, workflow YAML et script de contrôle |

Prefect orchestre les exécutions du pipeline et rend chaque tâche observable.
Sa planification permet de relancer régulièrement le réentraînement sans intervention.
La règle de qualité bloque le flow si le F1 est inférieur au seuil configuré.
GitHub Actions vérifie chaque modification sur un environnement propre et reproductible.
Les deux outils sont complémentaires : CI pour valider le code, Prefect pour exploiter le pipeline.
