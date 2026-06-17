# STORIES.md – silicon‑infer

## Overview
**silicon‑infer** is a local, high‑throughput coding LLM optimized for Apple Silicon (M‑series) GPUs/NPUs.  
Target performance: **≥ 200 tokens / second** on a single M2‑Max while preserving full reasoning, tool‑calling, and code‑generation capabilities.

The backlog below is organized into **Epics** that map to the MVP (core inference engine, model packaging, developer UX, and validation). Stories are written in the standard **“As a \<role\>, I want \<goal\>, so that \<benefit\>”** format with concrete **Acceptance Criteria (AC)**.

---

## EPIC 1 – Core Inference Engine

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 1.1 | **As a** performance engineer, **I want** the inference engine to load the model weights into Apple Silicon GPU memory in < 2 seconds, **so that** startup latency is negligible for interactive coding sessions. | - Model size ≤ 2 GB (quantized) loads on M2‑Max GPU in ≤ 2 s.<br>- Memory usage reported by `vm_stat` does not exceed 4 GB.<br>- Loading logs include timestamped “model‑loaded” event. |
| 1.2 | **As a** developer, **I want** the engine to accept a streaming token request (prompt → token stream) via a gRPC endpoint, **so that** IDE plugins can display incremental completions. | - gRPC service `InferStream` defined in `proto/infer.proto`.<br>- First token returned within 50 ms of request receipt.<br>- Stream continues until EOS or client cancel. |
| 1.3 | **As a** reliability engineer, **I want** the engine to recover from GPU OOM without crashing, **so that** the host process remains stable. | - Simulated OOM triggers graceful fallback to CPU inference.<br>- Process logs a warning and continues serving subsequent requests.<br>- No unhandled exceptions or segfaults. |
| 1.4 | **As a** product manager, **I want** the engine to achieve ≥ 200 t/s on the reference hardware (M2‑Max, 32 GB RAM), **so that** we meet the performance claim. | - Benchmark script `bench.py` reports ≥ 200 t/s on the CI runner with Apple Silicon hardware.<br>- Results stored as an artifact and compared against a baseline threshold. |
| 1.5 | **As a** security reviewer, **I want** all inbound payloads to be validated against a protobuf schema, **so that** malformed requests cannot cause undefined behavior. | - gRPC server validates `InferRequest` fields (max prompt length 4096 tokens).<br>- Invalid requests return `INVALID_ARGUMENT` with descriptive error. |

---

## EPIC 2 – Model Packaging & Optimization

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 2.1 | **As a** ML engineer, **I want** the model to be quantized to 4‑bit integer using `ggml`‑compatible format, **so that** memory footprint and latency are reduced. | - Quantization script `quantize.py` produces `model.q4.ggml` ≤ 1.2 GB.<br>- Accuracy drop < 2 % on the `code‑completion` benchmark suite. |
| 2.2 | **As a** DevOps engineer, **I want** a Homebrew formula that installs `silicon‑infer` and its model bundle in one step, **so that** end‑users have a frictionless setup. | - `brew install silicon-infer` succeeds on macOS 13+.<br>- Post‑install `silicon‑infer --version` reports correct version and model hash.<br>- Formula includes SHA‑256 verification of the model archive. |
| 2.3 | **As a** data scientist, **I want** the model to expose a `tool‑calling` API compatible with OpenAI function‑calling schema, **so that** existing tool‑integration code can be reused. | - `InferToolCall` protobuf mirrors OpenAI `function` spec.<br>- End‑to‑end test: a prompt requesting a `git_clone` function returns correctly formatted JSON payload. |
| 2.4 | **As a** compliance officer, **I want** the model distribution to include a clear license file (Apache‑2.0) and provenance metadata, **so that** we stay legally compliant. | - `LICENSE` present at repo root.<br>- `model_manifest.json` contains source URLs, hash, and license field.<br>- CI checks that the manifest matches the bundled model. |

---

## EPIC 3 – Developer Experience (CLI & SDK)

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 3.1 | **As a** command‑line user, **I want** a `silicon‑infer` CLI that accepts a file or stdin prompt and prints completions, **so that** I can quickly test the model locally. | - `silicon-infer -p "def foo():\n"` prints at least one token within 100 ms.<br>- Supports `--max-tokens`, `--temperature`, and `--stream` flags.<br>- Returns non‑zero exit code on error with helpful message. |
| 3.2 | **As a** VS Code extension developer, **I want** a Python SDK (`silicon_infer.client`) that wraps the gRPC API, **so that** I can embed the model in IDE plugins. | - `pip install silicon-infer-client` succeeds.<br>- Example script `example/vscode_completion.py` runs and streams tokens.<br>- SDK includes type hints and docstrings. |
| 3.3 | **As a** QA engineer, **I want** a test harness that can replay recorded prompt/response pairs, **so that** we can verify deterministic behavior across releases. | - `replay.py --suite regression.json` executes all cases.<br>- Differences > 1 % token‑level similarity cause test failure.<br>- Harness integrates with GitHub Actions. |
| 3.4 | **As a** product marketer, **I want** a one‑page “Getting Started” guide with screenshots for macOS Terminal and VS Code, **so that** prospects can evaluate the product instantly. | - `docs/GETTING_STARTED.md` exists, passes spell‑check.<br>- Includes commands for Homebrew install, CLI demo, and SDK usage.<br>- Linked from README and website landing page. |

---

## EPIC 4 – Validation & Monitoring

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 4.1 | **As a** data analyst, **I want** automated benchmarks (code‑completion, reasoning, tool‑calling) run on every PR, **so that** performance regressions are caught early. | - GitHub Action `benchmark.yml` runs three benchmark suites.<br>- Fails if any metric drops > 5 % compared to `main` baseline.<br>- Results posted as a comment on the PR. |
| 4.2 | **As an** ops engineer, **I want** runtime metrics (GPU utilization, token‑per‑second, request latency) exported via Prometheus, **so that** we can monitor production health. | - `/metrics` endpoint exposes `silicon_infer_gpu_util`, `silicon_infer_tps`, `silicon_infer_latency_seconds`.<br>- Grafana dashboard template included in `ops/`. |
| 4.3 | **As a** user researcher, **I want** a short in‑app survey after 10 completions, **so that** we collect willingness‑to‑pay signals. | - Survey pops up in CLI (`--survey`) after 10 calls.<br>- Responses stored in anonymized `surveys.db`.<br>- At least 30 % response rate in beta test. |

---

## MVP Scope (First Release)

| Epic | Stories Included |
|------|-------------------|
| Core Inference Engine | 1.1, 1.2, 1.4, 1.5 |
| Model Packaging & Optimization | 2.1, 2.2, 2.4 |
| Developer Experience | 3.1, 3.2 |
| Validation & Monitoring | 4.1, 4.2 |

All other stories are slated for **post‑MVP** (enhanced reliability, tool‑calling, compliance docs, QA harness, survey, etc.).

--- 

*Prepared by the silicon‑infer product/engineering lead, 2026‑06‑17.*
