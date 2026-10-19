# Predict-A-Trade — technical resume handoff

Recorded 2026-10-02 UTC. This is a server-preparation and Hermes-tooling handoff, not an
inspection of the application repository. Reported host state and intended configuration
are distinguished below. No SSH connection or execution on the Hetzner host was available.

## Resume block

**Objective:** prepare a Hetzner Robot dedicated Ubuntu 26.04 production server for
Predict-A-Trade, migrate from an old VPS, then configure DNS manually. The project serves
thousands of concurrent users and real-time market tick data through a public API. The
user calls it an HFT system; exchange proximity, deterministic latency, throughput, market
data licensing, trading implementation and application SLOs are not established here.
Work one automated script at a time. Avoid interactive installation confirmations and
unnecessary complexity. Preserve existing skills, agent profiles, MCP registrations,
provider credentials, memories and user customizations. Add capabilities and improve
token efficiency without deleting the collected library. Never print credentials.

**Host:** hostname `platform.simhainfobiz.com`, UTC; AMD Ryzen 9 7950X3D, 16 physical
cores/32 logical threads; 128305 MB non-ECC RAM; two 1920 GB NVMe devices
`/dev/nvme0n1` and `/dev/nvme1n1`. Raw capacity 3576 GiB; installed RAID, partitions,
filesystems, redundancy and usable capacity are unverified. Do not format or reinstall.
Active NIC `enp1s0`, MAC `98:b7:85:22:d1:3c`, Intel 82599/ixgbe, negotiated 10000 Mb/s,
full duplex, 64 Tx/Rx queues, MTU 1500, qdisc mq. Inactive NIC `enp4s0`, MAC
`b0:82:e2:06:b3:94`; leave its configuration alone. Negotiation does not measure provider
bandwidth entitlement or public throughput.

**Desired addressing:** `46.62.188.249/32`, gateway `46.62.188.129` on-link;
`2a01:4f9:3090:24b0::2/64`, gateway `fe80::1`. Hetzner DNS:
`185.12.64.2`, `185.12.64.1`, `2a01:4ff:ff00::add:1`, `2a01:4ff:ff00::add:2`.
One earlier live diagnostic showed DHCP `46.62.188.249/25` rather than the desired /32,
and networkd using `/run/systemd/network/zzzz-dracut-default.network` instead of Netplan.
The generated network script was corrected; current host addressing needs validation.

**Baseline:** root and `sysadmin` sudo access; preserve passwords already set and authorized
SSH keys. User explicitly selected SSH TCP/22 with root/password/key access. UFW supports
IPv4/IPv6, SSH rate limiting and web TCP/80,443, preserving existing rules. Fail2Ban SSH
jail uses systemd logs and UFW. Chrony uses Hetzner NTP plus Ubuntu pool, timezone UTC,
initial clock-step window only, no public NTP service. Unattended security upgrades are
enabled with automatic reboot disabled. Auditd, sysstat timers, vnStat and plocate are
configured. Interactive Bash defaults and tmux are added without replacing user files.
PAM login file limits are 1048576; the full installer uses service soft/hard defaults
1024/1048576 to avoid broad daemon compatibility problems. Service-specific limits for
the eventual application remain to be designed.

**Execution evidence:** user reports running the individual baseline steps. The full base
installer and Docker installer were delivered, but their latest remote validation logs
were not supplied. Locally checked shell syntax, generated configuration and helper
behavior do not prove remote service health.

**Docker design:** production rootful Docker uses its standard Unix socket, cgroup v2/
systemd, local log rotation and live restore. Official Docker Ubuntu repository, Buildx,
Compose and rootless prerequisites are used. Fresh defaults bind published ports to
loopback. Do not add Hermes to the production `docker` group, expose the daemon on TCP,
or assume UFW controls explicitly published Docker ports. The Docker installer is
`12-install-production-docker.sh`; it preserves managed reruns and refuses unidentified
existing runtimes/data instead of deleting them. Storage uses the supported Docker default
rather than forcing legacy overlay2 over Docker 29+ containerd image storage.

**Current task:** create a complete noninteractive Hermes installer from the supplied
8480-line attachment. Preserve all **87 supplied custom skills**, **29 specialist profiles**,
both custom catalog helpers, 30 community seed repositories/two GitHub topics, all four
MCP directory sources, existing APIs and memory providers. Original attachment contains
destructive profile overwrites, removal of `SUPERMEMORY_*` variables and `supermemory.json`,
old `venv/bin/hermes` assumptions and stale npm overrides. The revised installer avoids
those steps. Existing versions remain; supplied originals remain separately searchable
when they differ. Source installation uses a reviewed official commit, the managed PM
toolchain and current `.hermes/bin/hermes` launcher, with no upstream npm lockfile edits.

