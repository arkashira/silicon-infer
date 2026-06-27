<h3 align="center">🛠️ silicon-infer</h3>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/axentx/silicon-infer/blob/main/LICENSE)
[![Language](https://img.shields.io/badge/language-Python%203.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Build](https://img.shields.io/badge/build-Poetry-green.svg)](https://python-poetry.org/)
[![Stars](https://img.shields.io/github/stars/axentx/silicon-infer.svg)](https://github.com/axentx/silicon-infer/stargazers)

</div>

---

# 🚀 silicon-infer

**Empower Silicon Infer users with a seamless onboarding experience.**

## Why silicon-infer?

- **High-throughput inference**: Optimized for Apple Silicon with >200 t/s performance
- **Affordable local coding**: Reduce reliance on cloud services with cost-effective local models
- **Enhanced reasoning**: Improved tool-calling capabilities boost developer productivity
- **Built for developers**: Designed specifically for Silicon Infer users seeking streamlined setup
- **Modular architecture**: Clean separation of concerns for maintainability and scalability
- **Sandbox-tested**: Real-world tested implementations ensure reliability
- **Developer-first docs**: Comprehensive guides and artifacts included for easy adoption

## Feature Overview

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Onboarding Process     | Step-by-step guided setup for new users                                     |
| Performance Optimized  | Leverages Apple Silicon for high-throughput inference                       |
| Local Model Support    | Run models locally without cloud dependency                                 |
| Tool Integration       | Enhanced reasoning and tool-calling capabilities                            |
| Documentation Suite    | Includes PRD, REQUIREMENTS, TECH_SPEC, STORIES, and ROADMAP artifacts        |

## Tech Stack

- **Python 3.8**
- **Poetry** for dependency management

## Project Structure

```
silicon-infer/
├── business/           # Business logic and core functionality
├── docs/               # Documentation including PRD, REQUIREMENTS, etc.
├── src/                # Source code for the onboarding process
├── tests/              # Test files for the onboarding module
├── README.md           # This file
├── pyproject.toml      # Poetry configuration and dependencies
└── requirements.txt    # Legacy requirements file (if needed)
```

## Getting Started

### Prerequisites

- Python 3.8
- Poetry installed (`pip install poetry`)

### Installation

```bash
poetry install
```

### Running the Onboarding Process

```bash
poetry run python -m src.onboarding
```

### Testing

```bash
poetry run pytest tests/
```

## Deploy

To deploy the onboarding process:

```bash
poetry build
poetry publish
```

> Note: Deployment requires proper credentials and access to the target registry.

## Status

**Early-stage development**  
Latest commit: `1cbf19a feat(silicon-infer): real, sandbox-tested implementation`

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.