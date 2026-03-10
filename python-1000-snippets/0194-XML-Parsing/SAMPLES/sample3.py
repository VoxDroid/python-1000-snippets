# sample3.py
import xml.etree.ElementTree as ET
xml = '<ns:root xmlns:ns="urn"><ns:child>v</ns:child></ns:root>'
r = ET.fromstring(xml)
ns = {'ns':'urn'}
print('namespaced:', r.find('ns:child', ns).text)

