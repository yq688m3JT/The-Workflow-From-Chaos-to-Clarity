# Project Report: The Workflow From Chaos to Clarity

## Business Use Case: The "Meeting After the Meeting"
In a fast-paced corporate environment, the "meeting after the meeting" is often where projects either find their wings or go to die. If the synthesis is poor, people walk away with different interpretations of their responsibilities, leading to redundant "status update" meetings that exist only to clarify what was supposed to happen after the previous meeting. 

This prototype aims to bridge that gap by providing a definitive, structured source of truth immediately after a sync, ensuring that every participant leaves with a unified understanding of decisions and assignments.

## Model Choice: Gemma 4 vs. Qwen 3.5
For this local deployment, I selected **gemma4:e2b** after comparative testing:
- **Selected Model (gemma4:e2b):** This model was chosen for its ability to provide concise, high-entropy responses. In a business context, brevity is a feature, not a bug. It strips away conversational filler and focuses on the core data.
- **Comparison (qwen3.5:4b):** While capable, Qwen's output tended to be overly verbose and redundant. In professional communication, excessive word count dilutes the message. A more compact response carries higher information density, which is more valuable for busy stakeholders.

## Prompt Evolution: From Summary to Structure
The prompt iteration process moved from simple text summarization to a highly visual, structured format:
- **Baseline:** The initial prompts provided general summaries but lacked visual hierarchy, making it difficult to scan for specific responsibilities.
- **Optimization:** By introducing Markdown tables and clear section headers, we increased the efficiency of information transfer. This ensures that "Task Distribution" is unmistakable and "Key Decisions" are isolated from general discussion.

## Prototype Evaluation & Limitations
### Current Strengths:
- **Transcript Handling:** The demo is sufficiently robust to handle medium-to-long video meeting transcripts, transforming raw dialogue into a professional report.
- **Clarity:** The use of padded tables significantly improves scannability for human reviewers.

### Known Limitations:
- **Formatting Rigor:** The output format is not yet 100% rigorous; occasionally, table dimensions or padding may vary depending on the complexity of the input.
- **Context Constraints:** Due to the finite context window of the local models, extremely long meetings (multi-hour workshops) cannot be processed in a single pass without losing earlier information.
- **Alignment:** While improved, the Markdown table borders can still face alignment issues in non-monospace viewing environments.

## Conclusion
This prototype demonstrates that a local LLM workflow can effectively eliminate the "clarification meeting" cycle by providing immediate, high-density summaries. While it requires a human-in-the-loop for very long or high-stakes technical meetings, it offers a massive head start in professional documentation.
