#!/usr/bin/env python3
"""Add supplied assets and supported defaults; retain user integration data."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import stat
import subprocess
import tempfile
import yaml

BASE = Path(os.environ['HERMES_BASE_HOME'])
ASSETS = Path(__file__).parent
STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S') + f'-{os.getpid()}'
INVARIANTS = ['model','providers','mcp_servers','fallback_providers','credential_pool_strategies','auxiliary','memory','plugins']
CORE = {'project-context-handoff','cost-token-governance','prompt-context-engineering',
        'community-skill-librarian','mcp-universe-librarian','mcp-security-governance',
        'production-software-engineering','qa-testing','secure-engineering','api-integration',
        'secrets-iam','backup-disaster-recovery'}
ROUTES = {
 'orchestrator': ['product-project','release','automation','sre','devops','ai-llm','data-engineering'],
 'coding-engineer': ['database','ui-ux','devops','release','cloud','mcp-server','golang','rust','nextjs','nestjs','tailwind'],
 'qa-testing': ['qa-testing','web-api-security','statistics','sre','release'],
 'devops-sre': ['devops','sre','cloud','network','audit','supply-chain','cryptography','pat-','simhaonline','docker'],
 'cloud-infrastructure': ['cloud','devops','network','database'],
 'security-audit': ['security','identity','threat','vulnerability','supply-chain','cryptography','dfir','pashov','auditmos','cloudflare'],
 'ethical-hacking-pentest': ['authorized','pentest','security','vulnerability','identity','network','reporting'],
 'red-team': ['red-team','authorized','pentest','identity','network','reporting'],
 'blue-team': ['blue-team','threat','dfir','malware','sre','vulnerability','reporting'],
 'purple-team': ['purple-team','red-team','blue-team','threat','authorized','reporting'],
 'white-team': ['white-team','authorized','governance','reporting','legal'],
 'yellow-team': ['yellow-team','secure','supply-chain','devops','release'],
 'green-team': ['green-team','blue-team','authorized','dfir'],
 'orange-team': ['orange-team','authorized','product-project','copywriting'],
 'ai-llm-engineer': ['ai-','rag','nlp','computer-vision','ml-','mlops','data','mcp-server'],
 'ai-research-mlops': ['ai-','ml-','mlops','research','statistics','mathematics','scientific','data'],
 'data-knowledge': ['data','database','rag','knowledge','statistics'],
 'research-science': ['research','statistics','mathematics','logic','scientific'],
 'metatrader-quant': ['metatrader','mql','finance','statistics','mathematics','data-analysis','llmquant','algo-trading','quant-','pat-','tradingview','xauusd','indicators','wine'],
 'analytics-finance': ['finance','data','database','statistics','business-analytics','llmquant','timescale','questdb'],
 'business-operations': ['business','product-project','automation','release','alerting','human-ai'],
 'documents-office': ['documents','localization','copywriting','legal'],
 'legal-corporate': ['legal','business-documents','ai-governance'],
 'creative-media': ['graphic','ui-ux','marketing','copywriting','designer','tailwind','ui-ux-pro-max'],
 'marketing-growth': ['marketing','seo','copywriting','ecommerce','graphic','analytics'],
 'communications-sales': ['communications','sales','omnichannel','marketing','copywriting','localization','whatsapp','wassenger','telegram','discord','2chat'],
 'mcp-librarian': ['mcp','api','secrets'],
 'skill-librarian': ['community-skill','prompt','mcp','research'],
 'esoteric-advisor': ['astrology','numerology','chinese','witchcraft','esoteric','research'],
 'multi-agent-architect': ['multi-agent', 'orchestrator', 'superpowers', 'delegation', 'automation', 'agent'],
 'backend-architect': ['backend', 'database', 'api', 'cloud', 'system-design', 'microservices', 'superpowers', 'golang', 'rust', 'nestjs'],
 'database-optimizer': ['database', 'sql', 'query', 'postgres', 'sqlite', 'indexing', 'performance', 'timescale', 'questdb', 'redis', 'neon'],
 'code-reviewer': ['code-review', 'qa-testing', 'security', 'superpowers', 'verification', 'testing'],
 'agentic-search-optimizer': ['seo', 'marketing', 'search', 'mcp', 'api', 'web', 'agent'],
 'token-optimizer': ['token', 'compression', 'saver', 'context', 'cost', 'efficiency'],
 'tradingview-quant': ['tradingview', 'pinescript', 'indicators', 'signals', 'lightweight-charts', 'fibonacci', 'quant-', 'metatrader', 'mql'],
 'fabric-engineer': ['fabric', 'spark', 'synapse', 'databricks', 'powerbi', 'lakehouse', 'database', 'sql'],
 'web-scraping-specialist': ['scraping', 'crawler', 'anti-bot', 'scrapling', 'scrapfly', 'apify', 'browser'],
 'knowledge-graph-architect': ['graph', 'knowledge-graph', 'neo4j', 'memstack', 'ontology', 'lightrag', 'obsidian'],
 'product-manager': ['prd', 'product', 'sprint', 'roadmap', 'stakeholder', 'user-story', 'launch', 'pm-'],
 'chart-visualization': ['chart', 'visualization', 'antv', 'apexcharts', 'echarts', 'lightweight-charts', 'd3', 'infographic'],
 'pat-operations': ['pat-', 'xauusd', 'predictatrade', 'simhaonline', 'mql', 'wine', 'signal-', 'trading-', 'quant', 'indicators', 'mt4-mt5', 'docker-', 'migration', 'backtest', 'go-live', 'telemetry', 'realtime', 'drift', 'pine-', 'auth-session', 'audit-remediation', 'control-plane', 'edge-request', 'server-backup', 'repo-evaluation', 'docs-runbooks', 'ai-ml-engine'],
 'mathematics-ai': ['math', 'paper', 'research', 'scientific', 'statistics', 'logic', 'algebra', 'calculus', 'geometry', 'theorem', 'lean', 'coq'],
 'office-excel-pdf': ['excel', 'spreadsheet', 'pdf', 'weasyprint', 'compdf', 'formula', 'macro', 'vba', 'pivot', 'worksheet', 'document'],
 'nginx-caddy-infrastructure': ['nginx', 'caddy', 'proxy', 'reverse-proxy', 'web-server', 'tls', 'ssl', 'load-balancer', 'waf', 'security'],
 'astro-web-architect': ['astro', 'framework', 'content-collections', 'static-site', 'ssg', 'ssr', 'web', 'ui-ux', 'frontend', 'tailwind'],
 'minimax-voice-agent': ['minimax', 'voice', 'audio', 'tts', 'stt', 'music', 'sound', 'multimodal', 'speech'],
 'kimi-reasoning-specialist': ['kimi', 'moonshot', 'reasoning', 'long-context', 'superpowers', 'research', 'analysis'],
 'manus-autonomous-agent': ['manus', 'autonomous', 'workflow', 'automation', 'agent', 'research', 'browser', 'multi-step'],
 'workbuddy-enterprise': ['workbuddy', 'enterprise', 'powershell', 'automation', 'productivity', 'workflow', 'office'],
 'tencent-cloud-architect': ['tencent', 'cloudbase', 'rtc', 'lbs', 'map', 'wechat', 'cloud', 'architecture'],
 'laravel-architect': ['laravel', 'php', 'backend', 'bagisto', 'laraclaude', 'eloquent', 'blade', 'artisan', 'api'],
 'seo-growth-marketer': ['seo', 'search', 'ranking', 'keywords', 'backlinks', 'growth', 'marketing', 'seranking', 'content-strategy'],
 'foundation-agent': ['general', 'core', 'foundational', 'reasoning', 'assistant', 'prompt', 'automation'],
}

def sync_tree(src, dst):
    Path(dst).mkdir(parents=True, exist_ok=True)
    subprocess.run(['rsync', '-a', f"{src}/", f"{dst}/"], check=True)

def atomic(path, data, mode=0o600):
    if path.is_symlink():
        raise RuntimeError(f'Refusing to replace symlink: {path}')
    path.parent.mkdir(parents=True,exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.'+path.name+'-',dir=path.parent)
    try:
        with os.fdopen(fd,'w') as f:
            os.chmod(tmp,mode); f.write(data)
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def cfgread(path):
    data = yaml.safe_load(path.read_text()) if path.exists() else {}
    if data is None: data = {}
    if not isinstance(data,dict): raise RuntimeError(f'Config must be a mapping: {path}')
    return data

def copy_missing(src, dest, conflicts, top=True, origin_src=None, origin_dest=None):
    """Never overwrite existing target files; online-backup SQLite instead of copying WAL."""
    if not src.is_dir(): return
    origin_src = src if origin_src is None else origin_src
    origin_dest = dest if origin_dest is None else origin_dest
    dest.mkdir(parents=True,exist_ok=True)
    skip = {'hermes-agent','tools','runtime','.venv','venv','bin','cache','logs','terminal-sessions'} if top else set()
    for p in sorted(src.iterdir()):
        if p.name in skip or p.name.endswith(('-wal','-shm','-journal','.pid','.sock')): continue
        d = dest/p.name
        if p.is_symlink():
            if not d.exists() and not d.is_symlink():
                target = os.readlink(p)
                if target.startswith(str(origin_src)+'/'):
                    target = str(origin_dest) + target[len(str(origin_src)):]
                d.symlink_to(target)
            continue
        if p.is_dir():
            if d.is_symlink(): continue
            if d.exists() and not d.is_dir():
                copy_missing(p,conflicts/p.name,conflicts/p.name,False,origin_src,origin_dest); continue
            copy_missing(p,d,conflicts/p.name,False,origin_src,origin_dest); continue
        if not p.is_file(): continue
        if d.exists() or d.is_symlink():
            if d.is_file() and not d.is_symlink() and p.stat().st_size == d.stat().st_size:
                with p.open('rb') as original, d.open('rb') as existing:
                    if hashlib.file_digest(original,'sha256').digest() == hashlib.file_digest(existing,'sha256').digest(): continue
            conflicts.mkdir(parents=True,exist_ok=True)
            d = conflicts/p.name
            if d.exists(): continue
        with p.open('rb') as f: header = f.read(16)
        if header == b'SQLite format 3\0':
            uri = p.resolve().as_uri()+'?mode=ro'
            with sqlite3.connect(uri, uri=True,timeout=15) as original, sqlite3.connect(d) as backup:
                original.backup(backup, pages=256, sleep=0.05)
            os.chmod(d,0o600)
        else:
            shutil.copy2(p,d)

def migrate(source):
    # Called as root. Original paths are left intact. Do not launch a second gateway.
    source = Path(source)
    if source.resolve() != BASE.resolve():
        copy_missing(source,BASE,BASE/'migration-conflicts'/'legacy')
    for src,dest in [('/opt/hermes-community-skill-pool','.local/share/hermes-community-skill-pool'),
                     ('/opt/hermes-mcp-universe','.local/share/hermes-mcp-universe'),
                     ('/opt/hermes-mcp-servers','.local/share/hermes-mcp-servers')]:
        copy_missing(Path(src),Path(os.environ['HERMES_ACCOUNT_HOME'])/dest,BASE/'migration-conflicts'/Path(src).name)

def skills():
    manifest = json.loads((ASSETS/'collection-manifest.json').read_text())
    for record in manifest['skills']:
        p = ASSETS/'skills'/record['name']/'SKILL.md'
        if hashlib.sha256(p.read_bytes()).hexdigest() != record['sha256']:
            raise RuntimeError(f'Attachment skill checksum mismatch: {record["name"]}')
    for p in sorted((ASSETS/'skills').iterdir()):
        dest_custom = BASE/'skills'/'custom'/p.name
        if not dest_custom.exists() and not dest_custom.is_symlink():
            dest_custom.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(p, dest_custom, symlinks=True)
        dest_lib = BASE/'skill-library'/'submitted'/p.name
        if not dest_lib.exists() and not dest_lib.is_symlink():
            dest_lib.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(p, dest_lib, symlinks=True)
    # Copy all skill-library categories (community-elite, quant-trading, databases-timeseries, ui-ux-design, backend-languages, security-audit, omnichannel-messaging, etc.)
    if (ASSETS/'skill-library').is_dir():
        sync_tree(ASSETS/'skill-library', BASE/'skill-library')
    # Copy agent-library (Agency Agents)
    if (ASSETS/'agent-library').is_dir():
        sync_tree(ASSETS/'agent-library', BASE/'agent-library')
    # Copy mcp-library
    if (ASSETS/'mcp-library').is_dir():
        sync_tree(ASSETS/'mcp-library', BASE/'mcp-library')
    # Copy plugins (superpowers, homeassistant etc.)
    if (ASSETS/'plugins').is_dir():
        sync_tree(ASSETS/'plugins', BASE/'plugins')
    # Copy cron jobs, database and history
    if (ASSETS/'cron').is_dir():
        sync_tree(ASSETS/'cron', BASE/'cron')
    # Copy persistent memories
    if (ASSETS/'memories').is_dir():
        sync_tree(ASSETS/'memories', BASE/'memories')
    if (ASSETS/'pending_memory').is_dir():
        sync_tree(ASSETS/'pending_memory', BASE/'pending_memory')
    # Copy references (predictatrade setup, configs, backups)
    if (ASSETS/'references').is_dir():
        sync_tree(ASSETS/'references', BASE/'references')
    docs = BASE/'references'/'predictatrade-setup'
    docs.mkdir(parents=True,exist_ok=True)
    for name in ['submitted-installer.txt','collection-manifest.json','profiles.json','TOKEN_POLICY.md','PROJECT_HANDOFF.md']:
        p = ASSETS/name
        if p.is_file() and not (docs/name).exists(): shutil.copy2(p,docs/name)
    print(f'Retained {len(manifest["skills"])} supplied custom and elite skills, agent library, MCP library, plugins, cron, and memories.')

def skill_names(home):
    names = set()
    for p in (home/'skills').rglob('SKILL.md'):
        raw = p.read_text(errors='replace')
        m = re.match(r'\A---\s*\n(.*?)\n---',raw,re.S)
        if m:
            try: meta = yaml.safe_load(m[1])
            except yaml.YAMLError: continue
            if isinstance(meta,dict) and isinstance(meta.get('name'),str): names.add(meta['name'])
    return names

def apply_policy(home, new_profile=None):
    path = home/'config.yaml'
    cfg = cfgread(path)
    before = {k: json.loads(json.dumps(cfg.get(k))) for k in INVARIANTS}
    max_turns_env = os.environ.get('HERMES_MAX_TURNS', '250')
    try:
        max_turns = int(max_turns_env)
    except ValueError:
        max_turns = max_turns_env
    policy = {
      'agent': {'max_turns': max_turns,
                'budget_warning_ratio': 0.8, 'api_max_retries': 3},
      'compression': {'enabled': True, 'threshold': 0.75, 'target_ratio': 0.20,
                      'tail_mode': 'lean', 'protect_last_n': 20},
      'delegation': {'max_iterations': 250, 'max_concurrent_children': 3, 'max_spawn_depth': 2,
                     'orchestrator_enabled': True, 'worktree_isolation': False, 'max_summary_chars': 12000},
      'code_execution': {'mode': 'project', 'timeout': 300, 'max_tool_calls': 50},
      'tools': {'tool_search': {'enabled': 'on', 'listing': 'auto', 'listing_max_tokens': 2000}},
      'checkpoints': {'enabled': True, 'max_snapshots': 20},
    }
    for section,values in policy.items():
        node = cfg.setdefault(section,{})
        if not isinstance(node,dict): raise RuntimeError(f'{section} must be a mapping in {path}')
        for key,value in values.items():
            if isinstance(value,dict):
                # Old shorthand `tool_search: true` is supported upstream; retain that intent.
                old = node.get(key)
                if isinstance(old,bool): old = {'enabled':'on' if old else 'off'}
                if old is not None and not isinstance(old,dict): raise RuntimeError(f'Invalid {section}.{key}')
                node[key] = {**(old or {}),**value}
            else: node[key] = value
    cfg.setdefault('approvals',{}).setdefault('mode','smart')
    if home == BASE:
        kanban = cfg.setdefault('kanban',{})
        for key,value in {'orchestrator_profile':'orchestrator','default_assignee':'orchestrator','auto_decompose':True}.items():
            if not kanban.get(key): kanban[key] = value
    if new_profile:
        patterns = ROUTES.get(new_profile, [new_profile])
        all_names = skill_names(home)
        selected = CORE | {n for n in all_names if any(x in n for x in patterns)}
        original_disabled = set(cfg.setdefault('skills',{}).get('disabled',[]))
        cfg['skills']['disabled'] = sorted(original_disabled | (all_names-selected))
    # Preserve memory provider, API configuration, MCP definitions and plugin selection exactly.
    for key in INVARIANTS:
        if cfg.get(key) != before[key]: raise RuntimeError(f'Integration changed unexpectedly: {key}')
    if path.exists():
        backup = home/'configuration-backups'/f'config-{STAMP}.yaml'
        backup.parent.mkdir(mode=0o700,exist_ok=True)
        shutil.copy2(path,backup); os.chmod(backup,0o600)
    atomic(path,yaml.safe_dump(cfg,sort_keys=False,allow_unicode=True))

def profiles():
    apply_policy(BASE)
    for record in json.loads((ASSETS/'profiles.json').read_text()):
        name = record['name']; home = BASE/'profiles'/name
        new = not home.exists()
        if new:
            subprocess.run(['hermes','-p','default','profile','create',name,
                            '--clone-from','default','--no-alias','--description',record['description']],check=True)
        # Existing profile files/descriptions, keys, memory and skill selections stay intact.
        apply_policy(home,name if new else None)
    print(f'All {len(json.loads((ASSETS/"profiles.json").read_text()))} specialist profiles present; existing descriptions and skill selections preserved.')

def import_env():
    source = Path(os.environ['HERMES_ENV_FILE'])
    path = BASE/'.env'
    current = path.read_text() if path.exists() else ''
    pattern = re.compile(r'^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=')
    existing = set()
    for line in current.splitlines():
        m = pattern.match(line)
        if m and line[m.end():].strip() not in ['', '\"\"', "''"]: existing.add(m[1])
    added = []
    for line in source.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith('#'): continue
        m = pattern.match(line)
        if not m: raise RuntimeError('HERMES_ENV_FILE must use single-line KEY=value entries; contents were not printed.')
        if m[1] not in existing:
            added.append(line); existing.add(m[1])
    if path.exists():
        backup = BASE/'configuration-backups'/f'env-{STAMP}.backup'
        backup.parent.mkdir(mode=0o700,exist_ok=True)
        shutil.copy2(path,backup); os.chmod(backup,0o600)
    if added:
        atomic(path,current.rstrip()+'\n\n# Imported additional provider settings\n'+'\n'.join(added)+'\n')
    print(f'Imported {len(added)} missing/empty environment settings; existing non-empty values retained.')

def initialize_memory():
    path = BASE/'config.yaml'
    cfg = cfgread(path)
    memory = cfg.setdefault('memory',{})
    memory.update({'memory_enabled':True,'user_profile_enabled':True,'provider':'holographic'})
    cfg.setdefault('plugins',{}).setdefault('hermes-memory-store',{}).update(
        {'auto_extract':True,'default_trust':0.60,'hrr_dim':1024})
    atomic(path,yaml.safe_dump(cfg,sort_keys=False,allow_unicode=True))
    print('Fresh installation: bundled local Holographic memory enabled; no existing memory provider replaced.')

def validate():
    manifest = json.loads((ASSETS/'collection-manifest.json').read_text())
    for row in manifest['skills']:
        candidates = [BASE/'skills'/'custom'/row['name']/'SKILL.md',
                      BASE/'skill-library'/'submitted'/row['name']/'SKILL.md']
        if not any(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'] for p in candidates):
            raise RuntimeError(f'Missing retained original skill: {row["name"]}')
    for row in manifest['profiles']:
        home = BASE/'profiles'/row['name']
        if not any((home/p).is_file() for p in ['profile.yaml','config.yaml','.env','SOUL.md']):
            raise RuntimeError(f'Missing profile identity: {row["name"]}')
        cfgread(home/'config.yaml')
    cfgread(BASE/'config.yaml')
    print('Collection preservation and YAML/profile validation passed.')

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('action',choices=['migrate','assets','profiles','validate','import-env','initialize-memory'])
    p.add_argument('--source',default='/root/.hermes'); a = p.parse_args()
    if a.action == 'migrate': migrate(a.source)
    elif a.action == 'assets': skills()
    elif a.action == 'profiles': profiles()
    elif a.action == 'import-env': import_env()
    elif a.action == 'initialize-memory': initialize_memory()
    else: validate()
