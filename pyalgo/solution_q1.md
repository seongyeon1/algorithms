# 문제 1번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://pyalgo.co.kr/?page=1
* 통과 여부 : Y

```python
def solution(data):
    ans=''
    for d in data:
        d = d.replace(' ','').replace('+','1').replace('-','0')
        num = int(d, 2)
        ans+=chr(num)
    return ans
```