**Hermes target layout after the new script runs:** dedicated unprivileged `hermes` account,
data `/home/hermes/.hermes`, source `/home/hermes/.local/share/hermes-agent`, development
workspace `/srv/hermes-development`, rootless Docker socket
`/run/user/<hermes-uid>/docker.sock`. Production Docker is retained. Existing root Hermes
data/pools are copied additively; original locations remain. SQLite files use consistent
backup copying. The installer starts the user Docker service with linger, but does not
start a Hermes messaging gateway, public UI, scheduled model job or DNS cutover.

**Reviewed Hermes revision:** `4ed093cb6be8a2fadb39e770898f6989fc67201d` from official
NousResearch/hermes-agent source, reviewed on the recorded date. Its PM lock declares
Python `3.14.7+20260901`, Node `26.7.0`, uv `0.12.3`, agent-browser `0.26.0` and Chromium
`1208+145.0.7632.6`. These describe the reviewed managed toolchain, not versions verified
on the remote server or the Predict-A-Trade application stack. Existing dedicated-user
installations are retained and report their own version.

**Token policy:** native tool search, 2000-token discovery listing, lean context compression
at ratio 0.75 with protected recent messages, main-turn budget 250, child budget 100,
three concurrent children, depth two, bounded child summaries. These are iteration/context
controls, not a monetary spending cap. API model/provider routing is preserved. Newly
created specialists hide unrelated skills from their index using supported `skills.disabled`
while retaining all skill files; existing profile selections remain. Optional/community
libraries and the MCP universe stay searchable and selectively enabled. Keep prompts and
tool selections stable within a session for provider caching. No promised percentage savings.

**Memory:** keep configured providers, Supermemory settings and existing stores. Fresh
installations follow the attachment's local bundled Holographic provider, SQLite/FTS5,
local pattern-based extraction, trust 0.60, HRR dimension 1024, with locked NumPy support.
Do not force an existing provider to Holographic or strip its credentials.

**Handoff workflow:** `hermes-project-context /absolute/project/path` produces a private,
timestamped inventory without reading source/secret contents or calling an AI API. It
records Git branch/commit, relevant manifest paths, file paths and working-tree status.
It labels bounded/truncated inventories. The added `project-context-handoff` skill asks
the model to inspect actual manifests and relevant code, then write the real dense summary.
This inventory alone is not a verified application architecture. Keep a compact resume
block and link longer evidence, rather than refeeding all historical conversation logs.

**Local completion:** the full self-contained `13-install-hermes.sh` is generated. Shell
syntax, decoded payload hashes, all original skill contents and helper Python/YAML parse
checks passed. Temporary-fixture tests verified API/MCP/memory/profile preservation,
rerun skill retention, additive indexes, archived disables, safe skill enabling, a live
SQLite WAL backup and a private bounded inventory without source/secret values. These
are meaningful local checks, not a remote end-to-end Hermes/Docker installation test.

**Next:** run `13-install-hermes.sh` on the dedicated server, then inspect its output.
Provide missing API credentials/
OAuth/model selection only if not migrated. Validate an actual Hermes session and chosen
MCP endpoints after authentication. Obtain the real application repository and old-VPS
inventory before deciding reverse proxy, storage/RAID, database, queues, market-data feeds,
streaming protocol, CI/CD, production service limits, backup targets, observability or
migration sequence. Keep DNS/traffic on the old VPS until migration acceptance is complete.

## Architecture and domain routing

Planned topology: public clients → production web/API/live endpoints on this dedicated
host → application/data services whose implementations are not yet inspected. AI
development tooling is a separate OS account/rootless Docker environment on the same
physical host. This is a privilege separation boundary; CPU, memory, disks and uplink
remain shared. Performance measurements and resource policies are still required.

All following names are confirmed; service-role labels are planning interpretations.

| Domain | Intended role |
| --- | --- |
| simhainfobiz.com | Main website |
| dataset.simhainfobiz.com | Dataset service |
| status.simhainfobiz.com | Service status |
| api.simhainfobiz.com | Public API |
| platform.simhainfobiz.com | Platform/dashboard and server FQDN |
| live.simhainfobiz.com | Live market service |
| downloads.simhainfobiz.com | Downloads |
| docs.simhainfobiz.com | Documentation |

