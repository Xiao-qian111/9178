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
st.title("9178生成器", text_alignment="center")
st.subheader("未满18岁的用户可以使用，因为SCXG是给", text_alignment="center")
need = str(st.number_input("输入1~99999999999之间的整数：", min_value=1, max_value=99999999999, step=1))
gogogo = st.button("生成算式")
if gogogo:
    ans = r""
    index = 1
    for digit in need:
        ans += r"(" + number[int(need[len(need) - (index - 1)])] + r"\times{" + number[10] + r"}^{" + number[index - 1] + r"})"
        if index != len(need):
            ans += r"+"
        index += 1
    ans = need + r"=" + ans
    if ans[-1] == "+":
        ans = ans[:-1]
    emp.latex(ans)
    st.write("LaTeX代码：" + ans)
