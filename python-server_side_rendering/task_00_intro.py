#!/usr/bin/python3
from string import Template
import string

def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str):
        print("Error: Template is not str")
        return
    if not isinstance(attendees, list):
        print("Error: attendees is not a list")
        return

    if not template_content.strip():
        print("Error: Template is empty")
        return
    
    if not attendees:
        print("Error: attendees is empty.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        try:
            name = attendee.get("name") if attendee.get("name") else "N/A"
            output_content = template_content.replace('{name}', attendee.get("name", "N/A")) 
            event_title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
            output_content = output_content.replace('{event_title}', attendee.get("event_title", "N/A"))
            event_location = attendee.get("event_location") if attendee.get("event_location") else "N/A"
            output_content = output_content.replace('{event_location}', attendee.get("event_location", "N/A"))
            event_date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
            output_content = output_content.replace('{event_date}', event_date)
        except KeyError as e:
            print(f"Error: Clave faltante {e} en los datos del asistente.")
            continue
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
