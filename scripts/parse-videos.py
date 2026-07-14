import json

def load_entries(path):
    with open(path) as f:
        return json.load(f)["entries"]

def pick_latest_and_top(entries):
    if not entries:
        return None, None
    latest = entries[0]
    most_viewed = max(entries, key=lambda e: e.get("view_count") or 0)
    return latest, most_viewed

videos = load_entries("raw_videos.json")
shorts = load_entries("raw_shorts.json")

latest_video, top_video = pick_latest_and_top(videos)
latest_short, top_short = pick_latest_and_top(shorts)

def fmt(entry):
    if not entry:
        return None
    return {"id": entry["id"], "title": entry.get("title", "")}

output = {
    "latest": fmt(latest_video),
    "mostViewed": fmt(top_video),
    "latestShort": fmt(latest_short),
    "mostViewedShort": fmt(top_short),
}

with open("videos.json", "w") as f:
    json.dump(output, f, indent=2)

print(output)
