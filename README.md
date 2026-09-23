# AI Bug Description Clarifier

Turns informal, hard-to-reproduce bug reports into clear, structured, professional issue summaries using an LLM.

## Example

**Input:**
> the page goes blank after I log in sometimes

**Output:**
> **Title:** Blank Page Displayed After Successful Login
>
> **Description:** Users occasionally encounter a completely blank page immediately after logging in. The issue is intermittent and prevents access to the dashboard.
>
> **Expected Behavior:** After login, the user is redirected to their dashboard with all content visible.
>
> **Actual Behavior:** The browser shows a blank page with no content, errors, or navigation.

## Setup

```bash
git clone https://github.com/2003dinijay/AI-Bug-Clarifier.git
cd AI-Bug-Clarifier
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file (see `.env.example`). To use Google Gemini's free tier, get a key at [aistudio.google.com](https://aistudio.google.com) and add:

```
export OPENAI_API_KEY=your-gemini-key
export OPENAI_API_BASE=https://generativelanguage.googleapis.com/v1beta/openai/
export OPENAI_MODEL=gemini-2.5-flash
```

Then load it:

```bash
source .env
```

## Usage

```bash
python3 bug_clarifier.py "login button does nothing on mobile"
```

With no argument, it runs on a built-in sample report.

## Tech

Python, OpenAI Python SDK, Google Gemini (via its OpenAI-compatible endpoint)
