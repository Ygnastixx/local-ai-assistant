# Local AI Assistant (Prototype)

Prototype d’assistant IA vocal offline en Python.

## Fonctionnalités actuelles
- STT offline avec Vosk
- Push-to-talk faible latence

## 🧠 Configuration du modèle STT (Vosk)

Le modèle Vosk n’est **pas inclus dans le dépôt** afin d’éviter de versionner des fichiers volumineux.

### 📥 Télécharger le modèle
Télécharge le modèle français léger :

- `vosk-model-small-fr-0.22`

Depuis le site officiel :  
https://alphacephei.com/vosk/models

### 📂 Placement du modèle
Après téléchargement, décompresse-le dans le dossier suivant :

```text
models/stt_models/vosk-model-small-fr-0.22/
```

La structure attendue doit être :

```text
project_root/
├── models/
│   └── stt_models/
│       └── vosk-model-small-fr-0.22/
├── core/
└── ...
```

### ⚠️ Important
Le projet utilise actuellement ce chemin par défaut :

```python
models/stt_models/vosk-model-small-fr-0.22/
```

Si tu utilises un autre modèle ou un autre emplacement, modifie :

```python
core/stt/vosk_stt.py
```

## Lancer
```bash
python core/stt/push_to_talk.py
````

Maintenir `space` pour parler.

## État du projet

En cours de développement (architecture en construction).
