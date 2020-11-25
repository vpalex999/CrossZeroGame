
import pytest

from source.cell import Cell


@pytest.fixture
def cell():
    return Cell()
