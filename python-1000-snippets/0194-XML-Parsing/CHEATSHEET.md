# 0194-XML-Parsing Cheatsheet

* Use `xml.etree.ElementTree` for basic XML parsing.
* `ET.fromstring` or `ET.parse('file.xml')` to load XML.
* Navigate with `root.find('tag')`, `root.findall('tag')`, or `for elem in root.iter()`.
* Access text: `elem.text`; attributes: `elem.get('attr')`.
* Handle namespaces via a dict: `ns = {'ns':'uri'}` and use `find('ns:tag', ns)`.

