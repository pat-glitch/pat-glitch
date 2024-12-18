import json

def update_readme(json_file, readme_file):
    with open(json_file, "r") as f:
        badges = json.load(f)

    with open(readme_file, "w") as f:
        f.write("# My Certifications\n\n")
        for badge in badges:
            f.write(f"![{badge['name']}]({badge['image']})\n")
            f.write(f"**{badge['name']}** - {badge['issued_at']}\n\n")

update_readme("data/CredlyBadges.json", "README.md")
