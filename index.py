import streamlit as st
# import string
import time
# import numpy as np

st.text("hello")
# lis=[1,2,3,4,5,6,7,8,9]

# st.text(lis)
# a=int(input("eneter a number :"))
# a=0
# st.read(a)

# if st.button("click")==1:
#     st.text("clicked")
# s = "sendrela"
# for i in s:
#     st.text(i)
#     time.sleep(1)

# st.balloons()
# st.audio()
name=st.text_input('Enter your name :')
# st.camera_input('o')
# st.chat_input('Enter ')
if st.button('click me')==1:
    st.write(f'hey **{name}** i love you baby')
    st.balloons()
else:
    st.text('please enter your name ')

# st.download_button('this is devider')





