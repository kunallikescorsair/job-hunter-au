"""
Configuration settings for the Job Hunter AU Bot.

This module contains all configurable parameters for the job scraper:
- Search terms organized by job category
- Blacklist and required keyword filters
- Location-based filtering rules
- Telegram message templates

Target: Specific roles for BIT + MICT + nursing background that support PR goals in Australia.
"""

# =============================================================================
# JOB SEARCH SETTINGS
# =============================================================================

# Location for job searches (currently Australia-wide)
LOCATION = "Sydney, NSW, Australia"

# Number of results to fetch per search term (keep low to avoid rate limiting)
RESULTS_PER_TERM = 10

# =============================================================================
# SEARCH TERMS BY JOB CATEGORY
# =============================================================================
# Organized into 7 categories relevant to PR pathways (ANZSCO codes)
SEARCH_TERMS = [
    # --------------------------------------------------------------------------
    # Data Scientist / Applied Scientist
    # --------------------------------------------------------------------------
    "Data Scientist",
    "Junior Data Scientist",
    "Graduate Data Scientist",
    "Associate Data Scientist",
    "Applied Scientist",
    "Decision Scientist",

    # --------------------------------------------------------------------------
    # Machine Learning Engineer
    # --------------------------------------------------------------------------
    "Machine Learning Engineer",
    "Junior Machine Learning Engineer",
    "Graduate Machine Learning Engineer",
    "Associate Machine Learning Engineer",
    "ML Engineer",
    "AI Engineer",
    "Applied Machine Learning Engineer",

    # --------------------------------------------------------------------------
    # MLOps / ML Platform / AI Platform
    # --------------------------------------------------------------------------
    "MLOps Engineer",
    "Junior MLOps Engineer",
    "Machine Learning Operations Engineer",
    "ML Platform Engineer",
    "AI Platform Engineer",
    "Model Deployment Engineer",
    "Model Operations Engineer",

    # --------------------------------------------------------------------------
    # Data Analyst / Product Analyst / BI Analyst
    # Useful fallback roles for getting into DS/ML market
    # --------------------------------------------------------------------------
    "Data Analyst",
    "Junior Data Analyst",
    "Graduate Data Analyst",
    "Product Analyst",
    "Analytics Engineer",
    "Business Intelligence Analyst",
    "BI Analyst",

    # --------------------------------------------------------------------------
    # Data Engineer / Analytics Engineer
    # Relevant because many DS/ML entry roles ask for SQL, pipelines, cloud
    # --------------------------------------------------------------------------
    "Data Engineer",
    "Junior Data Engineer",
    "Graduate Data Engineer",
    "Analytics Engineer",
    "ETL Developer",
    "Data Platform Engineer",

    # --------------------------------------------------------------------------
    # GenAI / NLP / LLM roles
    # Relevant to your NLP, LLM, and Writegy-style profile
    # --------------------------------------------------------------------------
    "Generative AI Engineer",
    "LLM Engineer",
    "NLP Engineer",
    "AI Developer",
    "AI Software Engineer"
]

# =============================================================================
# BLACKLIST KEYWORDS - Jobs containing these will be EXCLUDED
# =============================================================================
# Jobs matching any of these keywords will be filtered out
BLACKLIST_KEYWORDS = [
    # --- Seniority Exclusions ---
    # Exclude roles clearly above entry/junior/graduate level
    "senior", "principal", "staff", "head of", "director",
    "engineering manager", "data science manager", "analytics manager",
    "machine learning manager", "ai manager",

    # --- Heavy Experience Exclusions ---
    "5+ years", "6+ years", "7+ years", "8+ years", "10+ years",
    "minimum 5 years", "minimum five years",
    "at least 5 years", "at least five years",

    # --- Citizenship / Security Clearance Exclusions ---
    # Important for many Australian gov/defence roles
    "australian citizen", "citizenship required", "citizens only",
    "must be australian", "must be a citizen", "citizen of australia",
    "security clearance", "nv1", "nv2", "baseline clearance",
    "defence clearance", "clearance required",

    # --- Irrelevant Non-DS/ML Roles ---
    "helpdesk", "service desk", "desktop support", "technical support",
    "field technician", "it support officer", "systems administrator",
    "network administrator", "cyber security analyst",
    "sales representative", "customer service", "call centre",
    "receptionist", "administration officer", "finance officer",
    "registered nurse", "occupational therapist", "teacher"
]

