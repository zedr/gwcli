import contextlib
from pathlib import Path
from typing import AnyStr, TextIO

import pytest


class FixtureLoader:
    home_path = Path(__file__).parent / 'fixtures'

    @contextlib.contextmanager
    def file(self, path: AnyStr) -> TextIO:
        """Open a file in the fixtures."""
        with open(self.home_path / path) as fd:
            try:
                yield fd
            finally:
                pass


@pytest.fixture
def fixture_loader():
    return FixtureLoader()
