# Module 5 — Hazard Identification and Control

> 20MCN401 Industrial Safety Engineering · B.Tech CSE Sem 7 (Saintgits, autonomous) · CO5 · 20% of ESE.
> This module owns **47 of the 172 questions** — the largest set in the paper. Fire, extinguishers, inventory rating, the Dow Index, PHA, HAZOP, chemical control and MSDS all sit here.
> Source: `m5.txt` (`slide N`). Anything the deck does not give is marked **(standard)**.
> Values the deck supplies are quoted as the deck writes them; nothing is invented to fill a gap.

---

## 1. Coverage — syllabus line and question number

### Table A — the eight syllabus lines

| Syllabus line (verbatim) | Hrs | Answered at |
|---|---|---|
| Hazard and risk — types of hazards — classification of fire | 5 | §2.1, §2.2, §2.3 |
| Types of fire extinguishers — fire, explosion and toxic gas release | 5 | §2.4, §2.3 |
| Inventory analysis — fire and explosion hazard rating of process plants | 5 | §2.5 |
| The Dow Fire and Explosion Hazard Index | 5 | §2.6, §2.7 |
| Preliminary hazard analysis — hazard and operability study (HAZOP) | 5 | §2.8, §2.9, §2.10 |
| Chemical hazard — classifications, control of chemical hazards | 5 | §2.11, §2.12 |
| Hazardous properties of chemicals | 5 | §2.13 |
| Material Safety Data Sheets (MSDS) | 5 | §2.14 |

Nothing in this module is a one-line topic. Three lines are methods you must apply — inventory
rating, the Dow Index, and PHA with HAZOP. The exam asks you to run those, not describe them.

### Table B — all 47 questions

| Q | Question, shortened | Answered at |
|---|---|---|
| Q7 | Define hazard and risk | §3.1 A · §2.1 |
| Q8 | List the types of hazards | §3.1 B · §2.2 |
| Q9 | List the types of fire hazards | §3.1 C · §2.3 |
| Q10 | What is a fire extinguisher | §3.1 D · §2.4 |
| Q11 | What to remember before installing an extinguisher | §3.1 E · §2.4 |
| Q12, Q42 | Items required to develop the Dow F&EI | §3.1 F · §2.6 |
| Q51 | Key objectives of a HAZOP study | §3.1 G · §2.9 |
| Q52, Q128 | Steps in conducting a HAZOP | §3.1 H · §3.2 G · §2.9 |
| Q53 | Key objectives of a PHA | §3.1 I · §2.8 |
| Q54 | Advantages and disadvantages of PHA | §3.2 A · §2.8 |
| Q55 | Common hazards considered in a PHA | §3.1 J · §2.8 |
| Q56 | Define MSDS and its purpose | §3.1 K · §2.14 |
| Q57 | Types of chemical hazards | §3.1 L · §2.11 |
| Q58, Q123, Q127, Q172 | Control measures for chemical hazards | §3.3 C · §3.2 H · §2.12 |
| Q59, Q124 | Toxicity, flammability, reactivity and environmental safety | §3.2 I · §2.13 |
| Q60 | Role of PPE in controlling chemical hazards | §3.2 J · §2.12 |
| Q61 | Administrative controls versus PPE, Indian automotive | §3.3 D · §2.12 |
| Q62, Q126 | Three common control measures in a plant | §3.1 M · §3.2 H |
| Q63 | Major GHS hazard symbols | §3.1 N · §2.11 |
| Q64 | Importance of HAZOP analysis | §3.1 O · §2.9 |
| Q65 | Results of a HAZOP study | §3.2 B · §2.9 |
| Q90 | Classify fires | §3.1 P · §2.3 |
| Q91 | Types of extinguishers used in industry | §3.2 C · §2.4 |
| Q92 | Four risk assessment tools | §3.1 Q · §2.10 |
| Q93, Q169 | Dow F&EI and its objectives | §3.1 R · §2.6 |
| Q94 | Steps to calculate the Dow F&EI | §3.3 A · §2.7 |
| Q105 | Flow chart for the Dow calculation | §3.2 E · §2.7 |
| Q106 | Hazard factors contributing to the index | §3.2 F · §2.6 |
| Q115 | Role of government in safety | §3.1 S (Module I owns the long form) |
| Q119 | Need and importance of a safety committee | §3.1 T (Module I owns the long form) |
| Q121, Q171 | PHA versus HAZOP, and when to choose each | §3.3 B · §2.10 |
| Q122 | (a) PHA's role (b) implementation criteria and plans | §3.1 U · §3.2 M |
| Q131 | Precautions in lifting and carrying | §3.1 V |
| Q132 | Precautions in pulling and pushing | §3.1 W |
| Q145 | Fourteen PPE with a figure | §3.3 F |
| Q165 | How handling aids cut lifting injuries | §3.2 L |
| Q168 | Fire safety plan from the fire classification | §3.3 E · §2.4 |
| Q170 | Identify fire class and pick the extinguisher | §3.2 K · §2.4 |

Q115, Q119, Q131, Q132, Q145 and Q165 are Module I and Module IV topics that the paper files
here. They are answered here in short form, and the Module I and Module IV kits carry the long
versions.

---

## 2. Concepts

### 2.1 Hazard and risk

*In plain English.* A hazard is a live wire lying on the floor. The wire is dangerous whether
or not anyone is in the room. Risk is the chance that somebody touches it before lunch. Standing
further back does not make the wire safe. It makes the risk small.

*The detail.*
- **Hazard** — a source with the potential to cause injury or ill health (ISO 45001 wording).
- **Risk** — the combination of how likely harm is and how bad it would be.
- Risk therefore needs exposure. Remove the exposure and the risk falls.
- The hazard stays exactly where it was. That is the sentence this topic turns on.
- **Residual risk** — what remains after controls; the number a safety officer signs off.
- **Risk assessment** runs in four moves: identify, analyse, evaluate, treat.
- **Individual risk** is one person's chance of harm. **Societal risk** is the chance of many
  people harmed in one event.
- The **F–N curve** plots frequency against the number of fatalities (standard).
- **ALARP** means the risk has been cut as low as is reasonably practicable (standard).
- A **5 × 5 matrix** scores likelihood against severity and lands in low, medium, high or
  extreme (standard).

| Question | Hazard | Risk |
|---|---|---|
| What is it? | A source of harm | The chance of harm from that source |
| Can it be removed? | Only by removing or replacing the agent | Yes, by any control at all |
| Depends on | The material, the energy, the design | Exposure, duration, frequency, safeguards |
| Reduced by PPE? | No | Yes |
| Example | Petrol in a tank | Welding beside that tank |

*What to write (3 marks).* Two definitions, one line of contrast, one consequence. Say that
the hazard is inherent and the risk is conditional. Close with the point that substitution kills
the hazard while PPE only lowers the risk.

**Mark anchor.** "The hazard is inherent; the risk is conditional." A script with that sentence
has understood the pair rather than memorised two definitions.

**Exam trap.** Do not write "eliminate the risk" when you mean "eliminate the hazard". A risk
is a probability and cannot be eliminated. It can only be reduced, and the leftover is residual
risk.

### 2.2 Types of hazards

*In plain English.* Factories hurt people in a small number of recognisable ways. Someone is
struck, crushed, burned, poisoned, infected, deafened, or worn down slowly. Sorting hazards into
families is how an inspector knows what to look for first.

*The detail.*
- The standard split is seven families: physical, mechanical, electrical, chemical, biological,
  ergonomic and psychosocial.
- Fire and explosion are usually carried as a separate family in process plants.
- Every family has a signature harm. The signature is what the mark scheme wants beside the name.
- Hazards also split by **energy source**: gravity, motion, electricity, pressure, heat, chemical
  reaction, radiation (standard).
- They split again by **mode of contact**: struck-by, caught-in, contact, inhalation, ingestion,
  absorption (standard).
- In a process plant the chemical family dominates, because the inventory is large and the harm
  is delayed.
- In construction the mechanical and physical families dominate, because the work is at height
  and in motion.

| Family | Examples | Signature harm |
|---|---|---|
| Physical | Noise, vibration, heat, cold, radiation, pressure | Deafness, heat stress, burns |
| Mechanical | Unguarded shafts, moving parts, falling loads | Cut, crush, amputation, fracture |
| Electrical | Live parts, arc flash, static discharge | Shock, burns, ignition |
| Chemical | Solvents, acids, dusts, gases, fumes | Burns, poisoning, fire, sensitisation |
| Biological | Bacteria, viruses, moulds, insects | Infection, allergy |
| Ergonomic | Repetition, posture, manual handling | Musculoskeletal disorder |
| Psychosocial | Shift work, workload, harassment | Stress, fatigue, error |
| Fire and explosion | Flammable inventory, dust clouds | Burns, blast, collapse |

*What to write (3 marks).* Name the families in one line each, with one example and one harm
per family. A table is faster than prose and scores the same.

**Mark anchor.** Seven families with a signature harm each. The harm is worth more than the
example, because it proves you know why the family exists.

**Exam trap.** "Physical" and "mechanical" are not interchangeable. Noise and heat are physical.
A rotating shaft is mechanical. Putting noise under mechanical signals a list copied without
understanding.

