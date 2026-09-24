import shutil
src = r"C:\Users\Ethan Jude R. Reyes\.gemini\antigravity\brain\c55adf21-e0a3-436e-bc0d-900c612a9640\.user_uploaded\uploaded_media_1790251398036.mp3"
dst = r"C:\Users\Ethan Jude R. Reyes\OneDrive\Documents\VSCode\OGIS-IGNITE\song.mp3"
shutil.copy(src, dst)
print("Copied successfully.")
