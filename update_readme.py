# import os
# import re

# README_TEMPLATE = "README_TEMPLATE.md"
# README_OUTPUT = "README.md"

# def extract_day_num(folder):
#     match = re.search(r"DAY(\d+)", folder, re.IGNORECASE)
#     return int(match.group(1)) if match else None

# def load_folders():
#     folders = [
#         f for f in os.listdir(".")
#         if os.path.isdir(f) and f.upper().startswith("DAY")
#     ]
#     folders.sort(key=extract_day_num)
#     return folders

# def build_table(folders):
#     rows = []
#     rows.append("| Day | Folder |")
#     rows.append("|-----|---------|")

#     for folder in folders:
#         day_num = extract_day_num(folder)
#         rows.append(f"| {day_num:02d} | [{folder}](./{folder}) |")

#     return "\n".join(rows)

# def main():
#     folders = load_folders()
#     table_md = build_table(folders)

#     with open(README_TEMPLATE, "r") as f:
#         template = f.read()

#     updated = template.replace("<!--DAY_TABLE-->", table_md)

#     with open(README_OUTPUT, "w") as f:
#         f.write(updated)

#     print("README.md updated successfully!")

# if __name__ == "__main__":
#     main()
