from xml.etree.ElementTree import Element,parse, SubElement, ElementTree

tree = parse('Korean.xml')
root_node = tree.getroot()
node = Element("data")
node.text = "연습"
root_node.append(node)
ElementTree(root_node).write('Korean.xml')