### 2.3 Fire — the tetrahedron, the five classes, and what escapes

*In plain English.* Fire needs four things at once: something to burn, air, heat, and a
runaway chain reaction. Take any one away and the fire stops. Every extinguisher in the
catalogue is just a device for taking one of those four away quickly.

*The detail.*
- The **fire triangle** has three sides: fuel, oxygen, heat.
- The **fire tetrahedron** adds a fourth: the self-sustaining chain reaction.
- That fourth side is why dry chemical powder works on a fire it cannot cool or smother well.
- Four extinguishing methods map onto the four sides: starvation, smothering, cooling,
  chemical inhibition.
- **Flash point** — the lowest temperature at which a liquid gives off enough vapour to ignite.
- **Fire point** — the slightly higher temperature at which the vapour keeps burning.
- **Autoignition temperature** — the temperature at which a material ignites with no spark.
- Fire classes follow the Indian and European convention, running A to E (`slide 18`).

| Class | Fuel | Everyday examples | Extinguish by |
|---|---|---|---|
| A | Solid combustibles | Wood, paper, cloth, rubber, plastics | Cooling — water, foam |
| B | Flammable liquids | Petrol, kerosene, diesel, paint, solvents | Smothering — foam, CO₂, powder |
| C | Flammable gases | LPG, acetylene, hydrogen, methane | Shut the supply off, then cool |
| D | Combustible metals | Sodium, potassium, magnesium, aluminium powder | Dry powder for metal, dry sand |
| E | Live electrical equipment | Panels, motors, wiring, switchgear | Isolate, then CO₂ or clean agent |

**What escapes.** A fire is only one of three outcomes from the same inventory.
- **Pool fire** — a burning puddle of liquid, radiating heat onto its neighbours.
- **Jet fire** — pressurised gas burning as a torch flame from a failed flange.
- **Flash fire** — a vapour cloud ignites and burns back through it in seconds.
- **Vapour cloud explosion** — a confined or congested cloud deflagrates and produces a blast.
- **BLEVE** — a vessel heated until the liquid boils and the shell bursts (standard).
- **Dust explosion** — a suspended dust cloud ignites; the first blast shakes loose more dust.
- **Toxic gas release** — the fire itself makes the poison: carbon monoxide, hydrogen cyanide,
  hydrogen chloride, sulphur dioxide (standard).

*What to write (3 marks, Q90).* The five classes with fuel and one example each. For Q9, add
the three escape routes: fire, explosion, toxic release.

**Mark anchor.** Five classes, and in the Indian scheme **C is gas and E is electrical**. Add
that E fires are attacked only after isolation.

**Exam trap.** The American NFPA scheme uses A, B, C, D with **C for electrical** and a separate
K for cooking oil. Writing NFPA letters under an Indian question loses the classification mark.

### 2.4 Extinguishers and their selection

*In plain English.* An extinguisher is a pressure bottle of something that removes one side of
the fire tetrahedron. Pick the wrong bottle and you either do nothing or make it worse. Water on
burning petrol spreads the fire. Water on a live panel electrocutes the user.

*The detail.*
- **Definition** — a portable, pressurised first-aid device that discharges an agent onto a
  small fire (`slide 18`, `slide 19`).
- **Water** is the primary agent, sometimes with wetting agents added (`slide 18`).
- Water freezes, so unheated sites need antifreeze or a different agent (`slide 18`).
- **Water mist** sprays distilled water as a fine fog, for rooms where residue ruins equipment.
- The deck names operating rooms, museums and book collections as water-mist sites (`slide 18`).
- **CO₂** leaves no residue, so it suits delicate and costly electronics (`slide 19`).
- The deck lists CO₂ for **Class B and Class C** fires (`slide 19`).
- CO₂ fails outdoors in wind, because the gas blows away before it smothers (`slide 19`).
- CO₂ in a confined space displaces oxygen and needs caution (`slide 19`).
- **Foam** blankets a liquid surface and seals the vapour.
- **Dry chemical powder** interrupts the chain reaction; ABC powder covers A, B, C and E.
- **Wet chemical** saponifies hot cooking oil, the class F or K fire (standard).
- **Clean agents** such as FM-200 leave no residue and are safe in occupied rooms (standard).
- **Dry sand or graphite** is used on metal fires, where water reacts violently (standard).

| Agent | Classes | Works by | Never use on |
|---|---|---|---|
| Water | A | Cooling | Live electrical, burning liquids, metals |
| Foam | A, B | Smothering and sealing | Live electrical |
| CO₂ | B, C, E | Smothering, some cooling | Confined spaces without caution |
| Dry powder ABC | A, B, C, E | Chain inhibition | Delicate electronics (residue) |
| Wet chemical | F (cooking oil) | Saponification | Most other classes |
| Clean agent | A, B, C, E | Smothering and inhibition | Cost-critical sites only |

**Choosing and siting.** Selection runs class first, agent second, size third, position last.
- The extinguisher must match the class of fuel present in that room.
- Siting follows IS 2190: one water-type unit per 100 m², travel distance under 15 m (standard).
- Mount the unit on a bracket with the handle about 1.5 m from the floor (standard).
- Keep the unit visible, signed, and clear of stock and forklift routes.
- Check the pressure gauge and the service tag monthly, and refill after any use.
- A freezing or corroding location needs a different agent or a cabinet.
- Staff must be trained to use it, or the unit is furniture.

*What to write (3 marks, Q10 and Q11).* Define the extinguisher in one line. Then list the pre-installation checks: class match, right number for the area, unobstructed siting, temperature, service date, signage, training.

**Mark anchor.** CO₂ for electrical equipment and for Class B, because it leaves no residue. The
residue point is the reason, and the reason is the mark.

**Exam trap.** Water is not "the general extinguisher". On Class B it spreads the fuel. On
Class E it conducts. On Class D it can react and explode. Water is a Class A answer only.

### 2.5 Inventory analysis and hazard rating

*In plain English.* The size of a fire is set by how much fuel is sitting there, not by what
lit it. So the first question in a process plant is boring and powerful: what is on site, where
is it, and how much of it is there at once?

*The detail.*
- **Inventory** — the mass of hazardous material held in a unit, a tank, or a pipeline at any
  moment.
- **Inventory analysis** lists every hazardous material, its quantity, its location and its
  properties.
- The aim is a **fire and explosion hazard rating** for each part of the plant.
- Hold-up inside pipework counts. A long line holds more than the vessel it feeds.
- **Capital density** — the value of equipment packed into a given area. Dense plants lose more
  per event.
- The Dow method uses the spill of a flammable liquid **3 inches deep** as its reference event
  (`slide 48`).
- **NFPA 704** rates a material from 0 to 4 on health, flammability and instability (standard).
- The diamond reads blue for health, red for flammability, yellow for instability, white for
  special hazards (standard).
- **Mond** extends Dow by adding a toxicity index (standard).
- Indian law sets threshold quantities in the MSIHC Rules, 1989, Schedules 1 to 3 (standard).
- Above the threshold, the site must prepare an on-site emergency plan and notify the authority.

| Rating tool | What it scores | Scale |
|---|---|---|
| NFPA 704 | One material's health, fire, reactivity | 0–4 per quadrant |
| Dow F&EI | One process unit's fire and explosion exposure | 1 to 159+ |
| Mond | Dow plus toxicity | Index plus toxicity rating |
| MSIHC threshold | Whether the site is a major accident hazard site | Quantity against schedule |

**Why inventory matters more than ignition.** Ignition sources are countless and cheap to
control one at a time. Inventory is one number, and it can be cut deliberately.
- Buy in smaller lots and hold less in the plant.
- Remove intermediate storage tanks between process steps.
- Shorten pipe runs and reduce line diameter where hold-up is large.
- Move storage away from process units to increase separation.
- A smaller inventory makes every downstream number smaller: fire size, exposure radius, loss.

*What to write (5 marks).* Define inventory, list what is counted, name the rating tools, and
close on inventory reduction as the cheapest real control.

**Mark anchor.** The **3-inch spill** as Dow's reference event, and **capital density** as one
of the five screening criteria for choosing a unit.

**Exam trap.** Inventory analysis is not a stock audit. The output is a hazard rating per unit,
not a stores list. A script that counts drums but never rates a unit has answered the wrong
question.

### 2.6 The Dow Fire and Explosion Index — what it is

*In plain English.* The Dow Index turns a process unit into a single number that says how much
fire and explosion damage it could do. You fill in a form, add up penalties, multiply, and read
a score. It began because the chemical industry's loss record in the 1960s was bad enough to
demand a scoreboard.

*The detail.*
- The method originated in **1966**, from a poor accident record in the chemical industry
  (`slide 26`).
- It was one of the first hazard analysis systems built for chemical plants (`slide 26`).
- Its selling point is that it puts damage in **money and days**, not adjectives (`slide 26`).
- The deck's own description of the paperwork is that you fill it out **like a tax form**
  (`slide 26`).
- Three verbs: **quantify** the damage, **identify** the equipment that can escalate, and
  **communicate** the potential to designers and operators (`slide 28`).
- The method needs engineering judgement and is not perfect (`slide 26`, `slide 27`).
- It is still upgraded and still used (`slide 26`).

