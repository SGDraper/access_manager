from lib.age_checker import *
import pytest

def test_date_format():

    with pytest.raises(Exception) as e:
        age_checker("string")
    message = str(e.value)
    
    assert message == "Incorrect format, format required YYYY-mm-dd"

def test_user_under_16():
    result = age_checker("2019-05-01")

    assert result == "Access denied. Minimum age required is 16. Your age is 4"