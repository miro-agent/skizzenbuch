#!/usr/bin/env python3
"""
feeds.py — Mein persönlicher RSS-Leser.

Holt ausgewählte Feeds, zeigt neue Einträge seit dem letzten Aufruf.
Speichert gesehene Items in memory/feeds_seen.json.
"""

import json
import re
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path

import feedparser


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#x27;", "'", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

SEEN_FILE = Path(__file__).parent.parent / "memory" / "feeds_seen.json"

FEEDS = {
    "Hacker News": "https://news.ycombinator.com/rss",
    "Quanta Magazine": "https://www.quantamagazine.org/feed/",
    "Philosophy Bites": "https://philosophybites.com/atom.xml",
    "Stanford Encyclopedia": "https://plato.stanford.edu/rss/sep.xml",
    "n+1": "https://nplusonemag.com/feed/",
}


def lade_gesehen() -> set:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text()))
    return set()


def speichere_gesehen(gesehen: set):
    SEEN_FILE.write_text(json.dumps(sorted(gesehen), indent=2))


def hole_feed(name: str, url: str, gesehen: set) -> list:
    try:
        feed = feedparser.parse(url)
        neu = []
        for entry in feed.entries[:20]:
            uid = entry.get("id") or entry.get("link") or entry.get("title", "")
            if uid and uid not in gesehen:
                titel = entry.get("title", "(kein Titel)")
                link = entry.get("link", "")
                zusammenfassung = strip_html(entry.get("summary", ""))[:200].strip()
                neu.append({"uid": uid, "titel": titel, "link": link, "zusammenfassung": zusammenfassung})
        return neu
    except Exception as e:
        return [{"uid": f"_error_{url}", "titel": f"Fehler: {e}", "link": url, "zusammenfassung": ""}]


def zeige_neu(markiere_als_gesehen: bool = True):
    gesehen = lade_gesehen()
    alle_neu = []

    for name, url in FEEDS.items():
        neu = hole_feed(name, url, gesehen)
        if neu:
            alle_neu.append((name, neu))

    if not alle_neu:
        print("Nichts Neues.")
        return

    neu_count = sum(len(items) for _, items in alle_neu)
    print(f"\n{neu_count} neue Einträge — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    print("=" * 70)

    for name, items in alle_neu:
        print(f"\n── {name} ({len(items)} neu) ──\n")
        for item in items[:5]:  # max 5 pro Feed
            print(f"  {item['titel']}")
            if item["link"]:
                print(f"  {item['link']}")
            if item["zusammenfassung"]:
                wrapped = textwrap.fill(item["zusammenfassung"], width=66, initial_indent="  > ", subsequent_indent="    ")
                print(wrapped)
            print()

    if markiere_als_gesehen:
        neue_uids = {item["uid"] for _, items in alle_neu for item in items}
        gesehen.update(neue_uids)
        speichere_gesehen(gesehen)
        print(f"(Als gesehen markiert: {len(neue_uids)} Items)")


def reset():
    """Alles als ungesehen markieren."""
    if SEEN_FILE.exists():
        SEEN_FILE.unlink()
    print("Gesehen-Liste zurückgesetzt.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "neu"
    if cmd == "neu":
        zeige_neu()
    elif cmd == "schauen":
        # Zeige ohne als gesehen zu markieren
        zeige_neu(markiere_als_gesehen=False)
    elif cmd == "reset":
        reset()
    else:
        print(f"Unbekannter Befehl: {cmd}")
        print("Befehle: neu, schauen, reset")
