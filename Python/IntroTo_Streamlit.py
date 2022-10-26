# To Upload the stramlit logo:
try:
  from PIL import Image
  logo = Image.open('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg')
  print(logo)

###################################

# To Install streamlit into your system: pip install streamlit
# To test if the installation is working or not : streamlit hello
# How to run your Streamlit code: streamlit run file_name.py

# To Import streamlit into your system:
except Exception as e:
  # print(e)
  
finally:
  
  import streamlit as st

  # To create title in streamlit:

  st.title('Hello, welcome to my streamlit app!')


  # App link: https://abdullahjaffrey-practiceprograme-pythonintroto-streamlit-vxtc3r.streamlitapp.com/

  # To write paragraph:

  st.write('This is something of a random paragraph!')


  st.write("""rem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentiumoptio, eaque rerum! Provident similique accusantium nemo autem. Veritatisobcaecati tenetur iure eius earum ut molestias architecto voluptate aliquamnihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdamrecusandae alias error harum maxime adipisci amet laborum. Perspiciatis minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit quibusdam sed amet tempora. Sit laborum ab, eius fugit doloribus tenetur fugiat, temporibus enim commodi iusto libero magni deleniti quod quam consequuntur! Commodi minima excepturi repudiandae velit hic maximedoloremque. Quaerat provident commodi consectetur veniam similique ad earum omnis ipsum saepe, voluptas, hic voluptates pariatur est explicabo fugiat, dolorum eligendi quam cupiditate excepturi mollitia maiores labore suscipit quas? Nulla, placeat. Voluptatem quaerat non architecto ab laudantiummodi minima sunt esse temporibus sint culpa, recusandae aliquam numquam totam ratione voluptas quod exercitationem fuga. Possimus quis earum veniam quasi aliquam eligendi, placeat qui corporis!""")
