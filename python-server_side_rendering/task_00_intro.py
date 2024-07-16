#!/usr/bin/python3
from string import Template
import string

def generate_invitations(template_content, attendees):
# Read the template from a file
    template = string.Template(template_content)
    for index, attendee in enumerate(attendees, start=1):
        try:
            output_content = template.safe_substitute(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A") if attendee.get("event_date") else "N/A",
                event_location=attendee.get("event_location", "N/A")
            )
        except KeyError as e:
            print(f"Error: Missing key {e} in attendee data.")
            continue

        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
