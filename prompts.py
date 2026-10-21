RESEARCH_REPORT_PROMPT = """
You are an AI research assistant.

The user wants research on:
{topic}

Below are web search results:
{research_data}

Create a structured research report with these sections:

# Title
# Executive Summary
# Key Findings
# Important Statistics
# Sources
# Conclusion

Rules:
1. Use only information supported by the search results.
2. Do not invent statistics.
3. Clearly separate facts from uncertain information.
4. Include the source URLs.
5. Keep it clear and easy to understand.
"""