import json
from dataclasses import dataclass
from typing import List

@dataclass
class VLLMModel:
    name: str
    throughput: float

class VLLM:
    def __init__(self, name: str):
        self.name = name
        self.throughput = 200.0  # tokens per second

    def get_throughput(self) -> float:
        return self.throughput
