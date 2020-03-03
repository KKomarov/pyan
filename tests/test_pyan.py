import pytest
import subprocess
# import pyan3
import os
import sys
from pathlib import Path
from pyan import main
samples_dir = Path('samples')
@pytest.fixture
def pyan_run():
    def run(test_file):
        sys.argv[1] = str(test_file)
        main()
    return run


@pytest.mark.parametrize('file', os.listdir(samples_dir))
def test_no_crash(file, pyan_run):
    pyan_run(samples_dir / file)
