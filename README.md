# 🔐 Gestionnaire d'Identifiants Sécurisé

> Application web de gestion d'identifiants déployée sur Kubernetes (AKS)  
> **Projet portfolio — Boureima SANKARA | Ingénieur DevOps & Sécurité Cloud**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)
![Docker](https://img.shields.io/badge/Docker-28.x-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-AKS-326CE5?logo=kubernetes)
![Helm](https://img.shields.io/badge/Helm-4.x-0F1689?logo=helm)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?logo=github-actions)

---

## 📋 Description

Application web sécurisée permettant de stocker et gérer des identifiants (site, login, mot de passe).  
Les mots de passe sont **chiffrés avec Fernet** avant d'être stockés en base de données PostgreSQL.  
Déployée sur **Azure Kubernetes Service (AKS)** via **Helm Chart**, avec pipeline **CI/CD GitHub Actions**.

---

## 🏗️ Architecture

```
Internet
    │
    ▼
LoadBalancer (Azure)
    │
    ▼
┌─────────────────────────────────────────┐
│           Kubernetes AKS                │
│                                         │
│  ┌──────────────────┐                  │
│  │  Flask App (v3)  │                  │
│  │  Python 3.11     │────────────┐     │
│  └──────────────────┘            │     │
│           │                      ▼     │
│           │             ┌─────────────┐│
│           │             │  PVC 1Gi    ││
│           ▼             │  (Persistant││
│  ┌──────────────────┐   └─────────────┘│
│  │   PostgreSQL 15  │◄───────┘         │
│  └──────────────────┘                  │
└─────────────────────────────────────────┘
```

---

## ✅ Fonctionnalités

- ➕ Ajouter des identifiants (site, login, mot de passe)
- 👁️ Afficher les identifiants (mot de passe flouté par défaut, visible au survol)
- 🗑️ Supprimer des identifiants
- 🔐 Chiffrement des mots de passe avec **Fernet**
- 💾 Persistance des données avec **PostgreSQL + Volume persistant**

---

## 🛠️ Stack technique

| Composant | Technologie |
|-----------|-------------|
| Backend | Python 3.11 / Flask |
| Base de données | PostgreSQL 15 |
| Chiffrement | Fernet (cryptography) |
| Containerisation | Docker |
| Orchestration | Kubernetes (AKS) |
| Package Manager K8s | Helm v4 |
| CI/CD | GitHub Actions |
| Cloud | Microsoft Azure |
| Registry | Docker Hub |

---

## 🚀 Déploiement avec Helm

### Prérequis

- [Docker](https://docker.com)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh)
- [Azure CLI](https://aka.ms/installazurecliwindows)
- Un cluster AKS actif

### Installation

```bash
# 1. Cloner le repository
git clone https://github.com/SANKARA91/gestion-identifiants.git
cd gestion-identifiants

# 2. Se connecter au cluster AKS
az aks get-credentials --resource-group rg-azure-infra-terraform --name aks-cluster-main

# 3. Déployer avec Helm
helm install gestion-identifiants helm/gestion-identifiants

# 4. Récupérer l'IP externe
kubectl get service gestion-identifiants
```

### Mise à jour

```bash
helm upgrade gestion-identifiants helm/gestion-identifiants
```

### Désinstallation

```bash
helm uninstall gestion-identifiants
```

---

## ⚙️ CI/CD Pipeline

À chaque `git push` sur `master`, GitHub Actions :

1. 🔨 **Build** l'image Docker automatiquement
2. 🔐 **Login** sur Docker Hub via secrets GitHub
3. 🚀 **Push** l'image avec les tags `latest` et SHA du commit

```yaml
# .github/workflows/docker-build.yml
on:
  push:
    branches: [master]
```

Image disponible sur : [hub.docker.com/r/sankara973/gestion-identifiants](https://hub.docker.com/r/sankara973/gestion-identifiants)

---

## 📁 Structure du projet

```
gestion-identifiants/
├── .github/
│   └── workflows/
│       └── docker-build.yml    # Pipeline CI/CD
├── app/
│   ├── templates/
│   │   └── index.html          # Interface web
│   ├── app.py                  # Application Flask
│   └── requirements.txt        # Dépendances Python
├── helm/
│   └── gestion-identifiants/
│       ├── templates/
│       │   ├── deployment.yaml # Déploiement app
│       │   ├── service.yaml    # Service LoadBalancer
│       │   └── postgres.yaml   # PostgreSQL + PVC
│       ├── Chart.yaml          # Metadata du chart
│       └── values.yaml         # Configuration
├── kubernetes/                 # Fichiers YAML bruts
├── Dockerfile                  # Image Docker
└── README.md
```

---

## 🔐 Sécurité

- ✅ Mots de passe chiffrés avec **Fernet** (chiffrement symétrique)
- ✅ Base de données isolée dans le cluster Kubernetes
- ✅ Volume persistant pour la durabilité des données
- ✅ Images Docker versionnées par SHA de commit
- ✅ Secrets GitHub Actions pour les credentials Docker Hub
- 
---

## 🔧 Configuration Helm

```yaml
# helm/gestion-identifiants/values.yaml
app:
  image:
    repository: sankara973/gestion-identifiants
    tag: latest
  replicas: 1

postgres:
  image: postgres:15
  storage: 1Gi
```

---

## 👨‍💻 Auteur

**Boureima SANKARA**  
Ingénieur DevOps & Sécurité Cloud  
📧 brsankara7@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/boureima-sankara)  
🐙 [GitHub](https://github.com/SANKARA91)  
🐳 [Docker Hub](https://hub.docker.com/r/sankara973/gestion-identifiants)

---

## 📄 Licence

Ce projet est open source — libre d'utilisation à des fins éducatives.