**Five items are needed to build one** (`slide 33`) — this is the answer to Q12 and Q42.
1. An accurate plot plan, for an existing plant.
2. A preliminary plot plan, for a new plant.
3. A process flow sheet.
4. The F&EI hazard classification guide.
5. The F&EI form itself.

**Choosing the unit.** Not every vessel is analysed (`slide 34`). Screen on five things:
- The chemical energy potential, which becomes the material factor.
- The quantity of hazardous material in the unit.
- The capital density of the area.
- The process pressure and temperature.
- The past history of problems in that unit.

**The four numbers.** The index is a chain of multiplications (`slide 29`, `slide 45`).
- **Material Factor (MF)** measures flammability and reactivity, adjusted for flash point and
  boiling point (`slide 35`).
- **F1, general process hazards**, set the magnitude of a loss (`slide 40`).
- **F2, special process hazards**, set the probability of a loss (`slide 41`).
- **Unit hazard factor F3 = F1 × F2**, and **F&EI = MF × F3** (`slide 45`).

| F1 — general process hazards | F2 — special process hazards |
|---|---|
| Exothermic or endothermic reaction | Toxic material, at 0.2 × NH |
| Material handling and transfer | Sub-atmospheric pressure, 0.5 |
| Enclosed or indoor process unit | Dust explosion |
| Access | Operating in the flammable range |
| Drainage and spill control | Low-temperature operation |
| | Corrosion and erosion |
| | Leakage at joints and packing |
| | Rotating equipment |
| | Pressure penalty |
| | Quantity of flammable material |
| | Fired equipment |

**Loss control credits** are features that prevent a serious incident or shrink it, grouped as
process control, material isolation and fire protection (`slide 30`).

**Reading the score** (`slide 47`).

| F&EI | Degree of hazard |
|---|---|
| 1–60 | Light |
| 61–96 | Moderate |
| 97–127 | Intermediate |
| 128–158 | Heavy |
| 159+ | Severe |

*What to write (5 marks, Q93 and Q169).* Definition and origin in 1966. Then the three verbs, the MF × F1 × F2 structure, the hazard bands, and one line on the credits.

**Mark anchor.** **128 is the trigger for a more detailed PHA** (`slide 47`). That single number
is the most useful fact in the topic, because it links the index to the next chapter.

**Exam trap.** MF is not the NFPA rating. MF is a number from about 1 to 40 built from the
flammability rating NF and the reactivity rating NR, then adjusted. Quoting "MF = 3" from a
0-to-4 scale is the commonest error in the whole module.

### 2.7 The Dow calculation, step by step

*In plain English.* The calculation is a recipe with fifteen steps and no cleverness in it. Each
step produces a number that the next step needs. What earns marks is the order, and knowing what
each number means when you arrive at it.

*The detail.* The chain is fixed and runs in this order.
1. Select the pertinent process unit and state why.
2. Assign the material factor MF from the classification guide.
3. Add the F1 penalties for the general process hazards.
4. Add the F2 penalties for the special process hazards.
5. Compute **F3 = F1 × F2**.
6. Compute **F&EI = MF × F3** and read the hazard band.
7. Take the exposure radius from the empirical curve, then compute the area.
8. Treat the volume of exposure as a cylinder with height equal to radius (`slide 49`).
9. Value the equipment inside that volume at replacement cost.
10. Read the damage factor from the F3 and MF curves (`slide 50`).
11. **Base MPPD = value of exposure × damage factor** (`slide 51`).
12. **Actual MPPD = base MPPD × credit factor** (`slide 53`).
13. Read **MPDO** from the actual MPPD curve (`slide 54`).
14. **BI = MPDO × (lost profit per day + fixed cost per day)** (`slide 55`).
15. Act: cut the hazard first, add credits second, increase spacing third (`slide 57`).

**Worked example.** A solvent recovery unit, illustrative numbers throughout.
- Material factor **MF = 16**, a toluene-class flammable solvent.
- F1 penalties: exothermic 0.30, handling 0.50, enclosed 0.25, access 0.20, drainage 0.25.
- F1 = 1.00 + 1.50 = **2.50**.
- F2 penalties: toxic 0.40, flammable range 0.50, corrosion 0.20, leakage 0.30, rotating 0.50,
  pressure 0.30, quantity 0.40.
- F2 = 1.00 + 2.60 = **3.60**.
- F3 = 2.50 × 3.60 = **9.00**.
- F&EI = 16 × 9.00 = **144**, which is **Heavy** (128–158) and past the 128 trigger.
- Equipment value inside the exposure area is taken as ₹40 crore.
- Damage factor off the curve is 0.62, so base MPPD = 40 × 0.62 = **₹24.8 crore**.
- Credit factor 0.75, so actual MPPD = 24.8 × 0.75 = **₹18.6 crore**.
- MPDO is read as 60 days, and lost profit plus fixed cost is ₹12 lakh a day.
- BI = 60 × 12 lakh = **₹7.2 crore**, so the event costs about **₹25.8 crore** in total.

**What the result means.** The number is not a prediction. It is a ranking and a budget.
- It ranks this unit against every other unit on the same site.
- It sets the exposure radius, which decides plant layout and separation.
- It prices the loss in property damage and in days of production.
- It tells you where a credit is worth buying and where it is waste.
- The deck's own conclusion is that reducing the hazard early beats adding credits late
  (`slide 57`).

*What to write (8 marks, Q94).* The step list, then the worked chain, then three lines on what
the answer means. Show the arithmetic. An examiner cannot award method marks for an unshown
product.

**Mark anchor.** **F3 = F1 × F2 and F&EI = MF × F3.** Two multiplications carry the entire
method. Write them as equations, not as sentences.

**Exam trap.** The exposure radius comes from an empirical curve, and the deck gives **no
equation** (`slide 48`). Do not invent a formula with a constant in it. Say "from the empirical
curve" and move on to the damage factor.

### 2.8 Preliminary Hazard Analysis

*In plain English.* PHA is the first pass. Before there is a drawing, a small team sits down and
asks what could go wrong with this idea. It is cheap because it happens before anything is
built, and rough because nothing is designed yet.

*The detail.*
- PHA is usually the **first attempt** in the system safety process (`slide 59`).
- It is used in the **early stages of system design** (`slide 59`).
- It is **semi-quantitative**: it ranks hazards rather than measuring them (`slide 59`).
- It identifies potential hazards and the accidental events that could follow (`slide 59`).
- It ranks those events by severity and names the controls and follow-up actions (`slide 59`).
- It also travels under the names **Rapid Risk Ranking** and **HAZID** (`slide 59`).
- It leans on **brainstorming and expert judgement** (`slide 60`).
- One or two knowledgeable people usually carry it out (`slide 60`).
- It applies to any activity or system, at any level (`slide 60`).
- Its quality depends on documentation, leader training and team experience (`slide 60`).

**The four steps** (`slide 62`, `slide 63`).
1. **Prerequisites** — form the team, describe the system, collect risk information from similar
   systems.
2. **Hazard identification** — consider every part of the system and record every finding. The
   deck's rule is that no hazard is too insignificant to record (`slide 62`).
3. **Consequence and frequency estimation** — for each event, estimate how often and how bad.
4. **Risk ranking and follow-up** — place each event on a risk matrix and let the ranking set the
   action.

**Advantages** (`slide 61`): it helps ensure the system is safe; changes are cheaper and easier
early in design; it shortens design time by reducing surprises.
**Disadvantages** (`slide 61`): hazards must be foreseen by the analysts; interactions between
hazards are not easily recognised.

**Output.** A hazard register with severity ranking and recommendations, produced before the
P&ID exists.

*What to write (3 marks, Q53).* Definition, the early-design timing, the semi-quantitative
nature, and the four steps in one line each. For Q54, swap the last item for the two advantages
and two disadvantages.

**Mark anchor.** "**No hazards are too insignificant to be recorded**" (`slide 62`). Also worth
a mark: PHA is also called **HAZID** and **Rapid Risk Ranking**.

**Exam trap.** PHA is not a small HAZOP. HAZOP examines deviations from a defined design intent,
node by node. PHA has no design intent to deviate from yet, so it works from experience and
imagination instead.

### 2.9 HAZOP

*In plain English.* HAZOP assumes the plant is designed correctly. Then it asks a rude question about every pipe: what if this flow is more, or less, or backwards? The team walks
the plant line by line with a fixed list of rude questions, so nothing depends on somebody
having a bright idea that afternoon.

*The detail.*
- HAZOP is a **structured and systematic** technique for system examination and risk management
  (`slide 64`).
- It finds hazards and also **operability problems** that would spoil the product (`slide 64`).
- Its founding assumption: risk events come from **deviations from design intent** (`slide 64`).
- Deviations are generated with **guide words**, the method's unique feature (`slide 64`).
- A **node** is a section of the plant with stated boundaries and one stated design intent.
- The node is normally bounded by isolation points such as valves or flanges.
- A **deviation** is one guide word applied to one parameter. The pair is the unit of work.

