from inference_engine import InferenceEngine, InferenceResult, create_inference_engine

def test_infer():
    engine = create_inference_engine("test_model")
    input_text = "This is a test sentence"
    result = engine.infer(input_text)
    assert result.tokens == ["This", "is", "a", "test", "sentence"]
    assert result.throughput > 0

def test_integrate_vllm():
    engine = create_inference_engine("test_model")
    vllm_model = "vllm_test_model"
    engine.integrate_vllm(vllm_model)
    assert engine.model == vllm_model

def test_infer_edge_case():
    engine = create_inference_engine("test_model")
    input_text = ""
    result = engine.infer(input_text)
    assert result.tokens == []
    assert result.throughput == 0
