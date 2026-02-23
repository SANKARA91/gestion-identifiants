# 🔐 Gestionnaire d'Identifiants Sécurisé

> Application web de gestion d'identifiants déployée sur Kubernetes (AKS)  
> **Projet portfolio — Boureima SANKARA | Ingénieur Systèmes & Sécurité Cloud**

---

## 📋 Description

Application web sécurisée permettant de stocker et gérer des identifiants (site, login, mot de passe).  
Les mots de passe sont **chiffrés avec Fernet** avant d'être stockés en base de données PostgreSQL.

---

## 🏗️ Architecture

```
Internet
    │
    ▼
LoadBalancer (Azure)
    │
    ▼
┌─────────────────────────────────────┐
│         Kubernetes (AKS)            │
│                                     │
│  ┌─────────────────┐               │
│  │   Flask App     │               │
│  │   (Python)      │──────────┐    │
│  └─────────────────┘          │    │
│                                ▼    │
│  ┌─────────────────┐  ┌────────────┐│
│  │   PostgreSQL    │  │  PVC 1Gi   ││
│  │   (Base de      │◄─│  (Volume   ││
│  │    données)     │  │ persistant)││
│  └─────────────────┘  └────────────┘│
└─────────────────────────────────────┘
```

---

## ✅ Fonctionnalités

- ➕ Ajouter des identifiants (site, login, mot de passe)
- 👁️ Afficher les identifiants (mot de passe flouté par défaut)
- 🗑️ Supprimer des identifiants
- 🔐 Chiffrement des mots de passe avec **Fernet (cryptography)**
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
| Package Manager K8s | Helm |
| CI/CD | GitHub Actions |
| Cloud | Microsoft Azure |
| IaC | Terraform |

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

### Désinstallation

```bash
helm uninstall gestion-identifiants
```

---

## ⚙️ CI/CD Pipeline

À chaque `git push` sur la branche `master`, GitHub Actions :

1. **Build** l'image Docker automatiquement
2. **Push** l'image sur Docker Hub avec le tag `latest` et le SHA du commit
3. L'image est disponible sur [Docker Hub](https://hub.docker.com/r/sankara973/gestion-identifiants)

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
- ✅ Images Docker versionnées et auditables

---

## 👨‍💻 Auteur

**Boureima SANKARA**  
Ingénieur Systèmes & Sécurité Cloud  
📧 brsankara7@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/boureima-sankara)  
🐙 [GitHub](https://github.com/SANKARA91)

---

## 📄 Licence

Ce projet est open source — libre d'utilisation à des fins éducatives.