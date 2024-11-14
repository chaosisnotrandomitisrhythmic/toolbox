# Utility Script Toolbox

*A collection of utilities designed to simplify tasks and enhance the workflow.*

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Utilities Overview](#utilities-overview)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

---

## Introduction

The Utility Script Toolbox provides an assortment of scripts, from cloud operations to system management, curated to optimize routine tasks for developers and sysadmins alike.

---

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chaosisnotrandomitisrhythmic/toolbox.git
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

## Utilities Overview

### Authentication (`/auth`)
- [`generate_jwt_token.py`](./auth/generate_jwt_token.py): Generate and decode JWT tokens for authentication purposes.

### Data Processing (`/data`)
- [`multi_label_split.py`](./data/multi_label_split.py): Perform stratified train-test splits for multi-label datasets while preserving label distributions.

### OpenAI Integration (`/openai`)
- [`create_embedding.py`](./openai/create_embedding.py): Generate text embeddings using OpenAI's embedding models.

### AWS Utilities (`/aws`)
- [`stop_ec2_instances.sh`](./aws/stop_ec2_instances.sh): A script to identify and stop running EC2 instances.

## Contribution Guidelines
We're always open to contributions to the Utility Script Toolbox. Whether you're enhancing an existing script, introducing a new one, or even just offering documentation improvements, we appreciate your effort.