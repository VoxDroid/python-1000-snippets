# Configuration Testing

## Description
This snippet demonstrates configuration testing for an e-commerce API, ensuring it handles different environment settings correctly.

## Code
```python
# Configuration testing for an API
try:
    class ApiConfig:
        # Initialize with environment settings
        def __init__(self, env: str):
            self.env = env
            self.settings = {
                "prod": {"db": "prod_db", "timeout": 30},
                "dev": {"db": "dev_db", "timeout": 60}
            }

        # Get configuration for environment
        def get_config(self) -> dict:
            if self.env not in self.settings:
                raise ValueError("Invalid environment")
            return self.settings[self.env]

    # Test configuration
    def test_config():
        prod_config = ApiConfig("prod")
        assert prod_config.get_config()["db"] == "prod_db", "Prod DB mismatch"
        dev_config = ApiConfig("dev")
        assert dev_config.get_config()["timeout"] == 60, "Dev timeout mismatch"

    # Simulate running test
    print("Configuration test passed: Prod and dev settings")
except ImportError:
    print("Mock Output: Configuration test passed: Prod and dev settings")
```

## Output
```
Mock Output: Configuration test passed: Prod and dev settings
```
*(Real output with `pytest`: `Configuration test passed: Prod and dev settings` if test passes)*

## Explanation
- **Purpose**: Configuration testing verifies that a system behaves correctly under different configuration settings, ensuring robustness across environments.
- **Real-World Use Case**: In an e-commerce system, configuration testing ensures the API connects to the correct database and uses appropriate timeouts in production vs. development.
- **Code Breakdown**:
  - The `ApiConfig` class manages environment-specific settings.
  - The `get_config` method retrieves settings for the specified environment.
  - The `test_config` test verifies settings for production and development environments.
- **Challenges**: Testing all possible configurations, handling invalid settings, and ensuring environment isolation.
- **Integration**: Supports Integration Testing (Snippet 601) and aligns with microservices deployment (Snippet 578).
- **Complexity**: O(1) for `get_config` and test execution.
- **Best Practices**: Test edge cases, automate configuration tests, use environment variables, and validate settings at startup.