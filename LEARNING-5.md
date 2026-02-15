# Learning Report – Joke Generator CLI App

## Project Overview
I built a Python CLI app that fetches random jokes from an online API.  
If the API is unavailable, the app shows a randomly saved joke from a local file.  
When the API works, new jokes are automatically saved.

## What I Learned

### Working with APIs
- How to send HTTP requests using `requests`
- How to handle JSON responses
- How client-server communication works

### File Handling
- How to read and write JSON files
- How to store data persistently
- How to append data to a file

### Error Handling
- How to use `try` and `except`
- How to handle network failures
- How to build fallback logic (offline mode)

### Python Environment
- How Python interpreters work
- Why `ModuleNotFoundError` happens
- How to correctly install packages using:
  `python -m pip install requests`

## Key Takeaway
This project helped me understand how real-world applications use APIs, store data locally, and handle failures properly.
