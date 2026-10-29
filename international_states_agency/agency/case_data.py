CASE_STUDIES = [
    {
        "slug": "autonomous-freight-manifest-reconciliation",
        "title": "Autonomous Multi-Modal Manifest & Customs Reconciliation Engine",
        "client_industry": "Global Freight Logistics & Maritime Shipping",
        "client_classification": "[Confidential Enterprise / EMEA Operations]",
        "summary": "Engineering a deterministic multi-agent pipeline to extract, cross-verify, and audit multilingual customs declarations across 14 European and North American ports.",
        "challenge": "The client processed over 4,500 shipping manifests weekly across 4 languages. An auditing team of 8 analysts spent 42 minutes per document reconciling tariff codes against legacy ERP records.",
        "solution": "We engineered an air-gapped, multi-agent cognitive architecture. Inbound documents are routed to a multimodal vision agent, structured into typed Pydantic models, and verified by deterministic mathematical guardrails.",
        "system_architecture": [
            {"step": "01", "name": "Ingestion Gateway", "desc": "Air-gapped S3 bucket webhook trigger capturing PDFs and EDIFACT feeds."},
            {"step": "02", "name": "Multimodal Extraction", "desc": "Vision LLM parsing 4 languages into strictly typed Pydantic models."},
            {"step": "03", "name": "Mathematical Guardrail", "desc": "Deterministic Python layer verifying weight balance and tariff compliance."},
            {"step": "04", "name": "ERP Mutation & Alerting", "desc": "Synchronous NetSuite API mutation + Slack alert to on-duty customs broker."}
        ],
        "technologies": ["Python 3.12", "LangGraph", "Pydantic V2", "FastAPI", "Docker", "NetSuite SuiteTalk API"],
        "process_steps": [
            {"phase": "Phase 01: Audit", "detail": "14-day analysis of 5,000 legacy manifests to map tariff edge-cases."},
            {"phase": "Phase 02: Architecture", "detail": "Specification of zero-drift validation contracts and human-in-the-loop fallbacks."},
            {"phase": "Phase 03: Sandbox", "detail": "Dual-run processing against live operations for 21 days with 0 production mutations."},
            {"phase": "Phase 04: Production", "detail": "Full cutover across 14 European and North American port terminals."}
        ],
        "verified_outcomes": [
            {"metric": "84%", "label": "Reduction in End-to-End Processing Latency", "note": "[Verified Production Benchmark]"},
            {"metric": "320 hrs", "label": "Reclaimed Analyst Capacity Per Week", "note": "[Audited Operations Metric]"},
            {"metric": "< 0.02%", "label": "Discrepancy Escape Rate", "note": "[Deterministic Guardrail Standard]"}
        ],
        "system_status": "OPERATIONAL // 14 NODES ACTIVE"
    },
    {
        "slug": "air-gapped-sovereign-contract-intelligence",
        "title": "Air-Gapped Sovereign RAG & Deal Diligence Vault",
        "client_industry": "Cross-Border Private Equity & Corporate Law",
        "client_classification": "[Tier-1 Financial Advisory / Zurich]",
        "summary": "Building a private, self-hosted vector intelligence environment to cross-examine 40,000+ proprietary M&A contracts without third-party data leakage.",
        "challenge": "During acquisitions, legal teams faced weeks of manual due diligence. Regulations prohibited uploading proprietary transaction data to commercial public LLMs.",
        "solution": "International States architected an on-premise, air-gapped retrieval-augmented generation (RAG) platform with self-hosted open-weights models and verbatim citation guardrails.",
        "system_architecture": [
            {"step": "01", "name": "Air-Gapped Ingestion", "desc": "Local pipeline parsing encrypted PDF, DOCX, and legacy records."},
            {"step": "02", "name": "Semantic Chunking", "desc": "Hierarchical clause-aware chunking preserving contextual legal relationships."},
            {"step": "03", "name": "Hybrid Vector Search", "desc": "Dense vector + BM25 sparse keyword retrieval with reranking."},
            {"step": "04", "name": "Citation Guard", "desc": "Deterministic post-processor blocking any answer lacking a direct document anchor."}
        ],
        "technologies": ["Qdrant", "Llama-3 70B", "vLLM", "FastAPI", "Tailwind CSS", "CUDA 12"],
        "process_steps": [
            {"phase": "Phase 01: Compliance", "detail": "Information security audit to ensure complete zero-egress hardware isolation."},
            {"phase": "Phase 02: Pipeline", "detail": "Custom legal tokenization and synthetic legal evaluation dataset creation."},
            {"phase": "Phase 03: Reranking", "detail": "Fine-tuning of cross-encoder reranking layer for specialized contract clauses."},
            {"phase": "Phase 04: Rollout", "detail": "Secured deployment to 45 M&A partners with hardware token auth."}
        ],
        "verified_outcomes": [
            {"metric": "480ms", "label": "Average Semantic Clause Retrieval Time", "note": "[Measured on 100K Chunk Corpus]"},
            {"metric": "0.00%", "label": "External Data Egress / Cloud Leakage", "note": "[SOC2 / Hardware Verified]"},
            {"metric": "140 hrs", "label": "Saved Per Transaction Audit Cycle", "note": "[Partner Review Feedback]"}
        ],
        "system_status": "DEPLOYED // AIR-GAPPED PRIVATE CLOUD"
    }
]

def get_all_case_studies():
    return CASE_STUDIES

def get_case_study(slug):
    return next((cs for cs in CASE_STUDIES if cs["slug"] == slug), None)
