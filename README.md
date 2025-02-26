# Steganography

## Overview
This project implements **image-based steganography** using OpenCV in Python. It allows users to securely hide a secret message inside an image and retrieve it using a password, ensuring confidentiality and preventing unauthorized access.

## Features
- **Secure Message Embedding:** Uses pixel manipulation to hide text inside an image.
- **Password-Protected Decryption:** Ensures only authorized users can extract the message.
- **Metadata Storage:** Stores encryption details (password & message length) for accurate retrieval.
- **Minimal Image Distortion:** Embeds messages while preserving image quality.
- **Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.

## Technologies Used
- **Python 3.6+**
- **OpenCV (cv2)** for image processing
- **File Handling** for storing metadata
- **OS Module** for system interactions

## System Requirements
- **OS:** Windows, macOS, or Linux
- **RAM:** Minimum 4GB (8GB recommended)
- **Processor:** Intel i3 or higher
- **Storage:** At least 500MB free space
- **Python Libraries:** Install dependencies using:
  ```sh
  pip install opencv-python
  ```

## Installation & Usage
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/Image-Steganography.git
cd Image-Steganography
```

### 2. Encrypt a Message
1. Place an image (e.g., `AIimpact.png`) in the project directory.
2. Run the script:
   ```sh
   python image_steganography.py
   ```
3. Select encryption (`1`), enter a message, and set a password.

### 3. Decrypt a Message
1. Run the script again:
   ```sh
   python image_steganography.py
   ```
2. Select decryption (`2`) and enter the correct password.
