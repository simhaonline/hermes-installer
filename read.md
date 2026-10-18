# Master Development Prompt — Upgrade Existing SIMHA Hermes Installer

## Project

**Existing GitHub repository:** https://github.com/simhaonline/hermes-installer

**Objective:** Enhance, extend, optimize and production-harden the existing Hermes Installer by integrating a comprehensive ecosystem of AI Skills, Specialized Agents, MCP Servers, Plugins and a built-in searchable Library.

**IMPORTANT: This is an existing, actively developed project. DO NOT rebuild it from scratch, replace its architecture, create a separate installer, or remove working functionality.**

## 1. Existing Repository Audit

Clone or open the existing repository and inspect its complete structure, including:

- `install-hermes-local.sh`
- `quick-install.sh`
- `hermes-registry`
- `hermes-vault`
- `package-content-vault.sh`
- `.agents/`
- `AGENTS.md`
- `GEMINI.md`
- `MEMORY.md`
- `README.md`
- `README-HERMES.md`
- `README-LOCAL-INSTALL.md`
- Existing configuration, dependencies, permissions, service integrations and installation workflows.

Understand how Hermes is installed, configured, updated and managed.

Identify existing functionality and determine precisely how the requested enhancements should integrate with it.

Preserve root and rootless installation, existing installations, configuration, credentials, memory, content vault and backward compatibility.

## 2. Integrate All Supplied Reference Resources

Use the complete GitHub URL collection provided with this task as the primary discovery source.

The references cover:

- SEO, GEO, AEO and AI search optimization
- Digital marketing and social media management
- Machine learning, deep learning and NLP
- Computer vision and data analytics
- MLOps and AI infrastructure
- Coding, software engineering and automation
- Prompt engineering and AI agent orchestration
- Research, fact-checking and knowledge extraction
- Cybersecurity, defensive security and authorized red-team testing
- AI governance, ethics and risk management
- Executive leadership and corporate operations
- Finance, accounting, investment and HR
- Sales, CRM and customer success
- Legal, contracts, procurement, supply chain and logistics
- Document processing and enterprise productivity
- Audio, video, voice and generative media
- RAG, knowledge management and document-to-skill conversion
- Agent frameworks, MCP ecosystems and skills registries

Process **every provided URL**.

Deduplicate repeated references, distinguish GitHub topic pages from actual repositories, discover relevant projects and inspect their technical suitability.

Do not treat a repository containing educational resources as an executable Skill. Classify resources correctly.

Maintain a source manifest containing repository URL, category, license, upstream version or commit, compatibility, dependencies, security findings and installation status.

## 3. Extend the Existing Hermes Skills System

Integrate supported third-party skills into Hermes through its existing native skill-loading mechanism.

Implement or extend:

- Skill discovery and categorization
- Skill installation and uninstallation
- Skill enable/disable controls
- Skill dependency management
- Skill version tracking
- Skill updates and rollback
- Skill compatibility checking
- Skill conflict detection
- Skill health validation
- Skill search and recommendations
- Skill permissions and security checks

Skills should be accessible to Hermes after installation without users having to manually copy files or edit configuration.

Do not invent unsupported Hermes-native APIs. Implement adapters only where compatibility has been verified.

## 4. Specialized Agents

Expand the existing agent system with domain-specialized agents covering the categories in the supplied collection.

Support:

- Agent registration and discovery
- Agent roles and capability definitions
- Agent-specific skills and tools
- Agent delegation
- Multi-agent coordination
- Task routing
- Context and memory boundaries
- Permission isolation
- Agent evaluation and performance logging

Agents should reuse the existing Hermes execution and model infrastructure.

Do not create a separate competing agent runtime unless an adapter is technically necessary.

## 5. MCP Server Integration

Extend Hermes with a managed MCP integration layer, compatible with its supported MCP transport and tool mechanisms.

Implement:

- MCP server discovery
- MCP installation and configuration
- Local and remote MCP connections
- Tool enumeration
- Connection health checks
- Authentication configuration
- Permission controls
- Server enable/disable
- Startup and shutdown management
- Error handling and reconnection
- Logging and diagnostics

Ensure external MCP servers cannot automatically gain unrestricted host filesystem, shell or credential access.

## 6. Plugin Management

Build upon any existing Hermes plugin or extension facilities.

Implement a standardized plugin lifecycle:

`DISCOVER → VALIDATE → INSTALL → CONFIGURE → ENABLE → UPDATE → DISABLE → UNINSTALL → ROLLBACK`

Each plugin must have a manifest, version, dependencies, permissions, upstream source, installation state and validation result.

Where a third-party plugin is incompatible with Hermes, implement a supported adapter or catalog it as unavailable rather than falsely claiming successful installation.

