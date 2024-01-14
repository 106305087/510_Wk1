import streamlit as st

def page_layout():
    st.set_page_config(
        page_title="Lily Chou Personal Website",
        page_icon="🌟",
        layout="centered",
        initial_sidebar_state="auto",
    )

def display_profile():
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

        ![](https://i.ibb.co/gJLmDYs/profile.png)
        </div>
        """,
            unsafe_allow_html=True,
        )
        # st.image('https://i.ibb.co/gJLmDYs/profile.png')

    with st.container():
        st.write("    ")
        st.write("    ")


def display_experience():
    tab1, tab2, tab3 = st.tabs(["Work Experience", "Education", "Hobbies"])

    with tab1:
        st.markdown(
            """
        #### :blue[Work Experience]
        - Front Desk Receptionist @ GIX, Bellevue, United State
        - UX Design Intern (full-time) @ ThunderCore, Taipei, Taiwan
        - UX/UI Design Intern @ Trend Micro, Taipei, Taiwan
        """
        )

    with tab2:
        st.markdown(
            """
        #### :blue[Education]
        - Tsinghua University, China (2022-Present)  
        M.S. in Data Science and Information Technology 
        - National Cheng-Chi University, Taiwan (2017-2021)  
        B.A. in Business Administration, Digital Content & Technology
        """
        )

    with tab3:
        st.markdown(
            """
        #### :blue[Hobbies]
        - Volleyball :volleyball:
        - Movie :movie_camera:
        - Music	:musical_note:
        """
        )

    with st.container():
        st.write("    ")

def display_contact():
    with st.expander("My Contact Info"):
        st.write("""
            E-mail: peisyc@uw.edu  
            Mobile: 425-208-666
        """)

    st.write("    ")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("    ")
    with col2:
        st.link_button("Contact Me", "mailto: peisyc@uw.edu")
    with col3:
        st.write("    ")

def display_footer():
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
    top:190px;
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

def main():
    page_layout()
    display_profile()
    display_experience()
    display_contact()
    display_footer()

if __name__ == "__main__":
    main()
