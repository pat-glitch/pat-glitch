import json

# File paths
BADGE_DATA_FILE = "data/credly_badges.json"
README_FILE = "README.md"

# Whitelisted certifications
WHITELIST = [
    "Microsoft Certified: Azure Fundamentals",
    "Associate Cloud Engineer Certification",
    "Cloud Digital Leader Certification",
    "Professional Cloud Network Engineer Certification",
    "Professional Cloud Security Engineer Certification",
    "Professional Cloud DevOps Engineer Certification"
]

def load_badge_data():
    with open(BADGE_DATA_FILE, "r") as f:
        data = json.load(f)
        # Extract the list of badges from the "data" key
        if "data" in data:
            return data["data"]
        else:
            raise ValueError("The JSON structure does not contain the expected 'data' key.")

def update_readme(badge_data):
    # Start writing the README content
    content = "# My Certifications\n\n"
    content += "Here are my latest certifications:\n\n"

    for badge in badge_data:
        badge_name = badge["badge_template"]["name"]
        badge_image = badge["badge_template"]["image_url"]
        badge_issued = badge.get("issued_at_date", "Unknown Date")

        # Only include badges in the whitelist
        if badge_name in WHITELIST:
            content += f'<img src="{badge_image}" alt="{badge_name}" width="200px">\n'
            content += f"**{badge_name}** - Issued on {badge_issued}\n\n"

    # Write to README.md
    with open(README_FILE, "w") as f:
        f.write(content)

def main():
    badge_data = load_badge_data()
    update_readme(badge_data)

if __name__ == "__main__":
    main()
