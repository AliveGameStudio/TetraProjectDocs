# -*- coding: utf-8 -*-

import glob
from pathlib import Path
import re
import io
import os
import sys
import shutil
import time



def ReadAllText(fn):
	return open(fn, 'r', encoding='utf-8').read()
def WriteAllText(fn,text):
	open(fn, 'w', encoding='utf-8').write(text)

def FindFilePathByName(folder,fn):
	for file in glob.iglob(folder + '/**/*.*', recursive=True):
		file =  os.path.abspath(file)
		if re.match(r'.*\\'+fn,file): return file

def SearchFileContent(folder,search):
	for file in glob.iglob(folder + '/**/*.*', recursive=True):
		text = ReadAllText(file)
		matches = re.finditer(search,text,re.MULTILINE)
		for match in matches:
			if match: return file


def main():
	docsFolder = './src/API'
	docsFolder = os.path.abspath(docsFolder)
	docsFolder = docsFolder.replace('\\','/')

	srcScriptFolder = '../Assets/Libs~/GameCore/Scripts/'
	if os.path.exists(docsFolder): shutil.rmtree(docsFolder)

	#将三斜杠///注释复制到文档
	for file in glob.iglob(srcScriptFolder + '/**/*.cs', recursive=True):
		text = open(file, 'r', encoding='utf-8', errors='ignore').read()

		#将多行表格换成有效格式
		#比如这样：
		#///abc|def|
		#///|多行表格第一行
		#///|多行表格第二行
		def f(match):
			return re.sub(r'\n(\t| )*///\|', '<br>', match.group(1), re.MULTILINE)
		text = re.sub(r'\|\n(((\t| )*///\|.*\n)+)', f, text , re.MULTILINE)


		# print(text)
		# matches = re.findall(r'///.*', text)
		rComment = r'///(.*\n)'
		destDocsFile = None
		# destDocsContent = ''
		matches = re.findall(rComment , text,re.MULTILINE)
		for match in matches:
			cmt =  match
			if len(cmt) > 0 and cmt[0] == '/': continue #跳过三个斜杠以上的注释，比如：////abc

			#取得目标md文件
			configMatch = re.match(r'docs:(.*)',cmt)
			if configMatch != None: 
				destDocsFilePath = configMatch[1]
				destDocsFilePath = docsFolder + "/" + destDocsFilePath
				os.makedirs(os.path.dirname(destDocsFilePath), exist_ok=True)
				destDocsFile = open(destDocsFilePath, 'a', encoding='utf-8')
				destDocsFile.write('\n')
				continue


			#写入
			if destDocsFile != None: 
				destDocsFile.write(cmt)


	for file in glob.iglob(docsFolder + '/**/*.md', recursive=True):
		#将 "#标题" 替换成 "<a name='标题'></a>\n#标题"
		text = ReadAllText(file)
		def f(match):
			indent = match.group(1) 
			indent = len(indent)+1
			id = match.group(2)
			name = match.group(4)
			if name:
				name = ': '+name 
			else:
				name = ''

			repl = '\n<a name="{1}"></a>\n{0}{1}{2}\n'.format('#'*indent,id.strip(),name)
			# print(repl)
			return repl
		text = re.sub(r'\n(#+)([^:\n]*)( *: *(.*))?\n', f, text , re.MULTILINE)


		WriteAllText(file,text)


	#将"{#引用}"替换成"[引用](引用路径)"
	for file in glob.iglob(docsFolder + '/**/*.md', recursive=True):
		text = ReadAllText(file)
		def f(match):
			name = match.group(1)
			# print('<a name="{0}"></a>'.format(name))
			destFile = SearchFileContent(docsFolder,'<a name="{0}"></a>'.format(name))
			# destFile = FindFilePathByName(docsFolder,name+".md")
			if not destFile: return match.group()
			destFile = destFile.replace('\\','/').replace(docsFolder+'/','/../API/')
			destFileNoExt = destFile.replace('.md','')
			repl = '[{0}]({1})'.format(name,destFileNoExt+"/#"+name)
			return repl
		text = re.sub(r'{#([^{}]*)}',f, text ,re.MULTILINE)
		WriteAllText(file,text)


main()



