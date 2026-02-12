# import customtkinter as ctk
# from PIL import Image
# import threading
# import Client as clnt
# root = ctk.CTk()

# dynamic_background_color="#16423C"
# dynamic_text_color="#F5F7F8"
# dynamic_border_color="#C4DAD2"
# dynamic_hover_color="#6A9C89"

# root.configure(fg_color=dynamic_background_color)
# root.geometry("900x700")
# root.title("CLIENT HANDLER")

# heading_label=ctk.CTkLabel(root,text="Welcome, Dear !!!, Client", height=100,font=("New Roman",40,"italic"),fg_color=dynamic_hover_color,corner_radius=15)
# heading_label.pack(pady=(30,10),fill="x", padx=10)

# scr_frame=ctk.CTkScrollableFrame(root,height=200,fg_color=dynamic_hover_color,scrollbar_button_color=dynamic_text_color,scrollbar_button_hover_color=dynamic_background_color)
# scr_frame.pack(pady=(20,10),fill="x",padx=10)

# text_area=ctk.CTkTextbox(root,height=150, fg_color="black",font=("Arial",15,"bold"),scrollbar_button_color=dynamic_text_color,scrollbar_button_hover_color=dynamic_border_color,text_color="white")
# text_area.pack(pady=(20,10),fill="x",padx=10)

# def createLabel():
    
#     send_message=text_area.get("0.0",'end')
   
   
#     receive_thread = threading.Thread(target=clnt.receiveData)
#     send_thread = threading.Thread(target=clnt.sendData,args=[send_message])
    
#     lbl=ctk.CTkLabel(scr_frame,text=str(receive_thread),width=50, height=10,corner_radius=20, font=("arial",13,"italic"),text_color="white",fg_color=dynamic_background_color)
#     lbl.pack(pady=(20,10),padx=100,side="bottom",anchor="center",fill="x")
    
#     receive_thread.start()
#     send_thread.start()


#     receive_thread.join()
#     send_thread.join()
#     if str(send_message).lower()=="finish":
#         clnt.closeConnection()
#     text_area.delete("0.0","end")
    

# send_btn=ctk.CTkButton(root,command=createLabel,height=100,fg_color=dynamic_hover_color,font=("Arial",25,"bold"),text="SEND",text_color=dynamic_background_color,hover_color=dynamic_border_color)
# send_btn.pack(pady=(20,10),padx=10,fill="x")

# root.mainloop()


import customtkinter as ctk
from PIL import Image
import threading
import Client as clnt  # Assuming this is your client module

# Define UI colors
dynamic_background_color = "#16423C"
dynamic_text_color = "#F5F7F8"
dynamic_border_color = "#C4DAD2"
dynamic_hover_color = "#6A9C89"

# Set up the main application window
root = ctk.CTk()
root.configure(fg_color=dynamic_background_color)
root.geometry("900x700")
root.title("CLIENT HANDLER")

# Create the heading label
heading_label = ctk.CTkLabel(root, text="Welcome, Dear !!!, Client", height=100, font=("New Roman", 40, "italic"),
                             fg_color=dynamic_hover_color, corner_radius=15)
heading_label.pack(pady=(30, 10), fill="x", padx=10)

# Create the scrollable frame for dynamic labels
scr_frame = ctk.CTkScrollableFrame(root, height=200, fg_color=dynamic_hover_color,
                                   scrollbar_button_color=dynamic_text_color, scrollbar_button_hover_color=dynamic_background_color)
scr_frame.pack(pady=(20, 10), fill="x", padx=10)

# Create the text area for user input
text_area = ctk.CTkTextbox(root, height=150, fg_color="black", font=("Arial", 15, "bold"),
                           scrollbar_button_color=dynamic_text_color, scrollbar_button_hover_color=dynamic_border_color, text_color="white")
text_area.pack(pady=(20, 10), fill="x", padx=10)


# Function to handle sending and receiving messages
def createLabel():
    send_message = text_area.get("0.0", 'end').strip()  # Get message from text area
    if not send_message:  # If no message is entered, do nothing
        return

    # Start threads for sending and receiving data
    receive_thread = threading.Thread(target=update_received_message)
    send_thread = threading.Thread(target=clnt.sendData, args=[send_message])

    receive_thread.start()
    send_thread.start()

    if send_message.lower() == "finish":
        clnt.closeConnection()

    text_area.delete("0.0", "end")  # Clear the text area


# Function to update the UI with the received message from the client
def update_received_message():
    received_data = clnt.receiveData()  # Simulating the function that fetches the client's response

    # Use the main thread to update the UI safely
    root.after(0, lambda: create_client_label(received_data))


# Helper function to create a new label in the scrollable frame
def create_client_label(message):
    lbl = ctk.CTkLabel(scr_frame, text=message, width=50, height=30, corner_radius=20, font=("Arial", 15, "italic"),
                       text_color="white", fg_color=dynamic_background_color)
    lbl.pack(pady=(20, 10), padx=100, anchor="center", fill="x")


# Create the send button
send_btn = ctk.CTkButton(root, command=createLabel, height=100, fg_color=dynamic_hover_color, font=("Arial", 25, "bold"),
                         text="SEND", text_color=dynamic_background_color, hover_color=dynamic_border_color)
send_btn.pack(pady=(20, 10), padx=10, fill="x")

# Run the main event loop
root.mainloop()