| Guide word | Meaning | Example with flow |
|---|---|---|
| NO or NOT | None of the intent is achieved | No flow through the line |
| MORE | Quantitative increase | Higher flow than design |
| LESS | Quantitative decrease | Lower flow than design |
| AS WELL AS | Intent plus an extra component | Solvent plus water ingress |
| PART OF | Only some of the intent | Only one phase arrives |
| REVERSE | The opposite of the intent | Backflow into the feed tank |
| OTHER THAN | Something entirely different | Wrong chemical transferred |

- **Parameters** are the second axis: flow, pressure, temperature, level, composition, time, pH,
  sequence.
- Batch plant HAZOP adds **early**, **late**, **before** and **after** as guide words (standard).
- Not every cell of the matrix is credible. The deck says so explicitly (`slide 70`).
- Non-credible combinations do not need to be documented (`slide 70`).
- **Four phases** carry the study (`slide 65`).

1. **Definition** — pick a cross-functional team of subject specialists, fix the scope,
   boundaries, interfaces and assumptions (`slide 66`).
2. **Preparation** — gather data, identify the audience, schedule meetings, agree the recording
   template and the guide-word set (`slide 67`).
3. **Examination** — split the system into elements or steps, then apply the guide words to each
   element (`slide 69`, `slide 70`).
4. **Documentation and follow-up** — record on the IEC 61882 template; the deck names that
   standard (`slide 71`).

- Documentation then feeds **risk review** and **risk communication** (`slide 72`, `slide 73`).
- The team climate matters: positive thinking and frank discussion are named requirements
  (`slide 66`).

**A worked node.** Node one: the feed line from tank T-1 to reactor R-1.
Intent: transfer 5 m³/h of solvent at 2 bar and 30 °C.

| Guide word + parameter | Deviation | Cause | Consequence | Safeguard |
|---|---|---|---|---|
| NO + flow | Pump stops | Power loss, pump failure | Reactor starves, batch spoils | Low-flow alarm, standby pump |
| MORE + flow | Over-transfer | Valve stuck open, controller fail | Vessel overfills, spill, fire | High-level trip, bund |
| LESS + flow | Restricted flow | Blockage, cavitation | Poor mixing, hot spot | Flow indicator, strainer |
| MORE + temperature | Overheat | Cooling failure, runaway reaction | Pressure rise, relief lifts | High-temperature trip |
| AS WELL AS + composition | Water ingress | Leaking jacket | Corrosion, off-spec batch | Conductivity check, drain |
| REVERSE + flow | Backflow | Check valve fails | Contamination of feed tank | Non-return valve, interlock |
| OTHER THAN + composition | Wrong solvent | Coupling error at unloading | Wrong reaction, possible runaway | Keyed couplings, labelling |

**What results** (`Q65`). The study produces a document, not an opinion.
- A deviation table: node, guide word, cause, consequence, existing safeguard, risk rank.
- A recommendation for each unacceptable risk, with an owner and a date.
- A ranked action list, which is what management actually reads.
- Input to management of change, inspection plans, operating procedures and training.
- Evidence for the regulator that the risks were examined systematically.

*What to write (8 marks, Q128).* Theory in one line, then the four phases. Then the seven guide words, the matrix against parameters, one worked deviation, and the output table.

**Mark anchor.** **Seven guide words, and deviation = guide word × parameter.** Add IEC 61882 as
the documentation standard; it shows the method is a standard, not a habit.

**Exam trap.** "MORE" on its own is not a deviation. "MORE pressure" is. A script that lists
guide words without pairing each to a parameter has listed vocabulary, not a method.

### 2.10 Choosing between PHA and HAZOP

*In plain English.* PHA is a wide, shallow sweep early. HAZOP is a narrow, deep sweep late.
Neither replaces the other, and the exam question is almost always about which to reach for.

*The detail.*

| Point | PHA | HAZOP |
|---|---|---|
| Timing | Concept and early design | Detailed design and modification |
| Input needed | System description, experience | P&ID, design intent, node boundaries |
| Team | One or two knowledgeable people | Cross-functional specialists |
| Method | Brainstorm against a hazard list | Guide words applied to parameters |
| Output | Ranked hazard register | Deviation table with causes and safeguards |
| Coverage | Whole system, coarse | One node at a time, fine |
| Cost | Low | High, in engineer-hours |
| Best at | Novel systems with no drawings | Complex continuous processes |

- **Use PHA** when the design is still fluid and changes are cheap (`slide 61`).
- **Use HAZOP** when the P&ID is fixed and a deviation has real consequences (`slide 64`).
- **Use both** on a major project: PHA at concept, HAZOP at detailed design.
- **Dow F&EI at 128 or above** is the standard trigger for the detailed study (`slide 47`).
- **FMEA** suits equipment failures and single-component reliability (standard).
- **LOPA** follows HAZOP to check whether the safeguards are enough (standard).

**Industry examples.** A new paint shop gets a PHA at layout stage. A solvent recovery column
gets a HAZOP on its P&ID. A warehouse of packaged goods gets a PHA and a fire risk assessment.
A pharma reactor gets a HAZOP, then a LOPA on the exothermic reaction.

*What to write (8 marks, Q121).* The comparison table first, then two paragraphs on when each
wins, then two named industry examples. Finish with the sequencing rule: PHA early, HAZOP late,
both on anything large.

**Mark anchor.** **PHA is wide and shallow and early; HAZOP is narrow and deep and late.** The
sentence is the answer to the whole comparison.

**Exam trap.** Do not claim HAZOP is "more accurate". HAZOP is more *detailed*, and detail is
wasted on a design that will change next week. Timing, not accuracy, is the discriminator.

### 2.11 Chemical hazards and how they are classified

*In plain English.* A chemical can hurt you in three separate ways. It can burn you, poison you,
or catch fire. It can also damage the river rather than the worker. Classification systems exist
so that the same symbol means the same thing on a drum in Kochi and a drum in Rotterdam.

*The detail.*
- **Physical hazards** — flammable, explosive, oxidising, pyrophoric, self-reactive,
  water-reactive, compressed gas, organic peroxide (standard).
- **Health hazards** — toxic, harmful, corrosive, irritant, sensitising, carcinogenic,
  mutagenic, toxic to reproduction (standard).
- **Environmental hazards** — toxic to aquatic life, harmful to the ozone layer (standard).
- **Asphyxiants** replace oxygen without being toxic themselves (standard).
- The **GHS** is the Globally Harmonised System for classifying and labelling chemicals
  (standard).
- GHS uses **nine hazard pictograms**, a red diamond border, and two signal words (standard).
- The signal words are **DANGER**, for the more severe, and **WARNING** (standard).
- Indian industry meets GHS through the **MSIHC Rules, 1989** and the Factories Act (standard).

| Pictogram | Means | Typical substance |
|---|---|---|
| Flame | Flammable | Petrol, acetone |
| Flame over circle | Oxidiser | Nitric acid, peroxides |
| Exploding bomb | Explosive, self-reactive | Ammonium nitrate |
| Gas cylinder | Compressed gas | LPG, oxygen |
| Corrosion | Burns skin, attacks metal | Sulphuric acid, caustic soda |
| Skull and crossbones | Acute toxicity | Cyanide salts |
| Health hazard | Chronic disease, cancer | Benzene, silica |
| Exclamation mark | Irritant, harmful, sensitising | Kerosene, resin |
| Environment | Aquatic toxicity | Chlorinated solvent |

**Routes of entry.** A chemical hazard reaches the body by four roads, and the road decides the
PPE (standard).
- **Inhalation** — the fastest route in industry, because the lung has a huge surface and no
  barrier worth the name.
- **Skin absorption** — solvents and pesticides pass through intact skin, so gloves matter as
  much as respirators.
- **Ingestion** — from hands, food and cigarettes at the workbench.
- **Injection** — from high-pressure leaks and sharps, rare but severe.
- **Target organs** follow the chemical: solvents attack the nervous system and liver, metals the
  kidney and nerve, dusts the lung.

*What to write (3 marks, Q57 and Q63).* For Q57, the three groups with two examples each. For
Q63, name the nine pictograms and give one substance per pictogram.

**Mark anchor.** **Nine GHS pictograms and two signal words.** The count is checkable, and an
examiner can mark it in two seconds.

**Exam trap.** The skull and crossbones is *acute* toxicity. The "health hazard" pictogram with
the chest is *chronic* harm, including cancer. Swapping them is a wrong answer, not a slip.

### 2.12 Controlling chemical hazards

*In plain English.* The best way to stop a chemical reaching a worker is to not have the chemical.
The second best is to keep it inside a box. Everything after that depends on people behaving
correctly, which is why the order is not a matter of taste.

*The detail.*
- Controlling exposure is the fundamental method of protecting workers (`slide 84`).
- The deck uses a **hierarchy of controls** to choose between options (`slide 84`).
- **Elimination or substitution** is the most desirable (`slide 84`).
- **Engineering controls** come next, and must be the primary means (`slide 84`).
- **Administrative and work-practice controls** suit cases engineering cannot reach (`slide 84`).
- **PPE is the least desirable but may still be effective** (`slide 84`).
- Respirators are required when engineering controls are infeasible, or while they are being
  installed (`slide 84`).
- Engineering options: enclosure, closed transfer, local exhaust ventilation, general
  ventilation, scrubbers, gas detection, deluge (standard).
