from inference_engine import InferenceEngine, InferenceResult
from vllm import VLLM

def test_infer():
    engine = InferenceEngine(VLLM("test_model"))
    input_text = "This is a test sentence"
    result = engine.infer(input_text)
    assert len(result.tokens) == 5  # Corrected the expected length
    assert result.throughput > 200.0

def test_integrate_vllm():
    engine = InferenceEngine(VLLM("test_model"))
    new_model = VLLM("new_model")
    engine.integrate_vllm(new_model)
    assert engine.model.name == "new_model"

def test_get_throughput():
    engine = InferenceEngine(VLLM("test_model"))
    assert engine.get_throughput() == 200.0

def test_edge_case_empty_input():
    engine = InferenceEngine(VLLM("test_model"))
    input_text = ""
    result = engine.infer(input_text)
    assert len(result.tokens) == 0
    assert result.throughput == 0.0
