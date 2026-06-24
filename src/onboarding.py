import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class OnboardingStep:
    description: str
    duration: int

class OnboardingProcess:
    def __init__(self):
        self.steps = [
            OnboardingStep("Introduction to Silicon Infer", 2),
            OnboardingStep("Setting up the development environment", 3),
            OnboardingStep("Completing a guided project", 5)
        ]

    def complete_onboarding(self):
        total_duration = sum(step.duration for step in self.steps)
        return total_duration

    def is_compatible(self, device):
        if device == "Apple Silicon Mac":
            return True
        return False

def main():
    parser = ArgumentParser(description="Silicon Infer Onboarding")
    parser.add_argument("--device", help="Device type")
    args = parser.parse_args()
    onboarding = OnboardingProcess()
    print(f"Total onboarding duration: {onboarding.complete_onboarding()} minutes")
    print(f"Is compatible with {args.device}: {onboarding.is_compatible(args.device)}")

if __name__ == "__main__":
    main()
