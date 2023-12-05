import library


def test_1_сm_to_inches_converter():
    result = library.сm_to_inches_converter(2.54)
    assert result == 1.0


def test_2_сm_to_inches_converter():
    result = library.сm_to_inches_converter(-10)
    assert result == -3.937008


def test_3_сm_to_inches_converter():
    result = library.сm_to_inches_converter(0)
    assert result == 0.0


def test_4_сm_to_inches_converter():
    result = library.сm_to_inches_converter(0.03)
    assert result == 0.011811
