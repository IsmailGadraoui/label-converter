from label_studio_converter import Converter

c = Converter('tests/config.xml','tests/project/')
c.convert_to_coco('tests/project/', 'tmp/output.json')