# def FindDocsInSrc(srcFilter):
# 	#在.cs里查找注释
# 	r = ''
# 	for file in glob.glob(srcFilter):
# 		text = open(file, 'r', encoding='utf-8').read()
# 		# print(text)
# 		# matches = re.findall(r'///.*', text)
# 		rComment = r'((^\t* *///.*\n)+)'
# 		rSignature = r' *\t*public ([^ ]*) +([^ (]* +)?([^ \(]*)'
# 		rArgs = r' ?\(([^\)]*)\)'
# 		matches = re.findall(rComment + rSignature + rArgs, text,re.MULTILINE)
# 		for match in matches:
# 			cmt =  match[0]
# 			ret =  match[2]
# 			methodName =  match[4]
# 			argsStr =  match[5]

# 			cmt = re.sub(r'\t* */// *','',cmt)

# 			# fullCmt = cmd
# 			cmt = methodName +"|"+ cmt
# 			r = r + cmt 

# 			# print('------')
# 			# print(re.sub(r' *\t*/// *', '', cmt).strip())
# 			# print(ret +" " + methodName + " (" +argsStr)
# 	return r

# def main():
# 	docsFolder = './'
# 	docsFileFilters =[
# 		docsFolder+"/*.md",
# 	]
# 	srcScriptFolder = '../../../TetraProject/Assets/Libs~/GameCore/Scripts'


# 	for filter in docsFileFilters:
# 		for file in glob.glob(filter):
# 			text = open(file, 'r', encoding='utf-8').read()
# 			# matches = re.findall(r'(<autogen:(.*)>)((.|\n)*)(</autogen>)', text,re.MULTILINE)
# 			matches = re.finditer(r'(<autogen:(.*)>)([^<]*)(</autogen>)', text,re.MULTILINE)
# 			offset = 0
# 			for m in matches:
# 				autogenStart = m.group(1)
# 				srcFilter = m.group(2)
# 				orgContent = m.group(3)
# 				autogenEnd = m.group(4)
# 				# print(srcFilter,m.start(),autogenStart,autogenEnd,m.end())
# 				docs = FindDocsInSrc(srcScriptFolder+"/"+srcFilter)
# 				docs = '\n'  + docs
# 				# print(docs)
# 				text = text[:m.start() + offset] + autogenStart + docs + autogenEnd + text[m.end() + offset:] 
# 				offset += len(docs) - len(orgContent)
# 				# print(text)
# 			open(file, 'w', encoding='utf-8').write(text)




# main()





# text='''

# ///aaaa
# public void Foreach(float a){

# }



# ///dddd111
# ///dddd222
# public async IEnumerable<Character>  GetPerferredTargets (int b){

# }

# '''
# matches = re.findall(r'((^\t* *///.*\n)+) *\t*public ([^ ]*) +([^ (]* +)?([^ \(]*) ?\(([^\)]*)\)', text,re.MULTILINE)

# for match in matches:
# 	print(match)
# 	print('\n*-------\n\n\n\n')



	# srcFileFilters =[
	# 	srcScriptFolder+"/*/CardCommandRunner*.cs",
	# ]
	# for filter in srcFileFilters:
	# 	for file in glob.glob(filter):
	# 		print(file)
	# 		text = open(file, 'r', encoding='utf-8').read()
	# 		# print(text)
	# 		# matches = re.findall(r'///.*', text)
	# 		rComment = r'((^\t* *///.*\n)+)'
	# 		rSignature = r' *\t*public ([^ ]*) +([^ (]* +)?([^ \(]*)'
	# 		rArgs = r' ?\(([^\)]*)\)'
	# 		matches = re.findall(rComment + rSignature + rArgs, text,re.MULTILINE)
	# 		for match in matches:
	# 			cmt =  match[0]
	# 			ret =  match[2]
	# 			methodName =  match[4]
	# 			argsStr =  match[5]
	# 			print('------')
	# 			print(re.sub(r' *\t*/// *', '', cmt).strip())
	# 			print(ret +" " + methodName + " (" +argsStr)


# ctest =  "abc 121 abc2"
	# for m in re.finditer(r"(121)", ctest, flags=re.MULTILINE):
	# 	print( ctest[:m.start()] + " " +ctest[m.end():])
	# return
