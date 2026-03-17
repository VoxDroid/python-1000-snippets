
# sample3.py
# Compile an XSD once and reuse it to validate multiple XML documents.

try:
    from lxml import etree  # type: ignore
except ImportError:
    print("lxml not installed; install with `pip install lxml`")
else:
    xsd = """
    <xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'>
      <xs:element name='root'>
        <xs:complexType>
          <xs:sequence>
            <xs:element name='value' type='xs:integer'/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:schema>
    """

    schema_doc = etree.fromstring(xsd)
    schema = etree.XMLSchema(schema_doc)

    good_xml = "<root><value>10</value></root>"
    bad_xml = "<root><value>not-a-number</value></root>"

    for xml in (good_xml, bad_xml):
        doc = etree.fromstring(xml)
        try:
            schema.assertValid(doc)
            print("Valid:", xml)
        except etree.DocumentInvalid as e:
            print("Invalid:", xml)
            print("  reason:", e)
