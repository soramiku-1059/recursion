import sys

#ファイルチェック
def filecheck(path):
    if len(path) >= 5 or path[-4] == ".txt":
        return True
    else:
        return False
    
#逆にして出力
def reverse(inputpath,outputpath):
    wtitecontens = ''
    with open(inputpath) as f:
        readcontens = f.read()
    for i in range(len(readcontens)+1):
        wtitecontens += readcontens[-i]
    with open(outputpath,'w') as f:
        f.write(wtitecontens)

#コピーを作成
def copy(inputpath,outputpath):
    wtitecontens = ''
    with open(inputpath) as f:
        readcontens = f.read()
    wtitecontens = readcontens
    with open(outputpath,'w') as f:
        f.write(wtitecontens)

#n回に複製
def duplicate(inputpath,n):
    wtitecontens = ''
    with open(inputpath) as f:
        readcontens = f.read()
    for i in range(0,int(n)):
        wtitecontens += (readcontens + "\n")
    with open(inputpath,'w') as f:
        f.write(wtitecontens)

#strをnewに変換
def replase(inputpath,str,newstr):
    wtitecontens = ''
    with open(inputpath) as f:
        readcontens = f.read()
    wtitecontens = readcontens.replace(str,newstr)
    with open(inputpath,'w') as f:
        f.write(wtitecontens)

if len(sys.argv) < 4:
    sys.exit("入力がすくないです")
if len(sys.argv) > 5:
    sys.exit("入力が多いです")
if filecheck(sys.argv[2]):
    if sys.argv[1] == "reverse":
        if filecheck(sys.argv[3]) and len(sys.argv) == 4:
            reverse(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "copy":
        if filecheck(sys.argv[3]) and len(sys.argv) == 4:
            copy(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "duplicate-contens":
        if sys.argv[3].isdecimal():
            duplicate(sys.argv[2],sys.argv[3])
        else:
            sys.exit("数値を入力してください")
    elif sys.argv[1] == "replase-string":
        if len(sys.argv) == 5:
            replase(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        sys.exit("コマンドが正しくありません")
else:
    sys.exit("入力ファイルが正しくありません")
    
