import json

# File paths
BADGE_DATA_FILE = "data/credly_badges.json"
README_FILE = "README.md"

def load_badge_data():
    with open(BADGE_DATA_FILE, "r") as f:
        return json.load(f)

def update_readme(badge_data):
    # Start writing the README content
    content = "# My Certifications\n\n"
    content += "Below is the list of my certifications fetched from [Credly](https://www.credly.com/):\n\n"

    for badge in badge_data:
        badge_name = badge["name"]
        badge_image = badge["image"]
        badge_issued = badge["issued_at"]
        content += f"![{badge_name}]({badge_image})\n"
        content += f"**{badge_name}** - Issued on {badge_issued}\n\n"

    # Write to README.md
    with open(README_FILE, "w") as f:
        f.write(content)

def main():
    badge_data = load_badge_data()
    update_readme(badge_data)

if __name__ == "__main__":
    main()
