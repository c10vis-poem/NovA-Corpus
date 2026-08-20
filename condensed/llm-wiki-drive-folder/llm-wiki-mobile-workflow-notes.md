# LLM Wiki on mobile — workflow notes (AI Mode research session)

Consolidated from several short Drive files in the same Gemini AI-Mode research session (`wiki on mobile.txt`, `wiki marcor obsidian.txt`, `wiki on desktop.txt`, `wiki desktop.txt`, `desktop.txt`, `Why do you.txt`).

## Why an LLM Wiki "download" isn't needed

"LLM Wiki" is a blueprint/method for structuring notes so an AI doesn't forget them, not software to download and run — irrelevant on a phone with no computer to unpack/run repo code anyway.

**The Android-native setup, no GitHub required**:
1. **Markor** (text creator) — type/paste raw text on the phone, save into a normal folder on Android storage.
2. **Obsidian** (visual interface) — "Open folder as vault," pointed at the same folder Markor saves to; becomes the visual UI with links and graph views.
3. **Claude/ChatGPT** (AI compiler) — copy a messy note, paste into the AI app with a formatting prompt, copy the clean markdown back into Markor.

## The mobile workflow, step by step

1. Set up a dedicated folder in the mobile notes app (Obsidian or plain text folders).
2. Feed the AI: copy-paste raw notes, article links, or document text into the AI chat app.
3. Use a prompt like: *"I am building an LLM Wiki on my phone. Based on the text above, write a new markdown wiki page with [[interlinked_tags]] or update my existing wiki list. Output it in a clean code block so I can copy it on mobile."*
4. Copy the AI's structured output back into the mobile notes app.

## Connecting Claude to Obsidian on mobile

Two options:
- **API-driven plugin**: get an Anthropic API key from the Anthropic Console, install "Copilot" (by Logseq/Community) or "Smart Connections" via Obsidian mobile's Community Plugins, paste the key into plugin settings. Opens a chat sidebar inside the mobile vault — highlight text and ask Claude to "turn this into an LLM Wiki page" or "index this into my concept graph."
- **The "Plugin" route (desktop)**: pair a command-line agent like Claude Code with the `green-dalii/obsidian-llm-wiki` plugin — the CLI modifies/updates notes, the Obsidian Desktop App visually browses/edits the interconnected wiki pages.

Important distinction: a Claude Pro subscription and the Anthropic Developer API are separate billing systems. An API key in Obsidian charges per-token on a developer balance; it does not use the Pro subscription.

## The mobile "split-screen" bridge (Claude Code PWA + Markor)

Since mobile Obsidian can't run terminal commands directly, bridge via the phone's file management:

1. Keep Obsidian/Markor pointed at one folder containing all `.md` wiki files.
2. Open Claude Code in its PWA (Pro-tier browser panel).
3. Split-screen: PWA on one half, Markor on the other.
4. The exchange: tap the file in Markor, select all, copy, paste into the Claude Code panel with a prompt like *"Review this wiki page, update any cross-links, and return the modified code block."* Copy the result, jump back to Markor, paste over the old note.

**Automating it**: Tasker or MacroDroid can macro this — highlighting text in Markor and hitting a custom share button auto-copies the text and switches to the Claude PWA. Gives a computer-free way to use the Pro account without paying for API tokens.

## Dual-app strategy (Markor + Obsidian)

Because both apps read plain-text folders on the phone, point both at the same folder:
- **Markor as the "Raw Inbox"** — a single `Inbox.md` file for fast, instant-load raw-thought dumps.
- **Obsidian as the "Wiki Viewer"** — used to browse the interconnected `[[Wiki Links]]` and the graph visualizer.

## The copy-paste mobile wiki prompt

```
You are the dedicated AI compiler for my personal LLM Wiki. I am working
entirely on a mobile device, so text formatting must stay copy-paste friendly.
Context: I use Markor for my raw text inbox and Obsidian for my final wiki
folders.
Task: Process the raw text provided below.
1. If it introduces a new core concept, person, or project, generate a brand
   new Markdown (.md) wiki page.
2. Ensure you aggressively use [[Double Bracket Wiki Links]] for all major
   entities, nouns, and sub-concepts so they interlink.
3. Keep the layout flat and compact. Do not add conversational fluff.
4. Output the result strictly inside a clean Markdown code block so I can
   easily copy it with one tap on my phone screen.

Here is the raw text to process:
[PASTE YOUR RAW TEXT HERE]
```
