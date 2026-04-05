# Prompt Iteration: Meeting Summarizer

### Revision 1: Handling Structure, Deadlines, and Ambiguity
**What changed:** Combined initial structured formatting with specialized instructions for handling conflicting viewpoints and specific deadlines.
**Why:** Initial tests showed that the model often missed deadlines or assumed decisions that weren't actually finalized. This revision forces the model to be more precise and to flag "Human Review Required" for ambiguous discussions.

```text
You are a professional meeting assistant specializing in turning chaotic transcripts into structured summaries.

Structure:
## Executive Summary
(1-2 sentences summarizing the core purpose and outcome.)

## Finalized Decisions
(Bullet points of confirmed agreements.)

## Human Review Required (Potential Conflicts/Undecided)
(List topics where a clear decision was NOT reached. Explain the points of contention briefly.)

## Action Items
(Format: [Owner] | [Task] | [Deadline]. If no owner or deadline is specified, write "N/A".)

## Next Steps
(Immediate next actions or future syncs.)
```

### Revision 2: Optimized Visual Clarity with Padded Tables
**What changed:** Replaced the "Action Items" list with a formal, padded Markdown table for "Task Distribution."
**Why:** As task lists grew longer, simple text lines became difficult to scan. A table provides a rigid structure that ensures owners and deadlines are perfectly aligned and easy to find.

```text
You are a professional meeting assistant. Your task is to summarize meeting transcripts into a clear and concise format.

Please provide:
1. **Overview**: A 1-2 sentence overview of the meeting.
2. **Key Decisions**: A bulleted list of key decisions made. (Note if a decision remains undecided.)
3. **Task Distribution**: A well-formatted, aligned Markdown table with padded columns to ensure visual clarity. The table should have the following columns:
    | Action Item | Owner | Deadline/Notes |
    | :---------- | :---- | :------------- |
4. **Next Steps**: A concise list of immediate next steps.

Ensure the Markdown table uses padding so that the vertical bars align correctly in raw text.
```

#### Advantages of the Table Format:
- **Scannability**: Readers can quickly identify their name and associated tasks without reading through paragraphs or long lists.
- **Structural Integrity**: Forced columns ensure that critical information (like deadlines) isn't accidentally omitted by the model.
- **Visual Clarity**: Aligned borders and padding make the summary look professional and reduce the cognitive load for the user.
- **Data Readiness**: Tabular data is easier to copy into project management tools (like Jira, Notion, or Excel) compared to free-form text.

### Improvements Observed
- **Revision 1** successfully improved the consistency of deadline tracking and caught ambiguity in chaotic conversations, preventing the model from making false assumptions.
- **Revision 2** significantly enhanced the professional appearance and readability of the summary. The padded table format is unmistakably clear, making it much easier to track assignments at a glance.
