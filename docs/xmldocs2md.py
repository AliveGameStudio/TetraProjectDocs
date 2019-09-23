# coding=utf-8
import xml.etree.ElementTree as ET
import re
import glob


path = 'D:/UnityProjects/TetraProject/Assets/Libs~/GameCore/bin/Debug/GameCore.xml'
root = ET.parse(path).getroot()

text="""
## Character表头
表头|值类型|名字|作用
---|---|---|---
"""
for member in [s for s in root.iter('member') if s.attrib['name'].startswith('M:GameCore.Character')]:
    # value = memmemberber.get('foobar')    /// Character
    fullName = member.attrib['name']
    name = re.search("\..*\.(.*)", fullName).group(1)
    desc = member.text.strip().encode("utf-8")
    text = text + name + "|" + str(desc) + "\n"

# print(text)


allFiles = glob.glob('./*.md') 
# allFiles = filter(lambda x: x[-3:] == '.md', allFiles)
print(allFiles)