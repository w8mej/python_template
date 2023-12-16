from unittest.mock import patch
import pytest
import sys
from typing import Any

sys.path.append('src/neovaultmatrixnet/')
from neovaultmatrixnet import NeoVaultMatrixNet  # noqa: E402


@pytest.fixture
def nvmn() -> NeoVaultMatrixNet:
    """
    Pytest fixture to provide a NeoVaultMatrixNet instance for each test.
    """
    test_nvmn = NeoVaultMatrixNet()
    test_nvmn.user_creation_url = "http://example.com/api"
    return test_nvmn


def test_initialization(nvmn: NeoVaultMatrixNet) -> None:
    """
    Test the initialization of NeoVaultMatrixNet.
    """
    assert nvmn.user_creation_url == "http://example.com/api"
