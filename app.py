import streamlit as st
import string,re,random

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="💪",
    layout="wide"
)
# Apply custom CSS for black background
# st.markdown(
#     """
#     <style>
#         body {
#             background-color: black;
#             color:white;
#         }
#         .stApp {
#             background-color: black;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("🔑 Password Strength Checker")
st.markdown(f"""
            <h1 style="color: #5EEAD4; ">
        🔑 Password Strength Checker
            </h1>
            """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center;'>Check the strength of your password & get a strong suggestion if needed</p>", unsafe_allow_html=True)

# st.form:
# Custom CSS for input size
st.markdown("""
    <style>
        /* Center the title */
        h1 {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #5EEAD4;
        }

        /* Style the input field */
        div[data-baseweb="input"] {
            width: 600px !important;  
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(94, 234, 212, 0.6);
        }

        /* Button Styling */
        .stButton > button {
            border-radius: 25px;
            width: 200px;
            height: 45px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
            box-shadow: 2px 2px 15px rgba(94, 234, 212, 0.4);
        }

        /* Hover effect for buttons */
        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 2px 2px 25px rgba(94, 234, 212, 0.8);
        }

        /* Password strength popover */
        .popover-box {
            padding: 10px;
            border-radius: 10px;
            background: rgba(94, 234, 212, 0.1);
            text-align: center;
            animation: fadeIn 0.5s ease-in-out;
        }

        /* Fade-in animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0px); }
        }
    </style>
""", unsafe_allow_html=True)

#Initialize ssession stage for generate password
if "generatePass" not in st.session_state:
    st.session_state.generatePass = ""

# for check strength of the password
passStrength = 0

#input for password
ourPassword =  st.text_input("Password",placeholder="Enter Your Password",type="password",value=st.session_state.generatePass)

#add columns for button
colOne,colTwo = st.columns(2)

# column one for check button
with colOne:
    checkBtn = st.button("🔍 Check Password")

# column two for hint button
with colTwo:
    hintBtn = st.button("💡 Get Hint",type="primary")

# generate a password if user doesn't have idea to write a strong password
def generatePassword(length:int):
    lowerCase = string.ascii_lowercase
    digits = string.digits
    upperCase = string.ascii_uppercase
    specialCharacters = string.punctuation
    mergedWithoutSepcial = lowerCase+upperCase+digits

    # Ensure at least one character from each category
    newPassword = [
        random.choice(lowerCase),
        random.choice(upperCase),
        random.choice(digits),
        random.choice(specialCharacters)
    ]

    # Fill Remaining Length
    newPassword.extend(random.choices(mergedWithoutSepcial,k=length-4))

    # Shuffle to randomize order
    random.shuffle(newPassword)

    #return that password in string
    return "".join(newPassword)




#when click on btn
if checkBtn:
    # check if password is not empty
    if ourPassword:
        #check the length of password
        if len(ourPassword) >=8:
            # if condition true it will increment by 1
            passStrength +=1
        else:
            st.error("❌ Please Enter atleast 8 characters")
        
        #check uppercase exist
        if re.search(r"[A-Z]",ourPassword):
            # if condition true it will increment by 1
            passStrength +=1
        else:
            st.error("❌ Please Enter atleast 1 uppercase letter")

        #check lowercase exist
        if re.search(r"[a-z]",ourPassword):
            # if condition true it will increment by 1
            passStrength +=1
        else:
            st.error("❌ Please Enter atleast 1 lowercase letter")

        #check number exist
        if re.search(r"\d",ourPassword):
            # if condition true it will increment by 1
            passStrength+=1
        else:
            st.error("❌ Please Enter atleast one digit (0-9)")
        
        #check special character ehist
        if re.search(r"[#@!$%^{}()=-?/.+,&*_]",ourPassword):
            # if condition true it will increment by 1
            passStrength+=1
        else:
            st.error('❌ Please Enter atleast 1 special character (#@!$%^&*_)')

         # if it's equal to 5 so the password is strong
        if passStrength == 5:
            st.success("Password is Strong")
            st.balloons()
        
        # if it's equal to 4 so the password is moderate
        elif passStrength == 4:
            st.warning("Password is Moderate")

        # otherwise password is weak
        else:
            st.error("Password is Weak")
    else:
        st.error("❌ Please Enter a Password")


# when click on hint button, so the popover will show
if hintBtn or passStrength in [3, 4,2,1]:
    #save the randon generated password in session state
    st.session_state.generatePass = generatePassword(8)
    st.markdown(
        f"""
        <div class="popover-box">
            <p>🔹  Try this strong password:</p>
            <p style="font-weight: bold; font-size: 18px; color: #FFD700; padding:0 5px; border:2px dashed #FFD700; width:100px;">{st.session_state.generatePass}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    