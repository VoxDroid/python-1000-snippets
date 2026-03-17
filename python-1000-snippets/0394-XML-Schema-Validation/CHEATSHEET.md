
# 0394-XML-Schema-Validation Cheatsheet

- Install `lxml` with `pip install lxml`.
- Use `etree.XMLSchema` to compile an XSD.
- Use `schema.assertValid(xml_doc)` to validate and raise on errors.
- Capture `etree.DocumentInvalid` to inspect validation messages.
