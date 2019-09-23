import xml.etree.ElementTree as ET
path = 'D:/UnityProjects/TetraProject/Assets/Libs~/GameCore/bin/Debug/GameCore.xml'
root = ET.parse(path).getroot()
for member in root.iter('member'):
    # value = memmemberber.get('foobar')
    print(member.attrib['name'], trim(member.text))

