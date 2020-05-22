import re
from pprint import pprint
text = """
1. 3的5次方
2. 7对2求模
3. 9除5，要求有小数部分
4. 9除5，要求没有小数部分
5. 用程序计算根号16，也就是16的2分之一次方
"""
text3 = """\
第{}题:
<pre class="python"><code>{}</code></pre>
<p>你的答案：</p>
<textarea rows="3" style="width:640px" name="answer{}"></textarea>
<p><br/></p> 
"""
test_list = text.split('\n')
list2 = [li for li in test_list if len(li) > 1]  # 第一次筛选去空格
# print(len(list2))
s = ''
for i in range(len(list2)):
    # print(list2[i])
    p = re.compile('[0-9]{1,2}.')
    result = p.sub('', list2[i], count=1)  # 替换一次，去除前面的抬头
    result2 = text3.format(i+1, result, i+1)
    s += result2
    # print('==')
print(s)
