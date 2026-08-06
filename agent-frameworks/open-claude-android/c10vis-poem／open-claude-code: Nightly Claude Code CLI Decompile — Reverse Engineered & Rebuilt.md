# c10vis-poem／open-claude-code: Nightly Claude Code CLI Decompile — Reverse Engineered & Rebuilt

Watch
0
Nightly Claude Code CLI Decompile — Reverse Engineered & Rebuilt
MIT License
github.com/ruvnet/RuVector
1 star
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from ruvnet/open-claude-code
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with ruvnet/open-claude-code:main .
Contribute
Sync fork
github-actions[bot] chore: update last-known Claude Code version to 2.1.220
09f4a1e · 5 days ago
.github/workflows
ci(nightly): protect metaharness optim…
last month
archive/open_claude_code
chore: move open_claude_code to arc…
3 months ago
assets
Add initial project structure and versio…
last year
docs/adr
feat: nightly verified release pipeline + …
3 months ago
rudevolution @ 53af4c0
feat: nightly verified release pipeline + …
3 months ago
scripts
chore: update last-known Claude Code…
5 days ago
v2
feat(optimize): opt-in metaharness sel…
last month
.gitignore
chore: update .gitignore for Node.js pr…
3 months ago
.gitmodules
feat: nightly verified release pipeline + …
3 months ago
LICENSE
Initial commit
last year
README.md
ci(nightly): protect metaharness optim…
last month
c10vis-poem
open-claude-code
Code
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
T
Open Claude Code
Open Source Claude Code CLI — Reverse Engineered & Rebuilt
README
License


A fully functional open source implementation of Anthropic's Claude Code CLI,
built from decompiled source intelligence using ruDevolution.
tests 991 passing
tools 25
commands 40
npm v2.1.0
License MIT
nightly veriﬁed releases
Automated Nightly Releases — Open Claude Code automatically detects new Claude Code releases, runs
903+ tests to verify zero regressions, and publishes verified builds with AI-powered discovery analysis. See
Releases | ADR-001 | pi.ruv.io
Requires: ANTHROPIC_API_KEY environment variable set.
Open Claude Code is a ground-up open source rebuild of Anthropic's Claude Code CLI, informed by ruDevolution's
AI-powered decompilation of the published npm package.
It's not a copy — it's a clean-room implementation that mirrors the actual Claude Code architecture: async
generator agent loop, 25 tools, 4 MCP transports, 6 permission modes, hooks, settings chain, sessions, and more.
1,581 tests. 61 files. 8,314 lines. 100% functional.
⚡ Quick Start
# Run instantly (no install)
npx @ruvnet/open-claude-code "explain this codebase"
# Or install globally
npm install -g @ruvnet/open-claude-code
occ "hello"
# Interactive mode
occ
export ANTHROPIC_API_KEY=sk-ant-...
npx @ruvnet/open-claude-code "what files are in this directory?"
🧠 What Is This?
📦 Installation
npx (no install needed)
npx @ruvnet/open-claude-code "your prompt here"
Global install


npm install -g @ruvnet/open-claude-code
occ "your prompt here"
From source
git clone https://github.com/ruvnet/open-claude-code.git
cd open-claude-code/v2
export ANTHROPIC_API_KEY=sk-ant-...
node src/index.mjs "hello"
🖥️ Usage
One-shot mode
occ "explain the auth module"
occ "fix the bug in server.js"
occ "create a REST API for user management"
occ "find all TODO comments in this project"
Interactive REPL
occ
# > explain this codebase
# > /help
# > /tools
# > /model claude-opus-4-6
# > refactor the database layer
# > /cost
# > /exit
CLI Options
occ [options] [prompt]
Options:
  -m, --model <model>          Model to use (default: claude-sonnet-4-6)
  -p, --print                  Print mode (non-interactive, output only)
  --permission-mode <mode>     Permission mode: default, auto, plan, acceptEdits, 
                               bypassPermissions, dontAsk
  --system-prompt <text>       Override system prompt
  --add-dir <path>             Additional CLAUDE.md directory
  --max-turns <n>              Maximum conversation turns
  --allowedTools <tools>       Comma-separated allowed tools
  --disallowedTools <tools>    Comma-separated denied tools
  --output-format <fmt>        Output: text, json, stream-json
  -v, --verbose                Verbose output
  -d, --debug                  Debug mode
  --version                    Show version
  -h, --help                   Show help


40 slash commands available in REPL mode:
Command
Description
/help
Show all commands
/model <name>
Switch model mid-conversation
/tools
List available tools
/tokens
Show current token usage
/cost
Show session cost estimate
/compact
Compact context window
/undo
Undo last file edit
/clear
Clear conversation history
/doctor
Check API connectivity + health
/fast
Toggle fast mode (Haiku)
/effort <level>
Set effort: low, medium, high, max
/resume [id]
Resume a previous session
/sessions
List saved sessions
/agents
List custom agents
/skills
List available skills
/hooks
Show active hooks
/config
Show current settings
/permissions
Show permission mode
Examples
# Use a different model
occ -m claude-opus-4-6 "design a database schema for a blog"
# Print mode (for piping)
occ -p "list all functions in src/" > functions.txt
# Plan mode (read-only, no edits)
occ --permission-mode plan "review the security of auth.js"
# Restrict tools
occ --allowedTools "Read,Glob,Grep" "find all API endpoints"
# With custom system prompt
occ --system-prompt "You are a senior Go developer" "review main.go"
🔧 Interactive Commands