# =============================================================================
# REQUIRED KEYWORDS - Jobs must contain at least ONE of these
# =============================================================================
# Jobs must mention at least one of these technology keywords to be considered relevant
REQUIRED_KEYWORDS = [
    # --- Core DS / ML / AI ---
    "data science", "data scientist", "machine learning", "ml engineer",
    "artificial intelligence", "ai", "predictive modelling", "predictive modeling",
    "statistical modelling", "statistical modeling", "classification",
    "regression", "forecasting", "recommendation", "nlp", "natural language processing",
    "computer vision", "deep learning", "generative ai", "llm", "large language model",

    # --- Programming / Data Stack ---
    "python", "sql", "pandas", "numpy", "scikit-learn", "sklearn",
    "pytorch", "tensorflow", "keras", "xgboost", "lightgbm", "catboost",

    # --- MLOps / Deployment ---
    "mlops", "model deployment", "model monitoring", "model registry",
    "feature store", "experiment tracking", "mlflow", "kubeflow",
    "docker", "kubernetes", "fastapi", "api", "ci/cd", "github actions",

    # --- Cloud / Data Platforms ---
    "aws", "azure", "gcp", "databricks", "snowflake", "bigquery",
    "spark", "pyspark", "airflow", "dbt",

    # --- Analytics / BI fallback ---
    "analytics", "data analysis", "business intelligence", "power bi",
    "tableau", "dashboard", "reporting", "ab testing", "a/b testing"
]

# =============================================================================
# ROLE-SPECIFIC KEYWORDS - Additional keywords for specific job categories
# =============================================================================
# These can be used for more granular filtering of specific role types
ROLE_SPECIFIC_KEYWORDS = {
    "Data Scientist": [
        "data science", "machine learning", "statistics", "modelling", "modeling",
        "classification", "regression", "forecasting", "experimentation",
        "python", "sql", "scikit-learn"
    ],
    "Machine Learning Engineer": [
        "machine learning", "ml engineer", "deep learning", "pytorch",
        "tensorflow", "model training", "model deployment", "python",
        "docker", "kubernetes", "api"
    ],
    "MLOps Engineer": [
        "mlops", "model deployment", "model monitoring", "mlflow",
        "kubeflow", "feature store", "docker", "kubernetes",
        "ci/cd", "aws", "azure", "gcp"
    ],
    "Data Engineer": [
        "data engineering", "etl", "elt", "pipelines", "spark",
        "pyspark", "airflow", "databricks", "snowflake", "sql",
        "dbt", "data warehouse"
    ],
    "Analytics": [
        "analytics", "data analyst", "product analyst", "power bi",
        "tableau", "dashboard", "reporting", "sql", "a/b testing"
    ],
    "GenAI/NLP": [
        "generative ai", "llm", "large language model", "nlp",
        "natural language processing", "rag", "langchain",
        "prompt engineering", "embeddings", "transformers"
    ]
}

# =============================================================================
# LOCATION FILTERING TERMS
# =============================================================================

# =============================================================================
# LOCATION FILTERING TERMS
# =============================================================================

# Terms indicating job is in Sydney / NSW
SYDNEY_LOCATION_TERMS = [
    "sydney", "nsw", "new south wales",
    "north sydney", "parramatta", "macquarie park",
    "chatswood", "barangaroo", "surry hills",
    "pyrmont", "eveleigh", "rhodes",
    "australia square", "cbd"
]

# Terms indicating remote or hybrid work
REMOTE_TERMS = [
    "remote", "work from home", "wfh", "anywhere",
    "virtual", "100% remote", "telecommute"
]

HYBRID_TERMS = [
    "hybrid", "hybrid working", "flexible working",
    "flexible work", "work from home", "wfh"
]

# =============================================================================
# PR-RELEVANT OCCUPATION CODES (ANZSCO)
# =============================================================================
# Australian and New Zealand Standard Classification of Occupations codes
# for roles that may be relevant for Permanent Residency pathways
PR_OCCUPATIONS = [
    "224999",  # Information and Organisation Professionals nec / Data Scientist often assessed here
    "261111",  # ICT Business Analyst
    "261112",  # Systems Analyst
    "261311",  # Analyst Programmer
    "261312",  # Developer Programmer
    "261313",  # Software Engineer
    "263111",  # Computer Network and Systems Engineer
    "262113"   # Systems Administrator
]

# =============================================================================
# TELEGRAM MESSAGE TEMPLATE
# =============================================================================
# Template for formatting job alerts sent via Telegram
TELEGRAM_MSG_TEMPLATE = (
    "🤖 *{title}*\n"
    "🏢 {company}\n"
    "📍 {location}\n"
    "📅 {posted_date}\n"
    "🔗 [Apply Here]({job_url})"
)