from datetime import datetime

TAGS = {
    "URGENT:": [],
    "GENERAL TASK:": [],
    "NOTE:": []
}

unsorted = []

def read_tasks(filename):
    """Read the raw text file and sort each line under the right tag."""
    print("(1) Reading your raw text file..\n")

    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
    print(contents)

    for line in contents.splitlines():
        line = line.strip()
        if not line:
            continue
            
        matched = False
        for tag, value in TAGS.items():
            if line.startswith(tag):
                cleaned_text = line.removeprefix(tag).strip()
                value.append(cleaned_text)
                matched = True
                break
                
        if not matched:
            print(f"*Warning! {line} does not match any tag.")
            unsorted.append(line)


def write_tasks(f, title, items, empty_message="Nothing here!"):
    """Write tasks with checkboxes."""
    f.write(f"\n## {title}\n")
    
    for item in items:
        f.write(f"- [ ] {item}\n")

    if not items:
        f.write(f"- {empty_message}\n")
        return


def build_agenda(filename):
    print("\n(2) Building agenda checklist..")

    urgents = TAGS["URGENT:"]
    general_tasks = TAGS["GENERAL TASK:"]
    notes = TAGS["NOTE:"]

    with open(filename, "w", encoding="utf-8") as f:
        today = datetime.now().strftime("%B %d, %Y")
        f.write("# AGENDA & TO-DO LIST\n")
        f.write(f"*Today's date* : {today}\n\n")
        f.write("------\n\n")

        f.write("## AT A GLANCE\n")
        f.write(f"- ***Number of urgent tasks*** : {len(urgents)}\n")
        f.write(f"- ***Number of general tasks*** : {len(general_tasks)}\n")
        f.write(f"- ***Number of notes*** : {len(notes)}\n")
        f.write(f"- ***Number of unsorted items*** : {len(unsorted)}\n")

        write_tasks(f, "URGENT *ACTION REQUIRED IMMEDIATELY*", urgents,
                       empty_message="No urgent tasks!")
        write_tasks(f, "GENERAL TASKS", general_tasks,
                       empty_message="No general tasks!")
        write_tasks(f, "NOTES", notes,
                       empty_message="No notes!")
        write_tasks(f, "UNSORTED *Could not match a tag*", unsorted,
					   empty_message="All sorted!")

    print("\n(3) Done! Open 'new_agenda.md' to see your agenda.")


read_tasks("raw_tasks.txt")
build_agenda("new_agenda.md")