The user will configure DNS manually after server readiness and old-VPS migration.
TLS method, reverse proxy, backend ports and whether to publish AAAA are undecided.

## Exact known file structure

Actual generated preparation files in the shared workspace, rather than an application
repository: `/workspace/scratch/2839179117db/` contains:

```text
01-setup-admin.sh
02-configure-network.sh
03-configure-hostname.sh
04-install-base-packages.sh
05-configure-ssh.sh
06-configure-firewall.sh
07-configure-time.sh
08-configure-security-updates.sh
09-configure-audit-metrics.sh
10-configure-limits-shell-tmux.sh
11-validate-base-server.sh
hermes-base-server.sh
12-install-production-docker.sh
13-install-hermes.sh                    (new deliverable)
Predict-A-Trade_Hetzner_Server_Baseline.md
Predict-A-Trade_Project_Handoff.md
upload/Pasted text(20261002-221546).txt  (supplied Hermes installer)
```

The full base installer uses isolated child Bash stages, not raw concatenation of scripts
with shared traps/variables. It runs packages first, preserves existing credentials,
generates private password files only for passwordless/locked accounts as intended,
includes the supplied public key and offers `--validate-only`. Treat that full installer's
service-limit choices as authoritative over older standalone limits scripts.

Intended new Hermes files (not a remote filesystem observation):

```text
/usr/local/bin/hermes                          # root/sudo dispatcher to dedicated account
/usr/local/bin/hermes-community-skills         # retained catalog helper dispatcher
/usr/local/bin/hermes-mcp-universe             # retained MCP helper dispatcher
/usr/local/bin/hermes-skill-catalog            # search/select retained skill packages
/usr/local/bin/hermes-project-context          # zero-API inventory helper
/home/hermes/.local/lib/hermes-agent/   # helper implementations
/home/hermes/.local/share/hermes-agent/        # official source + .hermes/bin/hermes
/home/hermes/.local/share/hermes-community-skill-pool/
/home/hermes/.local/share/hermes-mcp-universe/
/home/hermes/.local/share/hermes-mcp-servers/
/home/hermes/.hermes/
  config.yaml                                 # API/model/MCP/memory values retained
  .env                                        # secrets, never pasted into summaries
  auth.json                                   # existing authentication state, if present
  skills/custom/<skill>/SKILL.md               # 87 supplied skills + handoff skill
  skill-library/submitted/                    # retained incoming variants on conflicts
  skill-library/official-optional/             # complete official optional skill library
  profiles/<profile>/                         # all 29 agents; existing profiles preserved
  configuration-backups/                      # private pre-edit config copies
  migration-conflicts/                        # incoming legacy variants without overwrites
  context-snapshots/                          # bounded per-project inventories
  references/hermes-setup/
    submitted-installer.txt                   # complete original, retained as reference
    collection-manifest.json                  # original skill hashes + profile inventory
    profiles.json
    TOKEN_POLICY.md
    PROJECT_HANDOFF.md
/srv/hermes-development/               # account-owned development workspace
/home/hermes/.config/docker/daemon.json        # separate rootless daemon defaults
/home/hermes/.config/systemd/user/docker.service
/root/hermes-backups/hermes-*/           # private wrapper/config backup and refresh logs
```

Do not invent `/frontend`, `/backend`, framework/database versions, application tests,
Git branch, exchange connectors or deployment manifests. No application repository was
supplied in this conversation. The inventory helper must be run against the real checkout.

## Profiles and collection sources

Preserved agents: orchestrator; coding-engineer; qa-testing; devops-sre; cloud-infrastructure;
security-audit; ethical-hacking-pentest; red-team; blue-team; purple-team; white-team;
yellow-team; green-team; orange-team; ai-llm-engineer; ai-research-mlops; data-knowledge;
research-science; metatrader-quant; analytics-finance; business-operations; documents-office;
legal-corporate; creative-media; marketing-growth; communications-sales; mcp-librarian;
skill-librarian; esoteric-advisor. Existing descriptions and profile contents are retained;
only new profiles receive initial specialist index filtering.

Community discovery retains the attachment's 30 seed repositories and GitHub topics
`ai-agent-skills` and `ai-skills`. Exact seeds/custom skills are retained in the complete
submitted source and collection manifest; avoid refeeding the entire library into prompts.
Catalog refreshes merge previous entries instead of wiping history when sources fail.
Existing enabled skill edits are retained; disabling archives rather than deletes them.
Exhaustive discovery remains available, but rate limits/unavailable sources are reported.
Public catalogs are not automatically executable or trusted integrations.

