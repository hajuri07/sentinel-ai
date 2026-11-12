# Sentinel AI 🛡️

### Agentic AI Reliability, Evaluation & Security Platform

Sentinel AI is a developer-focused platform designed to build, execute, evaluate, secure, and monitor LLM-powered AI agents.

As AI agents become increasingly autonomous and capable of interacting with external tools and systems, ensuring their reliability, security, and performance becomes essential.

Sentinel AI aims to address these challenges by providing a unified infrastructure for agent orchestration, evaluation, security testing, guardrails, and observability.

## Key Features

- **Agent Runtime:** Execute multi-step AI agent workflows with tool calling, state management, and controlled execution.
- **LLM Integration:** Centralized model communication through a provider-agnostic LLM abstraction.
- **MCP Integration:** Connect AI agents to external tools and services through the Model Context Protocol.
- **Evaluation Engine:** Evaluate agent responses, reasoning trajectories, tool selection, and task completion.
- **AI Guardrails:** Validate inputs and outputs, detect prompt injection attempts, and enforce execution policies.
- **Security Testing:** Test AI agents against adversarial inputs and common LLM security vulnerabilities.
- **Observability:** Track agent execution traces, latency, token consumption, errors, and model usage.
- **Developer Dashboard:** Visualize agent executions, evaluation results, security events, and performance metrics.

## Technology Stack

| Component | Technologies |
|---|---|
| Backend | Python, FastAPI |
| Agent Orchestration | LangGraph |
| LLM Integration | LiteLLM |
| Validation | Pydantic |
| MCP | Official MCP Python SDK |
| Evaluation | DeepEval, Ragas |
| Security | OWASP LLM Top 10, Garak, PyRIT |
| Observability | Langfuse, OpenTelemetry |
| Database | PostgreSQL |
| Frontend | React, TypeScript |
| Infrastructure | Docker, GitHub Actions, pytest |

## Architecture Philosophy

Sentinel AI follows a modular monolithic architecture, keeping its core components independently organized while maintaining a unified application.

The platform prioritizes:

- Modular and maintainable architecture.
- Provider-independent LLM integration.
- Controlled agent execution and tool permissions.
- Reproducible evaluation and security testing.
- Production-oriented observability and reliability.

## Project Status

**Currently under active development.**

The initial development focuses on establishing the backend foundation, centralized LLM integration, and agent execution runtime. Evaluation, security, MCP infrastructure, observability, and the frontend dashboard will be developed incrementally.

---

**Sentinel AI — Building AI agents is one challenge. Making them reliable, secure, and observable is another.**