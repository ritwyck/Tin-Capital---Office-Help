import os
from extract_msg import Message


def convert_msg_to_txt(msg_file):
    try:
        msg = Message(msg_file)
        msg_subject = msg.subject
        msg_body = msg.body
        txt_file = msg_file[:-4] + ".txt"  # replace .msg with .txt

        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(f"Subject: {msg_subject}\n\n")
            f.write(msg_body)

        print(f"Converted {msg_file} to {txt_file}")

    except Exception as e:
        print(f"Failed to convert {msg_file}: {e}")


def convert_msgs_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".msg"):
                msg_file = os.path.join(root, file)
                convert_msg_to_txt(msg_file)


# Replace 'folder_path' with the path to your folder containing .msg files
folder_path = '/Users/wiksrivastava/Desktop/tinCapital/Email_Confirmation/Emails'
convert_msgs_in_folder(folder_path)
