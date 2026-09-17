import subprocess
import os

jpg_file = "Birmanese.jpg"
png_file = "Ragdoll.png"
zip_file = "metadata.zip"
zip_password = "P4ssw0rdC4t" # You can change this

# 1. Create a password-protected zip containing Birmanese.jpg
print("[*] Zipping Birmanese.jpg with password...")
subprocess.run(["zip", "-P", zip_password, zip_file, jpg_file], check=True)

# 2. Hide the zip password in Ragdoll.png's EXIF data (using the Comment tag)
print("[*] Embedding password into Ragdoll.png EXIF data...")
subprocess.run(["exiftool", f"-Comment={zip_password}", "-overwrite_original", png_file], check=True)

# 3. Append the zip archive to the end of Ragdoll.png (EOF injection)
print("[*] Appending zip archive to the end of Ragdoll.png...")
with open(zip_file, "rb") as z_in:
    zip_data = z_in.read()

with open(png_file, "ab") as p_out:
    p_out.write(zip_data)

# 4. Clean up the standalone zip file to leave only the final PNG
os.remove(zip_file)

print(f"[+] Done! {png_file} now contains the hidden zip at its EOF, and the password is in its EXIF data.")