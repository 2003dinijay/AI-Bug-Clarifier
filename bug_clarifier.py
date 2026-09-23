import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),  # optional; uses OpenAI's default if unset
)

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


def clarify_bug(description: str) -> str:
    """Rewrite an informal bug report as a clear, structured issue summary."""
    prompt = (
        "You are a senior QA engineer. Rewrite the following informal bug report "
        "into a clear, structured, and professional issue summary. Include a short "
        "title, a concise description of the problem, and the expected vs. actual "
        "behavior.\n\n"
        f"Bug report: {description}"
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.0,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        bug_report = " ".join(sys.argv[1:])
    else:
        bug_report = "App keeps crashing when I click save."
    response = clarify_bug(bug_report)
    print(response)
EOFcat > bug_clarifier.py << 'EOF'
import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),  # optional; uses OpenAI's default if unset
)

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")


def clarify_bug(description: str) -> str:
    """Rewrite an informal bug report as a clear, structured issue summary."""
    prompt = (
        "You are a senior QA engineer. Rewrite the following informal bug report "
        "into a clear, structured, and professional issue summary. Include a short "
        "title, a concise description of the problem, and the expected vs. actual "
        "behavior.\n\n"
        f"Bug report: {description}"
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.0,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        bug_report = " ".join(sys.argv[1:])
    else:
        bug_report = "App keeps crashing when I click save."
    response = clarify_bug(bug_report)
    print(response)