- Administrative options: job rotation, exposure time limits, permits, training, housekeeping,
  health surveillance (standard).
- Emergency options: spill kit, eye wash, safety shower, evacuation alarm, on-site plan.

**Indian legal frame.** Bhopal in 1984 produced Chapter IV-A of the Factories Act, inserted in
1987 (standard).
- Section 41B requires the occupier to disclose information on the hazardous processes
  listed in the First Schedule (standard).
- Section 41G requires a safety committee for factories in the hazardous list (standard).
- The MSIHC Rules, 1989, cover manufacture, storage and import of hazardous chemicals (standard).
- The Chemical Accidents Rules, 1996, require on-site and off-site emergency plans (standard).
- The Factories Act also requires disclosure of information to workers (standard).

**What to write (8 marks, Q58).** Draw the hierarchy, then take three rungs and give one concrete
measure for each. Close with the Indian statute that compels the control.

**Mark anchor.** "Engineering and work-practice controls must be the primary means; PPE is the
least desirable **but may still be effective**" (`slide 84`). The second half stops you sounding
as though PPE is forbidden.

**Exam trap.** PPE is not "the easy option that works". It protects one wearer, only while it
fits and is worn correctly, and it fails silently. A leaking respirator seal looks exactly like
a good one.

### 2.13 Hazardous properties of chemicals

*In plain English.* A safety data sheet answers a short list of physical questions. How easily
does it catch fire? How heavy is the vapour? How low can the air be before it will not burn? The
answers decide where you store it and what you do when it leaks.

*The detail.* The deck's properties slide is a heading with no table under it (`slide 86`), so
every value below is **(standard)**.
- **Flash point** — lowest temperature at which a liquid gives off ignitable vapour.
- **Fire point** — the temperature at which the vapour keeps burning once lit.
- **Autoignition temperature** — the temperature at which it ignites without a spark.
- **Vapour density** — weight of the vapour relative to air. Above 1, it sinks.
- **Vapour pressure** — how readily a liquid evaporates at a given temperature.
- **Boiling point** — sets how fast a spilled liquid produces vapour.
- **LFL and UFL** — the lean and rich limits of flammability in air.
- **Specific gravity** — decides whether a spilled liquid floats on water.
- **pH** — below 2 or above 12.5 signals a corrosive (standard).
- **LD50** — the dose killing 50 per cent of test animals, the standard acute toxicity figure.
- **Dust explosivity** — measured as Kst, which sizes a dust explosion hazard (standard).

| Substance | Flash point | Vapour density | Flammable range |
|---|---|---|---|
| Petrol | −43 °C | About 3 to 4 | 1.4 to 7.6 per cent |
| Kerosene | 38 to 74 °C | About 5 | 0.7 to 5 per cent |
| Diesel | 52 to 96 °C | About 5 | 0.6 to 6.5 per cent |
| Methane | Gas | 0.55, rises | 5 to 15 per cent |
| Hydrogen | Gas | 0.07, rises fast | 4 to 75 per cent |
| Carbon monoxide | Gas | 0.97, mixes | 12.5 to 74 per cent |

**Indian classification of petroleum** follows flash point (standard).
- **Class A** — flash point below 23 °C. Petrol and solvents.
- **Class B** — flash point from 23 °C to 65 °C. Kerosene and high-speed diesel.
- **Class C** — flash point from 65 °C to 93 °C. Heavy fuel oils.

**How the three headline properties hurt the environment.**
- **Toxicity** kills beyond the fence. A release reaches water, soil and the food chain.
- **Flammability** turns a spill into a fire, and the smoke carries the toxin downwind.
- **Reactivity** makes the release unpredictable: heat, gas, or a runaway in a stored drum.
- A substance that is toxic *and* flammable gives the responder no safe approach.
- A substance that reacts with water cannot be fought with the obvious extinguisher.

*What to write (5 marks, Q59).* Define the three properties, give one number for each, then one
consequence each for worker, plant and environment. Close on the combined case.

**Mark anchor.** **Flash point below 23 °C is Class A petroleum; the bands break at 23, 65 and
93 °C.** Indian-specific numbers beat generic ones in an Indian paper.

**Exam trap.** Flash point and autoignition temperature are different numbers with different
meanings. Petrol has a flash point well below zero and an autoignition temperature around
250 °C. Confusing them suggests you have memorised a word, not a property.

### 2.14 Material Safety Data Sheets

*In plain English.* An MSDS is the instruction sheet that comes with a hazardous chemical. It
tells the worker what the stuff does, how to handle it, what to wear, and what to do when it
spills or catches fire. If it is missing, the risk assessment for that area is guesswork.

*The detail.*
- **Definition** — a document supplied by the manufacturer that states the properties, hazards,
  safe handling, emergency action and disposal for a chemical product.
- The modern format has **16 sections**, fixed by GHS and ISO 11014 (standard).
- The order matters, because a responder reads section 5 while the fire is burning.

| Section | Content |
|---|---|
| 1 | Identification of the substance and supplier |
| 2 | Hazard identification, including GHS pictograms and signal word |
| 3 | Composition and ingredient information |
| 4 | First-aid measures |
| 5 | Firefighting measures |
| 6 | Accidental release measures |
| 7 | Handling and storage |
| 8 | Exposure controls and personal protection |
| 9 | Physical and chemical properties |
| 10 | Stability and reactivity |
| 11 | Toxicological information |
| 12 | Ecological information |
| 13 | Disposal considerations |
| 14 | Transport information |
| 15 | Regulatory information |
| 16 | Other information, including revision date |

- **Section 8** is the one supervisors actually use, because it names the PPE.
- **Section 9** carries flash point, boiling point and vapour pressure.
- **Section 2** must match the label on the drum exactly (standard).
- The sheet must be **accessible at the point of use**, not locked in an office (standard).
- It must be in a language the workers read (standard).
- It must be **current**: check the revision date in section 16.
- Training must cover the sheet, or its presence is decoration.

*What to write (3 marks, Q56).* Definition, purpose in one line, the 16-section structure named,
and the accessibility and training requirement. For 5 marks, add the table of the sections a
supervisor uses most.

**Mark anchor.** **16 sections**, with section 8 for exposure controls and PPE and section 9 for
physical properties. The count proves you have seen a real sheet.

**Exam trap.** An MSDS is not a label. The label carries six elements: identifier, pictograms,
signal word, hazard statements, precautionary statements and supplier. The sheet is the long
document behind the label.

---

## 3. Answer bank

### 3.1 Three-mark answers

**A — Hazard and risk (Q7).**
1. **Hazard** — a source with the potential to cause injury or ill health.
2. **Risk** — the combination of the likelihood of harm and its severity.
3. **Contrast** — the hazard is inherent in the agent; the risk depends on exposure.

**B — Types of hazards (Q8).**
1. **Physical** — noise, heat, radiation, pressure; deafness, heat stress, burns.
2. **Mechanical** — unguarded machinery, falling loads; cut, crush, fracture.
3. **Chemical** — solvents, acids, dusts; burns, poisoning, fire.
4. **Add** — biological, ergonomic, psychosocial, and fire and explosion.

**C — Types of fire hazards (Q9).**
1. **By fuel class** — A solids, B liquids, C gases, D metals, E electrical.
2. **By outcome** — fire, explosion, toxic gas release from the same inventory.
3. **By mechanism** — pool fire, jet fire, flash fire, vapour cloud explosion, BLEVE.

**D — What a fire extinguisher is (Q10).**
1. **Definition** — a portable pressurised device that discharges an agent onto a small fire.
2. **Principle** — it removes one side of the fire tetrahedron.
3. **Limit** — first-aid only; it is not a substitute for fixed protection or evacuation.

**E — Before installing an extinguisher (Q11).**
1. **Class match** — the agent must suit the fuel in that room.
2. **Siting** — visible, signed, unobstructed, handle about 1.5 m up, travel under 15 m.
3. **Conditions** — temperature range, corrosion, and a valid service tag; staff trained.

**F — Items needed for the Dow F&EI (Q12, Q42).**
1. **Plans** — an accurate plot plan for an existing plant, or a preliminary one for a new plant.
2. **Process** — the process flow sheet.
3. **Reference** — the F&EI hazard classification guide and the F&EI form.

**G — Objectives of a HAZOP (Q51).**
1. **Find hazards** — identify hazards arising from deviations from the design intent.
2. **Find operability problems** — catch the deviations that spoil product or stop the plant.
3. **Decide** — rank each deviation and recommend safeguards with owners.

**H — Steps in a HAZOP (Q52).**
1. **Define** — team, scope, boundaries, interfaces and assumptions.
2. **Prepare** — data, schedule, recording template, agreed guide words.
3. **Examine** — nodes, then guide word against parameter, then record credible deviations.
4. **Follow up** — document on the IEC 61882 template and track actions to closure.

**I — Objectives of a PHA (Q53).**
1. **Identify** — all potential hazards and the accidental events that could follow.
2. **Rank** — order those events by severity using a risk matrix.
3. **Control** — name the required controls and the follow-up actions, early in design.

**J — Hazards considered in a PHA (Q55).**
1. **Energy** — fire, explosion, pressure, electrical, stored mechanical energy.
2. **Materials** — toxic, corrosive, flammable and reactive substances.
3. **People and place** — ergonomic, access, environmental and interface hazards.

