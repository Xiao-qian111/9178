import streamlit as st
emp = st.empty
number = [
    r"((78+91)-(91+78))",    # 0
    r"\frac{78+91}{91+78}",    # 1
    r"(91-78-(9+1)+(7+(-8)))",    # 2
    r"\abs{(78+(-91))+(9+1)}",    # 3
    r"\sqrt{9\times1}-(7-8)",    # 4
    r"\lceil\sqrt{(9-1)+(7+8)}\rceil",    # 5
    r"\lfloor\frac{(91-78)}{\abs{(7-8)+(7-8)}}\rfloor",    # 6
    r"\lceil\frac{(91+(-78))}{\abs{(7-8)+(7-8)}}\rceil",    # 7
    r"(91-78)-\lceil\sqrt{(9-1)+(7+8)}\rceil",    # 8
    r"(91-78)-(\sqrt{9\times1}-(7-8))",    # 9
    r"((7+8)-\sqrt{9}+1)-\abs{(78+(-91))+(9+1)}"    # 10
]
st.title("9178生成器")
st.write("未满18岁的用户可以使用，因为SCXG是给")
