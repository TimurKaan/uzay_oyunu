from functools import lru_cache
import pytest
from uzay_oyunu.araclar import say


def test_fibonacci_yalnizca_say():
    @say
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    sonuc = fib(20)
    assert sonuc == 6765
    assert fib.cagri == 21891


def test_fibonacci_say_ustte_lru_cache_altta():
    @say
    @lru_cache(maxsize=None)
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    sonuc = fib(20)
    assert sonuc == 6765
    assert fib.cagri == 39


def test_fibonacci_lru_cache_ustte_say_altta():
    @lru_cache(maxsize=None)
    @say
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    sonuc = fib(20)
    assert sonuc == 6765
    assert fib.__wrapped__.cagri == 21
