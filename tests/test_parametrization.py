import pytest
from _pytest.fixtures import SubRequest



@pytest.mark.parametrize('number', [1, -1, 3, 2])
def test_numbers (number: int):
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1,1), (2,4), (3,9)])
def test_several_numbers (number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webkit'])
@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
def test_multi (os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'opening browser: {browser}')
