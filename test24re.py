#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
print("re:regular expression")

"""

[]  : word
.   : \nf를 제외한 문자
(*)  : 0개 이상 반복
(+)  : 1개 이상 반복
{m,n}  : ea count
\g  : 전역적

"""

pattern = re.compile("(\d{6})[-](\d{7})")
data = "kim 123456-1234567 010-1111-1111 lee 222222-2222222 010-2222-2222"
print(pattern.sub("\g<1>-*******", data)) 
print(pattern.sub("\g<1>-1******", data)) 
# \g<1>- 앞에는 전역적으로 두고, 뒤에는 ***...로 대체해라
