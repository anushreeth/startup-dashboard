import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning streamlit')
st.subheader('And I am loving it')

st.write('This is normal text')
st.markdown("""
### My favorite movies
- Race3
- Humshakals
- Housefull
""")
st.code("""
def foo(input):
    return foo**2

x = foo(2)

""")

st.latex('x^2+y^2+2=0')

df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3%')

st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.image('images.jpg')
# st.video()
st.sidebar.title('Sidebar Title')

col1, col2, col3 = st.columns(3)
with col1:
    st.image('images.jpg')
with col2:
    st.image('images.jpg')
with col3:
    st.image('images.jpg')

st.error('Login Failed')

st.success('Login Successful')

st.info('Information')

st.warning('Warning')

bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter Email')
number = st.number_input('Enter Age')
st.date_input('Enter Registratiom Date')


import streamlit as st

email = st.text_input("Enter Email")
password = st.text_input("Enter Password")
gender = st.selectbox('Select gender',['male', 'female', 'others'])

btn = st.button('Login')

#if the button is clicked
if btn:
    if email == 'anushree1234@gmail.com' and password == '1234':
        st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')




import streamlit as st
import pandas as pd

file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
