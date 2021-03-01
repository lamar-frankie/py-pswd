#!/usr/bin/env python3
"""tests for passed.py"""

import os
import passwd
from subprocess import getstatusoutput, getoutput


prg = './passwd.py'

# --------------------------------------------------
def test_exists():
    """program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_usge():
    """test program is executable"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

# --------------------------------------------------
def test_numbers:
    """test that numbers only contains numbers"""

    for number in passwd.main.numbers:
        assert type(number) == int