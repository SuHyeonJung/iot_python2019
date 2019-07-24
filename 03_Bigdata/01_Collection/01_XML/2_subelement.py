from xml.etree.ElementTree import Element,dump, SubElement

note = Element('note')

to = Element('to') #자식 노드
to.text = "Tove" #현재 엘리먼트(Tag)에 값 추가
note.append(to) #부모 노드에 자식노드 추가

SubElement(note,"form").text="jani"
#아래와 동일한 결과이다.
# from_tag = Element("from")
# from_tag.text = "jani"
# note.append(form_tag)
dump(note)