**K — MSDS, definition and purpose (Q56).**
1. **Definition** — a manufacturer's document on a chemical's properties, hazards and safe use.
2. **Purpose** — it feeds the risk assessment, the PPE choice and the emergency plan.
3. **Form** — 16 sections under GHS; kept accessible at the point of use and trained on.

**L — Types of chemical hazards (Q57).**
1. **Physical** — flammable, explosive, oxidising, pyrophoric, compressed gas.
2. **Health** — toxic, corrosive, irritant, sensitising, carcinogenic, mutagenic.
3. **Environmental** — aquatic toxicity, ozone depletion; plus asphyxiants.

**M — Three control measures in a plant (Q62).**
1. **Substitution** — replace the solvent or process with a less hazardous one.
2. **Engineering** — enclose the transfer and extract at source with local exhaust.
3. **Administrative and PPE** — rotation, permits, training, then gloves and respirators.

**N — GHS hazard symbols (Q63).**
1. **Physical** — flame, flame over circle, exploding bomb, gas cylinder.
2. **Health** — corrosion, skull and crossbones, health hazard, exclamation mark.
3. **Environment** — the dead tree and fish; with the signal words DANGER and WARNING.

**O — Importance of HAZOP (Q64).**
1. **Systematic** — it finds deviations that experience alone would miss.
2. **Documented** — it leaves a traceable record for the regulator and for change control.
3. **Cheap** — a study costs far less than the modification it prevents.

**P — Classification of fires (Q90).**
1. **A** — solids such as wood and paper; extinguish by cooling with water.
2. **B** — flammable liquids such as petrol; smother with foam, CO₂ or powder.
3. **C, D, E** — gases, combustible metals, live electrical equipment.

**Q — Four risk assessment tools (Q92).**
1. **PHA** — early, coarse, ranked hazard list for a new system.
2. **HAZOP** — node-by-node deviation study on a detailed design.
3. **FMEA** — component failure modes and their effects.
4. **LOPA or QRA** — layer counting, or full frequency and consequence modelling.

**R — Dow F&EI and its objectives (Q93, Q169).**
1. **Definition** — an index that rates a process unit's fire and explosion hazard from 1 upward.
2. **Quantify** — express damage as property loss in money and outage in days.
3. **Aim** — identify escalating equipment, compare layout options, and communicate risk.

**S — Role of government in safety (Q115).**
1. **Legislate** — the Factories Act, MSIHC Rules and state factory rules set duties.
2. **Enforce** — the factory inspectorate inspects, prohibits and prosecutes.
3. **Support** — DGFASLI, the National Safety Council and ISI standards guide industry.

**T — Need for a safety committee (Q119).**
1. **Legal** — Section 41G of the Factories Act requires one in hazardous factories.
2. **Tripartite** — management, supervisors and workers meet and agree actions.
3. **Effect** — it reviews incidents, inspections and training, and gives workers a voice.

**U — Role of PHA in modern safety management (Q122a).**
1. **Early** — it is the first structured look, taken while design changes are still cheap.
2. **Ranking** — it sorts hazards by severity so money goes to the worst first.
3. **Record** — it creates the hazard register that later studies build on.

**V — Lifting and carrying (Q131).**
1. **Assess** — check the weight, the route and the grip before lifting.
2. **Posture** — feet apart, back straight, load close, lift with the legs, no twisting.
3. **Limit** — use a trolley or two people above the safe manual limit.

**W — Pulling and pushing (Q132).**
1. **Push, do not pull** — pushing keeps the load visible and the spine in compression.
2. **Height** — hands between hip and shoulder, body weight doing the work.
3. **Surface** — good floor, good wheels, and no slope or threshold on the route.

### 3.2 Five-mark answers

**A — Advantages and disadvantages of PHA (Q54).**
1. **Advantage, safety** — it helps ensure the system is safe before it is built (`slide 61`).
2. **Advantage, cost** — modifications are cheaper and easier in the earlier design stages.
3. **Advantage, schedule** — it shortens design time by reducing the number of surprises.
4. **Disadvantage, imagination** — hazards must be foreseen by the analysts.
5. **Disadvantage, interaction** — the effects of interactions between hazards are not easily
   recognised. Add that quality depends on documentation and team experience (`slide 60`).

**B — Results of a HAZOP study (Q65).**
1. **The table** — node, guide word, deviation, cause, consequence, safeguard, risk rank.
2. **The recommendations** — one per unacceptable risk, with an owner and a due date.
3. **The ranking** — actions ordered so the worst deviations are fixed first.
4. **The record** — documentation on the IEC 61882 template, retained for audit.
5. **The follow-on** — input to change control, inspection, procedures and training.

**C — Types of fire extinguishers (Q91).**
1. **Water** — Class A only; cooling; freezes, so cold sites need antifreeze (`slide 18`).
2. **Water mist** — distilled water as a fog, for museums, operating rooms and book stores.
3. **CO₂** — Classes B and C, no residue, poor in wind, risky in confined spaces (`slide 19`).
4. **Foam and dry powder** — foam blankets liquids; ABC powder covers A, B, C and E.
5. **Special agents** — wet chemical for cooking oil, dry powder or sand for metals.

**D — Dow hazard factors (Q106).**
1. **Material factor** — flammability and reactivity, adjusted for flash and boiling point.
2. **F1 general** — reaction, handling and transfer, enclosure, access, drainage.
3. **F2 special** — toxicity at 0.2 × NH, sub-atmospheric 0.5, dust, flammable range, pressure.
4. **F2 continued** — low temperature, corrosion, leakage, rotating equipment, quantity, fired
   heaters.
5. **Combination** — F3 = F1 × F2, then F&EI = MF × F3, then read the hazard band.

**E — Dow flow chart (Q105).** Draw the chain and label each box.
1. Select unit → assign MF → add F1 penalties → add F2 penalties.
2. F3 = F1 × F2 → F&EI = MF × F3 → hazard band.
3. Exposure radius → area → value of equipment → damage factor → base MPPD.
4. Credit factor → actual MPPD → MPDO → business interruption.
5. Report: property damage in money, outage in days, and the ranked list of ways to cut it.

**F — Hazard factors contributing to the index (Q106, extended).**
1. **Material** — the chemical energy potential of what is inside the unit.
2. **General** — how the process is run and laid out: reaction, transfer, enclosure, access,
   drainage.
3. **Special** — what makes loss likely: toxicity, pressure, vacuum, corrosion, leakage, rotating
   equipment.
4. **Quantity** — the mass of flammable or unstable material, with separate curves for process,
   storage and solids (`slide 43`).
5. **Fired equipment** — heaters and furnaces, on curve A-1 above flash point or A-2 above
   boiling point (`slide 44`).

**G — HAZOP steps in detail (Q128).**
1. **Definition** — cross-functional team of specialists, scope, boundaries, interfaces,
   assumptions, and a climate of frank discussion (`slide 66`).
2. **Preparation** — supporting data, audience, meeting schedule, recording template, agreed
   guide words (`slide 67`).
3. **Examination** — split into elements, apply guide words, discard non-credible combinations
   without documenting them (`slide 69`, `slide 70`).
4. **Documentation** — record on the IEC 61882 form, modified for company policy and audit needs
   (`slide 71`).
5. **Review and communicate** — check the controls still work, watch for new risks created by the
   controls, and report at the right level for each audience (`slide 72`, `slide 73`).

**H — Control measures for chemical hazards (Q126).**
1. **Eliminate or substitute** — the most desirable option, and the only one that removes the
   hazard (`slide 84`).
2. **Engineer** — enclosure, closed transfer, local exhaust ventilation, scrubber, gas detection.
3. **Administer** — rotation, exposure time limits, permit to work, training, housekeeping.
4. **Protect** — respirators, gloves, goggles, aprons; the least desirable but still effective.
5. **Prepare** — spill kit, eyewash, shower, alarm, on-site emergency plan under the 1996 Rules.

**I — Toxicity, flammability, reactivity and environmental safety (Q59, Q124).**
1. **Toxicity** — kills beyond the fence; a release enters water, soil and the food chain.
2. **Flammability** — turns a spill into a fire, and the smoke carries the toxin downwind.
3. **Reactivity** — makes the release unpredictable: heat, gas, polymerisation or runaway.
4. **Combination** — toxic and flammable together leaves the responder no safe approach.
5. **Consequence** — the properties decide storage segregation, separation distance and the
   emergency plan.

**J — Role of PPE in controlling chemical hazards (Q60).**
1. **Place** — last in the hierarchy, because it protects one wearer and depends on fit.
2. **Selection** — by the chemical's own data: gloves by polymer and permeation, not by colour.
3. **Respiratory** — air-purifying for known contaminants with enough oxygen; SCBA otherwise.
4. **Limits** — no PPE is safe in an oxygen-deficient or immediately dangerous atmosphere.
5. **Support** — fit testing, training, cleaning, storage and replacement schedules.

**K — Identify the fire class and pick the extinguisher (Q170).**
1. **Look at the fuel** — solid, liquid, gas, metal or live electrical equipment.
2. **Solid** — Class A, water or foam.
3. **Liquid** — Class B, foam, CO₂ or dry powder; never water.
4. **Gas** — Class C, shut the supply off first, then cool and smother.
5. **Electrical** — Class E, isolate the supply, then CO₂ or clean agent.

