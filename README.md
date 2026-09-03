# Job Hunter AU

An automated Australian IT job discovery and alerting system built with Python, JobSpy, GitHub Actions, and Telegram.

The system searches job listings on a recurring schedule, applies configurable role, location, seniority, and eligibility filters, removes previously seen vacancies, maintains job-search history, and sends relevant opportunities through Telegram.

## Features

- Search IT job listings from Indeed and Google Jobs
- Configure job titles, technical keywords, locations, and exclusion rules
- Filter out senior roles, high experience requirements, and selected eligibility restrictions
- Deduplicate previously discovered vacancies
- Send matching jobs through Telegram
- Query recent jobs and job-search statistics through Telegram commands
- Run automatically on a scheduled GitHub Actions workflow
- Maintain persistent job-search history
- Review historical job-search activity
- Test Telegram bot functionality with Python unit tests

## Architecture

```text
GitHub Actions
    |
    | Scheduled every 4 hours
    v
main.py
    |
    |-- Search job listings
    |-- Apply filters
    |-- Deduplicate vacancies
    |
    v
config.py
    |
    |-- Search terms
    |-- Blacklist keywords
    |-- Required keywords
    |-- Location rules
    |
    v
job_history.json
    |
    |-- Store previously seen vacancies
    |-- Prevent duplicate alerts
    |
    v
Telegram
    |
    |-- Job alerts
    |-- Recent jobs
    |-- Statistics
    |-- Reports
```

## Project Structure

```text
job-hunter-au/
├── .github/
│   └── workflows/
│       └── scrape.yml
├── config.py
├── job_history.json
├── job_history_reviewer.py
├── main.py
├── requirements.txt
├── telegram_bot.py
├── test_bot.py
└── README.md
```

### Main Components

| File | Purpose |
|---|---|
| `main.py` | Core job-search, filtering, deduplication, and alert workflow |
| `config.py` | Search terms, keyword filters, and location rules |
| `telegram_bot.py` | Telegram notifications and interactive commands |
| `job_history_reviewer.py` | Job-history reporting and analysis |
| `job_history.json` | Stores previously discovered vacancies |
| `test_bot.py` | Unit tests for Telegram bot commands |
| `.github/workflows/scrape.yml` | Scheduled GitHub Actions workflow |

## Requirements

- Python 3.10 or higher
- Telegram bot token
- Telegram chat ID

## Installation

Clone the repository:

