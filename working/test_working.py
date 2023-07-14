from working import convert
import pytest

def main():
    test_errors()
    test_time()

#if hour > 12 or minute > 60 or 'to' omitted
def test_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
         convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("9.00 AM - 5.00 PM")

#valid time_formats
def test_time():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

if __name__ == "__main__":
    main()