**L — How handling aids cut injury (Q165).**
1. **Load** — a trolley or pallet truck removes the lift entirely.
2. **Reach** — vacuum lifters and hoists keep the load inside the safe zone.
3. **Distance** — conveyors and roller tracks remove carrying and turning.
4. **Repetition** — balancers and spring arms cut the number of lifts per shift.
5. **Result** — the aid removes the force, so the injury mechanism disappears rather than being
   tolerated.

**M — Implementation criteria and plans (Q122b).**
1. **Criteria** — set the risk level above which action is compulsory, using the matrix.
2. **Owner** — one named person per action, with authority and a budget.
3. **Date** — a completion date, and a review date for the residual risk.
4. **Verification** — the evidence that proves the control works, such as a test record.
5. **Plan** — fold the actions into the maintenance, training and capital plans, then re-audit.

### 3.3 Eight-mark answers

#### A — Steps to calculate the Dow F&EI (Q94)
**Structure (8):** the input list (1), the five-step factor build (3), the consequence chain (3),
what the answer means (1). Show arithmetic on every line.

**Answer**
- **Inputs** (`slide 33`): plot plan, flow sheet, classification guide, F&EI form.
- **Unit** (`slide 34`): screen on chemical energy, quantity, capital density, pressure and
  temperature, and past history.
- **MF** (`slide 35`): flammability and reactivity, adjusted for flash point and boiling point.
- **F1** (`slide 40`): exothermic reaction, handling and transfer, enclosure, access, drainage.
- **F2** (`slide 41`): toxic at 0.2 × NH, vacuum at 0.5, dust, flammable range, pressure,
  low temperature, corrosion, leakage, rotating equipment, quantity, fired heaters.
- **F3 and F&EI** (`slide 45`): F3 = F1 × F2 and F&EI = MF × F3. Worked: 2.50 × 3.60 = 9.00,
  then 16 × 9.00 = 144, which is Heavy.
- **Consequence** (`slide 48` to `slide 55`): radius from the curve, area, cylinder volume,
  equipment value, damage factor, base MPPD, credit factor, actual MPPD, MPDO, BI.
- **Meaning** (`slide 57`): reduce the hazard first, add credits second, increase spacing third.
**Traps:** (1) Do not skip the credits — they turn base MPPD into actual MPPD, and an answer
without them stops halfway. (2) Do not invent a radius formula; the deck gives a curve, not an
equation.

#### B — PHA compared with HAZOP, and when to choose each (Q121, Q171)
**Structure (8):** definitions (2), comparison table (3), when to choose (2), industry examples
(1).

**Answer**
- **PHA** — first structured look, early design, semi-quantitative, ranked hazard list, also
  called HAZID (`slide 59`). Four steps: prerequisites, identification, consequence and
  frequency, ranking and follow-up (`slide 62`).
- **HAZOP** — structured examination of deviations from design intent, node by node, using guide
  words (`slide 64`). Four phases: definition, preparation, examination, documentation (`slide
  65`).
- **Table** — timing, input, team, method, output, coverage, cost (see §2.10).
- **Choose PHA** — fluid design, novel system, no P&ID yet, or a whole-site first sweep.
- **Choose HAZOP** — fixed P&ID, continuous process, hazardous inventory, or a modification.
- **Sequence both** — PHA at concept, HAZOP at detailed design, LOPA after HAZOP.
- **Examples** — PHA for a new paint shop layout; HAZOP for a solvent recovery column; PHA for a
  warehouse; HAZOP then LOPA for an exothermic reactor.
**Traps:** (1) HAZOP is more detailed, not more accurate — do not claim it as the "better" method.
(2) PHA without the ranking step is only a hazard list, and it loses half the marks.

#### C — Control measures for chemical hazards (Q58, Q123, Q127, Q172)
**Structure (8):** hierarchy in order (3), three rungs developed (3), Indian law and emergency
preparedness (2).

**Answer**
- **Hierarchy** — elimination, substitution, engineering, administrative, PPE (`slide 84`).
- **Substitution** — water-based paint for solvent paint; a less toxic solvent in extraction.
- **Engineering** — enclosure, closed transfer, local exhaust ventilation, scrubber, gas
  detection and alarm, deluge, bunding.
- **Administrative** — rotation, exposure time limits, permit to work, training, housekeeping,
  health surveillance, exposure monitoring.
- **PPE** — gloves by polymer, respirators with fit testing, goggles, aprons; last and least
  reliable.
- **Law** — Chapter IV-A of the Factories Act, 1987, after Bhopal; MSIHC Rules 1989; Chemical
  Accidents Rules 1996 for on-site and off-site plans.
- **Emergency** — spill kit, eyewash, shower, evacuation alarm, mutual aid.
**Traps:** (1) Do not open with PPE. (2) Do not offer "training" as the answer to a design
problem — it belongs on the fourth rung, and the examiner knows it.

#### D — Administrative controls versus PPE, Indian automotive plant (Q61)
**Structure (8):** the comparison (3), the Indian context (2), the verdict with reasons (2), one
closing recommendation (1).

**Answer**
- **Administrative controls** change how the work is organised: rotation, time limits, permits,
  training, procedures, monitoring.
- **PPE** puts a barrier on the worker: gloves, respirators, goggles, aprons.
- **Effectiveness** — administrative controls cut exposure for the whole shift; PPE protects one
  wearer while it is worn correctly.
- **Failure mode** — an administrative control fails visibly; a PPE barrier fails silently.
- **Cost** — PPE is cheap to buy and expensive to sustain, through fit testing and replacement.
- **Indian context** — paint shops, foundries and battery plants run Chapter IV-A duties, MSIHC
  thresholds and Factories Act disclosure obligations.
- **Verdict** — administrative controls first, PPE to close the residual gap, never as the plan.
- **Recommendation** — enclose the paint booth and extract at source, then use PPE for the tasks
  that remain.
**Traps:** (1) The question asks for a comparison, not two lists — give the criterion for each
row. (2) Contract labour and shift work are the Indian specifics worth naming.

#### E — Fire safety plan from the fire classification (Q168)
**Structure (8):** survey the fuels (2), map the classes to zones (2), place the equipment (3),
support with training and maintenance (1).

**Answer**
- **Survey** — walk the plant and list every fuel by class, room by room.
- **Class A zones** — stores, packing, offices: water or ABC powder, one per 100 m² (standard).
- **Class B zones** — solvent store, paint shop, fuel point: foam or CO₂, with bunding and
  drainage.
- **Class C zones** — LPG bank, acetylene: isolation valves, gas detection, dry powder.
- **Class D zones** — magnesium or aluminium powder: dry sand or special powder, never water.
- **Class E zones** — MCC rooms, panels: CO₂ or clean agent, and no water units at all.
- **Placement** — visible, signed, unobstructed, travel under 15 m, handle about 1.5 m up.
- **Support** — monthly checks, annual refill, drills, and a named person per zone.
**Traps:** (1) The plan follows the fuel, not the floor plan symmetry. (2) Do not put a water
unit in a switch room because the corridor is convenient.

#### F — Fourteen PPE with a figure (Q145)
**Structure (8):** a labelled worker sketch (3), the list grouped head to foot (4), one line on
selection (1).

**Answer**
- **Head and face** — safety helmet, safety goggles, face shield, welding helmet.
- **Ears** — ear plugs, ear muffs.
- **Respiratory** — filtering half mask, full-face respirator, SCBA.
- **Hands and arms** — leather gloves, chemical gloves, arm sleeve.
- **Body** — coverall or apron, high-visibility vest, full-body harness.
- **Feet** — safety shoes, gum boots.
- **Figure** — one worker outline, labels on leaders, numbered 1 to 17 down one side. The question asks for at least fourteen.
- **Selection** — by the hazard, not by availability: a glove is chosen by polymer and permeation
  data.
**Traps:** (1) Fourteen is a minimum and a count, so number every label on the figure. (2) A
harness is fall protection, not general PPE; say so in the label.

### 3.4 Fourteen-mark skeleton (ESE Part B)

**Likely shape.** Either "explain the Dow Fire and Explosion Index and calculate it for a given
unit" or "explain PHA and HAZOP and compare them". Prepare both; they share the first page.

**Paragraph plan — the Dow version**
1. **Purpose (2)** — 1966 origin, one of the first chemical plant systems, quantify, identify,
   communicate; damage in money and days (`slide 26`, `slide 28`). *One third of a page.*
2. **Inputs and unit selection (2)** — the five items (`slide 33`), the five screening criteria
   (`slide 34`), and why not every vessel is analysed.
3. **The factors (3)** — MF from NF and NR; F1 with its five penalties; F2 with its eleven;
   F3 = F1 × F2; F&EI = MF × F3. **Draw the flow chart here** (§5). *Half a page.*
4. **Worked calculation (4)** — the fifteen-step chain with numbers. MF 16, F1 2.50, F2 3.60, F3 9.00, F&EI 144, Heavy, past the 128 trigger. Then MPPD, credits, MPDO and BI.
5. **Interpretation (2)** — hazard bands, exposure radius, layout and separation, and the deck's
   order of remedy: reduce hazard, add credits, increase spacing (`slide 57`).
