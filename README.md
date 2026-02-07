🧠 AI Agents: Simple vs Distributed Workflows

This repository compares two ways to build AI agents:

Simple execution for fast development

Temporal-based distributed workflows for production reliability

The goal is to show how the same agent logic scales from prototype to enterprise-grade systems.

📂 Repository Overview
.
├── simple_agent/        # Basic AI agent demo
├── docker_monitor/      # DevOps-focused Docker monitoring agent
├── config.py
└── requirements.txt

🔄 Two Approaches
Approach	Best For
Simple Agent	Prototyping & local development
Temporal Agent	Production, retries, observability
🐳 Docker Container Health Monitor

AI-powered Docker monitoring with optional Temporal reliability.

📍 docker_monitor/

Key Features

Container status & health checks

CPU / memory monitoring

Log inspection

Automatic restarts

Natural language queries

Quick Start
cd docker_monitor
docker compose -f docker-compose.demo.yml up -d
python docker_agent.py


Temporal version:

temporal server start-dev
python docker_worker.py
python docker_client.py

⚙️ Simple Agent Demo

Basic agent showcasing the Temporal execution pattern.

📍 simple_agent/

Example Queries

“What time is it?”

“List Python files”

“What’s the weather in Tokyo?”

cd simple_agent
python agent.py

🧩 Architecture

Simple

User → Agent → Tools → Result


Temporal

User → Client → Temporal → Worker → Activities → Result

✅ Why Temporal?

Automatic retries

Fault tolerance

Full execution history

Distributed execution

Monitoring UI → http://localhost:8233

🛠 Requirements

Python 3.8+

Docker

AWS Bedrock access

Temporal CLI

pip install -r requirements.txt
aws configure

🎯 Key Idea

Build fast with the simple agent.
Scale safely with Temporal when reliability matters.

Same logic. Different execution model.
