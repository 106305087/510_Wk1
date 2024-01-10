import streamlit as st

st.set_page_config(
    page_title="Lily Chou Personal Website",
    page_icon="🌟",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.7, 0.3])

with col1:
    #st.subheader('Hey there! :wave:')
    #st.title('I’m Pei-Syuan :blue[(Lily)] Chou')
    #st.subheader('I’m a UX designer with an interdisciplinary background in :blue[business analysis] and :blue[user research].')
    st.markdown(
        """
    *Hey there! :wave:*
    ## I’m Pei-Syuan :blue[(Lily)] Chou
    ##### I’m a UX designer with an interdisciplinary background in :blue[business analysis] and :blue[user research].
      
    - Pursuing HCI master dual degree in UW, Seattle & THU, Beijing
    - Working experience in Web3, cybersecurity, and NGOs industry
    """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
     """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![](https://avatars.githubusercontent.com/u/7678108?v=4)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://avatars.githubusercontent.com/u/7678108?v=4')

st.divider()

st.markdown(
    """
#### :blue[Work Experience]
- UX Design Intern (full-time) @ ThunderCore, Taipei, Taiwan
- UX/UI Design Intern @ Trend Micro, Taipei, Taiwan
"""
)

st.markdown(
    """
#### :blue[Education]
- Tsinghua University M.S. in Data Science and Information Technology (2022-Present)
- National Cheng-Chi University B.A. in Business Administration (2017-2021)
"""
)

st.markdown(
    """
#### :blue[Hobbies]
- Volleyball :volleyball:
- Movie :movie_camera:
- Music	:musical_note:
"""
)

st.markdown(
    """
# Contact
""")
col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/7678108?v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/7678108?v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)