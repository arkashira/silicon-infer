# Requirements Document  
**Project:** silicon‑infer  
**Owner:** AxentX – Senior Product/Engineering Lead  
**Date:** 2026‑06‑17  

---  

## 1. Overview  

silicon‑infer is a **local, high‑throughput coding LLM** optimized for Apple Silicon (M‑series) hardware. It must deliver **≥ 200 token‑per‑second (t/s) inference** while preserving full reasoning, tool‑calling, and code‑generation capabilities. The model will be packaged as a self‑contained binary/library that can be integrated into developer tools (IDE plugins, CI agents, local dev servers) without requiring external GPU or cloud resources.

---  

## 2. Functional Requirements  

| ID | Description |
|----|-------------|
| **FR‑1** | **Model Loading** – The system shall load a pre‑trained transformer model (size ≤ 7 B parameters) from a local file system in ≤ 3 seconds on Apple M2‑Max (12‑core CPU, 32 GB RAM). |
| **FR‑2** | **Inference API** – Expose a thread‑safe C‑API (`infer(prompt, max_tokens, temperature, top_p)`) and a Python wrapper (`silicon_infer.infer(...)`). |
| **FR‑3** | **Throughput** – Achieve **≥ 200 t/s** sustained throughput on a single Apple M2‑Max when processing batch size = 1, `max_tokens` = 256, `temperature` = 0.7. |
| **FR‑4** | **Latency** – 99th‑percentile latency for a 128‑token request must be ≤ 150 ms. |
| **FR‑5** | **Reasoning & Tool‑Calling** – Support the full SGLang‑style structured generation protocol (function calls, JSON output) with no degradation in correctness compared to the upstream model. |
| **FR‑6** | **Quantization** – Provide a 4‑bit integer quantized variant that fits within **≤ 8 GB** VRAM/CPU memory while preserving ≥ 95 % of baseline accuracy on the coding benchmark (HumanEval + MBPP). |
| **FR‑7** | **Dynamic Batching** – Automatically batch concurrent requests up to a configurable batch size (default = 4) to improve GPU/CPU utilization without violating latency SLAs. |
| **FR‑8** | **Model Versioning** – Support loading multiple model checkpoints (e.g., `v1.0`, `v1.1‑quant`) via a simple manifest file. |
| **FR‑9** | **Safety Filters** – Integrate a lightweight toxicity / PII filter that blocks generation of disallowed content with ≤ 1 % false‑negative rate on the internal safety test suite. |
| **FR‑10** | **CLI Tool** – Provide a command‑line interface (`silicon-infer-cli`) for quick testing: `silicon-infer-cli --prompt "..." --max-tokens 256`. |
| **FR‑11** | **Telemetry (opt‑in)** – Emit anonymized usage metrics (tokens processed, latency, hardware model) to the AxentX telemetry endpoint when the user enables it via `--telemetry`. |
| **FR‑12** | **Packaging** – Distribute as a Homebrew formula and a pip wheel (with `--platform‑macosx_13_0_arm64`) that includes all native dependencies (e.g., `vLLM` compiled for Apple Silicon). |
| **FR‑13** | **Documentation** – Generate a comprehensive README, API reference (Sphinx), and quick‑start guide covering installation, configuration, and example integrations. |

---  

## 3. Non‑Functional Requirements  

| ID | Category | Requirement |
|----|----------|-------------|
| **NFR‑1** | **Performance** | Sustained throughput ≥ 200 t/s on Apple M2‑Max; ≤ 150 ms 99th‑pct latency for 128‑token requests. |
| **NFR‑2** | **Scalability** | Architecture must allow future extension to Apple M3‑Ultra (up to 4× compute) without code changes; batch size parameterizable up to 16. |
| **NFR‑3** | **Security** | All binaries must be signed with an Apple‑trusted developer certificate. No external network calls are made unless telemetry is explicitly enabled. |
| **NFR‑4** | **Reliability** | Process must not crash on malformed inputs; any exception should be caught and returned as an error object with an error code (e.g., `ERR_INVALID_PROMPT`). |
| **NFR‑5** | **Resource Utilization** | Peak RAM usage ≤ 8 GB for the quantized model; ≤ 12 GB for the full‑precision model. CPU utilization should not exceed 85 % on a single M2‑Max core under load. |
| **NFR‑6** | **Portability** | Must run on macOS 13.0+ (Apple Silicon) without requiring Xcode command‑line tools beyond the bundled compiler. |
| **NFR‑7** | **Maintainability** | Codebase must follow AxentX’s Python/Swift style guide, include unit tests covering ≥ 90 % of the inference path, and CI must run on every PR. |
| **NFR‑8** | **Observability** | Provide Prometheus‑compatible metrics (`silicon_infer_requests_total`, `silicon_infer_latency_seconds`, `silicon_infer_throughput_tps`). |
| **NFR‑9** | **Compliance** | All third‑party libraries must be compatible with the project’s licensing policy (Apache‑2.0, MIT, BSD). No GPL components. |
| **NFR‑10** | **Usability** | Installation should complete in ≤ 5 minutes on a fresh macOS VM; the CLI must return helpful error messages and a `--help` description. |

---  

## 4. Constraints  

1. **Hardware** – Target hardware is Apple Silicon (M‑series). No reliance on external GPUs or cloud inference.  
2. **Model Size** – Must fit within the memory limits of the target devices (≤ 12 GB RAM).  
3. **Licensing** – Use only datasets and model weights that are permissively licensed (Apache‑2.0, MIT, CDLA‑permissive‑2.0).  
4. **Toolchain** – Build must use the Apple‑provided clang toolchain; no custom LLVM forks.  
5. **Dependency Footprint** – Total binary size (including model) must be ≤ 4 GB for the quantized variant.  
6. **Release Cadence** – Align with AxentX quarterly product release schedule; first GA due **2026‑09‑30**.  

---  

## 5. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | The upstream coding model (e.g., CodeLlama‑7B) is available under a permissive license and can be fine‑tuned on AxentX’s internal coding datasets. |
| **A‑2** | Apple Silicon’s Neural Engine (ANE) is not exposed to third‑party developers; inference will run on CPU/GPU cores only. |
| **A‑3** | The target user base has macOS 13+ with at least 16 GB RAM. |
| **A‑4** | AxentX’s telemetry endpoint is already provisioned and accepts JSON payloads over HTTPS. |
| **A‑5** | Existing internal libraries (vLLM, SGLang) can be cross‑compiled for arm64 without functional regression. |
| **A‑6** | The safety filter can be implemented using a lightweight rule‑based system; no large additional model is required. |

---  

## 6. Acceptance Criteria  

- All functional requirements FR‑1 – FR‑13 are demonstrated in an end‑to‑end test suite.  
- Performance benchmarks (NFR‑1) meet the specified thresholds on the reference hardware.  
- No license violations are detected by the internal compliance scanner.  
- Documentation passes the AxentX quality gate (spell‑check, completeness, examples).  
- The product is packaged and installable via Homebrew and pip without manual post‑install steps.  

---  

*Prepared by:*  
Senior Product/Engineering Lead – AxentX  

*Version:* 1.0  

---
