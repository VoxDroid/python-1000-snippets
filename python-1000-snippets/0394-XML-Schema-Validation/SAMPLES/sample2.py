
# sample2.py
# Validate an invalid XML document and print validation errors.

try:
    from lxml import etree  # type: ignore
except ImportError:
    print("lxml not installed; install with `pip install lxml`")
else:
    xml = "<root><unexpected>hi</unexpected></root>"
    xsd = """
    <xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'>
      <xs:element name='root'>
        <xs:complexType>
          <xs:sequence>
            <xs:element name='data' type='xs:string'/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:schema>
    """

    xml_doc = etree.fromstring(xml)
    schema_doc = etree.fromstring(xsd)
    schema = etree.XMLSchema(schema_doc)

    try:
        schema.assertValid(xml_doc)
    except etree.DocumentInvalid as e:
        print("Validation failed:")
        print(e)
