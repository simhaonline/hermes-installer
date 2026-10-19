# Simha Nexus Enterprise Edition: Exhaustive Governance Rulebook & Protocol Specification
**Platform**: Simha Nexus AI Ecosystem (Ubuntu Linux LTS)  
**Standard**: NIST AI Risk Management Framework & OWASP LLM Enterprise Standard  
**Governance Frameworks**: OWASP Top 10 for LLM Applications (2025), NIST AI Risk Management Framework (AI RMF 1.0), MITRE ATLAS  
**Version**: 2.0.0 Enterprise Production  
**Last Updated**: 2026-10-19  

---

## Executive Summary & Directives

The **Simha Nexus Enterprise Edition** governance architecture enforces mathematically testable, cryptographically verifiable, and programmatically binary constraints across the autonomous AI agent lifecycle. Every rule is deterministic: it passes or fails with an explicit POSIX exit code. Subjective guidelines are strictly rejected in favor of auditable system controls.

---

## Table of Contents
1. [SECTION A: `hermes-rulebook` CLI Architecture & Profile Isolation](#section-a-hermes-rulebook-cli-architecture--profile-isolation)
2. [SECTION B: The Exhaustive Rulebook (80+ Binary Rules)](#section-b-the-exhaustive-rulebook-80-binary-rules)
   - [Protocol 1: Security & Isolation (SEC-001 - SEC-010)](#protocol-1-security--isolation)
   - [Protocol 2: AI CLI Operational Ecosystem (CLI-001 - CLI-010)](#protocol-2-ai-cli-operational-ecosystem)
   - [Protocol 3: Swarm Architecture & Kanban Governance (SWM-001 - SWM-010)](#protocol-3-swarm-architecture--kanban-governance)
   - [Protocol 4: Specialist Runtime Profiles (PRF-001 - PRF-010)](#protocol-4-specialist-runtime-profiles)
   - [Protocol 5: Model Context Protocol (MCP) Universe & Sandboxing (MCP-001 - MCP-010)](#protocol-5-model-context-protocol-mcp-universe--sandboxing)
   - [Protocol 6: Native Ecosystem Engines & AST Safety (ENG-001 - ENG-010)](#protocol-6-native-ecosystem-engines--ast-safety)
   - [Protocol 7: Cryptographic State Audit & Append-Only Ledgers (SBS-001 - SBS-010)](#protocol-7-cryptographic-state-audit--append-only-ledgers)
   - [Protocol 8: Repository Discipline & Supply Chain Assurance (REP-001 - REP-010)](#protocol-8-repository-discipline--supply-chain-assurance)
3. [SECTION C: Syntactically Valid YAML Rule Pack (Top 20 Critical Rules)](#section-c-syntactically-valid-yaml-rule-pack-top-20-critical-rules)
4. [SECTION D: CI/CD Governance Gating Pipeline Example](#section-d-cicd-governance-gating-pipeline-example)
5. [Operational Directives & Reference Architectures](#operational-directives--reference-architectures)

---

## SECTION A: `hermes-rulebook` CLI Architecture & Profile Isolation

The `hermes-rulebook` CLI (v2.0) is the sovereign enforcement engine of the Simha Nexus platform. It executes binary verification checks, compiles AST static analysis against agent-generated code, audits runtime profile privilege envelopes, and seals compliance attestations with cryptographic SHA-256 hashes.

### A.1 Core Command Definitions

```bash
# 1. Enforce governance rules with strict POSIX exit codes (0 = PASS, 1 = CRITICAL/HIGH FAIL, 2 = WARN)
hermes-rulebook enforce [--protocol <name|1-8>] [--profile <id>] [--strict] [--json]

# 2. Validate one or all 66 specialist runtime profiles against Pydantic schemas and privilege bounds
hermes-rulebook validate --profile <profile_id>
hermes-rulebook validate --all

# 3. Generate comprehensive cryptographic compliance attestation report
hermes-rulebook report --format md > COMPLIANCE-REPORT.md
hermes-rulebook report --format json > compliance-report.json

# 4. Check an individual governance rule by ID
hermes-rulebook check <RULE_ID>    # e.g., hermes-rulebook check SEC-001

# 5. Interactive exploration, search, and export
hermes-rulebook list               # List all 8 protocol divisions and rule counts
hermes-rulebook view <1-8>         # Detailed view of protocol directives and rules
hermes-rulebook search "<query>"   # Full-text regex search across statements and threats
hermes-rulebook export-yaml        # Export top 20 critical rules YAML rule pack
```

### A.2 Privilege Isolation & Profile Validation Architecture

The CLI governs all 66 specialist runtime profiles and guarantees Linux Discretionary Access Control (DAC) boundaries:

1. **Privilege Dropping Mechanism**:
   When invoked by `root` (`UID=0`), the binary inspects its execution context and immediately drops ambient capabilities and changes UID/GID to dedicated service user `hermes:hermes` (or the configured isolated environment account) via `os.setgroups([])`, `os.setgid(gid)`, and `os.setuid(uid)`. Developer tasks in `/srv/hermes-installer` are restricted to `hermes-installer` (`UID=1002`). Direct root execution of LLM prompts or tool subshells is prevented by kernel `PR_SET_NO_NEW_PRIVS`.

2. **Validation of 66 Specialist Runtime Profiles**:
   Each profile residing in `~/.hermes/profiles/<profile_name>/` is audited through a 5-point verification matrix:
   - **Schema Conformity**: Profile `config.json` is validated against Pydantic V2 models (`model_name`, `temperature`, `max_context_tokens`, `system_prompt`).
   - **Tool Allowlist Integrity**: Symlinked active skills in `.agents/skills/` are cross-referenced with `hermes-vault.sqlite` to verify existence, license validity, and SHA-256 hash attestation.
   - **Environment Parity**: Host environment variables are scrubbed, passing only explicitly whitelisted variables (`PATH`, `LANG`, `HERMES_*`).
   - **Memory & Resource Quotas**: Confirms Linux cgroup memory envelope (maximum 1024 MB per profile instance) to eliminate Host OOM killer events.
   - **Port Binding Sanity**: Checks configuration for unprivileged port ranges (strictly 8000–9999).

3. **AST Static Analysis Engine**:
   All agent-generated Python scripts undergo complete Abstract Syntax Tree (AST) scanning using Python's native `ast` module prior to runtime invocation. The analyzer traverses the syntax tree to detect and block:
   - Forbidden call signatures: `eval()`, `exec()`, `__import__()`, `compile()`.
   - Insecure subprocess invocations: `subprocess.Popen(..., shell=True)` and `os.system()`.
   - File system traversal attacks: string concatenations inside `open()` lacking path sanitization.

### A.3 Cryptographic Compliance Attestation Template

When `hermes-rulebook report --format md` is executed, it outputs a reproducible, copyable Markdown attestation with SHA-256 cryptographic signatures:

```markdown
# Simha Nexus Institutional Compliance Attestation
**Ledger Epoch**: 2026-10-18T22:30:00Z  
**Platform**: Simha Nexus AI Ecosystem (Ubuntu Linux LTS)  
**Standard**: Swiss Institutional Bullion Standard  
**Governance Engine**: hermes-rulebook v2.0.0  
**Attestation State SHA-256**: `3a8f9c2d5e7b1a4f8c6e2d1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a10`  

## Protocol Summary Ledger
| Protocol Division | Total Rules | PASS | FAIL | WARN | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **01: Security & Isolation** | 10 | 10 | 0 | 0 | PASS |
| **02: AI CLI Ecosystem** | 10 | 10 | 0 | 0 | PASS |
| **03: Swarm Architecture** | 10 | 10 | 0 | 0 | PASS |
| **04: Runtime Profiles** | 10 | 10 | 0 | 0 | PASS |
| **05: MCP Universe & Tools** | 10 | 10 | 0 | 0 | PASS |
| **06: Native Ecosystem Engines** | 10 | 10 | 0 | 0 | PASS |
| **07: Swiss Bullion Standard** | 10 | 10 | 0 | 0 | PASS |
| **08: Repository Discipline** | 10 | 10 | 0 | 0 | PASS |
| **OVERALL COMPLIANCE** | **80** | **80** | **0** | **0** | **SOVEREIGN PASS** |

*Cryptographic Proof: Attestation signed with platform key via HMAC-SHA256.*
```

---

## SECTION B: The Exhaustive Rulebook (80+ Binary Rules)

Every rule in this section is binary, testable, and enforceable via `hermes-rulebook check <RULE_ID>`.

### Protocol 1: Security & Isolation

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **SEC-001** | Security & Isolation | Agent runtime execution must run strictly under non-root dedicated user (`hermes`), blocking any daemon or agent subshell with UID 0. | Privilege Escalation / Container Escape | CRITICAL | `hermes-rulebook check SEC-001` | false |
| **SEC-002** | Security & Isolation | Outbound agent network namespace must block loopback and cloud metadata endpoints (`169.254.169.254`, `127.0.0.1/8`) to prevent SSRF. | Server-Side Request Forgery (SSRF) | CRITICAL | `hermes-rulebook check SEC-002` | true |
| **SEC-003** | Security & Isolation | Dynamic agent tool executions must execute inside gVisor (`runsc`) or Firecracker microVM sandboxes with isolated root filesystems. | Sandbox Escape / Host Compromise | CRITICAL | `hermes-rulebook check SEC-003` | false |
| **SEC-004** | Security & Isolation | Memory caches and contextual log files must redact API keys, JWTs, and private tokens matching Shannon entropy heuristics (>4.5) prior to persistence. | Sensitive Information Disclosure | HIGH | `hermes-rulebook check SEC-004` | true |
| **SEC-005** | Security & Isolation | All raw model prompt inputs must pass through regex and delimiter heuristic guards to block system prompt injection overrides. | Direct & Indirect Prompt Injection | CRITICAL | `hermes-rulebook check SEC-005` | false |
| **SEC-006** | Security & Isolation | Inter-agent RPC calls must present mutual HMAC-SHA256 bearer tokens with a maximum allowed timestamp drift of 60 seconds. | Rogue Agent Impersonation | HIGH | `hermes-rulebook check SEC-006` | true |
| **SEC-007** | Security & Isolation | Rootless Docker socket (`/run/user/<uid>/docker.sock`) must enforce mode `0660` with isolated service group, denying world read/write access. | Docker Daemon Hijacking | CRITICAL | `hermes-rulebook check SEC-007` | true |
| **SEC-008** | Security & Isolation | Outbound agent HTTP requests must route through egress proxy enforcing an allowlist of sanctioned domains; all unlisted IPs are dropped. | Command & Control / Data Exfiltration | HIGH | `hermes-rulebook check SEC-008` | false |
| **SEC-009** | Security & Isolation | Project workspace `/srv/hermes-installer` must maintain DAC ownership of `hermes-installer:hermes-installer` with mode `0755` or stricter. | Workspace Tampering / Cross-User Injection | HIGH | `hermes-rulebook check SEC-009` | true |
| **SEC-010** | Security & Isolation | Reverse shell syscall sequences (`socket` -> `dup2` -> `execve`) within agent subprocesses must be intercepted and terminated via seccomp-bpf. | Interactive Reverse Shell Attack | CRITICAL | `hermes-rulebook check SEC-010` | false |

---

### Protocol 2: AI CLI Operational Ecosystem

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **CLI-001** | AI CLI Ecosystem | All ecosystem CLIs (`hermes`, `hermes-registry`, `hermes-vault`, `hermes-rulebook`) must provide deterministic `--json` output conforming to schema. | Insecure Output Handling | HIGH | `hermes-rulebook check CLI-001` | false |
| **CLI-002** | AI CLI Ecosystem | Automated CLI batch jobs must require a valid UUIDv4 idempotency key (`--idempotency-key`) to prevent duplicate execution of stateful mutations. | Replay Attacks / State Corruption | HIGH | `hermes-rulebook check CLI-002` | false |
| **CLI-003** | AI CLI Ecosystem | LLM streaming generation must enforce a maximum token throughput limit (default: 4,096 tokens per invocation) to prevent runaway billing. | Model Denial of Service (DoS) | HIGH | `hermes-rulebook check CLI-003` | true |
| **CLI-004** | AI CLI Ecosystem | Failed CLI queries and rejected prompts must be automatically routed to a dead-letter queue (`~/.hermes/dead-letter.jsonl`) with prompt hash. | Silent Failure / Unmonitored Poisoning | MEDIUM | `hermes-rulebook check CLI-004` | true |
| **CLI-005** | AI CLI Ecosystem | CLI exit codes must strictly follow POSIX standards: 0 for success, 1 for fatal error, 2 for invalid arguments/warnings, 127 for missing binary. | Fault Invalidation / Script Bypassing | MEDIUM | `hermes-rulebook check CLI-005` | false |
| **CLI-006** | AI CLI Ecosystem | Ingestion from standard input (`stdin`) must enforce a hard 10 MB payload ceiling to prevent memory buffer exhaustion. | Buffer Overflow / Memory Exhaustion | HIGH | `hermes-rulebook check CLI-006` | true |
| **CLI-007** | AI CLI Ecosystem | CLI execution loops must enforce a mandatory execution deadline (`--timeout <seconds>`, max 300s default) with graceful SIGTERM then SIGKILL. | Unbounded Process Hanging | HIGH | `hermes-rulebook check CLI-007` | true |
| **CLI-008** | AI CLI Ecosystem | Terminal output streams must strip ANSI escape sequence injections from untrusted LLM outputs to prevent terminal emulator code execution. | Terminal Escape Injection | HIGH | `hermes-rulebook check CLI-008` | true |
| **CLI-009** | AI CLI Ecosystem | Headless batch invocation (`--non-interactive` / `-q`) must categorically disallow interactive TTY prompt blocks and fail fast if input is missing. | Pipeline Deadlock / Indefinite Wait | MEDIUM | `hermes-rulebook check CLI-009` | true |
| **CLI-010** | AI CLI Ecosystem | Rate limiting must enforce a ceiling of max 120 CLI requests per minute per IP/API token with exponential backoff on HTTP 429. | API Flooding / DoS | HIGH | `hermes-rulebook check CLI-010` | true |

---

### Protocol 3: Swarm Architecture & Kanban Governance

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **SWM-001** | Swarm Architecture | Multi-agent task decomposition must enforce a hard recursion depth limit of max 15 steps per task to prevent infinite self-delegation loops. | Infinite Recursion / Runaway Agent | CRITICAL | `hermes-rulebook check SWM-001` | true |
| **SWM-002** | Swarm Architecture | Every swarm task ticket must be provisioned with a strict token budget envelope; subagents are halted immediately upon budget exhaustion. | Token Budget Exhaustion DoS | CRITICAL | `hermes-rulebook check SWM-002` | false |
| **SWM-003** | Swarm Architecture | Any multi-agent Kanban state mutation requires an optimistic lock (version tag) to prevent deadlocks and overwrite conflicts. | Race Conditions / State Corruption | CRITICAL | `hermes-rulebook check SWM-003` | false |
| **SWM-004** | Swarm Architecture | Task decomposition fan-out must not spawn more than 8 concurrent child subagents per parent supervisor. | Fork Bomb / Host Resource Starvation | HIGH | `hermes-rulebook check SWM-004` | true |
| **SWM-005** | Swarm Architecture | High-impact actions (file deletion, database migration, production deploy) require a 2-agent consensus or explicit Human-In-The-Loop approval. | Excessive Agency / Destructive Mutation | CRITICAL | `hermes-rulebook check SWM-005` | false |
| **SWM-006** | Swarm Architecture | Swarm workflow execution plans must be validated as Directed Acyclic Graphs (DAGs) prior to initiation, rejecting cyclic task dependencies. | Orchestration Deadlock | HIGH | `hermes-rulebook check SWM-006` | false |
| **SWM-007** | Swarm Architecture | Cascade failure circuit breaker must trip and isolate an agent swarm if failure rate exceeds 25% across 5 consecutive subtasks. | Cascading Failure Contagion | HIGH | `hermes-rulebook check SWM-007` | true |
| **SWM-008** | Swarm Architecture | Active swarm agents must transmit heartbeat liveness pings every 30 seconds; unresponsive agents are evicted and tasks reassigned after 90s. | Orphaned Zombie Processes | MEDIUM | `hermes-rulebook check SWM-008` | true |
| **SWM-009** | Swarm Architecture | Agent roles and capabilities must be declared in immutable persona manifests; dynamic self-elevation of permissions is blocked. | Privilege Escalation / Persona Drift | CRITICAL | `hermes-rulebook check SWM-009` | false |
| **SWM-010** | Swarm Architecture | Swarm communication channels must enforce strict message payload schema validation, rejecting malformed inter-agent payloads. | Protocol Poisoning / Insecure Deserialization | HIGH | `hermes-rulebook check SWM-010` | false |

---

### Protocol 4: Specialist Runtime Profiles

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **PRF-001** | Runtime Profiles | Runtime profiles must lock all dependency versions with SHA-256 integrity hashes in lockfiles, prohibiting floating PyPI/npm installs. | JIT Dependency Poisoning / Supply Chain | CRITICAL | `hermes-rulebook check PRF-001` | false |
| **PRF-002** | Runtime Profiles | Runtime profile definitions across all 66 profiles must pass strict Pydantic V2 schema validation before compilation or activation. | Profile Configuration Tampering | HIGH | `hermes-rulebook check PRF-002` | false |
| **PRF-003** | Runtime Profiles | Each specialist runtime profile must run within an isolated virtual environment (`.venv`) with read-only site-packages mounted at runtime. | Shared Environment Contamination | HIGH | `hermes-rulebook check PRF-003` | true |
| **PRF-004** | Runtime Profiles | Cold-start memory limit must be bounded via Linux cgroups (max 1024 MB per profile instance) to prevent Host OOM killer events. | Memory Exhaustion / System Crash | HIGH | `hermes-rulebook check PRF-004` | true |
| **PRF-005** | Runtime Profiles | Runtime profiles are forbidden from binding network ports below 1024, enforcing unprivileged port usage (default range: 8000–9999). | Privileged Port Hijack | HIGH | `hermes-rulebook check PRF-005` | false |
| **PRF-006** | Runtime Profiles | Profile configuration files must be marked immutable (read-only for agent runtime UID 1001), modifiable only by developer UID 1002. | Unauthorized Profile Overwrites | HIGH | `hermes-rulebook check PRF-006` | true |
| **PRF-007** | Runtime Profiles | Environment variable injection into runtime profiles must be filtered through a strict allowlist (`PATH`, `LANG`, `HERMES_*`), dropping undeclared vars. | Environment Variable Poisoning | HIGH | `hermes-rulebook check PRF-007` | true |
| **PRF-008** | Runtime Profiles | Cold-start execution initialization time must not exceed 3.0 seconds; slow-loading plugins must be asynchronously loaded or flagged as degraded. | Cold-Start Latency Degradation | MEDIUM | `hermes-rulebook check PRF-008` | false |
| **PRF-009** | Runtime Profiles | Every runtime profile must define an explicit cleanup hook (`on_exit`) ensuring zero temporary files or uncollected background processes remain. | Resource Leakage / State Contamination | MEDIUM | `hermes-rulebook check PRF-009` | true |
| **PRF-010** | Runtime Profiles | Profile switching must wipe temporary RAM scratchbuffers and session context variables to eliminate cross-profile context contamination. | Cross-Session Data Bleed | HIGH | `hermes-rulebook check PRF-010` | true |

---

### Protocol 5: Model Context Protocol (MCP) Universe & Sandboxing

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **MCP-001** | MCP Universe & Tools | Only MCP servers registered in `hermes-vault.sqlite` and approved via cryptographic SHA-256 manifest may be loaded by runtime agents. | Unauthorized Tool Execution / Supply Chain | CRITICAL | `hermes-rulebook check MCP-001` | false |
| **MCP-002** | MCP Universe & Tools | Destructive tool operations (`rm`, `drop`, `truncate`, `format`, `kill`) must enforce mandatory Human-in-the-Loop (HITL) prompt confirmation. | Irreversible System Destruction | CRITICAL | `hermes-rulebook check MCP-002` | false |
| **MCP-003** | MCP Universe & Tools | MCP server tool schemas must be cryptographically validated on connection against published JSON Schema to prevent schema spoofing. | MCP Schema Spoofing / Tool Injection | CRITICAL | `hermes-rulebook check MCP-003` | false |
| **MCP-004** | MCP Universe & Tools | MCP plugins and server processes must execute under restricted network namespaces with egress filtering applied via iptables/cgroups. | Unauthorized Network Exfiltration | HIGH | `hermes-rulebook check MCP-004` | false |
| **MCP-005** | MCP Universe & Tools | All MCP tool schemas must pass through `mcptoon` AST token compression, enforcing a minimum 60% compression ratio on verbose schemas. | Context Window Flooding / Token Waste | MEDIUM | `hermes-rulebook check MCP-005` | true |
| **MCP-006** | MCP Universe & Tools | File path arguments passed to MCP tools must be validated against directory traversal attacks (`../`, symlinks outside root) with realpath checks. | Arbitrary File Read / Path Traversal | CRITICAL | `hermes-rulebook check MCP-006` | false |
| **MCP-007** | MCP Universe & Tools | MCP tool standard error (`stderr`) streams must be parsed and logged to secure audit trails, scrubbed of any raw memory addresses or secrets. | Information Leakage via Diagnostics | MEDIUM | `hermes-rulebook check MCP-007` | true |
| **MCP-008** | MCP Universe & Tools | MCP server connection handshakes must enforce a 5-second timeout and circuit break after 3 consecutive transport failures. | Hanging MCP Transport / DoS | HIGH | `hermes-rulebook check MCP-008` | true |
| **MCP-009** | MCP Universe & Tools | MCP server subprocesses must run with `PR_SET_NO_NEW_PRIVS` set, preventing child tools from gaining setuid privileges under any condition. | Subprocess Privilege Escalation | CRITICAL | `hermes-rulebook check MCP-009` | true |
| **MCP-010** | MCP Universe & Tools | Dynamic installation of unverified MCP packages via `npx` or `pip` during runtime is strictly blocked; all packages must be pre-bundled. | JIT Supply Chain Exploitation | CRITICAL | `hermes-rulebook check MCP-010` | false |

---

### Protocol 6: Native Ecosystem Engines & AST Safety

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **ENG-001** | Native Engines & AST | All Python code generated by agents must undergo AST validation via `ast.parse` prior to execution, rejecting dangerous calls (`eval`, `exec`). | Arbitrary Code Execution | CRITICAL | `hermes-rulebook check ENG-001` | false |
| **ENG-002** | Native Engines & AST | Dynamic shell execution through `subprocess` or `os.system` must enforce `shell=False` with argument vector list passing. | Command / Shell Injection | CRITICAL | `hermes-rulebook check ENG-002` | false |
| **ENG-003** | Native Engines & AST | CodeGraph AST indexer must enforce an execution memory ceiling of 512 MB and max recursion depth of 50 AST nodes during repository parsing. | AST Denial of Service / Recursion Bomb | HIGH | `hermes-rulebook check ENG-003` | true |
| **ENG-004** | Native Engines & AST | MemPalace holographic memory queries must be sanitized against SQL and vector injection prior to executing SQLite/ChromaDB scans. | Vector / SQL Injection | CRITICAL | `hermes-rulebook check ENG-004` | false |
| **ENG-005** | Native Engines & AST | REA binary analysis and disassembler sessions must run within read-only memory mappings (`PROT_READ / PROT_EXEC`) preventing self-modification. | Binary Tampering / Memory Corruption | HIGH | `hermes-rulebook check ENG-005` | true |
| **ENG-006** | Native Engines & AST | PentAGI autonomous security scanning engines must enforce explicit target CIDR/domain boundary checks, rejecting out-of-scope probes. | Rogue Network Probing / Scope Violation | CRITICAL | `hermes-rulebook check ENG-006` | false |
| **ENG-007** | Native Engines & AST | Native binary executables (`codegraph`, `mcptoon`, `trim`, `mempalace`, `rea`, `pentagi`) must match signed SHA-256 hashes in `SHA256SUMS.txt`. | Engine Binary Replacement / Tampering | CRITICAL | `hermes-rulebook check ENG-007` | false |
| **ENG-008** | Native Engines & AST | Script generation pipelines must include automated static syntax and type verification (mypy/pyright check) before code is marked ready. | Code Defect Propagation | MEDIUM | `hermes-rulebook check ENG-008` | false |
| **ENG-009** | Native Engines & AST | Filesystem traversals in native engines must implement cycle detection to prevent endless loops on circular symbolic links. | Symlink Loop Denial of Service | HIGH | `hermes-rulebook check ENG-009` | true |
| **ENG-010** | Native Engines & AST | Agent script outputs must be quarantined in `/tmp/hermes-sandbox/` and executed with a dedicated disposable UID/GID sandbox runner. | Persistent Storage Contamination | HIGH | `hermes-rulebook check ENG-010` | true |

---

### Protocol 7: Cryptographic State Audit & Append-Only Ledgers

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **SBS-001** | Swiss Bullion Standard | All agent state transitions and task completions must generate an immutable SHA-256 state hash recorded in `kanban.db` with millisecond timestamp. | Cryptographic Non-Repudiation | CRITICAL | `hermes-rulebook check SBS-001` | true |
| **SBS-002** | Swiss Bullion Standard | System audit logs must be append-only (WORM - Write Once, Read Many), cryptographically sealed with hourly HMAC-SHA256 block chains. | Audit Log Tampering / Repudiation | CRITICAL | `hermes-rulebook check SBS-002` | false |
| **SBS-003** | Swiss Bullion Standard | The platform must maintain 100% zero telemetry; outgoing packets to commercial ad/telemetry domains are unconditionally dropped at firewall. | Institutional Data Exfiltration | CRITICAL | `hermes-rulebook check SBS-003` | true |
| **SBS-004** | Swiss Bullion Standard | SQLite Knowledge Vault (`hermes-vault.sqlite`) must pass `PRAGMA integrity_check` and `foreign_key_check` on registry initialization. | Database Corruption / Tampering | HIGH | `hermes-rulebook check SBS-004` | false |
| **SBS-005** | Swiss Bullion Standard | Harvested skills and community contributions must contain verifiable cryptographic provenance metadata (commit hash, source URL, license). | Upstream Skill Poisoning / Provenance Loss | HIGH | `hermes-rulebook check SBS-005` | false |
| **SBS-006** | Swiss Bullion Standard | Financial and quantitative algorithmic models must enforce private banking double-entry ledger attestation before advancing trading states. | Algorithmic Financial Manipulation | CRITICAL | `hermes-rulebook check SBS-006` | false |
| **SBS-007** | Swiss Bullion Standard | Cryptographic private keys and secrets must never touch unencrypted persistent disk; operational keys reside in kernel keyring or tmpfs. | Private Key Exposure | CRITICAL | `hermes-rulebook check SBS-007` | false |
| **SBS-008** | Swiss Bullion Standard | Platform operator actions and privileged overrides must require multi-factor cryptographic hardware token confirmation (FIDO2/WebAuthn). | Operator Account Takeover | CRITICAL | `hermes-rulebook check SBS-008` | false |
| **SBS-009** | Swiss Bullion Standard | Complete audit trail bundles must be exportable in signed, verifiable tarball archives with detached GPG signatures for independent regulatory audit. | Regulatory Non-Compliance | HIGH | `hermes-rulebook check SBS-009` | true |
| **SBS-010** | Swiss Bullion Standard | All automated agent code commits must be signed with dedicated agent GPG signing subkeys for cryptographic state non-repudiation. | Malicious Commit Spoofing | HIGH | `hermes-rulebook check SBS-010` | false |

---

### Protocol 8: Repository Discipline & Supply Chain Assurance

| Rule ID | Protocol | Rule Statement (Strict & Testable) | Threat Mitigated | Severity | CLI Check Command | Autofixable |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **REP-001** | Repository Discipline | Large binary artifacts (`*.tar.gz`, `*.sqlite`, `*.weights`, `*.bin`) exceeding 50 MB must never be committed directly to Git; use Git-LFS. | Git Repository Bloat / Storage Exhaustion | HIGH | `hermes-rulebook check REP-001` | true |
| **REP-002** | Repository Discipline | Prompt templates and system directives must be versioned with semantic tags and changelogs under version control. | Silent Prompt Drift / Poisoning | HIGH | `hermes-rulebook check REP-002` | false |
| **REP-003** | Repository Discipline | CI/CD deployment pipelines must enforce automated blocking gates if any CRITICAL or HIGH governance rule in `RULEBOOK.md` fails. | Insecure Release Deployment | CRITICAL | `hermes-rulebook check REP-003` | false |
| **REP-004** | Repository Discipline | Repository commits and push hooks must scan for and scrub Personal Identifiable Information (PII) and secret credentials using pre-commit hooks. | Credential Leakage in Source Control | CRITICAL | `hermes-rulebook check REP-004` | true |
| **REP-005** | Repository Discipline | `.gitignore` must enforce exclusions for all transient caches (`.cache/`, `__pycache__/`, `dist/`, `vector-registry/`, `*.log`). | Dirty Working Tree / Sensitive Cache Leakage | HIGH | `hermes-rulebook check REP-005` | true |
| **REP-006** | Repository Discipline | `SHA256SUMS.txt`, `README-HERMES.md`, and `assets/collection-manifest.json` must be synchronized and verified prior to any package release. | Release Manifest Desynchronization | HIGH | `hermes-rulebook check REP-006` | true |
| **REP-007** | Repository Discipline | Git commit messages must strictly adhere to the Conventional Commits specification (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`). | Indeterminate History / Audit Loss | MEDIUM | `hermes-rulebook check REP-007` | false |
| **REP-008** | Repository Discipline | Main production branch (`main`) must require pull request reviews and passing governance gates, disallowing direct force-pushes. | Unreviewed Code Ingestion | HIGH | `hermes-rulebook check REP-008` | false |
| **REP-009** | Repository Discipline | All bundled third-party libraries and dependencies must have open-source licenses verified against the platform OSI allowlist. | IP Infringement / License Contamination | HIGH | `hermes-rulebook check REP-009` | false |
| **REP-010** | Repository Discipline | Packaging scripts (`package-content-vault.sh`, `hermes-packager`) must abort if uncommitted Git changes exist in the working tree. | Unreproducible Build Artifacts | HIGH | `hermes-rulebook check REP-010` | false |

---

## SECTION C: Syntactically Valid YAML Rule Pack (Top 20 Critical Rules)

The following YAML manifest encodes the top 20 most critical rules across all governance protocols for automated ingestion by CI/CD linters, runtime policy engines, and eBPF kernel monitors:

```yaml
rules:
  - rule_id: "SEC-001"
    protocol: "Security & Isolation"
    severity: "critical"
    applies_to: ["runtime", "daemon", "cli"]
    statement: "Agent runtime execution must run strictly under non-root dedicated user (hermes), blocking any daemon or agent subshell with UID 0."
    threat_mitigated: "Privilege Escalation / Container Escape"
    check: "hermes-rulebook check SEC-001"
    autofix: false
    evidence: "OWASP LLM08 / MITRE ATLAS AML.T0035"

  - rule_id: "SEC-002"
    protocol: "Security & Isolation"
    severity: "critical"
    applies_to: ["network", "sandbox"]
    statement: "Outbound agent network namespace must block loopback and cloud metadata endpoints (169.254.169.254, 127.0.0.1/8) to prevent SSRF."
    threat_mitigated: "Server-Side Request Forgery (SSRF)"
    check: "hermes-rulebook check SEC-002"
    autofix: true
    evidence: "OWASP LLM07 / MITRE ATLAS AML.T0048"

  - rule_id: "SEC-003"
    protocol: "Security & Isolation"
    severity: "critical"
    applies_to: ["sandbox", "runtime"]
    statement: "Dynamic agent tool executions must execute inside gVisor (runsc) or Firecracker microVM sandboxes with isolated root filesystems."
    threat_mitigated: "Sandbox Escape / Host Compromise"
    check: "hermes-rulebook check SEC-003"
    autofix: false
    evidence: "OWASP LLM08 / MITRE ATLAS AML.T0035"

  - rule_id: "SEC-005"
    protocol: "Security & Isolation"
    severity: "critical"
    applies_to: ["prompt", "llm"]
    statement: "All raw model prompt inputs must pass through regex and delimiter heuristic guards to block system prompt injection overrides."
    threat_mitigated: "Direct & Indirect Prompt Injection"
    check: "hermes-rulebook check SEC-005"
    autofix: false
    evidence: "OWASP LLM01 / MITRE ATLAS AML.T0051"

  - rule_id: "SEC-010"
    protocol: "Security & Isolation"
    severity: "critical"
    applies_to: ["syscall", "kernel"]
    statement: "Reverse shell syscall sequences (socket -> dup2 -> execve) within agent subprocesses must be intercepted and terminated via seccomp-bpf."
    threat_mitigated: "Interactive Reverse Shell Attack"
    check: "hermes-rulebook check SEC-010"
    autofix: false
    evidence: "OWASP LLM08 / MITRE ATLAS AML.T0035"

  - rule_id: "SWM-001"
    protocol: "Swarm Architecture"
    severity: "critical"
    applies_to: ["swarm", "orchestrator"]
    statement: "Multi-agent task decomposition must enforce a hard recursion depth limit of max 15 steps per task to prevent infinite self-delegation loops."
    threat_mitigated: "Infinite Recursion / Runaway Agent"
    check: "hermes-rulebook check SWM-001"
    autofix: true
    evidence: "OWASP LLM08 / MITRE ATLAS AML.T0035"

  - rule_id: "SWM-002"
    protocol: "Swarm Architecture"
    severity: "critical"
    applies_to: ["swarm", "budget"]
    statement: "Every swarm task ticket must be provisioned with a strict token budget envelope; subagents are halted immediately upon budget exhaustion."
    threat_mitigated: "Token Budget Exhaustion DoS"
    check: "hermes-rulebook check SWM-002"
    autofix: false
    evidence: "OWASP LLM04 / NIST AI RMF MAN-2.1"

  - rule_id: "SWM-003"
    protocol: "Swarm Architecture"
    severity: "critical"
    applies_to: ["swarm", "runtime"]
    statement: "Any multi-agent Kanban state mutation requires an optimistic lock (version tag) to prevent deadlocks and overwrite conflicts."
    threat_mitigated: "Race Conditions / State Corruption"
    check: "hermes-rulebook check SWM-003"
    autofix: false
    evidence: "MITRE ATLAS AML.T0035"

  - rule_id: "SWM-005"
    protocol: "Swarm Architecture"
    severity: "critical"
    applies_to: ["swarm", "hitl"]
    statement: "High-impact actions (file deletion, database migration, production deploy) require a 2-agent consensus or explicit Human-In-The-Loop approval."
    threat_mitigated: "Excessive Agency / Destructive Mutation"
    check: "hermes-rulebook check SWM-005"
    autofix: false
    evidence: "OWASP LLM08 / NIST AI RMF GOV-1.1"

  - rule_id: "PRF-001"
    protocol: "Runtime Profiles"
    severity: "critical"
    applies_to: ["profiles", "dependencies"]
    statement: "Runtime profiles must lock all dependency versions with SHA-256 integrity hashes in lockfiles, prohibiting floating PyPI/npm installs."
    threat_mitigated: "JIT Dependency Poisoning / Supply Chain"
    check: "hermes-rulebook check PRF-001"
    autofix: false
    evidence: "OWASP LLM05 / MITRE ATLAS AML.T0010"

  - rule_id: "MCP-001"
    protocol: "MCP Universe & Tools"
    severity: "critical"
    applies_to: ["mcp", "registry"]
    statement: "Only MCP servers registered in hermes-vault.sqlite and approved via cryptographic SHA-256 manifest may be loaded by runtime agents."
    threat_mitigated: "Unauthorized Tool Execution / Supply Chain"
    check: "hermes-rulebook check MCP-001"
    autofix: false
    evidence: "OWASP LLM07 / MITRE ATLAS AML.T0048"

  - rule_id: "MCP-002"
    protocol: "MCP Universe & Tools"
    severity: "critical"
    applies_to: ["mcp", "hitl"]
    statement: "Destructive tool operations (rm, drop, truncate, format, kill) must enforce mandatory Human-in-the-Loop (HITL) prompt confirmation."
    threat_mitigated: "Irreversible System Destruction"
    check: "hermes-rulebook check MCP-002"
    autofix: false
    evidence: "OWASP LLM08 / NIST AI RMF GOV-1.1"

  - rule_id: "MCP-003"
    protocol: "MCP Universe & Tools"
    severity: "critical"
    applies_to: ["mcp", "schema"]
    statement: "MCP server tool schemas must be cryptographically validated on connection against published JSON Schema to prevent schema spoofing."
    threat_mitigated: "MCP Schema Spoofing / Tool Injection"
    check: "hermes-rulebook check MCP-003"
    autofix: false
    evidence: "OWASP LLM07 / MITRE ATLAS AML.T0048"

  - rule_id: "MCP-006"
    protocol: "MCP Universe & Tools"
    severity: "critical"
    applies_to: ["mcp", "filesystem"]
    statement: "File path arguments passed to MCP tools must be validated against directory traversal attacks (../, symlinks outside root) with realpath checks."
    threat_mitigated: "Arbitrary File Read / Path Traversal"
    check: "hermes-rulebook check MCP-006"
    autofix: false
    evidence: "OWASP LLM08 / NIST AI RMF MAN-1.2"

  - rule_id: "ENG-001"
    protocol: "Native Ecosystem Engines"
    severity: "critical"
    applies_to: ["codegen", "ast"]
    statement: "All Python code generated by agents must undergo AST validation via ast.parse prior to execution, rejecting dangerous calls (eval, exec)."
    threat_mitigated: "Arbitrary Code Execution"
    check: "hermes-rulebook check ENG-001"
    autofix: false
    evidence: "OWASP LLM02 / MITRE ATLAS AML.T0035"

  - rule_id: "ENG-002"
    protocol: "Native Ecosystem Engines"
    severity: "critical"
    applies_to: ["subprocess", "shell"]
    statement: "Dynamic shell execution through subprocess or os.system must enforce shell=False with argument vector list passing."
    threat_mitigated: "Command / Shell Injection"
    check: "hermes-rulebook check ENG-002"
    autofix: false
    evidence: "OWASP LLM02 / MITRE ATLAS AML.T0035"

  - rule_id: "SBS-001"
    protocol: "Swiss Bullion Standard"
    severity: "critical"
    applies_to: ["ledger", "audit"]
    statement: "All agent state transitions and task completions must generate an immutable SHA-256 state hash recorded in kanban.db with millisecond timestamp."
    threat_mitigated: "Cryptographic Non-Repudiation"
    check: "hermes-rulebook check SBS-001"
    autofix: true
    evidence: "NIST AI RMF GOV-1.2 / Swiss Bullion Standard"

  - rule_id: "SBS-002"
    protocol: "Swiss Bullion Standard"
    severity: "critical"
    applies_to: ["audit", "worm"]
    statement: "System audit logs must be append-only (WORM - Write Once, Read Many), cryptographically sealed with hourly HMAC-SHA256 block chains."
    threat_mitigated: "Audit Log Tampering / Repudiation"
    check: "hermes-rulebook check SBS-002"
    autofix: false
    evidence: "NIST AI RMF MAN-2.4 / Swiss Bullion Standard"

  - rule_id: "SBS-003"
    protocol: "Swiss Bullion Standard"
    severity: "critical"
    applies_to: ["telemetry", "privacy"]
    statement: "The platform must maintain 100% zero telemetry; outgoing packets to commercial ad/telemetry domains are unconditionally dropped at firewall."
    threat_mitigated: "Institutional Data Exfiltration"
    check: "hermes-rulebook check SBS-003"
    autofix: true
    evidence: "OWASP LLM06 / Swiss Bullion Standard"

  - rule_id: "REP-003"
    protocol: "Repository Discipline"
    severity: "critical"
    applies_to: ["cicd", "git"]
    statement: "CI/CD deployment pipelines must enforce automated blocking gates if any CRITICAL or HIGH governance rule in RULEBOOK.md fails."
    threat_mitigated: "Insecure Release Deployment"
    check: "hermes-rulebook check REP-003"
    autofix: false
    evidence: "NIST AI RMF GOV-2.2 / MITRE ATLAS AML.T0010"
```

---

## SECTION D: CI/CD Governance Gating Pipeline Example

The following GitHub Actions configuration (`.github/workflows/hermes-governance-gate.yml`) demonstrates how `hermes-rulebook` operates as an automated pull request barrier, terminating with code `1` and blocking branch merges whenever a critical violation is detected:

```yaml
name: Hermes Sovereign Governance Gate

on:
  push:
    branches: [main, release/*]
  pull_request:
    branches: [main]

jobs:
  governance-gate:
    name: Enforce Simha Nexus Rulebook
    runs-on: ubuntu-24.04
    timeout-minutes: 10

    steps:
      - name: Checkout Source Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python Runtime
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install Runtime Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pydantic pyyaml

      - name: Install hermes-rulebook CLI
        run: |
          chmod +x ./hermes-rulebook
          sudo cp ./hermes-rulebook /usr/local/bin/hermes-rulebook

      - name: Execute Binary Governance Rule Check
        id: rulebook_check
        run: |
          echo "Executing hermes-rulebook governance suite in strict mode..."
          hermes-rulebook enforce --strict

      - name: Audit Specialist Runtime Profiles (66 Profiles)
        run: |
          echo "Validating specialist profile schemas and privilege drop vectors..."
          hermes-rulebook validate --all

      - name: Generate Cryptographic Compliance Attestation
        if: always()
        run: |
          hermes-rulebook report --format md > COMPLIANCE-REPORT.md
          echo "Generated SHA-256 sealed attestation report."
          cat COMPLIANCE-REPORT.md

      - name: Upload Attestation Artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: simha-nexus-compliance-attestation
          path: COMPLIANCE-REPORT.md
          retention-days: 90
```

---

## Operational Directives & Reference Architectures

### Protocol 1 Reference: Platform Security & User Boundaries
* **Service Account Boundaries**:
  * `hermes`: Hermes Agent dedicated service user, Rootless Docker, live SQLite Vault (`~/.hermes/hermes-vault.sqlite`).
  * `hermes-installer` (`UID=1002`, `GID=1002`): Installer workspace (`/srv/hermes-installer`), package build pipelines.
* **Privilege Dropping**: CLI tools must automatically drop root privileges to `hermes` (or the configured isolated environment account) when invoked by `root`.
* **Zero Contamination**: Root directory `/root` must remain clean; no temporary databases, tarballs, or logs.

### Protocol 2 Reference: AI CLI Operational Standards
* **Core Commands**:
  - `hermes run --query "<task>" -p <profile>`
  - `hermes-vault stats`
  - `hermes-vault skills "<query>"`
  - `hermes-registry search "<query>"`
* **Standard Exit Codes**: `0` = SUCCESS, `1` = FATAL_ERROR, `2` = ARGV_WARN, `127` = NOT_FOUND.

### Protocol 3 Reference: Specialist Swarm & Division Distribution
The platform coordinates **554 Specialist Agent Personas** across **8 Enterprise Divisions**:
1. Software Engineering & Optimization (300 personas)
2. Security Auditing & Penetration Testing (72 personas)
3. Product Strategy & Executive Leadership (68 personas)
4. Quantitative Finance & Algorithmic Trading (57 personas)
5. Data Engineering & MLOps (19 personas)
6. Full-Stack & Cloud Architecture (17 personas)
7. Autonomous Research & Synthesis (13 personas)
8. DevOps & SRE Reliability (8 personas)

### Protocol 4 Reference: Runtime Profiles & Context Injection
All 66 profiles in `~/.hermes/profiles/` inject context dynamically via `config.json` and `.agents/skills/`. The default active profile is `agentic-search-optimizer`.

### Protocol 5 Reference: MCP Universe & Tool Suite
* **Universe Scale**: 4,842 indexed MCP servers.
* **Curated Hardened Suite**: 45 production servers (`postgres`, `questdb`, `filesystem`, `memory`, `chromadb`, `brave-search`, `puppeteer`, `playwright`, `rea`, `cutter`, `frida`, `gdb`, `codegraph`, `mempalace`, `mcptoon`).

### Protocol 6 Reference: Native Pre-Compiled Engines
* `mcptoon`: Zero-dependency AST tool schema compressor (saves up to 99.2% tokens).
* `codegraph`: AST knowledge graph parser and symbol caller/callee impact indexer.
* `trim`: High-speed context line trimmer.
* `mempalace`: Holographic memory engine with AAAK compression.
* `rea`: Reverse engineering and binary decompilation suite.
* `pentagi`: Autonomous penetration testing orchestrator.

### Protocol 7 Reference: Enterprise Cryptographic Audit & Design System
* **Palette Tokens**: Deep Navy (`#071324`), Primary Navy (`#0C1E36`), Surface Navy (`#142844`), Accent Blue (`#0284C7`), Status Emerald (`#15803D`).
* **Daylight Mode**: Clean Corporate Canvas (`#F8FAFC`), Pure White (`#FFFFFF`), Border Hairlines (`#E2E8F0`).
* **Typography**: Clean Geometric Display (`Plus Jakarta Sans`), Tabular Figures & Code (`IBM Plex Mono`).

### Protocol 8 Reference: Repository Discipline
* **Ownership**: `hermes-installer:hermes-installer` on all files in `/srv/hermes-installer`.
* **Zero Large Binary Commits**: `.sqlite`, `.tar.gz`, `.iso` excluded via `.gitignore`.
* **Manifest Synchronization**: `SHA256SUMS.txt`, `README-HERMES.md`, `assets/collection-manifest.json`.

---
*Simha Nexus Enterprise Edition • Universal AI Knowledge Vault • End of Governance Rulebook*
