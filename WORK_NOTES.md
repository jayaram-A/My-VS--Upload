# AI Research Agent — Work Notes

## 1. Purpose

This project accepts a research topic, searches the web for supporting material, asks Gemini to turn that material into a structured report, and displays the report in a Streamlit app. The report can also be downloaded as Markdown.

## 2. One-time setup

1. Open a terminal in the project directory.
2. Activate the project virtual environment if it is not already active:
   - PowerShell: `.\.venv\Scripts\Activate.ps1`
3. Install the packages used by the project if they are not installed in the environment:
   - `streamlit`
   - `google-genai`
   - `python-dotenv`
   - `tavily-python`
4. Create or update the local `.env` file with the required credentials:
   - `GEMINI_API_KEY` — used for Gemini report generation.
   - `TAVILY_API_KEY` — used for web search.
5. Keep `.env` private; do not commit or share API keys.

## 3. Run the application

Start the Streamlit app from the project directory with `streamlit run app.py`. Streamlit opens the interface in a browser.

## 4. Work flow, step by step

1. **Enter a topic.** The app accepts the research topic in a text area.
2. **Validate input.** When Generate is clicked, the app warns if the topic is blank.
3. **Check Gemini credentials.** The research agent requires `GEMINI_API_KEY`; if missing, it raises a clear configuration error.
4. **Search the web.** The search helper requires `TAVILY_API_KEY` and requests up to five search results for the topic.
5. **Prepare source material.** Each result's title, URL, and content are assembled into a text block.
6. **Build the report prompt.** The topic and collected search material are inserted into the report instructions. The expected sections are Title, Executive Summary, Key Findings, Important Statistics, Sources, and Conclusion. The instructions require claims to be supported by the search results and prohibit invented statistics.
7. **Generate the report.** The agent calls Gemini using `gemini-flash-latest`, then `gemini-flash-lite-latest` as a fallback. Server errors are retried with waits of 5, 10, and 20 seconds for each model.
8. **Show and download the result.** The app displays the generated Markdown and offers it as `research_report.md`.
9. **Handle failures.** Exceptions raised during research or generation are shown in the app as an error message.

## 5. Main files

- `app.py` — Streamlit interface, input validation, progress indicator, report display, download, and user-facing error handling.
- `agent.py` — coordinates credentials, web search, source formatting, prompt creation, and Gemini retries/fallback.
- `tools.py` — Tavily web-search helper and its API-key check.
- `prompts.py` — report structure and source-grounding instructions.

## 6. Troubleshooting checklist

- **Missing API key:** Check that the `.env` file is in the project directory and the key name is spelled exactly as `GEMINI_API_KEY` or `TAVILY_API_KEY`.
- **Search or model service errors:** Confirm network access and that the corresponding API key is valid; Gemini server errors are retried automatically.
- **No report appears:** Confirm a non-empty topic was submitted, then inspect the error shown by the app.
- **Import errors:** Confirm the virtual environment is active and the four packages listed in setup are installed in it.
