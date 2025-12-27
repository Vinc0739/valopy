# Contributing to ValoPy

Thanks for your interest in contributing! I maintain this as a hobby and can't always keep up with API changes or add new features. That's why I need your help, to keep this wrapper useful for everyone. If you need help or have questions, feel free to contact me through discord.

## Getting Started

- Check out the [project roadmap](https://github.com/users/Vinc0739/projects/10) to see what's being worked on
- Browse [existing issues](https://github.com/Vinc0739/valopy/issues) or create a new one
- Have a feature request? Open an issue and create a separate PR to add your changes.

## Development Setup

1. Install development version:
   ```bash
   pip install valopy[dev]
   ```
2. Make your changes
    - Use `ruff` and `black` for code formatting (configured in `pyproject.toml`)
    - Update the documentation with your changes
    - Add new unit tests for your features
3. Run tests:
   ```bash
   pytest
   ```
4. Submit a pull request

## Guidelines

- **Branch strategy**: All changes go to `dev`, then to `main` when stable
  - `dev` branch: Active development and new features
  - `main` branch: Stable releases only
  - Submit all PRs to `dev` first

- **Commit messages** follow this format:
  ```
  <type>(<ref>): <short description>
  ```
  - **Types**: `feat`, `fix`, `refactor`, `docs`, `chore`, `test`
  - **Ref**: Link to issue/PR (e.g., `#17`)
  - **Description**: Use Present tense action verbs (e.g., `adds`, `fixes`, `updates`, `removes`)
  - **Examples**:
    - `feat(#17): adds account lookup by PUUID`
    - `fix(#23): fixes endpoint path for V2 PUUID`
    - `docs(#25): updates v0.4.0 release notes`
    - `refactor(#30): removes deprecated AccountV2PUUID model`
