# XML Schema Validation

## Description
This snippet demonstrates XML schema validation using `lxml`.

## Code
```python
# Note: Requires `lxml`. Install with `pip install lxml`
try:
    from lxml import etree
    xml = "<root><data>value</data></root>"
    schema = "<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'><xs:element name='root'><xs:complexType><xs:sequence><xs:element name='data' type='xs:string'/></xs:sequence></xs:complexType></xs:element></xs:schema>"
    xml_doc = etree.fromstring(xml)
    schema_doc = etree.fromstring(schema)
    schema = etree.XMLSchema(schema_doc)
    schema.assertValid(xml_doc)
    print("XML is valid")
except ImportError:
    print("Mock Output: XML is valid")
```

## Output
```
Mock Output: XML is valid
```
*(Real output with `lxml`: `XML is valid`)*

## Explanation
- **XML Schema Validation**: Validates XML against an XSD schema.
- **Logic**: Parses XML and schema, checks validity using `lxml`.
- **Complexity**: O(n) for n nodes in XML.
- **Use Case**: Used for data exchange or API input validation.
- **Best Practice**: Handle validation errors; use robust schemas; test edge cases.