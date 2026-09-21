import streamlit as st
emp = st.empty()
number = [
    r"((78+91)-(91+78))",    # 0
    r"(\frac{78+91}{91+78})",    # 1
    r"(91-78-(9+1)+(7+(-8)))",    # 2
    r"|(78+(-91))+(9+1)|",    # 3
    r"(\sqrt{9\times1}-(7-8))",    # 4
    r"(\lceil\sqrt{(9-1)+(7+8)}\rceil)",    # 5
    r"\lfloor\frac{(91-78)}{|(7-8)+(7-8)|}\rfloor",    # 6
    r"\lceil\frac{(91+(-78))}{|(7-8)+(7-8)|}\rceil",    # 7
    r"((91-78)-\lceil\sqrt{(9-1)+(7+8)}\rceil)",    # 8
    r"((91-78)-(\sqrt{9\times1}-(7-8)))",    # 9
    r"(((7+8)-\sqrt{9}+1)-|(78+(-91))+(9+1)|)"    # 10
]
yesiknow = {}

def compute(need):
    need = int(need)
    if need <= 10:
        return number[need]
    try:
        return yesiknow[need]
    except:
        pass
    ans = r""
    flag = False
    if need < 0:
        flag = True
    need = str(need)
    index = 1
    for digit in need:
        ans += r"(" + compute(int(need[len(need) - index])) + r"\times{" + compute(10) + r"}^{" + compute(index - 1) + r"})"
        if index != len(need):
            ans += r"+"
        index += 1
    if ans[-1] == "+":
        ans = ans[:-1]
    yesiknow[int(need)] = ans
    if flag:
        ans = r"-(" + ans + r")"
    return ans
    

st.title("9178生成器", text_alignment="center")
st.subheader("未满18岁的用户可以使用，因为SCXG是给", text_alignment="center")
num = int(st.number_input("输入一个整数：", step=1))
gogogo = st.button("生成算式")
if gogogo:
    ans = compute(num)
    ans = str(num) + r"=" + ans
    emp.latex(ans)
    st.write("LaTeX代码：" + ans)
