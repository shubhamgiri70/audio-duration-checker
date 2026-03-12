import os
import librosa

folder = "dataset"

durations = []

for file in os.listdir(folder):
    if file.endswith(".wav") or file.endswith(".mp3"):

        path = os.path.join(folder, file)

        audio, sr = librosa.load(path, sr=None)

        duration = len(audio) / sr

        durations.append(duration)

        print(f"{file} → {round(duration,2)} seconds")

print("\nDataset Stats")

total_files = len(durations)

if total_files > 0:
    total_duration = sum(durations)
    avg_duration = total_duration / total_files
    shortest = min(durations)
    longest = max(durations)

    print(f"Files analyzed: {total_files}")
    print(f"Total duration: {round(total_duration,2)} seconds")
    print(f"Average duration: {round(avg_duration,2)} seconds")
    print(f"Shortest clip: {round(shortest,2)} seconds")
    print(f"Longest clip: {round(longest,2)} seconds")

else:
    print("No audio files found")