Command
Description
/mcp
Show MCP server status
/memory
Show memory usage
/exit
Exit
25 built-in tools matching Claude Code's tool system:
Tool
Description
Bash
Execute shell commands (sandboxed)
Read
Read files with line numbers
Edit
Replace strings in files
Write
Create/overwrite files
Glob
Find files by pattern
Grep
Search file contents (regex)
LS
List directory contents
Agent
Spawn sub-agents
WebFetch
Fetch URL content
WebSearch
Web search
TodoWrite
Task management
NotebookEdit
Edit Jupyter notebooks
MultiEdit
Atomic multi-file edits
ToolSearch
Discover deferred tools
AskUser
Prompt user for input
Skill
Invoke a skill
SendMessage
Agent team messaging
CronCreate/Delete/List
Scheduled tasks
EnterWorktree/ExitWorktree
Git worktree isolation
RemoteTrigger
Remote execution
LSP
Language server protocol
ReadMcpResource
Read MCP resources
🔨 Tools


Create .claude/settings.json in your project or ~/.claude/settings.json globally:
Settings are loaded from 4 sources (in priority order):
1. .claude/settings.local.json (local, gitignored)
2. .claude/settings.json (project, shared)
3. ~/.claude/settings.json (user global)
4. Managed policy (enterprise)
Create a CLAUDE.md in your project root to customize behavior:
CLAUDE.md files are loaded from: ~/.claude/CLAUDE.md → parent directories → project root →
.claude/CLAUDE.md .
Create .claude/agents/reviewer.md :
⚙️ Configuration
Settings
{
  "model": "claude-sonnet-4-6",
  "permissions": {
    "defaultMode": "auto"
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{ "type": "command", "command": "echo 'Running bash...'" }]
    }]
  },
  "autoCompactEnabled": true,
  "alwaysThinkingEnabled": true
}
CLAUDE.md
# Project Rules
- Always use TypeScript
- Follow TDD
- Keep files under 500 lines
Custom Agents
---
name: reviewer
description: Code review specialist
model: claude-sonnet-4-6
tools: [Read, Glob, Grep]
---
You are a thorough code reviewer. Check for bugs, security issues, and style.


Create .claude/skills/deploy/SKILL.md :
Invoke with /deploy in the REPL.
Works with 5 AI providers:
Connect to MCP servers for additional tools:
Supports 4 transports: stdio, SSE, Streamable HTTP, WebSocket.
Skills
---
name: deploy
description: Deploy to production
---
1. Run tests: npm test
2. Build: npm run build
3. Deploy: ./scripts/deploy.sh
🔐 Multi-Provider Support
# Anthropic (default)
ANTHROPIC_API_KEY=... occ "hello"
# OpenAI
OPENAI_API_KEY=... occ -m gpt-4o "hello"
# Google
GOOGLE_AI_API_KEY=... occ -m gemini-2.5-flash "hello"
# AWS Bedrock
AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... occ -m bedrock/claude-sonnet "hello"
# Google Vertex
GOOGLE_APPLICATION_CREDENTIALS=... occ -m vertex/claude-sonnet "hello"
🔗 MCP Integration
// .mcp.json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "my-mcp-server"],
      "env": { "API_KEY": "..." }
    }
  }
}


On March 31, 2026, Anthropic accidentally shipped source maps in the Claude Code npm package, exposing the
full TypeScript source. This project takes a different approach — we use ruDevolution to analyze the published
npm package legally and rebuild from that intelligence.
Discovery
Evidence
🤖 Agent Teams
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS
🌙 Auto Dream Mode
tengu_auto_dream_completed
🔮 claude-opus-4-6
Unreleased model ID
🔐 6 "amber" codenames
Internal feature gates
☁️ Cloud Code Runner
BYOC compute
📡 MCP Streamable HTTP
New transport
Download decompiled releases →
This is a clean-room implementation — no leaked source used. Architecture informed by analysis of the published
npm package, legal under US DMCA §1201(f), EU Software Directive Art. 6, UK CDPA §50B.
ruDevolution — AI-Powered JavaScript Decompiler
Decompiled Releases — Every Claude Code version
v2 Architecture (ADR-001)
Path to 100% (ADR-002)
Nightly Release Pipeline
Releases
No releases published
Create a new release
Packages
🔍 Background: The Claude Code Source Leak
What ruDevolution Found
⚖️ Legal
📚 Related
📄License


No packages published
Publish your first package
Contributors
No contributors
Languages
JavaScript 99.8%
Other 0.2%
Suggested workflows
Based on your tech stack
Publish Node.js Package
Publishes a Node.js package to npm.
By GitHub Actions
Configure
Datadog Synthetics
Run Datadog Synthetic tests within your GitHub Actions workflow
By Datadog
Configure
Webpack
Build a NodeJS project with npm and webpack.
By GitHub Actions
Configure
More workflows
