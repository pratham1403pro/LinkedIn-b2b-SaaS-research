import requests
import os

# API keys stored separately, not committed to repo
SUPADATA_API_KEY = "YOUR_API_KEY_HERE"

videos = {
    "Adam_Robinson": [
        "https://youtube.com/watch?v=eUzqVJpZPP4",
        "https://youtube.com/watch?v=kS9ii5vYbOM"
    ],
    "Richard_van_der_Blom": [
        "https://youtube.com/watch?v=QkYcDycfsIA",
        "https://youtube.com/watch?v=qhzyFBPz-bQ"
    ],
    "Lara_Acosta": [
        "https://youtube.com/watch?v=e3E83C-Xxn0",
        "https://youtube.com/watch?v=7SKd2cchGd4"
    ],
    "Pierre_Herubel": [
        "https://youtube.com/watch?v=mc7nK3PYgjw",
        "https://youtube.com/watch?v=h9BQP6-IzZo"
    ],
    "Devin_Reed": [
        "https://youtube.com/watch?v=-RAJVNnewkY",
        "https://youtube.com/watch?v=KDhM9j3utEQ"
    ],
    "Kevin_Indig": [
        "https://youtube.com/watch?v=Har2UcMSNHA",
        "https://youtube.com/watch?v=AFYhY6lvk2E"
    ],
    "Ross_Simmonds": [
        "https://youtube.com/watch?v=BUZQeQ2w8iQ",
        "https://youtube.com/watch?v=wXOou9LE-hA"
    ],
    "Andrei_Zinkevich": [
        "https://youtube.com/watch?v=V9SSusoVqZA",
        "https://youtube.com/watch?v=wCWlQ1uEnlQ"
    ],
    "Sam_Dunning": [
        "https://youtube.com/watch?v=v0f6gBXt6oQ",
        "https://youtube.com/watch?v=SDvsVDbP7ro"
    ],
    "Daniel_Murray": [
        "https://youtube.com/watch?v=tmzgUeplYsA",
        "https://youtube.com/watch?v=YgnWgwS5FcA"
    ]
}

output_dir = r"C:\Users\Lenovo\Desktop\transcripts"
os.makedirs(output_dir, exist_ok=True)

for person, urls in videos.items():
    for i, url in enumerate(urls, 1):
        print(f"Fetching transcript: {person} - video {i}")
        try:
            response = requests.get(
                "https://api.supadata.ai/v1/youtube/transcript",
                headers={"x-api-key": SUPADATA_API_KEY},
                params={"url": url, "text": "true"}
            )
            if response.status_code == 200:
                data = response.json()
                transcript = data.get("content", "No transcript available")
                filename = f"{person}_video{i}.txt"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"Source: {url}\n\n")
                    f.write(transcript)
                print(f"  Saved: {filename}")
            else:
                print(f"  Error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"  Failed: {e}")

print("\nDone! Check your Desktop/transcripts folder.")
