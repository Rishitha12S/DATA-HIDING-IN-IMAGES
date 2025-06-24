import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image
import numpy as np
import base64

# === XOR ENCRYPTION ===
def xor_encrypt_decrypt(message, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))

def encrypt_message(message, password):
    return "ENC:" + base64.b64encode(xor_encrypt_decrypt(message, password).encode()).decode()

def decrypt_message(encrypted_text, password):
    try:
        decoded = base64.b64decode(encrypted_text).decode()
        return xor_encrypt_decrypt(decoded, password)
    except:
        return None

# === STEGANOGRAPHY FUNCTIONS ===
def text_to_bin(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def hide_message(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)
    binary_message = text_to_bin(message) + '1111111111111110'  # End marker
    flat_data = data.flatten()

    if len(binary_message) > len(flat_data):
        raise ValueError("Message too long for this image.")

    for i in range(len(binary_message)):
        flat_data[i] = (flat_data[i] & 254) | int(binary_message[i])

    new_data = flat_data.reshape(data.shape)
    new_img = Image.fromarray(new_data.astype('uint8'), 'RGB')
    new_img.save(output_path)

def reveal_message(image_path):
    img = Image.open(image_path).convert('RGB')
    data = np.array(img).flatten()
    bits = [str(pixel & 1) for pixel in data]
    binary = ''.join(bits)
    end_marker = '1111111111111110'
    end_index = binary.find(end_marker)
    if end_index != -1:
        return bin_to_text(binary[:end_index])
    return None

# === GUI ===
def select_image_to_hide():
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp *.tiff")])
    if not img_path:
        return
    message = simpledialog.askstring("Message", "Enter the message to hide:")
    if not message:
        return
    use_password = messagebox.askyesno("Encrypt", "Do you want to password-protect the message?")
    if use_password:
        pwd = simpledialog.askstring("Password", "Enter password:", show='*')
        message = encrypt_message(message, pwd)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    try:
        hide_message(img_path, message, save_path)
        messagebox.showinfo("Success", f"Message hidden in:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_image_to_reveal():
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.bmp *.tiff")])
    if not img_path:
        return
    message = reveal_message(img_path)
    if not message:
        messagebox.showerror("Error", "No hidden message found.")
        return
    if message.startswith("ENC:"):
        pwd = simpledialog.askstring("Password", "Enter password to decrypt:", show='*')
        decrypted = decrypt_message(message[4:], pwd)
        if decrypted is not None:
            message = decrypted
        else:
            messagebox.showerror("Error", "Wrong password or corrupt message.")
            return
    messagebox.showinfo("Hidden Message", message)

# === GUI Layout ===
root = tk.Tk()
root.title("Steganography Tool (XOR-Based)")

tk.Label(root, text="🕵️‍♂️ Steganography: XOR Message Hiding", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Hide Message in Image", command=select_image_to_hide, width=30).pack(pady=5)
tk.Button(root, text="Reveal Message from Image", command=select_image_to_reveal, width=30).pack(pady=5)

root.mainloop()
