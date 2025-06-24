# DATA-HIDING-IN-IMAGES
XOR-Based Steganography Tool:-
A Python-based GUI application to hide and reveal secret messages in image files using LSB (Least Significant Bit) steganography and optional XOR encryption for added security.

🔐 Features
Hide text messages inside .png, .bmp, or .tiff images.

Secure your message with a password using XOR encryption.

Extract and decrypt hidden messages from steganographic images.

Simple and user-friendly Tkinter GUI.

End-of-message marker for reliable message recovery.

📦 Requirements
Python 3.x

Pillow for image handling

numpy for efficient image data manipulation

Install required libraries:

bash
Copy
Edit
pip install pillow numpy
🚀 How to Use
1. Run the App
Save the script to a .py file and run:

bash
Copy
Edit
python steganography_tool.py
2. Hide a Message
Click "Hide Message in Image".

Select a cover image (.png, .bmp, .tiff).

Enter your secret message.

(Optional) Choose to encrypt the message with a password.

Choose a location and name for the output image.

A new image with the hidden message will be saved.

3. Reveal a Message
Click "Reveal Message from Image".

Select the image containing a hidden message.

If encrypted, you’ll be prompted to enter the password.

The message will be displayed.

📌 Notes
The application uses XOR cipher for basic encryption (not secure for high-risk applications).

Make sure your image is large enough to hide your message (1 char ≈ 8 bits).

Uses a binary end marker (1111111111111110) to detect the end of a message.

🛡️ Disclaimer
This tool is for educational and personal privacy use only. It is not intended for secure communication in high-risk environments.
