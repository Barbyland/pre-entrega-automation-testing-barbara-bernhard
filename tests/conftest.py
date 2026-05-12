from pathlib import Path
import sys

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.saucedemo_helpers import create_driver, save_screenshot  # noqa: E402


@pytest.fixture
def driver(request):
    browser = create_driver()
    request.node.driver = browser
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    browser = getattr(item, "driver", None)
    if report.when == "call" and report.failed and browser:
        screenshot_path = save_screenshot(browser, item.name)
        report.sections.append(("screenshot", str(screenshot_path)))
