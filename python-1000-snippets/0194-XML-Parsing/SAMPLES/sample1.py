# sample1.py
import xml.etree.ElementTree as ET
xml = '<root><child id="1">hello</child></root>'
r = ET.fromstring(xml)
print('child text:', r.find('child').text)

