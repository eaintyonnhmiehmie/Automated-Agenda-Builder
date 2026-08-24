# Automated-Agenda-Builder
This is a Python automation tool to sort raw notes and generate categorized agenda and task checklists.

## Problems it solves
- Too much time spent on manually reorganizing agenda
- Urgent tasks getting lost
- No clear overview of action items and notes at a glance

## How to use
1. Write down tasks and notes in raw_tasks.txt
2. Run the script
   ```bash
   agenda_builder.py
   ```
3. Open new_agenda.md in a text editor.

### Input formatting rules
To ensure the script categorizes each item properly,
- Start every line with one of the 3 supported tags: `URGENT:`, `GENERAL TASK:`, or `NOTE:`.
- Place each task or note on its own line (e.g., `URGENT: Submit report`).
- Lines that do not fit any tag will be placed in the unsorted section.
