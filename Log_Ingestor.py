
import gradio as gr
from pymongo import MongoClient
import win32evtlog
import win32evtlogutil
import datetime
import tkinter as tk
from tkinter import messagebox

# MongoDB setup
port=0000
mongo_client = MongoClient('localhost', port=port)
db = mongo_client['windows_logs']
collection = db['event_logs']

def extract_event_properties(event):
    trace_id = event.StringInserts[0] if event.StringInserts else ''
    span_id = event.StringInserts[1] if event.StringInserts and len(event.StringInserts) > 1 else ''
    commit = event.StringInserts[2] if event.StringInserts and len(event.StringInserts) > 2 else ''
    parent_resource_id = event.StringInserts[3] if event.StringInserts and len(event.StringInserts) > 3 else ''
    return trace_id, span_id, commit, parent_resource_id

def map_event_to_format(event):
    timestamp = datetime.datetime.utcfromtimestamp(event.TimeGenerated.timestamp()).isoformat() + 'Z'
    trace_id, span_id, commit, parent_resource_id = extract_event_properties(event)

    return {
        'level': 'info',  # You may need to derive the log level based on event properties
        'message': win32evtlogutil.SafeFormatMessage(event, 'System'),
        'resourceId': event.SourceName,
        'timestamp': timestamp,
        'traceId': trace_id,
        'spanId': span_id,
        'commit': commit,
        'metadata': {
            'parentResourceId': parent_resource_id,
        }
    }

def show_message_box(log_count):
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    messagebox.showinfo("Logs Recorded", f"{log_count} logs recorded in the database.")
    root.destroy()

def ingest_windows_logs(target_logs, servername, logtype):
    hand = win32evtlog.OpenEventLog(servername, logtype)
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    log_count = 0

    try:
        while target_logs > 0:
            buffer_size = min(target_logs, 1000)  # Adjust the buffer size based on your needs
            events = win32evtlog.ReadEventLog(hand, flags, 0, buffer_size)

            if not events:
                break

            for event in events:
                log_data = map_event_to_format(event)

                # Insert into MongoDB
                collection.insert_one(log_data)

                target_logs -= 1
                log_count += 1

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        win32evtlog.CloseEventLog(hand)
        show_message_box(log_count)

def windows_log_ingestor_interface(logtype, servername, target_logs_str="100000"):
    target_logs = int(target_logs_str)
    print(f"Ingesting logs. Target logs: {target_logs}")
    ingest_windows_logs(target_logs, servername, logtype)

# Gradio UI
iface = gr.Interface(
    fn=windows_log_ingestor_interface,
    inputs=[
        gr.Dropdown(label="Log Type", choices=["System", "Security", "Application"]),
        gr.Textbox(label="Server Name"),
        gr.Slider(label="Target Logs", minimum=1, maximum=100000, step=1),
    ],
    outputs=None,
    title="Windows Log Ingestor",
    description="Configure and start the Windows Event Log Ingestor.",
)

iface.launch(server_port=3000)
