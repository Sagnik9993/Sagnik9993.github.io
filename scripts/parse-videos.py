import json

with open("raw.json") as f:
    data = json.load(f)

entries = data["entries"]

# Channel's videos tab lists newest first
latest = entries[0]

# Highest view count among the checked videos
most_viewed = max(entries, key=lambda e: e.get("view_count") or 0)

output = {
    "latest": {"id": latest["id"], "title": latest.get("title", "")},
    "mostViewed": {"id": most_viewed["id"], "title": most_viewed.get("title", "")},
}

with open("videos.json", "w") as f:
    json.dump(output, f, indent=2)

print(output)
