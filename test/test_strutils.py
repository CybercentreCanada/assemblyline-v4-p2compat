from assemblyline_v4_p2compat.common.str_utils import safe_str, translate_str


def test_safe_str():
    assert safe_str("hello") == "hello"
    assert safe_str("hello\x00") == "hello\\x00"
    assert safe_str("\xf1\x90\x80\x80") == "\xf1\x90\x80\x80"
    assert safe_str("\xc2\x90") == "\xc2\x90"
    assert safe_str("\xc1\x90") == "\\xc1\\x90"


def test_translate_str():
    assert translate_str("\xf1\x90\x80\x80\xc2\x90")['encoding'] == "utf-8"
    assert translate_str("fran\xc3\xa7ais \xc3\xa9l\xc3\xa8ve")['encoding'] == "utf-8"
    assert translate_str('\x83G\x83\x93\x83R\x81[\x83f\x83B\x83\x93\x83O\x82'
                         '\xcd\x93\xef\x82\xb5\x82\xad\x82\xc8\x82\xa2')['language'] == "Japanese"
