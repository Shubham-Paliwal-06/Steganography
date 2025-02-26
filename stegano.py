import cv2
import os

def save_metadata(password, message_length, metadata_file="metadata.txt"):
    with open(metadata_file, "w") as f:
        f.write(f"{password}\n{message_length}")

def load_metadata(metadata_file="metadata.txt"):
    try:
        with open(metadata_file, "r") as f:
            lines = f.readlines()
            return lines[0].strip(), int(lines[1].strip())
    except FileNotFoundError:
        return None, 0

def encrypt_message(image_path, output_path, message, password, metadata_file="metadata.txt"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0
    
    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    print("Message encrypted and saved to", output_path)
    os.system(f'start {output_path}')  # Open image on Windows
    
    # Flush file and save new metadata
    with open(metadata_file, "w") as f:
        f.write(f"{password}\n{len(message)}")

def decrypt_message(image_path, password, metadata_file="metadata.txt"):
    stored_password, message_length = load_metadata(metadata_file)
    
    if password != stored_password:
        print("Authentication failed!")
        return
    
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0
    
    for _ in range(message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)

def main():
    image_path = "AIimpact.png"
    output_path = "AIimpact_encrypted.png"
    
    choice = input("Do you want to (1) Encrypt or (2) Decrypt? Enter 1 or 2: ")
    if choice == "1":
        msg = input("Enter secret message: ")
        password = input("Enter a passcode: ")
        encrypt_message(image_path, output_path, msg, password)
    elif choice == "2":
        pas = input("Enter passcode for decryption: ")
        decrypt_message(output_path, pas)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
