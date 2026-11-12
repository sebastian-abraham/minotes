"""ise_drills.py — 20MCN401 Industrial Safety Engineering practice.

One combined drill per module: an 8-mark answer prompt, a model answer in the
same plain voice as the kits, and the marks scheme.
"""

ISE_DRILLS = [
    dict(id="i1", m=1, type="write", topic="Domino theory → prevention",
         q="Explain the Domino theory of accident causation and show what it changes about prevention. (8 marks)",
         model="""**In plain English.** Heinrich imagined an accident as five dominoes in a line. Each one knocks the next over. Remove any domino and the last one never falls — so prevention is about pulling one out, not about blaming the worker who was hit.

**The five dominoes.**
1. Ancestry and social environment — upbringing and background that shape a person's habits.
2. Fault of the person — carelessness, recklessness, or ignorance of safe practice.
3. Unsafe act or unsafe condition — the immediate mechanical or human cause.
4. Accident — the unplanned event itself: the fall, the release, the contact.
5. Injury — the consequence.

**What it changes.** The first two are hard for a manager to influence. The third is where control actually happens: guard the machine, fix the floor, train the task. Removing domino 3 stops the sequence before domino 4.

**Its limits.** It puts the focus on the worker's fault, and it treats the sequence as linear. Later theories — human factors, systems theory — model multiple causes acting together.

**For marks:** name five dominoes in order, state the removal principle, then give one construction example and one limitation.""",
         points=["five dominoes in order", "removal principle (any one domino)", "focus on unsafe act/condition",
                 "one worked example", "one limitation (blames worker, linear model)"]),
    dict(id="i2", m=2, type="write", topic="safety performance rates",
         q="Define frequency rate, severity rate, incidence rate and activity rate, and explain what each one tells a manager that the others do not. (8 marks)",
         model="""**In plain English.** Four rates measure four different things. Frequency counts how often injury happens. Severity counts how badly. Incidence counts how many workers were affected in a period. Activity counts how much safety work was actually done.

**The formulas.**
- **Frequency rate** = (number of lost-time injuries × 1,000,000) ÷ total man-hours worked. It answers: how often per million hours.
- **Severity rate** = (total man-days lost × 1,000,000) ÷ total man-hours worked. It answers: how many days lost per million hours.
- **Incidence rate** = (number of injuries × 1,000) ÷ average number of workers employed. It answers: how many of my people were hurt.
- **Activity rate** = (number of safety activities completed ÷ number planned) × 100. It answers: are we doing the work we promised.

**Why four and not one.** Frequency can stay flat while severity climbs — the same number of accidents but worse ones. Incidence shifts with headcount, so a growing site looks worse. Activity is the leading indicator; the other three are lagging.

**Worked check.** 4 lost-time injuries, 2,000 man-days lost, 500,000 man-hours, 250 workers.
Frequency = 4 × 1,000,000 ÷ 500,000 = **8**. Severity = 2,000 × 1,000,000 ÷ 500,000 = **4,000** man-days per million hours. Incidence = 4 × 1,000 ÷ 250 = **16**.

**Trap.** Forgetting the multiplier, or mixing man-hours with man-days. Write the formula, substitute, then state the unit.""",
         points=["four formulas with multipliers", "what each measures", "lagging vs leading distinction",
                 "worked calculation", "unit stated"]),
    dict(id="i3", m=3, type="write", topic="scaffolding + demolition",
         q="State the safety precautions for scaffolding and working platforms, then the safety measures for demolishing a ten-storey building in a congested area. (8 marks)",
         model="""**In plain English.** A scaffold is a temporary structure carrying people, so it gets treated like a permanent structure. Demolition is the reverse of construction: it must be planned in the order the building was built, but backwards.

**Scaffolding precautions.**
1. Designed and erected by a competent person, on a stable base with sole plates.
2. Standards, ledgers and transoms braced; ties to the building at intervals.
3. Platform fully decked, with guardrails about 1 m high and toe boards.
4. Inspected before first use, after alteration, and after bad weather; tagged safe.
5. No overloading; materials spread evenly; work stops in high wind.
6. Access by a tied ladder, never by climbing the frame.

**Demolition in a congested area.**
1. Survey and structural report first; method statement and sequence approved before work.
2. Services isolated — electricity, gas, water — and proven dead.
3. Exclusion zone with hoarding and signage; adjacent structures monitored for vibration and settlement.
4. Debris controlled: chutes, enclosed skips, no throwing from height; dust suppression by water.
5. Work from the top down; never undercut walls; temporary supports where load paths change.
6. Trained crew, PPE, fall protection, and a first-aid plan; no demolition by untrained labour.
7. Neighbours notified; noise and dust limited to permitted hours.

**For marks:** two labelled lists. The examiner is checking that scaffolding is about *structure and inspection*, and demolition is about *sequence and exclusion*.""",
         points=["competent person + inspection", "guardrails, toe boards, decking", "bracing and ties",
                 "services isolated", "top-down sequence + exclusion zone", "dust, vibration, neighbours"]),
    dict(id="i4", m=4, type="write", topic="machine guarding",
         q="Explain the principle of machine guarding and describe three types of guards or devices, with one power-press example. (8 marks)",
         model="""**In plain English.** The point of operation is where the machine cuts, bends or presses. Guarding means the hand cannot reach that point while the machine can move — and the machine cannot move while the hand is there.

**The principle.** Three rules:
1. The guard prevents contact with the point of operation.
2. It does not create a new hazard — no sharp edges, no trap points.
3. It must not be easy to defeat or remove; it needs a tool to open.

**Three types.**
- **Fixed guard** — a physical barrier, no moving parts. Cheapest and most reliable; needs no interlocks, but access for maintenance is harder.
- **Interlocked guard** — the machine cannot run while the guard is open. Good for presses and doors; relies on the interlock working, so it is tested.
- **Presence-sensing device** — a light curtain or pressure mat that stops the stroke when a hand enters. Fast enough for a press, but needs a brake that actually stops the ram in time.

**Power-press example.** On a press brake, a fixed guard covers the back, an interlocked gate covers the front, and the two-hand control keeps both hands out of the die during the stroke.

**Trap.** A guard that only slows the hand down is not a guard. Guarding is about distance, time and barriers, not warnings.""",
         points=["point of operation defined", "three rules of guarding", "three guard types",
                 "power-press application", "defeat-resistance"]),
    dict(id="i5", m=5, type="write", topic="HAZOP",
         q="Explain the objectives and steps of a HAZOP study, and work one deviation for a feed line. (8 marks)",
         model="""**In plain English.** HAZOP asks one question in many ways: *what if this parameter is not what we intended?* A team walks the plant line by line, applying guide words to each parameter, and records what could go wrong.

**Objectives.** Identify hazards and operability problems in a design or an existing plant. Find the causes of deviations. Decide whether existing safeguards are enough. Produce actions with owners.

**Steps.**
1. Define the scope and the nodes, and mark them on a P&ID.
2. Assemble the team — process, operations, maintenance, safety, and a trained leader who is not the designer.
3. For each node, list the parameters that matter: flow, pressure, temperature, level.
4. Apply each guide word to each parameter: no, more, less, as well as, part of, reverse, other than.
5. Record the deviation, its causes, its consequences, and the safeguards that already exist.
6. Decide: acceptable, or an action with a named owner and a date.
7. Write the report and follow up the actions.

**One worked deviation.** Node: feed line to reactor. Parameter: flow. Guide word: *no*.
- Deviation: no flow.
- Causes: pump trip, closed valve, blocked strainer, empty tank.
- Consequences: reaction stops, or unreacted material accumulates and reacts later.
- Safeguards: low-flow alarm, pump interlock, level indication.
- Action: add a low-flow trip, and test the interlock quarterly.

**Trap.** HAZOP is a team study, not a checklist. Writing "operator error" as a cause is a non-answer; name the mechanism.""",
         points=["one-sentence purpose", "objectives", "seven steps", "guide words with a parameter",
                 "worked node with cause/consequence/safeguard/action"]),
]