MCP directory sources: `punkpeye/awesome-mcp-servers`, `mctrinh/awesome-mcp-servers`,
`jaw9c/awesome-remote-mcp-servers`, `soxoj/awesome-osint-mcp-servers`, plus the native
Hermes approved catalog. Existing MCP configuration stays intact. Registration of a
selected new endpoint may require provider-specific authentication/OAuth; not every
catalog entry is remotely verified or usable without credentials.

## Bugs and corrections to retain

- Network desired/live mismatch: initial validator required /32 but live DHCP lease used
  /25. Networkd selected dracut fallback. Generated `.network` files previously inherited
  overly restrictive permissions; fixed to readable 0644 with normal file umask. Use live
  addresses/routes/networkctl to verify actual recovery, not `netplan get` alone.
- Network confirmation prompts timed out and frustrated the user. Final approach uses
  automatic validation/commit with a timed rollback guard; no `CONFIRM` question.
- UFW inserted at position 1 when no rules existed: `ERROR: Invalid position '1'`.
  Firewall script corrected for an empty ruleset; preserve existing rules.
- Chrony validation under `/root/hermes-backups/chrony-*/chrony.conf.new` failed
  `Permission denied` after privilege dropping. Validate at the readable installed config
  path; retain backup privately. Chrony must be synchronized, not merely running.
- Auditd restart can be prohibited by its unit. Start/enable appropriately; do not rely on
  unconditional restart. Sysstat health is primarily its collection/summary timers.
- A blanket 1M soft NOFILE service default can disrupt some daemons. Full base installer
  uses 1024 soft/1048576 hard; set individual production units only after their needs are known.
- Hermes attachment assumed old venv paths and mutated npm versions. Current reviewed
  source uses the managed package system and `.hermes/bin/hermes`; retain lockfile authority.
- Original Hermes source removed Supermemory config and overwrote profile skills/config.
  Revised behavior preserves existing state and adds missing assets; fresh memory defaults
  do not replace a configured provider.
- Original community/MCP sync rewrote indexes from only the current run, losing prior
  records on source outages. Revised sync is additive, with atomic primary-index writes
  and catalog CLI serialization; existing captures stay searchable.
- `hermes skills check` checks for upstream skill updates; it is not a local validity test.
  Local content hashes/YAML/profile identity checks are used for collection validation.
- Provider credentials/API reachability, external plugin dependencies, root-only legacy
  MCP paths, external CLI logins and trading throughput cannot be certified by offline
  installer checks. Validate these on the actual host after installation.

## Immediate acceptance sequence

1. Run the new Hermes installer after the baseline and production Docker scripts. Review
   errors/warnings. Recheck with `bash 13-install-hermes.sh --validate-only`.
2. Confirm Hermes runs as the dedicated account and Docker reports the `rootless` security
   option for development; production Docker remains active on its original socket.
3. Confirm all 87 originals and 29 profiles are present, existing provider/memory/MCP data
   survived, and existing skill edits remain. Review catalog failures before claiming an
   exhaustive community import. A partial catalog refresh is not an API failure.
4. Configure missing API/OAuth/model selection, then run a real inexpensive test session
   and selected MCP tests. Do not publish gateway/UI ports during installation.
5. Obtain the real checkout and run `hermes-project-context /actual/repository`. Read its
   manifests and architecture docs; replace unknown product-stack details with evidence.
6. Inventory current disks/RAID, old VPS services/data, restore-tested backups and migration
   requirements before proposing database/reverse-proxy/service scripts or traffic cutover.
7. Measure representative market-data ingestion, fan-out, concurrent API clients, tail
   latency, loss/backpressure, sustained bandwidth and failure recovery. Tune from evidence.

## Official references reviewed

- Hermes source/installer: https://github.com/NousResearch/hermes-agent
- Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Context files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
- Memory providers: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers
- Docker rootless: https://docs.docker.com/engine/security/rootless/
- Hetzner network: https://docs.hetzner.com/robot/dedicated-server/network/net-config-debian-ubuntu/

## Reusable request for the next model

"We are at the context limit. Please write a highly dense, comprehensive technical summary
of our project. Include: the overall architecture, the tech stack, the exact file structure,
the current state of development, and the immediate next steps or bugs we are working on.
Keep it formatted so I can feed it back to a new model to instantly resume where we left off."

Use the known facts above, inspect the actual checkout, and label unknowns. Preserve
authorization/preferences and exact outstanding errors. Keep a compact resume block and
reference large logs, file trees and collections separately. Never include passwords,
API tokens, private keys, environment values or hidden assumptions as established facts.
