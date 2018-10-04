#编写一个程序，删除字符串中的标点符号
punctuation='''。，、\＇:：；?‘’“”〝〞ˆˇ
            ﹕︰﹔﹖﹑·¨….¸;！!´？～—ˉ
            ｜‖＂〃｀@﹫¡¿﹏﹋﹌︴々﹟#﹩$
            ﹠&﹪%*﹡﹢﹦﹤‐￣¯―﹨ˆ˜﹍﹎+=
            <­­＿_-\ˇ~﹉﹊（）〈〉‹›﹛﹜『』
            〖〗［］《》〔〕{}「」【】︵︷︿
            ︹︽_﹁﹃︻︶︸﹀︺︾ˉ﹂﹄︼'''
str1=input("请输入一个字符串：")
list1=[]
for item in str1:
    if item not in punctuation:
        list1.append(item)
str2="".join(list1)
print("删除标点符号后的字符串：",str2)