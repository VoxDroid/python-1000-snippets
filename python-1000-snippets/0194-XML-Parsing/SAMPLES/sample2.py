# sample2.py
import xml.etree.ElementTree as ET
root = ET.Element('root')
c = ET.SubElement(root,'child')
c.text='world'
tree = ET.ElementTree(root)
tree.write('out.xml')
print('wrote out.xml')

