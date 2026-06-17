# TECH_SPEC.md – silicon‑infer  

**Project:** silicon‑infer  
**Owner:** AxentX – Product Engineering  
**Status:** MVP → Production (target Q4 2026)  
**Last Updated:** 2026‑06‑17  

---  

## 1. Overview  

silicon‑infer is a **local, high‑throughput coding LLM** optimized for Apple Silicon (M1/M2/M3 series). It delivers **≥ 200 tokens / second** on a single device while preserving full reasoning, chain‑of‑thought, and tool‑calling capabilities.  

The system is built on top of the **vLLM** inference engine (GPU‑accelerated) with **Metal‑based kernels** and **Apple Neural Engine (ANE)** off‑load for matrix multiplications. The model is a **7B‑parameter transformer** (code‑focused, fine‑tuned on the `instr‑resp` and `auto` datasets) that is **4‑bit quantized** (GPTQ) and **compiled to CoreML** for maximum latency reduction.

---  

## 2. Architecture  

```
+-------------------+       +-------------------+       +-------------------+
|   Client (REST/   | <---> |   Inference API   | <---> |   Model Engine    |
|   gRPC/Python)    |       |   (FastAPI)       |       |   (vLLM + Metal) |
+-------------------+       +-------------------+       +-------------------+
          |                         |                         |
          |                         |                         |
          v                         v                         v
   +-----------------+      +-----------------+      +-----------------+
   | Tokenizer       |      | Scheduler       |      | Execution Core |
   | (SentencePiece) |      | (dynamic batch) |      | (Metal/ANE)    |
   +-----------------+      +-----------------+      +-----------------+
          |                         |                         |
          v                         v                         v
   +---------------------------------------------------------------+
   |                     Shared Memory Cache                      |
   |  (kv‑cache, quantized weights, compiled CoreML model)        |
   +---------------------------------------------------------------+
```

### 2.1 Core Components  

| Component | Responsibility | Implementation |
|-----------|----------------|----------------|
| **Client SDK** | Language‑agnostic wrappers (Python, Node, Swift) for request/response handling, streaming tokens, tool‑call orchestration. | `silicon_infer/sdk/` – thin wrapper over HTTP/WS or gRPC. |
| **Inference API** | HTTP/REST (FastAPI) + gRPC endpoints; request validation, auth, rate‑limiting, request logging. | `silicon_infer/api/` |
| **Scheduler** | Dynamic batching, KV‑cache reuse, back‑pressure handling, per‑user QoS. | Integrated into vLLM’s `Scheduler` class, extended for Metal. |
| **Model Engine** | Executes transformer layers on Apple Silicon using Metal kernels; falls back to ANE for GEMM via CoreML. | Fork of `vllm-project/vllm` with `MetalBackend` and `CoreMLBackend`. |
| **Tokenizer** | Byte‑pair‑encoding (SentencePiece) for code‑centric vocab (≈ 50 k tokens). | Pre‑compiled `tokenizer.model` stored in `assets/`. |
| **Cache Layer** | In‑process shared memory for KV‑cache (FP16) and quantized weight shards. | `torch` shared memory + `mmap`. |
| **Monitoring** | Prometheus metrics, OpenTelemetry traces, health‑check endpoints. | `silicon_infer/monitoring/`. |
| **Deployment Orchestrator** | macOS‑only Docker image + `launchd` service for auto‑restart; optional `brew` formula. | `Dockerfile.macos`, `install.sh`. |

---  

## 3. Data Model  

### 3.1 Request / Response Schema  

| Field | Type | Description |
|-------|------|-------------|
| `model` | `string` | Identifier (`silicon-infer-7b`). |
| `messages` | `list[Message]` | Chat history (role: `system|user|assistant`). |
| `max_tokens` | `int` (default 256) | Upper bound on generated tokens. |
| `temperature` | `float` (0‑2) | Sampling temperature. |
| `top_p` | `float` (0‑1) | Nucleus sampling. |
| `stream` | `bool` | If `true`, server streams token deltas via SSE / gRPC. |
| `tools` | `list[ToolSpec]` | Optional tool definitions for function calling. |
| `metadata` | `object` | Caller‑provided opaque dict (passed back in response). |

**Message**  

```json
{
  "role": "user|assistant|system",
  "content": "string"
}
```

**ToolSpec** (optional)  

```json
{
  "name": "string",
  "description": "string",
  "parameters": { "type": "object", "properties": {...} }
}
```

**Response** (non‑streaming)  

```json
{
  "id": "uuid",
  "object": "chat.completion",
  "created": 1698427200,
  "model": "silicon-infer-7b",
  "choices": [
    {
      "index": 0,
      "message": { "role": "assistant", "content": "..." },
      "finish_reason": "stop|length|tool_calls"
    }
  ],
  "usage": { "prompt_tokens": 123, "completion_tokens": 456, "total_tokens":
