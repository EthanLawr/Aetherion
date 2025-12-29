# Architecture Overview

This document provides a high-level overview of the architecture for the Aetherion Password Manager project. It outlines the main components, their responsibilities, and how they interact within the system.

## Table of Contents

- [1. Project Structure](#1-project-structure)
- [2. High-Level System Diagram](#2-high-level-system-diagram)
- [3. Core Components](#3-core-components)
  - [3.1 Frontend](#31-frontend)
  - [3.2 Backend Services](#32-backend-services)
  - [3.3 Crypto Engine](#33-crypto-engine)
  - [3.4 Storage Backend](#34-storage-backend)
- [4. Data Stores](#4-data-stores)
- [5. External Integrations / APIs](#5-external-integrations--apis)
- [6. Deployment & Infrastructure](#6-deployment--infrastructure)
- [7. Security Considerations](#7-security-considerations)
- [8. Development & Testing Environment](#8-development--testing-environment)
- [9. Future Considerations / Roadmap](#9-future-considerations--roadmap)
- [10. Project Identification](#10-project-identification)
- [11. Glossary / Acronyms](#11-glossary--acronyms)

## 1. Project Structure

This section provides a high-level overview of the project's directory and file structure, categorised by architectural layer or major functional area.

```py
[Project Root]/
├── docs/                 # Documentation files
│   ├── flowcharts/       # Flowchart diagrams
│   └── uml/              # UML diagrams
├── src/                  # Main application source code
│   ├── checker           # Password strength evaluation module
│   ├── generator         # Password generation module
│   └── manager           # Password management module
├── test/                 # Unit and integration tests
├── .env                  # Environment variables for local development
├── .gitignore            # Specifies intentionally untracked files to ignore
├── LICENSE               # License information
├── pyproject.toml        # Project metadata and dependencies
└── README.md             # Project overview and quick start guide
```

## 2. High-Level System Diagram

```haskell
[User]
   |
   v
[Password Manager]
   |         |
   v         v
[Password Generator]   [Password Checker]
       |
       v
[Crypto Engine]
       |
       v
[Encrypted Storage]
```

## 3. Core Components

### 3.1 Frontend

#### 3.1.1 CLI/Library Interface

Name: CLI/Library Interface Module

Description: The main user interface for interacting with the password manager, allowing users to generate, evaluate, and manage passwords.

Technologies: Python, Click (for CLI)

Deployment: Local module invoked by Aetherion

### 3.2 Backend Services

#### 3.2.1 Password Generator

Name: Password Generator Module

Description: Generates crpytographically secure passwords that respect configurable policies

Technologies: Python (secrets)

Deployment: Local module invoked by Password Manager Module

#### 3.2.2 Password Checker

Name: Password Strength Checker Module

Description: Evaluates password quality using entropy estimation and pattern detection.

Technologies: Python

Deployment: Local module invoked by Password Manager Module

#### 3.2.3 Password Manager

Name: Password Manager Module

Description: Coordinates password generation, strength evaluation, encryption, and storage. Delegates tasks to the Password Generator and Password Checker modules.

Technologies: Python (cryptography)

Deployment: Local module invoked by Aetherion.

### 3.3 Crypto Engine

Description: Handles key derivation and authenticated encryption of stored passwords

Technologies: AES-GCM

### 3.4 Storage Backend

Description: Abstract persistence layer. Responsible for storing encrypted passwords and metadata.

Technologies: File System, JSON, Binary Storage

## 4. Data Stores

### 4.1 Encrypted Credential Store

Name: Local Encrypted File Storage

Type: File-based Storage

Purpose: Persistant encrypted passwords and metadata securely at rest.

Key Data Objects:

- Credential Entries
- Salts and nonces

## 5. External Integrations / APIs

- None currently.

## 6. Deployment & Infrastructure

Cloud Provider: N/A (Local Application)

Key Services Used: N/A

CI/CD Pipeline: GitHub Actions for automated testing.

Monitoring & Logging: Standard output logging for CLI operations.

## 7. Security Considerations

Authentication: Master password-derived key

Authorization: Single-user, local access only

Data Encryption: AES-GCM

Key Security Tools/Practices:

- No plaintext storage of passwords
- Strict access controls on local files

## 8. Development & Testing Environment

Local Setup Instructions: [README](./README.md)

Testing Frameworks: Pytest

Code Quality Tools: Black, Ruff

## 9. Future Considerations / Roadmap

- Event-driven Audit Logging
- Migration Options
- Multi-device Sync
- Browser Extension

## 10. Project Identification

Project Name: Aetherion Password Manager

Repository URL: https://www.github.com/ethanlawrence/Aetherion-Password-Manager

Primary Contact/Team: Ethan Lawrence

Date of Last Update: 2025-12-29

## 11. Glossary / Acronyms

AES-GCM: Authenticated encryption algorithm providing confidentiality and integrity

CLI: Command Line Interface

Entropy: Measure of password unpredictability