```bash
git clone https://github.com/kunallikescorsair/job-hunter-au.git
cd job-hunter-au
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

The application requires the following environment variables:

| Variable | Description | Required |
|---|---|---|
| `TELEGRAM_TOKEN` | Telegram bot token created through BotFather | Yes |
| `CHAT_ID` | Comma-separated Telegram chat IDs that receive alerts | Yes |

### macOS and Linux

```bash
export TELEGRAM_TOKEN="your_bot_token_here"
export CHAT_ID="your_chat_id_here"
```

### Windows PowerShell

```powershell
$env:TELEGRAM_TOKEN="your_bot_token_here"
$env:CHAT_ID="your_chat_id_here"
```

Do not commit Telegram tokens or chat IDs directly to the repository.

## Running Locally

Run the job-search workflow with:

```bash
python main.py
```

## Search Configuration

Search behaviour is configured in `config.py`.

The current configuration covers several junior and early-career Australian IT role categories.

### Job Categories

1. **ICT Support Technician / Service Desk Analyst**
   - IT Support Officer
   - Service Desk Analyst
   - Helpdesk Support
   - Desktop Support Technician
   - Technical Support Officer

2. **Clinical Systems Support / Health ICT**
   - Clinical Systems Support Officer
   - Health ICT Support
   - Clinical Applications Support
   - eHealth Support Officer

3. **Junior Systems Administrator**
   - Junior Systems Administrator
   - ICT Systems & Network Officer
   - Infrastructure Support Officer
   - Network Administrator

4. **Junior Business Analyst / Process Analyst**
   - Junior Business Analyst
   - Systems Analyst
   - Business Process Analyst
   - IT Business Analyst

5. **Junior Data / Reporting Analyst**
   - Junior Data Analyst
   - Reporting Officer
   - BI Assistant
   - Business Intelligence Analyst

6. **Junior Software / Web Developer**
   - Junior Software Developer
   - Junior Web Developer
   - Backend Developer
   - Full Stack Developer

7. **QA Tester / Software Tester**
   - QA Engineer
   - Software Tester
   - Test Analyst
   - UAT Tester
   - Quality Assurance Analyst

## Filtering Logic

### Excluded Keywords

The current configuration can exclude jobs containing terms associated with:

**Seniority**
- senior
- lead
- principal
- staff
- manager
- head of
- director

**Experience requirements**
- 5+ years
- 7+ years
- 10+ years

**Eligibility requirements**
- australian citizen
- citizenship required
- security clearance

### Required Keywords

Jobs can also be required to contain at least one relevant technical term.

Examples include:

**Core IT**
- ICT
- Helpdesk
- Service Desk
- Technical Support

**Technical**
- Network
- Database
- SQL
- Software Development

**Tools and platforms**
- Power BI
- Tableau
- Azure
- AWS
- Linux
- VMware

## Location Filtering

The default configuration applies different rules depending on location.

| Location | Behaviour |
|---|---|
| Sydney / NSW | Primary search region with flexible filtering |
| Remote | Remote roles across Australia can be accepted |
| Part-time | Part-time roles outside Sydney can be included |
| Other locations | Excluded unless they satisfy configured conditions |

These rules can be changed in `config.py`.

## Telegram Bot

The Telegram bot supports several commands for reviewing job-search activity.

| Command | Description |
|---|---|
| `/start` | Display the command list |
| `/report` | Generate a job-history report for the previous 14 days |
| `/stats` | Display summary job statistics |
| `/recent` | Show the 10 most recent jobs from the previous 7 days |
| `/help` | Display usage information |

## Automation

The scraper runs automatically through GitHub Actions.

Current schedule:

```text
Every 4 hours
```

Cron configuration:

```yaml
0 */4 * * *
```

The workflow:

1. Checks out the repository
2. Sets up Python 3.10
3. Installs dependencies
4. Runs the job scraper
5. Updates `job_history.json`

The workflow can also be triggered manually using `workflow_dispatch`.

### GitHub Actions Secrets

Configure the following repository secrets before enabling the workflow:

```text
TELEGRAM_TOKEN
CHAT_ID
```

## Job History

`job_history.json` stores previously discovered vacancies so that the same job is not repeatedly sent through Telegram.

Example:

```json
[
  {
    "title": "Service Desk Analyst",
    "company": "Example Company",
    "url": "https://example.com/job/123",
    "scraped_at": "2026-02-03T15:21:53"
  }
]
```

The application keeps up to 1,000 history entries and removes older entries as new vacancies are collected.

## Testing

Run the Telegram bot tests with:

```bash
python -m unittest test_bot.py
```

The tests cover:

- `/start`
- `/report`
- `/stats`
- `/recent`
- `/help`

## Customisation

### Add Search Terms

Edit the search terms in `config.py`:

```python
SEARCH_TERMS = [
    "Junior Data Analyst",
    "Service Desk Analyst",
    "Junior Software Developer",
]
```

### Modify Exclusion Rules

```python
BLACKLIST_KEYWORDS = [
    "senior",
    "lead",
    "principal",
]
```

### Modify Required Keywords

```python
REQUIRED_KEYWORDS = [
    "ICT",
    "SQL",
    "Technical Support",
]
```

### Change the Schedule

Edit:

```text
.github/workflows/scrape.yml
```

For example:

```yaml
on:
  schedule:
    - cron: "0 */4 * * *"
```

## ANZSCO Targeting

The configuration also supports targeting Australian IT occupations associated with selected ANZSCO classifications.

| Code | Occupation |
|---|---|
| 313199 | ICT Support Technicians nec |
| 261111 | ICT Business Analyst |
| 262113 | Systems Administrator |
| 261312 | Developer Programmer |
| 261313 | Software Engineer |
| 261314 | Software Tester |

This targeting is part of the configurable job-search logic and can be adapted independently of the core scraping and alerting workflow.

## Dependencies

Core dependencies include:

| Package | Purpose |
|---|---|
| `python-jobspy` | Job listing retrieval from supported job platforms |
| `pandas` | Data processing and filtering |
| `requests` | HTTP communication |

See `requirements.txt` for the complete dependency list.

## License

This project is available under the MIT License.

## Author

Kunal Gurung

## Acknowledgments

- [JobSpy](https://github.com/cullenwatson/jobspy) for job listing retrieval
- Telegram tooling for notification functionality
- GitHub Actions for scheduled automation
