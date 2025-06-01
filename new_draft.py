import os
from datetime import datetime

def create_draft(title):
    safe_title = (
        title.lower()
        .replace(" ", "-")
        .replace(":", "")
        .replace("/", "-")
        .replace("\\", "-")
    )
    filename = f"{safe_title}.md"
    drafts_dir = "_drafts"
    os.makedirs(drafts_dir, exist_ok=True)
    filepath = os.path.join(drafts_dir, filename)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""---
title: "{title}"
date: {now}
tags: []
---

# {title}

Start writing here...
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Draft created: {filepath}")

if __name__ == "__main__":
    user_title = input("Enter the draft title: ").strip()
    create_draft(user_title) 