## 7. Built-in Unified Library

Extend the existing `hermes-registry` and `hermes-vault` rather than replacing them.

The goal is one unified **Hermes Extension Library** containing:

- Skills
- Specialized Agents
- MCP Servers
- Plugins
- Workflow templates
- Prompt libraries
- Knowledge resources
- Research resources

Provide searchable metadata, filtering, categories, tags, versions, compatibility indicators, installed state, update availability and source attribution.

The registry should distinguish:

1. Discovered resources
2. Verified resources
3. Installable resources
4. Installed resources
5. Enabled resources
6. Unsupported or quarantined resources

Provide CLI-based management and integrate with any existing user-facing management interface without introducing unnecessary dependencies.

## 8. Improve the Existing Installation Scripts

Modify the existing scripts in place.

Ensure both fresh installation and upgrades of existing Hermes installations are supported.

Requirements:

- Root and rootless operation
- Idempotent installation and reruns
- Automatic dependency detection
- OS and architecture compatibility checks
- Minimal prompts
- No unnecessary manual configuration
- Secure credential handling
- Preserve existing user data and settings
- Incremental extension installation
- Network retry and timeout controls
- Disk space and dependency checks
- Atomic configuration writes
- Transactional rollback where feasible
- Detailed diagnostics
- Service health checks
- Automatic recovery from interrupted installs
- Safe uninstall and upgrade procedures

Integrate the new Skills, Agents, MCP, Plugins and Library capabilities into the existing installation workflow.

Do not force-install hundreds of potentially incompatible packages. Ship validated, safe defaults and make additional extensions discoverable and installable through the Library.

## 9. Security and Production Hardening

Treat all third-party repositories as untrusted until evaluated.

Perform:

- License and dependency checks
- Pinning to verified releases or commits
- Supply-chain verification
- Static code and shell-script analysis
- Secret scanning
- Path traversal protection
- Shell injection prevention
- Download integrity validation
- Filesystem permission auditing
- Rootless compatibility testing
- Least-privilege execution
- Controlled external command execution
- Secure MCP credentials
- Rollback testing

Never print, commit, or expose `/root/.git-credentials`, API keys, tokens, passwords or other secrets.

Use existing authentication mechanisms only for their intended authenticated Git operations.

## 10. Testing and Validation

Test the upgraded repository through automated checks and practical installation scenarios.

Required scenarios:

- Clean installation
- Existing installation upgrade
- Repeated installation
- Root installation
- Rootless installation
- Interrupted installation
- Network failure recovery
- Skill installation and execution
- Agent discovery and routing
- MCP server connection
- Plugin installation and removal
- Registry and Library searching
- Dependency failure
- Permission failure
- Update and rollback
- Uninstall without unintended data loss

Verify backward compatibility with existing Hermes functionality.

Do not claim a test passed unless it was actually executed successfully.

## 11. Documentation Updates

Update the existing documentation rather than replacing it with unrelated content.

Update:

- `README.md`
- `README-HERMES.md`
- `README-LOCAL-INSTALL.md`
- `AGENTS.md`
- Other relevant existing technical documentation

Document the revised architecture, installation and upgrade commands, extension management, troubleshooting, compatibility, security, and supported resource categories.

Include clear distinctions between built-in, optional, installed and merely discoverable resources.

## 12. GitHub Commit and Delivery

Once implementation and testing are complete:

1. Review the complete Git diff.
2. Verify no credentials, secrets or sensitive files are included.
3. Run available tests and record their actual results.
4. Update documentation and applicable release manifests.
5. Commit changes to the existing repository.
6. Push to the intended branch using the configured Git credentials.
7. Verify the remote commit.
8. Report the commit SHA, modified files, supported capabilities, test results and unresolved limitations.

**Repository:** `simhaonline/hermes-installer`

**Do not create a replacement repository.**

## Final Mandatory Requirements

- Enhance the existing Hermes Installer, not a new system.
- Retain all currently working functionality.
- Reuse existing architecture wherever technically possible.
- Process the complete supplied reference URL collection.
- Include Skills, Agents, MCP and Plugins.
- Provide a unified built-in Library using the existing registry and vault.
- Support both root and rootless installation.
- Make the installer upgrade-safe, repeatable and production-oriented.
- Preserve backward compatibility and user data.
- Avoid unnecessary complexity or unrelated features.
- Do not stop after producing recommendations or a development plan: implement supported changes, test them and deliver the resulting repository updates.
- Never report an integration or production test as completed without evidence.

**Success means the existing SIMHA Hermes Installer has been genuinely improved, remains installable and upgradeable, and can manage verified AI capabilities through its integrated extension ecosystem.**
