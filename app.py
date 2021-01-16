import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# text/title
st.title("Streamlit Tutorials")
st.text("welcome !")

# header/subheader
st.header('This is a header')
st.subheader('This is a subheader')

#Markdownd
st.markdown('### This is a markdown')
st.markdown('## This is a markdown')
st.markdown('# This is a markdown')
st.markdown('#** This is a markdown**')
st.markdown('Streamlit is **_really_ cool**.')
st.markdown('`This is a markdown`')

#color box
st.success("this is a green box")
st.info("this is info")
st.warning("this is warning")
st.error("this is error")

st.subheader('This is a subheader')
st.write('Hello, *World!* :sunglasses:')

#help
st.help(range)

#extra
st.write(1234)
st.write(pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40],}))

#checkbox
if st.checkbox('Show/Hide'):
	st.text('that shows bec you checked box')
else:
	st.text('now its closed')

#radio buttons
status = st.radio('What is your status?', ('Active', 'Inactive'))
if status == 'Active':
	st.success("You are Active")
else:
	st.warning("You are inactive")
status2 = st.radio('What is your 2nd status?', ('1','2','3'))

#selectbox
occupation = st.selectbox('Your occupation', ('DS','Dev','CEO'))
st.write('You picked:',occupation)
if occupation == "DS":
    st.success("wooo!")
else:
    st.warning("damn!")

#Multiselect box
options = st.multiselect('What are your favorite colors',
['Green', 'Yellow', 'Red', 'Blue'],
['Yellow', 'Red'])
st.write('You selected:', options)

options2 = st.multiselect('Where do you live',('USA', 'GSermany', 'UK', 'Other'))
st.write('You selected:', options2)
if len(options2) > 1:
	st.write('You selected:', len(options2), 'locations')
else :
	st.write('You selected:', len(options2), 'location')

#sliders
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

level = st.slider("what is your level", 0,40,20, step=5)
st.write('I am ', level, 'yeah')

values = st.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

#TimeSlider
from datetime import time
appointment = st.slider("Schedule your appointment:",value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

#DateTimeSlider
from datetime import datetime
start_time = st.slider("When do you start?",value=datetime(2020, 1, 1, 9, 30),format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

#Button
st.button('SImple Button') # start analysis etc.Run

if st.button('About'):
	st.write('Streamlit is Cool')
else:
	st.write('Hasta pronto')

#text input
first_name = st.text_input("Enter Your First Name")
if st.button('Submit'):
	st.success(first_name.title())

#text area
message = st.text_area("Enter your text", "Type here...")
if st.button('submit'):
	result = message.title()
	st.success(result)

#date input
import datetime
today = st.date_input('TOday is ', datetime.datetime.now())


d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


#time input
the_time = st.time_input('Time is ', datetime.time(8,45))

#Raw Data
st.text("DIsplay Text")
st.code('import pandas as pd')



with st.echo():
	import numpy as np
	import pandas as pd


#progress bar
my_bar = st.progress(0)
for p in range(10):
	my_bar.progress(p+1)

import time
my_bar = st.progress(0)
for p in range(20):
	my_bar.progress(p+1)
	time.sleep(0.1)

#spinner
import time
with st.spinner("wait for it .... "):
	time.sleep(3)
st.success('Finished')
st.balloons()


#SidebAr
st.sidebar.title('Churn Probabaility of a sngle CUstiner')

#SidebAr align
html_temp = st.sidebar.title('Churn Probabaility of a sngle CUstiner')
st.markdown(html_temp,unsafe_allow_html=True)
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 50px;
            }}
        </style>
    ''',
    unsafe_allow_html=True)



import pickle
import pandas as pd
df = pickle.load(open("df_saved.pkl",'rb'))

st.write(df.head())
st.text(df.head())





#images
from PIL import Image
im = Image.open('image.png')
st.image(im, width=600, caption='GD')
if st.checkbox('Show/Hide Picture'):
	st.image(im, width=600, caption='GD')

#video file
vid_file = open('download.mp4','rb')
st.video(vid_file)



import pandas as pd
import numpy as np
import altair as alt
df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


st.map()