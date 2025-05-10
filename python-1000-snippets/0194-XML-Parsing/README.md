# XML Parsing

## Description
This snippet demonstrates parsing an XML string using `xml.etree.ElementTree`.

## Code
```python
import xml.etree.ElementTree as ET

# Sample XML content (normally in a file)
xml_content = """
<config>
    <server host="127.0.0.1" port="8080"/>
    <database host="localhost" user="admin"/>
</config>
"""

root = ET.fromstring(xml_content)
print("Server Host:", root.find("server").get("host"))
print("Database User:", root.find("database").get("user"))
```

## Output
```
Server Host: 127.0.0.1
Database User: admin
```

## Explanation
- **XML Parsing**: Uses `ElementTree.fromstring` to parse XML and access attributes.
- **Logic**: Finds elements by tag and retrieves attributes with `get`.
- **Complexity**: O(n) for parsing n nodes.
- **Use Case**: Used for processing XML-based configurations or APIs.
- **Best Practice**: Handle missing elements; use namespaces for complex XML; validate input.