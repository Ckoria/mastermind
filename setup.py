from pathlib import Path
from PIL import Image
import streamlit as st
from mastermind import check_user_input
from datetime import datetime, time

def layout():
# --------------------------------- PATH CONFIGURATION ------------------------
    current_dir = "D:\\PyProjects\Mastermind\\mastermind\\" #Path(__file__).parent if "__file__" in locals() else Path.cwd()
    style_file =     current_dir +"style\\style.css"
    ppic_file = current_dir +"assets\\ppic.png" 
    scoreboard = current_dir +"assets\\leaderboard.txt"

    # -------------------------------- PAGE SETUP --------------------------------
    page_title = "Mastermind by Chris Black"
    page_icon = ":100:"

    # -------------------------------- PERSONAL DEATILS --------------------------
    nick_name = "Ckoria"
    email_address = "sindiso.chris@gmail.com"
    social_media = {"YouTube": "https://www.youtube.com/@TX521",
                    "LinkedIn": "https://www.linkedin.com/in/chris-ndlovu-020847116/",
                    "Website": "https://www.tradingxposed.co.za",
                    "GitHub": "https://github.com/ckoria",
                    "Twitter": "https://twitter.com/tradingxposed"
                }

# --------------------------------- Layout Design ---------------------------------
    st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")
    with open(style_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    with open(scoreboard, "wb") as f:
        leaderboard = f.read()
    ppic = Image.open(ppic_file)

    pic_col, desc_col = st.columns(2, gap="small")
    with pic_col:
        st.image(ppic, width=225)
    with desc_col: 
        st.title(nick_name)
        st.download_button(
            label=" :floppy_disk: Download Resume",
            data= leaderboard,
            file_name=scoreboard.name,
            mime="application/octet-stream"    
        )
        st.write(f" :email: {email_address}")
    
    # ----- Social Media -----
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
    #image = Image.open('Samsung.png')
    #st.image(image)
    st.write("#")
    st.write("MASTERIND REMASTERED")
    
def sidebar(player_name):
    header  = st.container()
    with header:
        st.title("Game Dashboard by Ckoria")
        sidebar = st.sidebar
        with sidebar:
            st.header(player_name)
            difficulty_level =  st.selectbox("Select Level", ("Easy", "Medium", "Hard"))
    return difficulty_level
    
def ask_user_input():
    #text_input_container = st.empty()
    user_input = st.text_input("Input 4 digit code: ")
    """ if user_input != "":
        text_input_container.empty()
        st.info(user_input) """
    return user_input

def instructions(no_of_attempts):
    expander = st.expander("Read game instructions")
    expander.write(f"Guess 4 digit code in a correct order between 0 - 9. You have {no_of_attempts} attempts to find the correct sequence")
    expander.write("Hint: Track the number of correct and incorrect positions after an attempt.")
    
def run_game():
    layout()
    text_input_container = st.empty()
    player_name = text_input_container.text_input("Please enter your name: ")
    if player_name != "":
        text_input_container.empty()
        st.info(player_name)
    difficulty_level = sidebar(player_name)
    if difficulty_level == "Easy":
        no_of_attempts = 15
    elif difficulty_level == "Medium":
        no_of_attempts = 10
    else:
        no_of_attempts = 5
    instructions(no_of_attempts)
    user_input = ask_user_input()
    start_time = datetime.now()
    while no_of_attempts > 0: 
        output= check_user_input(user_input)
        if len(output) < 3:
            correct_positions = output.get('correct_pos')
            incorrect_positions = output.get('correct_pos') 
            st.write(f'Number of correct digits in correct place:     {correct_positions}')
            st.write(f'Number of correct digits not in correct place: {incorrect_positions}')
            if correct_positions == 4:
                st.write('Congratulations! You are a codebreaker!')
                break
            else:
                no_of_attempts -= 1
                st.write(f'Attempts left: {no_of_attempts}')
            finish_time = datetime.now()
            st.write(f'The code was: {user_input}. You\'ve spent {finish_time - start_time} minutes on the game')
    else:
        st.write(output)
        #run_game()
   
