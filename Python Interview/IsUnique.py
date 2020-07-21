import pytest

# max num of asci
ASCI_MAX = 128


def unique(data):
    if len(data) > ASCI_MAX:
        return False

    checked = [False] * ASCI_MAX
    for char in data:
        if checked[ord(char)]:
            return False
        checked[ord(char)] = True
    return True


def test_unique_true():
    assert unique("ABCDEFGHIJKLMNOPQRSUVWXYabcdefghijklmnopqrsuvwxy") is True


def test_unique_false():
    assert unique("ABCDEFGHIJKLMNOPQRSUVWXYabcdefghijklmnopqrsuvwxyA") is False
