# AI Bug Description Clarifier

Turns informal, hard-to-reproduce bug reports into clear, structured, professional issue summaries using an LLM.

## Example

**Input:**
> App keeps crashing when I click save.

**Output:**
> **Title:** Application Crashes Upon Clicking Save Button
>
> **Description:** The application unexpectedly crashes whenever the user clicks the "Save" button...
>
> **Expected Behavior:** Clicking "Save" should save the current data without errors.
>
> **Actual Behavior:** The application crashes immediately after "Save" is clicked.

## Setup

```bash
git clone https://github.com/2003dinijay/ai-bug-clarifier.git
cd ai-bug-clarifier
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your API key to .env
source .env
```

## Usage

```bash
python3 bug_clarifier.py "login button does nothing on mobile"
```

With no argument, it runs on a built-in sample report.

## Tech

Python, OpenAI Python SDK (Chat Completions API)
