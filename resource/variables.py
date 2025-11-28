import os
from copy import deepcopy

# Returns default value for TEST_ENV from environment or fallback to 'test'
ENV_NAME = os.environ.get('TEST_ENV') or 'test'


# Common variables shared by all environments
COMMON_VARS = {
    'BASE_URL': 'https://dev.example.com',
    'API_TIMEOUT': 30,
    'RETRIES': 2,
    'API_KEY': None,
}


# Environment-specific overlays (these extend/override COMMON_VARS)
TEST_VARS = {
    'BASE_URL': 'https://test.example.com',
    'API_KEY': 'test-api-key-123',
}

STAGING_VARS = {
    'BASE_URL': 'https://staging.example.com',
    'API_KEY': 'staging-api-key-abc',
    'RETRIES': 3,
}


_ENV_OVERLAYS = {
    'dev': {},
    'test': TEST_VARS,
    'staging': STAGING_VARS,
}


# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#getting-variables-from-a-special-function
def get_variables() -> dict:
    """Return the variable dictionary for the requested environment.

        - Merges `COMMON_VARS` with a per-environment overlay and returns the result.
    """
    result = deepcopy(COMMON_VARS)
    overlay = _ENV_OVERLAYS.get(ENV_NAME.lower(), {})
    result.update(overlay or {})
    return result


if __name__ == '__main__':
    # Quick local debug print
    print('Active env:', ENV_NAME)
    print('Vars:', get_variables())
