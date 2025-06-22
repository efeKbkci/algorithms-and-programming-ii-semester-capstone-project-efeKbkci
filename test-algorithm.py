import pytest
from algorithm import lzw_compress, lzw_decompress

def test_known_compression():
    text = "TOBEORNOTTOBE"
    expected_compressed = [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258]
    compressed, _ = lzw_compress(text)
    assert compressed == expected_compressed

def test_known_decompression():
    compressed = [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258]
    expected_text = "TOBEORNOTTOBE"
    decompressed, _ = lzw_decompress(compressed)
    assert decompressed == expected_text

def test_single_letter_repeat():
    text = "AAAAAA"
    expected_compressed = [65, 256, 257]
    compressed, _ = lzw_compress(text)
    decompressed, _ = lzw_decompress(expected_compressed)
    assert compressed == expected_compressed
    assert decompressed == text