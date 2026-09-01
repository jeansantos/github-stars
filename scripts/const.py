import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "stars.yaml"
README_FILE = ROOT / "README.md"

USER = os.environ.get("GITHUB_REPOSITORY_OWNER", "jeansantos")
REPO = os.environ.get("GITHUB_REPOSITORY", f"{USER}/github-stars")
STARS_URL = f"https://github.com/{USER}?tab=stars"
ACTIONS_URL = f"https://github.com/{REPO}/actions"
CONTACT_EMAIL = "contact@jeansantos.net"

CATEGORY_NOTES = {
    "AI and Machine Learning": (
        "the tool itself performs or is built specifically for AI/ML inference, "
        "training, or LLM agent workflows; not just AI-adjacent or popular among ML users"
    ),
    "Automation and Orchestration": (
        "infrastructure, IT, or workflow automation/orchestration platforms; not personal "
        "calendars, task/kanban trackers, or notification utilities"
    ),
    "Backup and Storage": (
        "tools whose primary purpose is backing up, syncing, or storing data; not full "
        "backend/database platforms that merely offer storage as one feature"
    ),
    "CI/CD and DevOps": (
        "build, deployment, and infrastructure-as-code tooling used in software delivery "
        "pipelines"
    ),
    "Containers and Kubernetes": (
        "container runtimes, Kubernetes tooling, and container orchestration UIs"
    ),
    "Databases and Data": (
        "databases, data platforms, data visualization tools, and backend-as-a-service "
        "platforms centered on data"
    ),
    "Developer Tools and CLI": (
        "general-purpose developer utilities, CLIs, libraries, and dev-productivity tools "
        "that don't fit a more specific category"
    ),
    "Finance and Business": "personal or business finance, accounting, and budgeting tools",
    "Frontend, UI and Design": (
        "UI component libraries, design tools, and frontend frameworks; not generic homelab "
        "service dashboards (see Monitoring and Observability)"
    ),
    "Infrastructure and Homelab": (
        "self-hosted infrastructure, virtualization, and homelab-specific tooling"
    ),
    "Knowledge and Learning": (
        "educational content, courses, and general knowledge-base/wiki tools; topic-specific "
        "guides (e.g. a security hardening checklist) belong in that topic's category instead"
    ),
    "Media and Streaming": "video/audio streaming, media servers, and content playback tools",
    "Monitoring and Observability": (
        "monitoring, metrics, logging, uptime tracking, and homelab/service dashboards"
    ),
    "Networking and Remote Access": (
        "networking, VPNs, proxies, and remote access/remote desktop tools"
    ),
    "Personal and Lifestyle": (
        "personal productivity tools: task/kanban trackers, calendars, bookmark managers, "
        "and other individual-use tools without a stronger domain fit"
    ),
    "Security and DevSecOps": (
        "security tooling, identity/auth platforms, and security guides or checklists"
    ),
}

CATEGORIES = list(CATEGORY_NOTES)

FALLBACK_CATEGORY = "Other"

TAGS = [
    "ai-powered",
    "api",
    "authentication",
    "automation",
    "backup",
    "browser-extension",
    "caching",
    "cli",
    "cloud-native",
    "collaboration",
    "cpp",
    "cross-platform",
    "csharp",
    "dashboard",
    "data-pipeline",
    "database",
    "desktop-app",
    "distributed",
    "docker",
    "embedded",
    "encryption",
    "extensible",
    "go",
    "gui",
    "homelab",
    "infrastructure-as-code",
    "iot",
    "java",
    "javascript",
    "kubernetes",
    "lightweight",
    "load-balancer",
    "low-code",
    "monitoring",
    "networking",
    "no-code",
    "oauth",
    "offline-first",
    "orchestration",
    "php",
    "privacy-focused",
    "productivity",
    "project-management",
    "proxy",
    "python",
    "real-time",
    "ruby",
    "rust",
    "search",
    "self-hosted",
    "self-service",
    "serverless",
    "shell",
    "ssh",
    "sso",
    "tui",
    "typescript",
    "virtualization",
    "vpn",
    "web-app",
    "zero-trust",
]

TAG_NOTES = {
    "ai-powered": (
        "the tool itself uses AI/ML/LLMs to do its job at runtime; infrastructure for "
        "building AI agents doesn't count unless the tool itself also runs AI"
    ),
    "automation": "automatically executes or triggers actions/tasks",
    "orchestration": "coordinates or schedules multiple services/workloads across a system",
    "self-hosted": "can run on your own infrastructure instead of only as a SaaS",
    "homelab": "specifically aimed at home-lab/personal-infrastructure use (Proxmox, home networks, etc.), not just any self-hosted tool",
    "dashboard": "presents an at-a-glance visual overview UI",
    "productivity": "helps an individual's personal workflow efficiency",
    "collaboration": "built for multi-user/team use, not solo use",
    "self-service": "lets end users do something themselves without needing an operator/admin",
    "extensible": "designed to be extended via plugins/integrations, not just configurable",
    "lightweight": "notably minimal in resource use or footprint, not merely small in scope",
}

TAGS_PER_REPO = 3

MODEL = "composer-2.5"
BATCH_SIZE = 25

CATEGORY_LINES = "\n".join(
    f"  - {name}: {note}" for name, note in CATEGORY_NOTES.items()
)

TAG_LINE = ", ".join(
    f"{tag} ({TAG_NOTES[tag]})" if tag in TAG_NOTES else tag for tag in TAGS
)

PROMPT = (
    "You classify GitHub repositories for a personal starred showcase.\n\n"
    "For each repository return a JSON object with:\n"
    '- "repo": the exact full name provided\n'
    '- "description": one concise sentence, max 100 characters, on what it does and why it '
    "stands out; never copy the GitHub text verbatim. If the provided info is sparse, stay "
    "literal and factual instead of inventing marketing language, and avoid generic "
    'templated openers like "AI-powered X for Y" or "Self-hosted X for Y" unless that '
    "genuinely is the repo's defining trait\n"
    '- "category": exactly one of the following. Pick the category whose definition '
    "actually matches what the repo does, not just a keyword it happens to mention:\n"
    + CATEGORY_LINES + "\n"
    f'- "tags": exactly {TAGS_PER_REPO} tags, chosen only from this fixed list, picking '
    "whichever fit the repo best (do not invent tags outside this list; where a tag has a "
    "parenthetical note, that note is its definition): "
    + TAG_LINE + "\n\n"
    "Return only a JSON array of these objects, no markdown, no commentary."
)

MONTH_ABBREVIATIONS = [
    "", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]


ICONS_DIR = "assets/icons"


def _icon_html(name):
    return f'<img src="{ICONS_DIR}/{name}.png" width="14" height="14" alt="">'


TAG_ICON = _icon_html("tag")
STAR_ICON = _icon_html("star")
CLOCK_ICON = _icon_html("clock")
