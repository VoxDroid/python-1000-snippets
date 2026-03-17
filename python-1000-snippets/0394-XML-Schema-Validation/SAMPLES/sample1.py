
# sample1.py
# Validate a simple XML document against an XSD.

try:
    from lxml import etree  # type: ignore
except ImportError:
    print("lxml not installed; install with `pip install lxml`")
else:
    xml = "<root><data>value</data></root>"
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
    schema.assertValid(xml_doc)
    print("XML is valid")