6. **Limits (1)** — needs engineering judgement, is not perfect, is not a substitute for HAZOP on
   a detailed design (`slide 27`).

**Paragraph plan — the HAZOP version**
1. **Definition and theory (2)** — deviations from design intent; structured and systematic; also
   finds operability problems (`slide 64`).
2. **Team and phases (3)** — cross-functional specialists, frank discussion; definition,
   preparation, examination, documentation (`slide 66` to `slide 71`). **Draw the node schematic**
   (§5).
3. **Nodes and guide words (3)** — node boundaries at isolation points; the seven guide words;
   the parameter axis; deviation = guide word × parameter. Give the worked node table (§2.9).
4. **Results (3)** — cause, consequence, safeguard, risk rank, recommendation, owner, date;
   IEC 61882 documentation; review and communication (`slide 72`, `slide 73`).
5. **PHA contrast (2)** — early, coarse, ranked; the four steps; when each wins (§2.10).
6. **Closing (1)** — HAZOP is expensive per node and cheap per prevented modification.

---

## 4. Definitions and numbers

### 4.1 The table to memorise

| Term or number | Exact value or definition | Used in |
|---|---|---|
| Hazard | A source with the potential to cause injury or ill health | Q7, any 14-mark opener |
| Risk | The combination of likelihood of harm and its severity | Q7 |
| Fire tetrahedron | Fuel, oxygen, heat, chain reaction | Q9, Q90, Q170 |
| Fire classes | A solids, B liquids, C gases, D metals, E electrical (Indian scheme) | Q9, Q90, Q168, Q170 |
| Water | Class A only; freezes, so antifreeze is used (`slide 18`) | Q91 |
| CO₂ | Classes B and C; no residue; poor in wind; asphyxiation risk (`slide 19`) | Q91, Q170 |
| Water mist | Distilled water as fog; operating rooms, museums, book collections (`slide 18`) | Q91 |
| Extinguisher siting | One water unit per 100 m², travel under 15 m **(standard; deck silent)** | Q11, Q168 |
| Dow origin | **1966**, from a poor accident record (`slide 26`) | Q93, Q169 |
| Dow inputs | Plot plan, flow sheet, classification guide, F&EI form (`slide 33`) | Q12, Q42 |
| Material factor | Flammability NF plus reactivity NR, adjusted for flash and boiling point | Q106 |
| F1 penalties | 5 groups: reaction, handling, enclosure, access, drainage (`slide 40`) | Q106 |
| F2 penalties | 11 groups, incl. toxic at **0.2 × NH** and vacuum at **0.5** (`slide 41`) | Q106 |
| F3 | F1 × F2 (`slide 45`) | Q94 |
| F&EI | MF × F3 (`slide 45`) | Q94, Q105 |
| Hazard bands | 1–60 light, 61–96 moderate, 97–127 intermediate, 128–158 heavy, 159+ severe (`slide 47`) | Q93, Q169 |
| PHA trigger | **128** is the trigger for a more detailed PHA (`slide 47`) | Q94, Q121 |
| Exposure radius | Empirical curve; deck gives **no equation**, only the 3-inch spill basis (`slide 48`) | Q94 |
| Volume of exposure | Cylinder with height equal to radius (`slide 49`) | Q94 |
| Base MPPD | Value of exposure area × damage factor (`slide 51`) | Q94 |
| Actual MPPD | Base MPPD × credit factor (`slide 53`) | Q94 |
| MPDO | Days to rebuild the plant to original capacity (`slide 31`, `slide 54`) | Q94 |
| Business interruption | MPDO × (lost profit per day + fixed cost per day) (`slide 55`) | Q94 |
| Credits | Process control, material isolation, fire protection (`slide 30`) | Q94 |
| PHA alias | Rapid Risk Ranking, HAZID (`slide 59`) | Q53, Q121 |
| PHA steps | Prerequisites, identification, consequence and frequency, ranking (`slide 62`) | Q53, Q122 |
| PHA rule | No hazards are too insignificant to be recorded (`slide 62`) | Q55 |
| HAZOP basis | Risk events come from deviations from design intent (`slide 64`) | Q51, Q128 |
| Guide words | NO, MORE, LESS, AS WELL AS, PART OF, REVERSE, OTHER THAN (`slide 68`) | Q52, Q128 |
| HAZOP standard | IEC 61882 recording template (`slide 71`) | Q65 |
| HAZOP phases | Definition, preparation, examination, documentation (`slide 65`) | Q52, Q128 |
| GHS pictograms | Nine, with signal words DANGER and WARNING **(standard)** | Q63 |
| MSDS | 16 sections; section 8 PPE, section 9 physical properties **(standard)** | Q56 |
| Petroleum classes | A below 23 °C, B 23–65 °C, C 65–93 °C **(standard)** | Q59, Q124 |
| Control hierarchy | Elimination, substitution, engineering, administrative, PPE (`slide 84`) | Q58, Q61, Q122 |

The deck gives **no numerical values** for flash point, vapour density, flammable range, Dow
penalty magnitudes, damage factors or exposure radius. Every number in that list above is marked
standard, and any script that offers a Dow penalty value should say it comes from the workbook
table.

---

## 5. Diagrams to draw

### 5.1 The six figures

| Figure | Where | What to draw |
|---|---|---|
| Fire tetrahedron | §2.3, Q9, Q90 | Four-sided shape: fuel, oxygen, heat, chain reaction. Four arrows out labelled water, foam, isolation, dry powder. |
| Dow flow chart | §2.7, Q94, Q105 | Vertical chain of boxes: unit → MF → F1 and F2 → F3 → F&EI → band → radius → area → value → damage factor → MPPD → credits → MPDO → BI. Two side boxes for credits and for "reduce hazard first". |
| HAZOP node schematic | §2.9, Q128 | Tank T-1 → pump → control valve → reactor R-1. Bracket the line, mark "Node 1", and write the design intent under the bracket. Arrows for the seven guide words entering the node. |
| Hazard bands strip | §2.6 | One horizontal bar split 1–60, 61–96, 97–127, 128–158, 159+, with light to severe under each and a star at 128. |
| Hierarchy ladder | §2.12, Q58 | Five rungs, elimination at the top. Left arrow "protects everyone, no behaviour needed". Right arrow "protects one wearer, while worn". |
| Extinguisher selection grid | §2.4, Q170 | Rows A to E, columns water, foam, CO₂, powder, clean agent. Tick the valid cells and cross the dangerous ones. |
| PHA four-step flow | §2.8, Q53 | Four boxes in series: prerequisites, hazard identification, consequence and frequency, risk ranking. Under box two write "no hazard too small to record". |
| Exposure circle on a plot plan | §2.5, §2.7 | Plan view with the unit at the centre and a circle for the exposure radius. Shade and value the equipment inside. Caption it "value × damage factor = base MPPD". |
| Node walk for a HAZOP | §2.9 | One line drawing split into four bracketed nodes, numbered, with the design intent written under each bracket. It shows the plant is never studied as one object. |

Draw all nine small, label them, and refer to each one in the text. A labelled sketch earns more
than a neat one. Two of the nine are compulsory in practice: the Dow flow chart for a calculation
question, and the node schematic for a HAZOP question.

---

## 6. Say this if grilled

### 6.1 Sixteen lines to have ready

1. A hazard is inherent and a risk is conditional. Substitution removes the hazard. PPE only
   lowers the risk.
2. Dow started in 1966, because the chemical industry's loss record was bad enough to need a
   scoreboard. Its output is money and days, not adjectives.
3. F&EI = MF × F1 × F2. Two multiplications carry the method, so show them as equations.
4. 128 is the number that matters most. It is the trigger for a detailed PHA.
5. The exposure radius comes off an empirical curve built on a 3-inch spill. The deck gives no
   equation, so quote the curve rather than invent a constant.
6. Reducing the hazard early beats adding loss control credits late. The deck says so on its
   last summary slide.
7. PHA is wide, shallow and early. HAZOP is narrow, deep and late. Detail is wasted on a design
   that changes next week.
8. Deviation equals guide word times parameter. MORE alone is a word; MORE pressure is a
   deviation.
9. In the Indian scheme C is gas and E is electrical. The NFPA letters are a different scheme.
10. CO₂ is the electrical answer because it leaves no residue. The residue is the reason.
11. PPE is last because it protects one wearer, only while it fits, and it fails silently. A dead
    extraction hood is visible; a leaking respirator seal is not.
12. An MSDS has sixteen sections. Section 8 is the one the supervisor actually reads.
13. A PHA without a ranking is only a hazard list. The ranking is the step that turns it into a
    decision.
14. MSIHC came after Bhopal, and Chapter IV-A of the Factories Act is the same response written
    into factory law. Both arrive in 1987 and 1989, so the dates are close for a reason.
15. A fire plan follows the fuel, not the floor plan. A water unit in a switch room is a hazard,
    not a control.
16. The Dow number is not a prediction. It is a ranking and a budget, and it is meant to be
    argued with. A unit scoring 144 says "look here first", not "this will burn on Tuesday".
