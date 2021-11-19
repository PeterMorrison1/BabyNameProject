from extracting.USANames import ExtractUSANames

extractor = ExtractUSANames()
extractor.download()
extractor.read()
extractor.write()