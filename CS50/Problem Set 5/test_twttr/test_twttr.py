import pytest
# pip install pytest
# pytest test_twttr.py
from io import StringIO
import sys
from twttr import main

def test_regular_string(monkeypatch, capsys):
    # Input simulation
    monkeypatch.setattr('sys.stdin', StringIO("Hello, World" + "\n"))

    main()

    # Output capture
    capture = capsys.readouterr()

    # Check output
    assert capture.out.strip() == "Input: Output: Hll, Wrld"


def test_caoitalized_vowels(monkeypatch, capsys):
    # Input simulation
    monkeypatch.setattr('sys.stdin', StringIO("HELLO, WORLD" + "\n"))

    main()

    # Output capture
    capture = capsys.readouterr()

    # Check output
    assert capture.out.strip() == "Input: Output: HLL, WRLD"

def test_numbers(monkeypatch, capsys):
    # Input simulation
    monkeypatch.setattr('sys.stdin', StringIO("H3LL0, W0RLD" + "\n"))

    main()

    # Output capture
    capture = capsys.readouterr()

    # Check output
    assert capture.out.strip() == "Input: Output: H3LL0, W0RLD"
