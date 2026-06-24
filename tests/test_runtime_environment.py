from runtime_environment import RuntimeEnvironment
from model import Model

def test_runtime_environment_integrate_model():
    runtime_environment = RuntimeEnvironment({"config": "test_config"})
    model = Model()
    runtime_environment.integrate_model(model)
    assert model.runtime_environment == {"config": "test_config"}
