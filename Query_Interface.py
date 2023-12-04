import gradio as gr
import pymongo
import json
import tkinter as tk
from tkinter import messagebox

# MongoDB setup
port=0000  # Enter your MongoDB port
mongo_client = pymongo.MongoClient('localhost', port=port)  # Replace 'localhost' with address of your MongoBD
db = mongo_client['windows_logs']
collection = db['event_logs']

def is_collection_empty():
    return collection.count_documents({}) == 0

def filter_logs(level, message, resourceId, start_timestamp, end_timestamp, traceId, spanId, commit, parentResourceId):
    # Check if the collection is empty
    if is_collection_empty():
        root = tk.Tk()
        root.withdraw()
        root.lift()
        root.attributes('-topmost', True)
        messagebox.showinfo("No Logs", "No logs found in the database. Run Log_Ingestor to populate logs.")
        return "No logs found in the database."

    # Customize the MongoDB query based on filter criteria
    query = {}
    if level:
        query['level'] = level
    if message:
        query['message'] = {"$regex": message, "$options": "i"}  # Case-insensitive regex search for message
    if resourceId:
        query['resourceId'] = resourceId
    if traceId:
        query['traceId'] = traceId
    if spanId:
        query['spanId'] = spanId
    if commit:
        query['commit'] = commit
    if parentResourceId:
        query['metadata.parentResourceId'] = parentResourceId
    if start_timestamp and end_timestamp:
        query['timestamp'] = {"$gte": start_timestamp, "$lte": end_timestamp}
    elif end_timestamp:
        query['timestamp']={"$lt": end_timestamp}
    elif start_timestamp:
        query['timestamp'] = {"$gte": start_timestamp}

    # Fetch logs from MongoDB based on the query
    filtered_logs = collection.find(query)

    # Format logs for display
    logs_list = [
        {
            'Level': log['level'],
            'Message': log['message'],
            'Timestamp': log['timestamp'],
            'TraceId': log['traceId'],
            'SpanId': log['spanId'],
            'Commit': log['commit'],
            'ParentResourceId': log['metadata']['parentResourceId']
        }
        for log in filtered_logs
    ]

    # Convert logs to JSON format
    logs_json = json.dumps(logs_list, indent=2)

    return logs_json

# Gradio UI
iface = gr.Interface(
    fn=filter_logs,
    inputs=[
        gr.Textbox(label="Log Level (e.g., info, error)"),
        gr.Textbox(label="Log Message (Regex)"),
        gr.Textbox(label="Resource ID"),
        gr.Textbox(label="Start Date (YYYY-MM-DDTHH:mm:ssZ)"),
        gr.Textbox(label="End Date (YYYY-MM-DDTHH:mm:ssZ)"),
        gr.Textbox(label="Trace ID"),
        gr.Textbox(label="Span ID"),
        gr.Textbox(label="Commit"),
        gr.Textbox(label="Parent Resource ID"),
    ],
    outputs=gr.Text(),
    live=True,
    title="Log Filtration UI",
    description="Enter log filter criteria to view filtered logs.",
)

# Launch the Gradio interface
iface.launch(server_port=3000)
