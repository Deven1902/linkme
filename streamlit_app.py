import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('deven_img.jpg'))

st.header('Deven Nandapurkar')

st.info('ADAPTABLE AND RESOURCEFUL COMPUTER SCIENCE GRADUATE')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/deven-nandapurkar-951719212/', 'Connect with me onLinkedIn', icon_size)
st_button('twitter', 'https://twitter.com/dev__en', 'Not so shitposting on Twitter', icon_size)
st_button('github', 'https://github.com/Deven1902', 'Follow me on GitHub', icon_size)
st_button('medium', 'https://medium.com/@devenamazingnandapurkar', 'Read my blogs here', icon_size)
st_button('instagram', 'https://www.instagram.com/dev_en.n/', 'Follow me on Instagram', icon_size)
st_button('youtube', 'https://www.youtube.com/channel/UCsbehR2sxvo8NsadX6QZ5-w', 'Check out YouTube', icon_size)
