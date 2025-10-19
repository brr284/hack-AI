# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Hack-AI is a Windows desktop application providing a cybersecurity AI assistant with a Tkinter GUI. The application interfaces with the Pollinations AI API to generate security-related content including malware analysis, exploit code, penetration testing tools, and security audits.

## Commands

### Setup
```powershell
pip install -r requirements.txt
```

### Run Application
```powershell
hackai open
```
Or directly:
```powershell
python hackai_app.py
```

## Architecture

### Two-Module Design

**hackai_app.py** - GUI and Application Logic
- Tkinter-based desktop interface with left sidebar navigation
- Five operational modes accessed via category buttons:
  - `malware`: Generates malware samples for analysis
  - `exploit`: Creates security testing exploits  
  - `pentest`: Generates penetration testing tools
  - `audit`: Performs security code audits
  - `free`: General AI text generation
- Threading model: AI generation runs in background threads to prevent UI blocking
- User input flows through `generate_content()` which dispatches to appropriate AI functions based on selected mode

**pollinations_ai.py** - API Client Layer
- Wraps Pollinations AI text and image generation endpoints
- Base URL: `https://text.pollinations.ai`
- All text generation goes through GET requests with prompt in URL path
- `PollinationsAI` class methods construct specialized prompts for each security domain
- Module-level helper functions (`create_virus_sample()`, `create_penetration_test_tool()`, `analyze_vulnerability()`) instantiate client and call with domain-specific prompt templates

### Key Data Flow

1. User selects mode and enters prompt in GUI
2. `generate_content()` reads current mode from `self.current_mode`
3. Spawns thread calling appropriate function from `pollinations_ai.py`
4. API response streamed back to GUI's scrolled text widget
5. User can save output via file dialog

## Important Notes

- **Windows-only**: Uses `hackai.bat` launcher script
- **No authentication**: Pollinations AI endpoints are public and unauthenticated
- **Error handling**: API errors return string "Error generating response: {exception}"
- **Threading**: Always access GUI widgets from main thread; use `.after()` for cross-thread updates if modifying the code
- **Prompt engineering**: All security functions rely on prompt templates in `pollinations_ai.py`—modify these to change AI behavior
