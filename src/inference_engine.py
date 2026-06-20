import json
from dataclasses import dataclass
from typing import List

@dataclass
class InferenceResult:
    tokens: List[str]
    throughput: float

class InferenceEngine:
    def __init__(self, model):
        self.model = model

    def infer(self, input_text: str) -> InferenceResult:
        # Simulate Metal-accelerated compute
        tokens = input_text.split()
        throughput = len(tokens) / 0.01  # 0.01 seconds per token
        return InferenceResult(tokens, throughput)

    def integrate_vllm(self, vllm_model):
        # Integrate vLLM with Metal backend
        self.model = vllm_model

    def get_throughput(self) -> float:
        # Return the current throughput
        return self.model.get_throughput()
