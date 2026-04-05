# Evaluation Set: Meeting Summarizer

This evaluation set contains 5 representative inputs for testing the Meeting Summarizer.

---

### Case 1: Normal Meeting (Standard Transcript)
**Input:**
```text
Sarah: Okay, let's start the weekly sync. Engineering, how's the new API coming along?
Tom: We're about 80% done. We had a slight delay with the authentication module, but we should have it ready for testing by Wednesday.
Sarah: Great. Marketing, did we finalize the copy for the landing page?
Jane: Not yet. We're still debating the headline. I'll sync with the design team tomorrow to wrap it up.
Sarah: Okay. Let's aim to have the landing page live by Friday. Tom, make sure the API is stable before then.
```
**Expected Output:** A clear summary showing API progress (80%, testing by Wednesday), landing page status (pending headline), and the Friday deadline.
**Note:** A good output should clearly link tasks to the responsible parties (Tom and Jane).

---

### Case 2: Messy Shorthand Notes
**Input:**
```text
- budget review mtg 
- q3 overspend by 5%
- fix: cut back on external contractors next month
- need new vendor for cloud storage (aws too expensive?)
- Mark to research Google Cloud vs Azure by EOD Friday
- next mtg Tuesday 10am
```
**Expected Output:** Structured summary highlighting the Q3 overspend and the decision to reduce contractors. Clearly lists Mark's research task with the Friday deadline.
**Note:** A good output should expand the shorthand into professional, readable summaries without losing the core facts.

---

### Case 3: Complex Transcript with Multiple Action Items (Edge Case)
**Input:**
```text
Alex: The product launch is in two weeks. We need to finalize everything. 
Beth: I still need the technical specs from David. 
David: I'll send those over by noon. 
Alex: Good. Once Beth has those, she can finish the manual. 
Chris: What about the demo video? 
Alex: Chris, you're handling that, right? 
Chris: Yes, but I need a script. 
Beth: I can draft a script after the manual is done, probably Thursday.
David: Also, we need to book the conference room for the launch event. I'll take care of that today.
Alex: Don' forget the catering. Beth, can you look into that?
Beth: Sure, I'll call the caterers tomorrow morning.
```
**Expected Output:** A comprehensive list of at least 5 action items with their respective owners and deadlines.
**Note:** This tests the model's ability to track multiple owners and interdependent tasks (Beth needs David's specs before she can do the manual).

---

### Case 4: Ambiguous/Conflicting Instructions (Failure/Human Review Case)
**Input:**
```text
John: We should definitely use Python for this project.
Kelly: I disagree, Java is much more stable for our infrastructure.
John: Well, maybe we can use a bit of both? Or maybe just stick to Node.js since the team knows it best.
Kelly: Actually, Node might work. Let's think about it and decide later.
John: Okay, let's have someone start the initial setup in something.
```
**Expected Output:** The summary should highlight that the technology choice is **undecided** and requires further discussion.
**Note:** This is a failure case where the model might hallucinate a decision (like "They decided on Node.js") when no clear decision was actually reached. It should flag this for human review.

---

### Case 5: Short Informal Check-in
**Input:**
```text
Mike: Hey, just checking in on the bug fixes.
Leo: Most are done. Just one left on the login page. I'll have it fixed in an hour.
Mike: Awesome, thanks!
```
**Expected Output:** A very brief summary: login bug fix in progress, expected finish in one hour.
**Note:** Tests the model's ability to be concise without adding unnecessary fluff to a very short interaction.
