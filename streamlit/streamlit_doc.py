import streamlit as st
import pandas as pd
import time
st.title('Startup Dashboard')
st.header('I am learning streamlit')
st.subheader('And I am loving it !')

st.write('This is normal text')
st.markdown("""
### My favourite movies
- Harry potter
- KGF
- pushpa
""")
st.code("""
def foo(input):
   return foo**2
x=foo(2)

""")
st.latex('x^2 + y^2 + 2xy = (x + y)^2')

df=pd.DataFrame({
     'name':['saurav','ankit','shan'],
     'marks':[50,60,70],
     'package':[10,12,14]

})
st.dataframe(df)
st.metric('Revenue','Rs 3L','-3%')
st.json({
     'name':['saurav','ankit','shan'],
     'marks':[50,60,70],
     'package':[10,12,14]

})
st.image('D:/python_basic/streamlit/1636556624905.jpg')
st.video('D:/python_basic/streamlit/VID-20220728-WA0003.mp4')
st.sidebar.title('side bar')
col1,col2=st.columns(2)
with col1:
     st.image('D:/python_basic/streamlit/1636556624905.jpg')
with col2:
     st.image('streamlit/1636556624905.jpg')

st.error('logi failed')
st.success('login successful')
st.info('this is practice session')
st.warning('dont share otp')

bar=st.progress(0)
for i in range(1,101):
     #time.sleep(0.1)
     bar.progress(i)

email=st.text_input('enter email')
number=st.number_input('Enter age')
date=st.date_input('enter reg date')


email=st.text_input('Enter email')
password=st.text_input('password')
gender=st.selectbox('select gender',['male','female','others'])

btn=st.button('login')
#if the button is click
if btn:
     if email=='ankit@gmail.com' and password=='1234':
          st.success('login successful')
          st.balloons()
          st.write(gender)
     else:
          st.error('Login Failed')