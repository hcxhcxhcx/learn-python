@@ -0,0 +1,8 @@
import re
txt = 'this is a sentence, I don\'t know why I was writing this sentence.'
keyword = 'why'
p_txt = txt.split(' ')
for i in p_txt:
    if re.search(keyword,i) is not None:
        print(i)
        
