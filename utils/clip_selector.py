def select_important_clips(segments, max_clips=3):
    print("🔍 اختيار المقاطع المهمة...")
    selected = []
    for s in segments:
        if any(word in s["text"].lower() for word in ["important", "mistake", "secret", "you should", "don't"]):
            selected.append((s["start"], s["end"]))
            if len(selected) >= max_clips:
                break
    return selected
