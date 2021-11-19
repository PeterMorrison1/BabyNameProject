from extracting.USANames import ExtractUSANames

def test_correct_url():
    test = ExtractUSANames()
    result = test.download()
    assert result == './temp/USA/USA.zip'


