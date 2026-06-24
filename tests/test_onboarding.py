from onboarding import OnboardingProcess, OnboardingStep

def test_complete_onboarding():
    onboarding = OnboardingProcess()
    assert onboarding.complete_onboarding() == 10

def test_is_compatible():
    onboarding = OnboardingProcess()
    assert onboarding.is_compatible("Apple Silicon Mac") == True
    assert onboarding.is_compatible("Other Device") == False

def test_onboarding_step():
    step = OnboardingStep("Test Step", 5)
    assert step.description == "Test Step"
    assert step.duration == 5
