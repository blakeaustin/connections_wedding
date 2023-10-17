# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:44:50 2023

@author: BGigout
"""

import streamlit as st
import random
import base64
import requests
import pytz 
from datetime import datetime

# Initialize game variables
if "selected_words" not in st.session_state:
    st.session_state['selected_words'] = []
    st.session_state['mistakes'] = 0
    st.session_state['correct_words'] = []
    st.session_state['game_over'] = False 
    st.session_state['help_1'] = False
    st.session_state['correct_themes'] = []
    st.session_state['win_game'] = False
    st.session_state['authenticated'] = False
    st.session_state['whodis'] = ""
    st.session_state['user'] = ""
    st.session_state['shuffle'] = False
    st.session_state['words'] = [
        "Livestock", "Fest", "Daphne", "The Old",
        "Line", "Judge", "Spooky", "William",
        "Lively", "Harvest", "Palos Verdes", "Gourd",
        "Vaquero", "Oso", "Shelton", "Baptist"
    ]
    st.session_state['submitted'] = False

########################################## Secrets
db_key1 = st.secrets["API_KEY"]
db_owner1 = st.secrets["DB_OWNER"]
db_name1 = st.secrets["DB_NAME"]
app_code = st.secrets["APP_CODE"]
names = st.secrets["NAMES"]

# # Define the words for the game
# words = [
#     "Livestock", "Fest", "Daphne", "The Old",
#     "Line", "Judge", "Spooky", "William",
#     "Lively", "Harvest", "Palos Verdes", "Gourd",
#     "Vaquero", "Oso", "Shelton", "Baptist"
# ]

# Shuffle the words if requested
if st.session_state.shuffle == True:
    random.shuffle(st.session_state.words)
    st.session_state.shuffle = False
    st.experimental_rerun()
    
words = st.session_state.words


def display_grid():
    col1, col2, col3, col4 = st.columns(4,gap="Medium")
    with col1:
        if words[0] not in st.session_state.correct_words:
            if st.button(words[0], key=0, use_container_width=True):
                if words[0] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[0])
                else:
                    st.session_state.selected_words.append(words[0])
        else:
            btn0 = st.button(words[0], key=0, disabled=True, use_container_width=True)
    with col2:
        if words[1] not in st.session_state.correct_words:
            if st.button(words[1], key=1, use_container_width=True):
                if words[1] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[1])
                else:
                    st.session_state.selected_words.append(words[1])
        else:
            btn1 = st.button(words[1], key=1, disabled=True, use_container_width=True)
    with col3:
        if words[2] not in st.session_state.correct_words:
            if st.button(words[2], key=2, use_container_width=True):
                if words[2] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[2])
                else:
                    st.session_state.selected_words.append(words[2])
        else:
            btn2 = st.button(words[2], key=2, disabled=True, use_container_width=True)
    with col4:
        if words[3] not in st.session_state.correct_words:
            if st.button(words[3], key=3, use_container_width=True):
                if words[3] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[3])
                else:
                    st.session_state.selected_words.append(words[3])
        else:
            btn3 = st.button(words[3], key=3, disabled=True, use_container_width=True)
    with col1:
        if words[4] not in st.session_state.correct_words:
            if st.button(words[4], key=4, use_container_width=True):
                if words[4] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[4])
                else:
                    st.session_state.selected_words.append(words[4])
        else:
            btn4 = st.button(words[4], key=4, disabled=True, use_container_width=True)
    with col2:
        if words[5] not in st.session_state.correct_words:
            if st.button(words[5], key=5, use_container_width=True):
                if words[5] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[5])
                else:
                    st.session_state.selected_words.append(words[5])
        else:
            btn5 = st.button(words[5], key=5, disabled=True, use_container_width=True)
    with col3:
        if words[6] not in st.session_state.correct_words:
            if st.button(words[6], key=6, use_container_width=True):
                if words[6] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[6])
                else:
                    st.session_state.selected_words.append(words[6])
        else:
            btn6 = st.button(words[6], key=6, disabled=True, use_container_width=True)
    with col4:
        if words[7] not in st.session_state.correct_words:
            if st.button(words[7], key=7, use_container_width=True):
                if words[7] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[7])
                else:
                    st.session_state.selected_words.append(words[7])
        else:
            btn7 = st.button(words[7], key=7, disabled=True, use_container_width=True)

    with col1:
        if words[8] not in st.session_state.correct_words:
            if st.button(words[8], key=8, use_container_width=True):
                if words[8] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[8])
                else:
                    st.session_state.selected_words.append(words[8])
        else:
            btn8 = st.button(words[8], key=8, disabled=True, use_container_width=True)
    with col2:
        if words[9] not in st.session_state.correct_words:
            if st.button(words[9], key=9, use_container_width=True):
                if words[9] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[9])
                else:
                    st.session_state.selected_words.append(words[9])
        else:
            btn9 = st.button(words[9], key=9, disabled=True, use_container_width=True)
    with col3:
        if words[10] not in st.session_state.correct_words:
            if st.button(words[10], key=10, use_container_width=True):
                if words[10] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[10])
                else:
                    st.session_state.selected_words.append(words[10])
        else:
            btn10 = st.button(words[10], key=10, disabled=True, use_container_width=True)
    with col4:
        if words[11] not in st.session_state.correct_words:
            if st.button(words[11], key=11, use_container_width=True):
                if words[11] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[11])
                else:
                    st.session_state.selected_words.append(words[11])
        else:
            btn11 = st.button(words[11], key=11, disabled=True, use_container_width=True)
    with col1:
        if words[12] not in st.session_state.correct_words:
            if st.button(words[12], key=12, use_container_width=True):
                if words[12] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[12])
                else:
                    st.session_state.selected_words.append(words[12])
        else:
            btn12 = st.button(words[12], key=12, disabled=True, use_container_width=True)
    with col2:
        if words[13] not in st.session_state.correct_words:
            if st.button(words[13], key=13, use_container_width=True):
                if words[13] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[13])
                else:
                    st.session_state.selected_words.append(words[13])
        else:
            btn13 = st.button(words[13], key=13, disabled=True, use_container_width=True)
    with col3:
        if words[14] not in st.session_state.correct_words:
            if st.button(words[14], key=14, use_container_width=True):
                if words[14] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[14])
                else:
                    st.session_state.selected_words.append(words[14])
        else:
            btn14 = st.button(words[14], key=14, disabled=True, use_container_width=True)
    with col4:
        if words[15] not in st.session_state.correct_words:
            if st.button(words[15], key=15, use_container_width=True):
                if words[15] in st.session_state.selected_words:
                    st.session_state.selected_words.remove(words[15])
                else:
                    st.session_state.selected_words.append(words[15])
        else:
            btn15 = st.button(words[15], key=15, disabled=True, use_container_width=True)

def has_common_thread(selected_words):
    
    list1 = ["Oso","Judge","Line","Baptist"] #Related to Baylor University
    list2 = ["The Old","Palos Verdes","Vaquero","Livestock"] #Related to Rancho
    list3 = ["Gourd","Fest","Harvest","Spooky"] #Related to October
    list4 = ["Lively","Daphne","Shelton","William"] #Famous 'Blakes'
    
    
    for words in [list1, list2, list3, list4]:
        if all(word in words for word in selected_words):
            return True
    return False

def count_words(list_str):
    count = 0
    for word in list_str:
        count = count + 1
    return count

    

def main():
    st.title("Final Challenge: Connections")
    st.caption("Rules: Find common threads between words. You must select four groups of four words without making more than four mistakes. Select four words at a time and click 'Submit.' Once you submit, click 'Next Round.' To remove a selection, select the word in the grid again. Good luck.")
    with st.sidebar:
        st.subheader("Hints")
        st.caption("There are two levels of hints. 'Basic Help' will give you a hint to the themes. 'Advanced Help' will provide the themes. Only use if absolutely necessary.")
        if st.button("Basic Help"):
            st.write("Theme 1: College")
            st.write("Theme 2: Cowboys en Espanol")
            st.write("Theme 3: Month")
            st.write("Theme 4: Name")
            st.session_state.help_1 = True
        if st.session_state.help_1:
            if st.button("Advanced Help"):
                st.write("Theme 1: Related to 'Baylor University'")
                st.write("Theme 2: Related to 'Rancho'")
                st.write("Theme 3: Related to 'October'")
                st.write("Theme 4: Famous Blakes")
        st.caption("Click below to shuffle the order of the current words.")
        if st.button("Shuffle words"):
            st.session_state.shuffle = True
            st.experimental_rerun()
    
    display_grid()
    st.subheader("Selected Words:") 
    scol1, scol2, scol3, scol4 = st.columns(4, gap="Medium")
    i = 0
    for guess in st.session_state.selected_words:
        if i == 0:
            scol1.button(guess,key="g1",use_container_width=True, type="primary")
        elif i == 1:
            scol2.button(guess,key="g2",use_container_width=True, type="primary")
        elif i == 2:
            scol3.button(guess,key="g3",use_container_width=True, type="primary")
        elif i == 3:
            scol4.button(guess,key="g4",use_container_width=True, type="primary")
        i = i+1
    
    #st.write(st.session_state.selected_words)
    
    if st.session_state.game_over == True:
        st.session_state.game_over = False
        
        
    
    if st.button("Submit"):
        if count_words(st.session_state.selected_words) != 4:
            st.warning("Please select FOUR words at a time.")
            st.session_state.selected_words = []
            if st.button("Reset"):
                st.experimental_rerun()
        else:
            if has_common_thread(st.session_state.selected_words):
                for word in st.session_state.selected_words:
                    st.session_state.correct_words.append(word)
                # Display success message
                correct_theme1 = ""
                if "Oso" in st.session_state.selected_words:
                    st.session_state.correct_themes.append("Related to 'Baylor University'")
                    correct_theme1 = "Related to 'Baylor University'"
                elif "The Old" in st.session_state.selected_words:
                    st.session_state.correct_themes.append("Related to 'Rancho'")
                    correct_theme1 = "Related to 'Rancho'"
                elif "Gourd" in st.session_state.selected_words:
                    st.session_state.correct_themes.append("Related to 'October'")
                    correct_theme1 = "Related to 'October'"
                elif "Lively" in st.session_state.selected_words:
                    st.session_state.correct_themes.append("Famous Blakes")
                    correct_theme1 = "Famous Blakes"
                    
                st.success(f"Correct! Selected words follow the theme {correct_theme1}.")
                st.session_state.selected_words = []
                if count_words(st.session_state.correct_words) == 16:
                    st.balloons()
                    st.success("WINNER WINNER CHICKEN DINNER!")
                    st.session_state.win_game = True
                    if st.button('CONTINUE...',use_container_width=True, type="primary"):
                        st.experimental_rerun()        
  
            else:
                st.session_state.mistakes += 1
                if st.session_state.mistakes == 4:
                    st.error("Welp. That's the maximum number of mistakes my friend. Ya done. Click 'Try again.'")
                    st.session_state.selected_words = []
                    st.session_state.mistakes = 0
                    st.session_state.correct_words = []
                    st.session_state.game_over = True
                    st.session_state.correct_themes = []
                else:
                    st.warning("Nah - one try down.")
                    st.session_state.selected_words = []
        if st.session_state.game_over == False:
            if st.session_state.win_game == False:
                if st.button("Next Round", use_container_width=True, type="primary"):
                    st.experimental_rerun()        
        else:
            if st.button("Try Again"):                
                st.experimental_rerun()
    tries = 4-st.session_state.mistakes
        
        
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.subheader("Found Themes:")
        for theme_found in st.session_state.correct_themes:
            st.write(theme_found)
            if theme_found == "Related to 'Baylor University'":
                st.caption("Oso, Judge, Line, Baptist")
            if theme_found == "Related to 'Rancho'":
                st.caption ("The Old, Palos Verdes, Vaquero, Livestock")
            if theme_found == "Related to 'October'":
                st.caption("Gourd, Fest, Harvest, Spooky")
            if theme_found == "Famous Blakes":
                st.caption("Lively, Daphne, Shelton, William")
    with info_col2:
        st.subheader("Lives:")
        if tries == 4:
            st.write(":face_with_cowboy_hat: :face_with_cowboy_hat: :face_with_cowboy_hat: :face_with_cowboy_hat:")
        elif tries == 3:
            st.write (":face_with_cowboy_hat: :face_with_cowboy_hat: :face_with_cowboy_hat: :skull_and_crossbones:")
        elif tries == 2:
            st.write(":face_with_cowboy_hat: :face_with_cowboy_hat: :skull_and_crossbones: :skull_and_crossbones:")
        elif tries == 1:
            st.write(":face_with_cowboy_hat: :skull_and_crossbones: :skull_and_crossbones: :skull_and_crossbones:")
        elif tries == 0:
            st.write(":skull_and_crossbones: :skull_and_crossbones: :skull_and_crossbones: :skull_and_crossbones:")
def send_post_request(apikey, dbowner, dbname, sql):
    url = 'https://api.dbhub.io/v1/execute'
    
    data = {
        'apikey': apikey,
        'dbowner': dbowner,
        'dbname': dbname,
        'sql': sql
    }
    try:
        # Send the POST request
        response = requests.post(url, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return "200"  # Return the response content
        else:
            return f"Request failed with status code {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def encode_to_base64(input_string):
    # Encode the input string to Base64
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    
    # Convert the bytes to a string
    encoded_string = encoded_bytes.decode('utf-8')
    
    return encoded_string

def win_game():
#To Do: Code for altering the name 
    st.subheader('Would you accept the prestigious role of becoming my')    
    st.title(f"{st.session_state.whodis}?")
    st.caption("Disclaimer: May require a detour to your 2024 summer plans and a penchant for outshining everyone else's punctuality. Prepare for unexpected applause..")
    st.balloons()

    col_answer1, col_answer2 = st.columns(2)
    with col_answer1:
        if st.button("Yes",use_container_width=True, type="primary"):
            """NOICE"""
            #st.caption("Here's even more balloons! A celebratory drink should arrive at your house tonight - reach out to Blake and let him know you've completed the games.")
            if st.session_state.submitted == False:
                utc_now = datetime.now(pytz.utc)
                query = f"INSERT INTO tblParty(FinishStamp,Name) VALUES('{utc_now}','{st.session_state.user}');"
                sql = encode_to_base64(query)
                submit_time = send_post_request(db_key1,db_owner1,db_name1,sql)
                if submit_time == "200":
                    st.caption("Here's even more balloons! A celebratory drink should arrive at your house tonight - reach out to Blake and let him know you've completed the games.")
                else:    
                    st.caption("A celebratory drink should arrive at your house tonight - reach out to Blake and let him know you've completed the games.")
                    st.error(f"Weird that the database doesn't know you're done. Balloons anyway. {submit_time}")
            else:
                st.caption("Here's even more balloons! A celebratory drink should arrive at your house tonight - reach out to Blake and let him know you've completed the games.")
            st.balloons()
            if st.button('I WANT MORE BALLOONS',use_container_width=True):
                st.balloons()


            
    with col_answer2:
        btn14 = st.button("No", disabled=True, use_container_width=True)
                
        
def login():
    placeholder = st.empty()
    with placeholder.form("Enter Login"):
        user_input = st.text_input("Username")
        secret_input = st.text_input("Secret", type="password")
        secret_btn = st.form_submit_button("Login")
    if secret_btn:
        if secret_input == app_code: #TODO - use app secrets: == secret
            #st.session_state.authenticated = True
            
            if user_input.lower() == names[0] or user_input.lower() == names[1]:
                st.session_state.whodis = "Best Ma'am"
                st.session_state.user = "MK"
                st.session_state.authenticated = True
            elif user_input.lower() == names[2] or user_input.lower() == names[3]:
                st.session_state.whodis = "Nate of Honor"
                st.session_state.user = "Natty"
                st.session_state.authenticated = True
            elif user_input.lower() == names[4] or user_input.lower() == names[5]:
                st.session_state.whodis = "Groomsman"
                st.session_state.user = "Scoot"
                st.session_state.authenticated = True
            elif user_input.lower() == names[6]:
                st.session_state.whodis = "Groomsman"
                st.session_state.user = "Austin"
                st.session_state.authenticated = True
            elif user_input.lower() == names[7] or user_input.lower() == names[8]:
                st.session_state.whodis = "Groomsman"
                st.session_state.user = "JRho"
                st.session_state.authenticated = True
            elif user_input.lower() == names[9] or user_input.lower() == names[10]:
                st.session_state.whodis = "Groomsman"
                st.session_state.user = "JDaugh"
                st.session_state.authenticated = True
            elif user_input.lower() == names[11]:
                st.session_state.whodis = "Officiant"
                st.session_state.user = "Tyler"
                st.session_state.authenticated = True
            elif user_input.lower() == names[12]:
                st.session_state.whodis = "Test User"
                st.session_state.user = "Anon"
                st.session_state.authenticated = True
            
            if st.session_state.authenticated == True:
                full_name = user_input.split('_')
                first_name = full_name[0]
                st.success(f"Thank you for logging in {first_name}!")
                if st.button("Start the game",use_container_width=True):
                    st.experimental_rerun()
            else:
                st.error("The username or secret is incorrect. Please try again.")
        else:
            st.error("The username or secret is incorrect. Please try again.")

if __name__ == "__main__":
    if st.session_state.authenticated == False:
        login()
    else:    
        if st.session_state.win_game == False:
            main()
        else:
            win_game()
     
