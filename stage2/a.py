from stegano import lsb

secret_url = "https://www.mediafire.com/view/q3hz1h7rmcugr83"
input_image = "Orange.png"
output_image = "Orange.png" # Overwriting the original to keep the same filename

print("[*] Hiding URL in the LSB of Orange.png...")
# Hide the data and save
secret = lsb.hide(input_image, secret_url)
secret.save(output_image)

print(f"[+] Done! The URL is now hidden inside the LSB of {output_image}")
