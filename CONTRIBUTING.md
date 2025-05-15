# Contributing to Python 1000 Snippets

Thank you for your interest in contributing to the **Python 1000 Snippets** repository! We welcome contributions from the community to improve snippets, add cheatsheets, samples, or documentation, and address issues.

## How to Contribute

### 1. Reporting Issues
- Check the [issue tracker](https://github.com/VoxDroid/python-1000-snippets/issues) to ensure the issue hasn’t been reported.
- Use the appropriate issue template (bug report, feature request, or documentation improvement) in `.github/ISSUE_TEMPLATE/`.
- Provide clear details, including steps to reproduce, expected behavior, and actual behavior.

### 2. Submitting Pull Requests
- Fork the repository and create a new branch for your changes (`git checkout -b feature/your-feature-name`).
- Follow the structure of existing snippets:
  - Place new snippets in `python-1000-snippets/XXXX-Title-Name/` with a `README.md`.
  - Ensure the `README.md` includes description, code, output, and explanation sections.
- Update `snippets_list.md` if adding a new snippet.
- Test your code to ensure it runs without errors.
- Submit a pull request using the [PULL_REQUEST_TEMPLATE.md](https://github.com/VoxDroid/python-1000-snippets/blob/main/.github/PULL_REQUEST_TEMPLATE.markdown).
- Ensure your code adheres to PEP 8 style guidelines.

### 3. Adding Cheatsheets or Samples
- Cheatsheets summarize key concepts for a snippet.
- Samples provide practical applications or extended examples.
- Place these in the respective snippet folder and update the `README.md` to reference them.

### 4. Code Style
- Follow PEP 8 for Python code.
- Use clear, descriptive variable names and comments.
- Ensure compatibility with Python 3.8+.
- Include dependencies in the snippet’s `README.md` (e.g., `pip install numpy scipy`).

### 5. Testing
- Test your snippet on a clean Python environment.
- Include any setup instructions in the `README.md`.
- If applicable, add unit tests in the snippet folder.

### 6. Documentation
- Update `README.md` in the snippet folder with clear explanations.
- Suggest improvements to the main `README.md` or other documentation files if needed.

## Getting Help
If you need assistance, refer to [SUPPORT.md](SUPPORT.md) or open an issue with the “question” label.

## Code of Conduct
All contributors must adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Thank you for helping make **Python 1000 Snippets** better!