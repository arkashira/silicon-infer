import json
from dataclasses import dataclass

@dataclass
class RuntimeEnvironment:
    config: dict

    def integrate_model(self, model):
        model.integrate(self.config)
