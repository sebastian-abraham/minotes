# Module 4 — Machinery Safeguard and Material Handling

> **20MCN401 Industrial Safety Engineering · B.Tech CSE, Sem 7 (Saintgits, autonomous) · Module IV of five · 20 per cent of the ESE paper.** This module is where the marks come from lists: guard types, device types, welding hazards, handling hazards, hook rejection criteria. Five numbers do most of the work — 10 per cent wear, 15 per cent throat opening, 10 degrees of twist, 1/8 inch work-rest gap, and 10,000 cubic feet of air per welder. Sources: `m4.txt` (`slide N`); values marked **(standard)** are exam-standard but absent from the deck.

---

## 1. Coverage

### Table A — syllabus line → section

| Syllabus line (verbatim) | Hrs | Answered at |
|---|---|---|
| Point of operation — principle of machine guarding | 4 | §2.1 |
| Types of guards and devices | 4 | §2.2, §2.3 |
| Safety in power presses — primary and secondary operations, shearing, bending, rolling, drawing | 4 | §2.4 |
| Safety in turning, boring, milling, planing and grinding | 4 | §2.5 |
| Welding and cutting — safety precautions for gas and arc welding | 4 | §2.6 |
| Cutting and finishing | 4 | §2.7 |
| Material handling — classification, safety considerations, manual and mechanical handling, assessments, lifting, carrying, pulling, pushing, palletizing, stocking | 4 | §2.8 |
| Material handling equipment — operation and maintenance, wire rope, chain slings, hooks, clamps | 4 | §2.9 |

Every line is four hours, so no line is allowed to shrink. Where the deck is image-only (presses, lathes, mills, rigging) the content is supplied as **(standard)** and flagged in the text.

### Table B — the 30 assigned questions

| Q | Marks | Answered at | What the answer covers |
|---|---|---|---|
| Q32 | 3 | §3.1 | Injuries from moving machinery |
| Q33 | 3 | §3.1 | Three safeguards |
| Q34 | 5 | §3.4 | Principle of machine guarding |
| Q35 | 3 | §3.1 | Methods of safeguarding |
| Q36 | 3 | §3.2 | Welding safety gear |
| Q37 | 3 | §3.2 | Adjustable guards, pros and cons |
| Q66 | 3 | §3.2 | Palletizing and finishing |
| Q67 | 3 | §3.3 | Transport equipment for materials |
| Q68 | 3 | §3.3 | Clamp precautions |
| Q69 | 3 | §3.3 | Manual handling hazards |
| Q70 | 3 | §3.3 | Mechanical handling hazards |
| Q71 | 3 | §3.3 | Stocking, and why it matters |
| Q109 | 5 | §3.4 | Mechanical machinery hazards and prevention |
| Q110 | 8 | §3.8 | Guarding devices and sustainability |
| Q111 | 5 | §3.4 | Machinery safeguard and guard types |
| Q112 | 5 | §3.5 | Grinding safety practice |
| Q113 | 5 | §3.6 | Arc welding safety practice |
| Q114 | 5 | §3.5 | Milling safety practice |
| Q129 | 5 | §3.7 | Manual handling safety |
| Q130 | 5 | §3.7 | Mechanical handling safety |
| Q133 | 8 | §3.9 | Hook maintenance, with sketch |
| Q134 | 8 | §3.10 | Chain sling maintenance, with sketch |
| Q135 | 8 | §3.11 | Wire rope maintenance, with sketch |
| Q160 | 5 | §3.4 | Guarding principle and its importance |
| Q161 | 8 | §3.8 | Guarding devices, sustainability analysis |
| Q162 | 5 | §3.5 | Milling, grinding and planing measures |
| Q163 | 5 | §3.6 | Arc and gas welding risks and control |
| Q164 | 5 | §3.7 | Classification of handling equipment |
| Q166 | 8 | §3.10 | Chain sling maintenance, with sketch |
| Q167 | 8 | §3.9 | Hooks versus clamps, inspection |

Twelve three-mark, eleven five-mark, seven eight-mark. §3.12 carries the 14-mark skeleton you adapt when the Part B question is "machine guarding" or "material handling".

---

## 2. Concepts

### 2.1 Point of operation and the principle of machine guarding (`slide 2`–`slide 6`, `slide 15`)

*In plain English.* A machine hurts you in one place: where the tool touches the metal. Call that place the point of operation. Guarding means putting something solid between that place and your hand. A warning notice is not a guard. A guard has to work on the day you are tired, rushed and looking the other way.

*The detail.*
- **Point of operation** is where work is done on the material: cutting, shaping, boring, forming (`slide 3`).
- **Power transmission apparatus** carries energy from the motor to the tool.
- Its members: flywheels, pulleys, belts, connecting rods, couplings, cams, spindles, chains, cranks and gears (`slide 3`).
- **Operating controls** are the third machine part; **other moving parts** (feed mechanisms, auxiliary parts) are the fourth (`slide 4`).
- **Three injury routes** (`slide 2`): caught by or drawn into the machine, struck by a moving part, struck by a failed component or a flying particle.
- **Six guarding principles** (`slide 15`): prevent contact; make the guard hard to remove; stop objects falling in.
- The rest of the list: add no new hazard, do not slow the job, allow lubrication without removal.
- **Two zones need guarding**, not one: the die or blade (hands) and the drive (sleeves, hair, rags).
- **Distance can be the guard** where the opening is small and far enough away (§4.1).

*What to write.* For 3 marks: define the point of operation, then give the three injury routes. For 5: add the four machine parts and the six principles. For 8: add the device families and the distance rule.

**Mark anchor.** Name the *power transmission apparatus* and two of its members. Most answers guard the blade only, and lose the mark that the belt drive was also a hazard.

**Exam trap.** Point of operation and power transmission are different hazards with different fixes. A nip at the belt drive gets a fixed enclosure. A press die gets presence sensing or a two-hand control. Swap the two and both marks go.

### 2.2 Types of guards (`slide 24`–`slide 34`)

*In plain English.* A guard is a barrier. It does not sense you and it does not think; it simply stands between you and the moving part. The four types differ in one question: who is allowed to move the barrier, and when?

*The detail.*
- **Fixed guard** is a permanent part of the machine. Removal needs a tool.
- It depends on nothing moving to do its job. Sheet metal, screen, wire cloth, bars or plastic all serve (`slide 25`).
- A fixed guard is usually first choice, for simplicity and permanence (`slide 25`).
- Power transmission is best protected by fixed guards that enclose the danger (`slide 26`).
- **Interlocked guard** cuts power or trips the machine when it opens (`slide 29`).
- The machine cannot cycle until the guard is back in place (`slide 29`).
- The interlock may be electrical, mechanical, hydraulic or pneumatic (`slide 30`).
- Closing the guard must not restart the machine by itself (`slide 30`).
- **Adjustable guard** has an opening you set by hand to suit the stock (`slide 32`).
- **Self-adjusting guard** has an opening set by the stock itself. It moves just enough to admit the work and returns to rest (`slide 34`).

*What to write.* For 3 marks: name the four guards and give one line each. For 5: add the fixed-guard characteristics and the interlock behaviour on closing.

**Mark anchor.** "Replacing the guard must not restart the machine." That single sentence separates an interlocked guard from a door switch, and it is on `slide 30`.

**Exam trap.** An interlocked guard can be defeated, and the deck shows one taped down (`slide 31`). Say that plainly, then say the control is supervision and planned maintenance. Claiming interlocks cannot fail loses the credibility mark.

### 2.3 Types of devices (`slide 36`–`slide 48`)

*In plain English.* A device is the smarter cousin of a guard. It watches the danger area and stops the machine when you enter. The difference matters: a guard blocks, a device reacts. A device that reacts too slowly is worse than useless, because it teaches people to trust it.

*The detail.*
- **Presence sensing, photoelectric:** a light curtain; breaking the beam stops the cycle (`slide 37`).
- **Presence sensing, radio frequency:** a capacitance field; breaking it stops or prevents the cycle (`slide 37`).
- **Pullback:** cables on hands, wrists or arms haul the operator clear as the ram descends (`slide 42`).
- Pullback suits machines with a stroking action; access is allowed only while the slide is up.
- **Restraint (holdout):** straps fix the hands at a point, so they cannot reach the die at all (`slide 40`).
- Restraint has no retracting action; it only limits travel.
- **Two-hand control:** both buttons held down together, all the time, to keep the stroke running (`slide 45`).
- **Two-hand trip:** both buttons pressed together to start, then the hands are free (`slide 47`).
- **Gate:** a barrier synchronised with the cycle, closed during the dangerous part (`slide 48`).
- **Location and distance** is a separate strategy: fence, height, or small stock opening (`slide 50`).
- **Feeding and ejection** by machine, semi-automatic or robot keeps hands out entirely (`slide 52`–`slide 57`).
- **Miscellaneous aids** give margin only: awareness barrier, shield, holding tool, push stick (`slide 58`).

*What to write.* For 5 marks: five devices, one line of mechanism each, plus the two-hand pair distinguished. For 8: add the limits of each device.

**Mark anchor.** Two-hand **control** must be held; two-hand **trip** is pressed once. Naming that difference is the mark most scripts miss.

**Exam trap.** A device protects only the entry it senses. A light curtain across the front does nothing about a hand coming over the top or round the side. Say "the perimeter must be closed" and you have answered the follow-up before it is asked.

### 2.4 Safety in power presses (`slide 60`–`slide 63`)

*In plain English.* A press is a heavy slide that comes down hard, again and again, onto a die. The die is where the work happens and where fingers are lost. The machine is harmless between strokes and lethal during one, so the guard must act faster than a reflex.

*The detail.*
- **Press** = a machine that punches, shears, forms or assembles, using dies on a slide or ram (`slide 61`).
- **Parts:** frame, motor, flywheel, crankshaft, clutch, brake (`slide 62`).
- **Three drives:** mechanical (flywheel and clutch), hydraulic, pneumatic (`slide 60`).
- **The main injury is amputation**, from a hand placed in the point of operation (`slide 63`).
- **Three causes** in the deck: hand in the die, unguarded or badly guarded press, safeguard defeated or overridden (`slide 63`).
- **Safeguards used:** barrier guard on a fixed surface, radio-frequency sensor, light curtain, pullback device, fixed guard (`slide 63`).
- **Primary operation** = the first cut that makes the blank: shearing, blanking, piercing.
- **Secondary operation** = shaping that blank afterwards: bending, drawing, forming.
- **Shearing** cuts sheet with a straight blade; the hazard is the hand under the hold-down.
- **Bending** is a press brake driving a punch into a V die; the hazard is fingers between punch and die.
- **Rolling** passes plate between powered rolls to curve it; the hazard is the in-running nip.
- **Drawing** pulls sheet into a die to form a cup; the hazard is the draw-in at the die mouth.

**The four processes at a glance** (standard).

| Process | Tool | Where the hand is lost | Guard that fits |
|---|---|---|---|
| Shearing | Straight blade on a bed | Under the hold-down, behind the blade | Fixed barrier plus hold-down; light curtain |
| Bending | Punch into V die on a press brake | Between punch tip and die shoulder | Die guard, two-hand control, light curtain |
| Rolling | Powered rolls, plate fed between | In-running nip between rolls | Trip wire or bar along the nip |
| Drawing | Punch pulls sheet into a die | At the die mouth, on the draw-in | Enclosure with small opening; two-hand control |

*What to write.* For 5 marks: press definition, three drives, the amputation hazard, three safeguards. For 8: add the four processes with the hazard that belongs to each.

**Mark anchor.** One hazard per process: shear has the blade and hold-down, bend has punch and die, roll has the nip, draw has the die mouth. Four pairs, four marks.

**Exam trap.** "Primary" and "secondary" here mean first cut and later forming. In manufacturing textbooks they mean casting and machining. State which sense you are using in one line, then move on.

### 2.5 Safety in turning, boring, milling, planing and grinding (`slide 64`–`slide 86`)

*In plain English.* These five machines all remove metal with a sharp edge, and all five throw it. The difference is what moves. On a lathe the work spins. On a mill the cutter spins. On a planer the table slides. On a grinder a stone spins fast enough to burst.

*The detail.*
- **Turning:** the lathe spins the work and a single-point tool feeds along it.
- Hazards are the chuck jaws, bar stock sticking out of the spindle, entanglement, hot swarf and a workpiece thrown from the chuck.
- Guard the chuck and the spindle end; keep the tool over the work; never leave the key in the chuck.
- **Boring** enlarges a hole already drilled, usually on a boring mill (`slide 71`).
- Broken drilling heads are a leading cause of injury; match the tool to the spindle speed and the workpiece (`slide 71`).
- Dress tight, with no loose hanging cloth, and wear eye protection (`slide 72`).
- Know the machine: inexperienced boring operators are three times as likely to cause an accident (`slide 73`).
- Service the machine regularly; worn tooling causes both bad work and breakdowns (`slide 74`).
- **Milling:** a multi-tooth cutter rotates while the table feeds the work past it.
- Hazards are cutter contact, flying chips, draw-in at the cutter, and a workpiece pulled out of an unclamped vice.
- **Planing:** the table carries the work back and forth under a fixed tool, or the tool strokes over fixed work.
- The hazard is the traverse: being struck at the end of the stroke, or caught by work overhanging the table.
- **Grinding:** an abrasive wheel runs at high surface speed and can burst.
- A burst wheel throws fragments across the shop; dust and sparks add to the fire and lung risk.

**Wheel rules for grinding** (standard).

| Rule | Value | Why |
|---|---|---|
| Work rest gap | 1/8 inch (3 mm) | Stops work being drawn between wheel and rest |
| Tongue guard gap | 1/4 inch | Contains fragments if the wheel bursts |
| Wheel speed | Never above the marked speed | Overspeed is the commonest cause of burst |
| Ring test | Tap and listen before mounting | A cracked wheel rings dull |
| Starting | Stand to one side for the first run | Burst happens at start-up |
| Dressing | With a proper dresser, dust extraction on | Removes glaze and silica dust |

*What to write.* For 5 marks: one hazard and one control per machine, five short pairs. For 8: add the wheel rules for grinding and the clamping rules for milling.

**Mark anchor.** Boring's three-times figure (`slide 73`) and the 1/8 inch work-rest gap (§4.2). One is quotable evidence, the other is a number a marker can check.

**Exam trap.** Guards on these machines are not interchangeable with press safeguards. A lathe chuck gets a hinged or fixed cover; a milling cutter gets an adjustable nose guard; a wheel gets a casing plus a work rest. Naming "light curtain" for a lathe is a wrong answer.

### 2.6 Welding — safety precautions for gas and arc (`slide 87`–`slide 101`)

*In plain English.* Welding is the only common shop job that carries its own fire, its own gas cylinder, its own electric supply and its own sun. You are holding an arc brighter than daylight at arm's length. Every precaution below exists because one of those four has killed someone.

*The detail.*
- **Acetylene** is the usual fuel gas. It ignites over a very wide range of concentrations, so a small leak is already a risk (`slide 88`).
- **Oxygen** does not burn or explode by itself. It makes everything else burn far faster (`slide 88`).
- A damaged valve turns a cylinder into a rocket; chain every cylinder upright (`slide 88`, `slide 89`).
- **Storage rules** (`slide 89`): keep clear of heat and damage, chain upright, caps on, valves closed before moving, oxygen and acetylene stored apart.
- Move a cylinder by rolling it on its bottom edge. Never drag it (`slide 89`).
- **Leak test** every connection with approved solution; inspect hoses and replace worn ones (`slide 90`).
- Light with a **flint lighter**, never a match, and stand to the side of the regulators (`slide 90`).
- Open the acetylene valve only **one quarter to three quarters of a turn**, and leave the wrench on it (`slide 90`).
- Light the acetylene first, then open oxygen to a neutral flame (`slide 90`).
- **Ventilation is adequate** at 10,000 cubic feet per welder and a 16 foot ceiling (`slide 92`).
- Otherwise supply **2000 cfm per welder**, or use local exhaust or an air-line respirator (`slide 92`).
- **Arc hazards, six of them** (`slide 95`): fumes and gases, electric shock, arc rays, fire and explosion, noise, hot objects.
- **Primary voltage** is 230 or 460 volts; **secondary** is 6 to 100 volts (`slide 97`).
- The arc is brighter than the sun. Ultraviolet light burns the eye and the skin (`slide 98`).
- **Sparks travel up to 35 feet.** Clear flammables, keep an extinguisher, re-check the area 30 minutes after (`slide 99`).

*What to write.* For 5 marks: five hazards with one control each, then the ventilation rule. For 8: split gas and arc, and give the cylinder rules as a list.

**Mark anchor.** 35 feet, 10,000 cubic feet, 2000 cfm, one quarter to three quarters of a turn. Any two of those four numbers prove you read the standard.

**Exam trap.** Gas and arc hazards overlap but are not the same. Gas adds cylinder handling and flashback; arc adds electric shock and ultraviolet. An answer that lists only "fire and fume" for both is a half answer.

### 2.7 Cutting and finishing (`slide 90`–`slide 99`, standard)

*In plain English.* Cutting separates metal; finishing smooths it. Both throw something at you: sparks and slag from the cut, dust and grit from the finish. The control is the same in both cases — catch it at the source, then protect the face.

*The detail.*
- **Oxy-fuel cutting** heats the metal to ignition, then a jet of oxygen burns it away.
- **Plasma cutting** uses a constricted arc and a fast gas jet; it cuts faster and throws more fume.
- **Mechanical cutting** means shears, saws, and abrasive cut-off wheels.
- Cutting hazards: molten slag and sparks, hot cut edge, fume, noise, and fire in nearby combustibles.
- Screen the cut, wet down or shield combustibles, and keep an extinguisher within reach.
- **Finishing** covers chipping, grinding, buffing, polishing, sanding and deburring.
- Finishing hazards: airborne dust (metal and silica), noise, hand-arm vibration, flying particles, repetitive strain.
- Solvent-based finishing adds vapour, dermatitis (skin inflammation) and a fire risk.
- Controls, in order: local exhaust at the tool, wet methods, enclosure, then PPE.
- PPE for both: face shield over goggles, hearing protection, gloves, and a flame-resistant apron for cutting.

*What to write.* For 3 marks: three hazards of cutting and three of finishing, with one control each. For 8: add the control hierarchy and the fire watch.

**Mark anchor.** "Catch it at the source" — local exhaust before respirator. Hierarchy of control is the phrase that earns the mark beyond the list.

**Exam trap.** A face shield alone is not eye protection for grinding. Particles come from below and around the shield. Say "goggles under the shield" and you have covered the gap.

### 2.8 Material handling — manual and mechanical (`slide 129`–`slide 152`)

*In plain English.* Material handling is everything you do to a load between one place and another: pick it up, carry it, push it, stack it. Done by hand it wears the body out. Done by machine it can drop a tonne on someone. Both need a plan, and the plan starts with the weight.

*The detail.*
- **Manual handling** means using your own strength to move material (`slide 129`).
- It raises injury risk and adds cost to the product, so the first move is to remove it (`slide 129`).
- Remove it by combining operations, eliminating them, or mechanising them (`slide 129`).
- **Mechanical handling** covers lifting, transporting, stacking, loading and unloading by machine (`slide 137`).
- The deck's machines: palletizer, chain pulley block, forklift, conveyor, crane and hoist (`slide 137`).
- It removes the musculoskeletal risk of manual work and raises productivity (`slide 137`).
- **TILE** is the assessment frame: Task, Individual, Load, Environment (`slide 146`).
- Some add **Other factors** (pace, monotony) and call it TILEO (`slide 146`).
- **Lifting:** feet shoulder width, squat with knees bent, back straight, load close to the body (`slide 149`).
- Never lift above chest height; test the weight with the "big toe" push first (`slide 149`).
- **Pulling:** feet hip width, hips dropped, knees bent, core tight, small backward steps (`slide 150`).
- **Carrying:** load close to the body, back straight, eyes ahead, and set it down with the same knee bend.
- **Pushing beats pulling.** Push with legs and body weight, back straight, and do not twist at the hips (`slide 151`).
- Face the load squarely, not at its top edge or its bottom edge (`slide 151`).
- **Palletizing** stacks goods on a pallet so a forklift can move the whole load at once.
- **Stocking** puts material in a defined, labelled place, so it can be found and counted.

*What to write.* For 5 marks: define manual and mechanical, give TILE, then the lifting sequence. For 8: add the mechanical hazard list and the dos and don'ts.

**Mark anchor.** TILE spelled out, plus "push, don't pull". Both are on the deck and both are cheap marks.

**Exam trap.** The injury in manual handling is usually the back, but the cause is often the *task design*, not the worker's technique. Say "redesign first, technique second" and you have the modern answer.

### 2.9 Handling equipment — wire rope, chain slings, hooks, clamps (`slide 138`–`slide 164`)

*In plain English.* A sling is the weakest link in any lift, because it is the part that is handled, dragged and dropped every day. It fails quietly: a wire breaks, a link stretches, a hook opens. Inspection is how you find the failure before the load does.

*The detail.*
- **General rule:** never use gear that has lost more than **10 per cent of its breaking strength** (`slide 142`).
- **Wire rope** is strands laid around a core. A **lay** is one complete turn of the strands.
- Discard on broken wires, diameter loss, corrosion, kinking, bird-caging or heat damage (§4.3).
- **Chain sling:** check every link for cracks, bends, twists and stretch; check the tag and the WLL.
- Never shorten a chain by knotting it, and never hammer a link back into shape.
- **Hooks:** the deck gives seven rejection criteria, all quotable (`slide 161`).
- A hook is rejected for cracks, nicks or gouges, or for twist over **10 degrees**.
- It is rejected if the latch is damaged, or the throat has opened by more than **15 per cent**.
- It is rejected for wear over **10 per cent**, heat damage, or an unauthorised repair (`slide 161`).
- The **hook bowl** carries the load, never the latch. Seat the sling properly (`slide 161`).
- Never side load, back load or point load a hook. Point loading can cut capacity by **60 per cent** (`slide 161`).
- Grind a nick lengthwise along the hook contour, and replace it if 10 per cent is lost (`slide 161`).
- Never weld, heat, burn or bend a hook back into shape without the maker's approval.
- **Clamps:** plate clamps for plate, beam clamps for beams; check jaw teeth and the pivot.
- Keep clamps clean and dry, free of grit and oil, and store them off the floor (`slide 163`, `slide 164`).

*What to write.* For 8 marks: one paragraph per item — rope, chain, hook, clamp — each with its inspection points and one number.

**Mark anchor.** The three percentages: 10 per cent wear, 15 per cent throat, 10 degrees twist. They are the only numbers in this topic and they are asked for directly.

**Exam trap.** A hook that has been repaired by welding is scrap, not repaired. The deck says so twice. Writing "weld it and return to service" fails the question outright.

## 3. Answer bank

The numbering follows the mark bands: 3.1–3.3 are three-mark, 3.4–3.7 are five-mark, 3.8–3.11 are eight-mark, 3.12 is the 14-mark skeleton. Answers are grouped by topic so that one read covers a cluster of questions.

### 3.1 Three-mark — machinery injuries, safeguard types, methods (Q32, Q33, Q35)

**Q32 · Explain the injuries caused due to moving machinery. (3)**
Three routes, one line each. **Caught in or drawn into:** a rotating shaft grips a sleeve or a glove and pulls the arm in. **Struck by a moving part:** the ram, the chuck jaw or the flywheel hits you. **Struck by a failed part or particle:** a burst wheel or a broken tool throws fragments. Name the outcomes: amputation, fracture, crushing and eye injury. The worst is amputation, because the point of operation takes fingers, not bruises.

**Q33 · Discuss any 3 machinery safeguards. (3)**
Take one from each family and give the mechanism. **Fixed guard** on the belt drive: a sheet-metal cover that needs a tool to remove. **Interlocked guard** on the access door: opening it cuts the power, and the machine will not restart until it is closed. **Light curtain** at the press die: a hand in the beam stops the stroke before the ram reaches the work. Add one line on why each fits: the first is cheap and permanent, the second allows access, the third allows fast loading.

**Q35 · Explain the methods of safeguarding. (3)**
Five methods, listed. **Guards:** fixed, interlocked, adjustable, self-adjusting. **Devices:** presence sensing, pullback, restraint, two-hand control or trip, gates. **Location and distance:** fence, height, or a small stock opening. **Feeding and ejection:** automatic, semi-automatic, or robot. **Miscellaneous aids:** awareness barrier, shield, holding tool, push stick.

**Mark anchor.** "Guard blocks; device reacts; distance removes the reach; feeding removes the hand." That one line organises all five methods.

**Exam trap.** The question says *methods*, so a list of four guard types is not a complete answer. Guards are one method out of five.

### 3.2 Three-mark — welding gear, adjustable guards, palletizing (Q36, Q37, Q66)

**Q36 · List welding safety gear. (3)**
Head and eyes: welding helmet with the right filter shade, and safety glasses underneath. Body: flame-resistant jacket or apron, long sleeves, straight-legged trousers, leather boots. Hands: gauntlet gloves. Ears: plugs or muffs for arc work. Add a cap or shoulder cover for overhead work, and a respirator or local exhaust where ventilation is poor. For **gas** welding a filter goggle replaces the helmet; for **arc** welding the helmet is mandatory because of ultraviolet.

**Q37 · List the advantages and disadvantages of using adjustable safeguards. (3)**
Advantages: one guard covers a range of stock sizes, so tooling cost falls. The opening can be set to the job, so odd shapes can still be run. Disadvantages: the setting is only as good as the operator, and it can be left wide open. It adds a setup step and needs checking at each changeover. It is easier to defeat than a fixed guard.

**Q66 · Explain the importance of palletizing and finishing. (3)**
**Palletizing** groups goods on a pallet so a forklift moves the whole load in one trip. That cuts handling time, handling damage and the number of manual lifts. It also gives a standard footprint for racking and counting. **Finishing** is the last operation, and it decides how the part survives service. It adds corrosion resistance, wear resistance and appearance. It also removes burrs that would cut the fitter or the customer.

**Mark anchor.** "One lift instead of twenty" for palletizing; "the last operation decides the life of the part" for finishing.

**Exam trap.** Finishing is a safety topic, not only a quality topic. Name its hazards — dust, noise, vibration, solvent vapour — or the answer reads as a production answer.

### 3.3 Three-mark — handling equipment, clamps, handling hazards, stocking (Q67–Q71)

**Q67 · What are the different equipment for the transportation of materials? (3)**
Four families with one example each. **Conveyors:** belt, roller, screw, bucket, overhead chain. **Industrial trucks:** forklift, pallet truck, platform truck, tractor-trailer. **Cranes and hoists:** overhead crane, jib crane, chain pulley block, monorail hoist. **Unit-load and robotic equipment:** palletizer, automated guided vehicle, robot arm. Bulk solids move by pneumatic pipeline or chute.

**Q68 · What are the safety precautions to be considered while using clamps? (3)**
Use the clamp made for the shape — plate clamp for plate, beam clamp for beams. Check the marked working load and never exceed it. Seat the jaws fully on the material, with the load square to the clamp body. Pad sharp edges, and lift one plate at a time. Inspect jaw teeth, the pivot and the spring before every shift. Never side-load a clamp or use it as a hook.

**Q69 · What are the hazards associated with manual material handling? (3)**
Musculoskeletal injury is the main one: back strain, shoulder injury, hernia, wrist and knee damage. Then dropping the load on the feet, cuts from sharp edges, and trapping fingers. Awkward posture and repetition add cumulative trauma. Heat, poor lighting and uneven floors raise the risk further. The cost is not only the injury: it is absenteeism, compensation and lower output.

**Q70 · What are the hazards associated with mechanical handling? (3)**
The deck lists them (`slide 138`). Equipment used without a valid inspection certificate. Wrong or inadequate selection of tool for the load. Damaged or faulty equipment. Congested operating space. Incompetent operator. Overloading. Unbalanced loads. Poor rigging and lifting. Overspeeding and unauthorised use. Machines running without guards. Each one has a matching control: certification, rated capacity, inspection, layout, training and guarding.

**Q71 · Define stocking. Explain the importance of stocking. (3)**
**Stocking** means placing material in a defined, identified location, in a known quantity, so it can be found and issued. Importance: it cuts search and travel time, which is a direct labour cost. It prevents overstock and shortage, so production does not stop. It allows first-in-first-out, which matters for dated and coated material. It keeps aisles and exits clear, which is a fire and housekeeping requirement. It also makes counting and audit possible.

**Mark anchor.** Q70 has ten named hazards on the slide. Ten is more than three marks need, so give six with controls attached.

**Exam trap.** "Poor rigging" belongs to mechanical handling, not manual. Sorting hazards into the right column is the whole point of the pair Q69 and Q70.

### 3.4 Five-mark — guarding principle, safeguards, machinery hazards (Q109, Q34, Q111, Q160)

**Q34 · Explain the principle of machine guarding. (5)**
Start with the aim: keep the body out of the danger area, at every stage of the cycle. Then the six principles (`slide 15`). **Prevent contact** between the hazard and any part of the body or clothing. **Secure the guard**, so it cannot be shifted or lifted off by hand. **Block falling objects**, so nothing drops into the moving parts. **Add no new hazard**: no sharp edges, no pinch points, no trap. **Do not interfere** with the job, the comfort or the speed of work. **Allow safe lubrication**, without taking the guard off. Close with: a guard that slows the job will be removed, so design for the job.

**Q111 · Explain machinery safeguard. Discuss the different types of guards. (5)**
A **safeguard** is any physical or control measure that keeps a person out of a machine's danger area. Guards are the first family. **Fixed:** permanent, tool needed to remove, independent of moving parts. **Interlocked:** opening it cuts power or trips the machine, and closing it must not restart the machine. **Adjustable:** the opening is set by hand to suit the stock. **Self-adjusting:** the stock itself opens the guard just enough, and the guard returns to rest. Say where each fits: fixed for the drive, interlocked for access doors, adjustable for mixed stock, self-adjusting for repetitive feeding.

**Q160 · Explain the principle of machine guarding and its importance. (5)**
Give the principle as the six rules above, then the importance. It prevents amputation and crushing, which are the injuries that cannot be undone. It protects people who are not operating the machine: cleaners, setters, visitors. It makes the machine legal and defensible after an accident. It removes the fear that makes operators slow and careless. It reduces compensation, downtime and retraining cost. One line to close: guarding is cheaper than the accident it prevents.

**Q109 · Explain mechanical machinery hazards. Discuss possible ways to prevent them. (5)**
Group the hazards by motion (standard). **Crushing** between two parts. **Shearing** between a moving and a fixed edge. **Cutting** by a sharp tool or edge. **Entanglement** with a rotating shaft, coupling or spindle. **Drawing-in** at a nip point. **Impact** from a moving part or an ejected workpiece. **Stabbing** by a tool or a flying chip. Prevention follows the same order: guard the hazard, add a protective device, use distance or a feeding aid, then train and supervise.

**Mark anchor.** The six principles, verbatim and in order, are worth three of the five marks on Q34. Learn them as a sequence, not as prose.

**Exam trap.** Q34 and Q160 look identical and are not. Q34 wants the principle. Q160 wants the principle *plus* why it matters. An answer that repeats the six rules twice earns five once.

### 3.5 Five-mark — grinding, milling, planing (Q112, Q114, Q162)

**Q112 · Describe the safety practices to be followed during grinding. (5)**
Wheel: use a wheel rated for the machine speed, ring-test it before mounting, and never exceed the marked speed. Guarding: a casing over the wheel, a tongue guard at 1/4 inch, a work rest at 1/8 inch. Mounting: use the correct flanges, and do not over-tighten. Starting: stand to one side for the first run, because burst happens at start-up. Working: hold small work in a tool, not in the fingers; grind on the face, not the side; dress with a proper dresser. Health: eye shield plus goggles, dust extraction, and hearing protection.

**Q114 · Describe the safety practices to be followed during milling. (5)**
Clamp the work and the vice before starting; a workpiece thrown from a mill kills. Guard the cutter with an adjustable nose guard, and keep the chip shield down. Use the right cutter, speed and feed, so the cutter is not overloaded. Never reach over or near a rotating cutter, and never measure or clear chips while the spindle turns. Stop the spindle for swarf removal, and use a brush, not a hand. Keep the floor clear of chips and coolant. No gloves or loose sleeves near the cutter.

**Q162 · List the safety measures for milling, grinding and planing operations. (5)**
Three columns, three lines each. **Milling:** clamp work, guard the cutter, stop the spindle before measuring. **Grinding:** rated wheel, ring test, casing and work rest, goggles. **Planing:** keep clear of the table traverse, guard the stroke ends, clamp the work so it cannot overhang, and never reach across the moving table. Add the common lines: eye protection, no loose clothing, housekeeping, and a stop control within reach.

**Mark anchor.** 1/4 inch tongue guard, 1/8 inch work rest. Those two numbers answer half of Q112 on their own.

**Exam trap.** A ring test is not a strength test. It only finds a cracked wheel. Say that, and you avoid claiming more than the test can do.

### 3.6 Five-mark — arc welding, and arc versus gas (Q113, Q163)

**Q113 · Describe the safety practices to be followed during arc welding. (5)**
Six hazards, one control each (`slide 95`). **Fumes and gases:** keep your head out of the plume, exhaust at the arc, or wear an air-line respirator. **Electric shock:** do not touch live parts, insulate yourself from work and ground, and never repair the set yourself. **Arc rays:** helmet with the right shade and safety glasses under it; screen the arc from others. **Fire and explosion:** clear flammables, because sparks reach 35 feet, keep an extinguisher, and re-check 30 minutes after. **Noise:** plugs or muffs. **Hot objects:** gloves and tongs, and mark hot work.

**Q163 · What are the common safety risks in arc and gas welding, and how can they be controlled? (5)**
Give the shared risks first, then what each process adds. **Shared:** fire from sparks and slag, fume, burns from hot metal, and eye damage from radiation. **Arc adds:** electric shock, at 230 or 460 volts on the primary side. **Gas adds:** cylinder handling, a fuel gas that ignites over a wide range, and flashback into the hose. Controls: ventilation or exhaust, fire watch and extinguisher, correct filter shade, dry gloves and insulated holder, cylinders chained upright with flashback arrestors, and a leak test at every connection.

**Mark anchor.** "Sparks reach 35 feet" and "primary 230 or 460 volts" are the two facts that separate a read answer from a remembered one.

**Exam trap.** A welding helmet protects against radiation, not against fume. If the question mentions confined space, ventilation is the answer, not a better helmet.

### 3.7 Five-mark — manual and mechanical handling safety, classification (Q129, Q130, Q164)

**Q129 · What are the safety considerations in manual material handling? (5)**
Assess first, with TILE. Look at the task, the individual, the load and the environment. Then remove the lift if you can: use a trolley, a hoist or a team lift. If the lift stays, use the technique: feet apart, knees bent, back straight, load close, no twisting. Never lift above chest height, and test the weight before committing. Keep the path clear, wear gloves and safety footwear, and break heavy work with rest. Train the worker, then supervise the technique.

**Q130 · What are the safety considerations in mechanical material handling? (5)**
Equipment: certified, inspected, and marked with its safe working load. Operator: trained and authorised, and only that person uses the machine. Before the lift: check the emergency stop, the limit switches and the overload alarm. Plan the lift: estimate weight, distance and the hazards on the route. Rigging: correct sling, padded corners, a guide rope on the load. During the lift: slow near the destination, keep eye contact with the load, barricade the area. Never stand or pass under a suspended load.

**Q164 · Explain the classification of material handling equipment with suitable examples. (5)**
Classify by function, which is how the exam wants it. **Conveyors:** belt, roller, screw, bucket, for continuous flow. **Cranes and hoists:** overhead crane, jib, chain pulley block, for intermittent lifting. **Industrial trucks:** forklift, pallet truck, platform truck, for flexible movement. **Containers and unit loads:** pallet, skid, bin, crate. **Robots and automated vehicles:** pick-and-place arm, AGV, for repeat work. **Bulk handling:** pump, pipeline, chute, for powders and liquids. Then split all of it into manual and mechanical.

**Mark anchor.** "Continuous versus intermittent" is the distinction that makes a conveyor list and a crane list different, and it is worth a mark.

**Exam trap.** A pallet is equipment in the classification sense, but it is not machinery. Putting it under "cranes" loses the structure mark.

### 3.8 Eight-mark — guarding devices and their sustainability (Q110, Q161)

**Q110 · Which are the various types of machine guarding devices used in industries. Discuss the sustainability of each machine guarding device. (8)**
**Q161 · Explain the various types of machine guarding devices used in industries and analyze the sustainability of each type. (8)**

Both questions want the same thing: a list of devices, then a judgement on each. Answer once, and take the second wording as permission to spend longer on the judgement.

**Structure.** Four guarded families, then a two-column judgement for each. Use the words *reliable*, *maintainable*, *defeatable* and *cost* in the judgement; they are the four things "sustainability" means here.

**Answer.**
Guards come first. **Fixed:** a barrier that needs a tool to remove. Sustainable because it has no moving parts and nothing to fail. Its weakness is that it allows no access, so it gets cut away for setting. **Interlocked:** cuts power when opened. Sustainable only with planned maintenance, because the switch wears and the deck shows one taped down (`slide 31`). **Adjustable:** set by hand to the stock. Sustainable if the setting is checked at each changeover; otherwise it drifts open. **Self-adjusting:** opened by the stock itself. Sustainable for one product family, useless when the family changes.

Devices come second. **Presence sensing by light curtain:** stops the stroke when the beam breaks. Sustainable if the lenses are cleaned and the beam is aligned; blind spots at the edges are the failure. **Radio-frequency sensing:** stops when the field is disturbed. Sustainable, but needs tuning to the machine, and is easily defeated by a fixed object in the field. **Pullback:** cables pull the hands clear. Sustainable only with a daily check, because a slack cable no longer saves the hand. **Restraint:** straps fix the hands outside the zone. Cheap and reliable, but operators dislike it and it is often removed. **Two-hand control and trip:** both hands occupied. Sustainable and cheap, but it protects the hands only, not a second person. **Gate:** a barrier synchronised with the cycle. Sustainable with interlock maintenance.

Close with the ranking. Fixed and interlocked guards last longest. Devices need calibration and cleaning, so they need a maintenance budget. Anything an operator can tape over will be taped over, so buy-in and supervision are part of the design.

**Traps.** Do not describe only guards; the question says devices. Do not call a device "maintenance free": a light curtain with dusty lenses is a false sense of safety. And never claim an interlock cannot be defeated, because the deck shows one defeated.

**Mark anchor.** One sentence per device on how it fails. Eight devices with a failure mode each reads as understanding; eight definitions read as memory.

### 3.9 Eight-mark — hooks, and hooks versus clamps (Q133, Q167)

**Q133 · Explain the maintenance practices for the use of hooks with a neat sketch. (8)**
**Structure.** Sketch first, then inspection, then rejection criteria, then loading rules.

**Sketch.** Draw the hook in profile. Show the **bowl** at the bottom, where the sling sits. Mark the **throat** opening as a dimension. Draw the **latch** across the throat, and a dotted centre line to show the plane of the hook. Label the throat opening and the twist axis. Five labels are enough.

**Inspection.** An experienced rigger inspects every hook before use (`slide 161`). Check for cracks, nicks and gouges, and look closely at the inside of the bowl. Check the latch for damage or a weak spring. Measure the throat opening and compare it with the original. Measure wear at the bowl, and check for heat damage or colour change. Ask whether the hook has been repaired without authority.

**Rejection criteria, the deck's seven.** Cracks, nicks or gouges. Twist greater than **10 degrees** from the plane of the unbent hook. Latch damage or malfunction. Throat opening more than **15 per cent** over the original. Wear more than **10 per cent** of the original dimension. Heat damage. Any unauthorised repair. Any one of these removes the hook from service.

**Repair and loading.** A qualified person may grind a nick, working lengthwise along the contour. If grinding removes more than 10 per cent of the dimension, replace the hook. Never weld, heat, burn or bend a hook back into shape without the maker's approval. Load the bowl, never the latch. Never side load, back load or point load; point loading can cut capacity by **60 per cent**.

**Traps.** A hook with a good latch and a 20 per cent throat opening is still scrap. The latch is not the strength member, and it is not the acceptance criterion. And a hook that has been welded is not repaired; it is unapproved.

**Mark anchor.** The 10 degree / 15 per cent / 10 per cent triple. Quote all three and the sketch becomes a bonus rather than a crutch.

**Q167 · What are the key differences in the inspection criteria for hooks and clamps during regular maintenance checks? (8)**
**Structure.** One paragraph on what each component is, then a comparison table, then the reason for the difference.

**Answer.** A hook is a single forged part that carries the load in tension through its bowl. Its inspection is therefore **dimensional and metallurgical**. You measure twist, throat opening and wear, and you look for heat damage and unapproved repair. A clamp is a mechanism: jaws, a pivot, a spring and sometimes a screw. Its inspection is therefore **functional**. You check that the jaws grip, that the teeth are not worn smooth, that the pivot is not loose, and that the spring returns the jaw. Both need a legible working-load mark and a record of inspection. Both are rejected for cracks. Only the hook is rejected for twist and throat opening, because only the hook is loaded through a single opening.

**Traps.** Do not give the hook criteria for a clamp. A clamp has no throat opening and no twist limit. Say instead what the clamp has: jaw wear, pivot play, spring return, and a body free of cracks at the jaw root.

**Mark anchor.** "Hook: dimensional. Clamp: functional." That single contrast is the answer the question is testing.

### 3.10 Eight-mark — chain slings (Q134, Q166)

**Q134 · Explain the maintenance practices while using a chain sling with a neat sketch. (8)**
**Q166 · Explain the maintenance practices to be followed while using a chain sling, supported by a neat sketch. (8)**

Same answer for both; Q166 adds nothing but the sketch emphasis.

**Structure.** Sketch, then pre-use inspection, then rejection criteria, then use rules, then storage and records.

**Sketch.** Draw a two-leg chain sling: master link at the top, the two legs, a hook at the end of each leg, and the identification tag on the master link. Mark the **included angle** between the legs. Add a second small sketch of a single link with a dimension across the straight side, which is where wear is measured.

**Pre-use inspection.** Inspect link by link, not the sling as a whole (`slide 134`, standard). Check every link for cracks, particularly at the weld. Check for bent, twisted or gouged links. Check for stretch: compare the leg length with the recorded original. Check the end fittings and hooks against §3.9. Check that the tag is present and readable, with the grade and the working load.

**Rejection criteria** (standard). A crack in any link. Elongation of a link beyond about 5 per cent, or a leg that no longer matches its pair. Wear more than 10 per cent of the link diameter. Bent or twisted links. Heat damage or corrosion pitting. A missing or illegible tag. Any of these means the sling is cut up, not repaired.

**Use rules.** Never knot a chain or shorten it with a bolt through the links. Pad sharp corners, because a chain cuts itself on an edge. Keep the included angle at 90 degrees or less; at 120 degrees each leg carries the full load (§4.4). Never hammer a link straight. Never weld a link. Do not drag a chain on the floor (`slide 142`).

**Storage and records.** Hang the sling on a rack, off the floor, away from heat and chemicals. Record each inspection, and keep the certificate with the sling's identity number.

**Traps.** The angle is the mark most scripts miss. Two legs at 120 degrees do not share the load equally with a vertical lift; each leg sees the whole load. And a stretched chain is not "still strong"; elongation is the warning before failure.

**Mark anchor.** "Link by link, and the angle." Those two phrases carry the answer.

### 3.11 Eight-mark — wire rope (Q135)

**Q135 · Explain the maintenance practices for the use of wire ropes with a neat sketch. (8)**
**Structure.** Sketch, construction, inspection, rejection criteria, then care in service.

**Sketch.** Draw a cross-section of a 6×19 rope: six strands around a core, with the wires inside one strand shown. Beside it, draw one **lay**, marked as the length of one complete helical turn of a strand. Label the core, a strand, a wire, and the lay. The lay is the unit every wire-count rule uses, so it must be on the drawing.

**Construction.** Wires make a strand, strands are laid around a core, and the result is the rope. A fibre core is flexible; a steel core carries more load. The lay direction and length decide how the rope wears on a sheave.

**Inspection** (standard). Run the rope through a cloth or a gloved hand and feel for broken wires. Count broken wires over one lay, and count the worst single strand separately. Measure the diameter at several points; a rope that has lost diameter is worn or crushed. Look for corrosion, which shows as pitting and a reddish-brown stain. Look for kinking, crushing and bird-caging, where the strands have opened into a cage. Check the end fittings for cracks, slip and corrosion.

**Rejection criteria** (standard, OSHA running-rope figures). **Six** randomly distributed broken wires in one lay, or **three** broken wires in one strand in one lay. A diameter reduction of about 10 per cent. Kinking, crushing, bird-caging or heat damage. Any cracked or deformed end attachment. Wear of one third of the outer wire diameter.

**Care in service.** Keep the sheave diameter large enough for the rope, because a tight bend fatigues wires. Avoid reverse bending over more than one sheave. Lubricate to the maker's schedule, which also slows corrosion. Do not drag the rope over edges or let it cross itself on the drum. Store coiled and dry, and keep the certificate with the rope.

**Traps.** Broken wires are counted **per lay**, not per metre. And a rope can pass the wire count and still fail on diameter loss, so give both criteria.

**Mark anchor.** "Six in a lay, three in a strand." That pair, with the lay marked on the sketch, is the whole answer.

### 3.12 Fourteen-mark skeleton (ESE Part B)

Use this shape when Part B asks for guarding, or for material handling, as one long question. The marks are roughly 2 + 4 + 4 + 2 + 2.

1. **Frame it (2).** One paragraph: machines injure at the point of operation and at the drive; the fix is a safeguard, not a warning. Name the module's two halves, machines and handling.
2. **The hazard (4).** Three injury routes, then the motion types: rotating, reciprocating, transverse, cutting, punching, shearing, bending. One line each, with an example machine.
3. **The controls (4).** Guards (fixed, interlocked, adjustable, self-adjusting), devices (presence sensing, pullback, restraint, two-hand, gate), distance, feeding aids, robotics. Add the six guarding principles as the test each control must pass.
4. **Apply it (2).** Two worked cases: a power press with a light curtain and a two-hand control; a lathe with a chuck guard and a spindle cover. Say what each control does and what it does not cover.
5. **Handling and upkeep (2).** One paragraph on manual handling (TILE, push not pull) and one on equipment inspection (10 per cent, 15 per cent, 10 degrees). Close with the management line: guarding and inspection are planned activities, not good intentions.

**Mark anchor.** The 2 + 4 + 4 + 2 + 2 split, written as sub-headings, tells the examiner where each mark is. It also stops you writing four pages on guards and nothing on handling.

**Exam trap.** A 14-mark answer that describes only guards loses the handling half. The module title has two halves for a reason.

## 4. Definitions and numbers

Everything here is quotable as a one-line answer. Each entry says whether it comes from the deck or from the standard.

### 4.1 Guard distances (the opening rule)

A fixed barrier does not have to be far away. It has to be far enough that a finger entering the opening cannot reach the die before the ram arrives. The rule is on opening size, not on guesswork: **the wider the opening, the further the guard must sit**. Deck: none. Values: **(standard)**, OSHA 1910.217 Table O-10.

| Opening in the guard | Minimum distance from the point of operation |
|---|---|
| 1/4 inch | 1/2 to 1 1/2 inches |
| 3/8 inch | 1 1/2 to 2 1/2 inches |
| 1/2 inch | 2 1/2 to 3 1/2 inches |
| 3/4 inch | 4 1/2 to 5 1/2 inches |
| 1 1/4 inches | 6 1/2 to 7 1/2 inches |
| 2 1/4 inches | 9 1/2 to 10 1/2 inches |

Two sentences make it usable. An opening of 3/8 inch or less can sit close to the die. A barrier with a large opening is not a barrier at all, because the hand passes through it.

The table assumes a hand moving at about 63 inches per second, and a ram that takes a known time to close. That is why the values come as a range: a fast press needs the longer distance. Do not quote one number without saying which press it belongs to.

The practical rule for the exam: choose the opening first, then read the distance. A guard designed the other way round, distance first and opening afterwards, always ends up with a slot the hand fits through.

### 4.2 Machine-tool numbers

Each of these is a single checkable value, and each earns a mark when quoted instead of described.

| Value | Where it applies | Source |
|---|---|---|
| 1/8 inch (3 mm) | Work-rest gap on a bench or pedestal grinder | standard |
| 1/4 inch | Tongue-guard gap at the top of the wheel | standard |
| Marked wheel speed | Never exceed it; overspeed bursts wheels | standard |
| 10,000 cubic feet per welder | Ventilation without mechanical help | `slide 92` |
| 16 feet | Minimum ceiling height for natural ventilation | `slide 92` |
| 2000 cfm per welder | Mechanical ventilation when space is short | `slide 92` |
| 35 feet | How far welding sparks and spatter travel | `slide 99` |
| 230 or 460 volts | Primary voltage of an arc set | `slide 97` |
| 6 to 100 volts | Secondary, welding voltage | `slide 97` |
| 1/4 to 3/4 turn | How far to open an acetylene cylinder valve | `slide 90` |
| 30 minutes | Fire watch after welding ends | `slide 99` |

Two of these get confused, so keep them apart. **Primary** voltage is what the mains supplies to the set, and it is the lethal side. **Secondary** is what the arc runs at, and it is lower but still enough to kill on a wet floor.

The grinder pair matters for a different reason. A work rest more than 1/8 inch from the wheel lets the work drop into the gap and be pulled through. The gap does not warn you; it swallows the workpiece and then the fingers holding it.

### 4.3 Rope, chain, hook and clamp discard criteria

The three percentages are the backbone. Learn them as a triple: **10 per cent wear, 15 per cent throat, 10 degrees twist**. All are on `slide 161`, and all refer to the hook.

| Item | Reject when | Source |
|---|---|---|
| Hook | Cracks, nicks or gouges | `slide 161` |
| Hook | Twist more than 10 degrees from the plane | `slide 161` |
| Hook | Latch damaged or not working | `slide 161` |
| Hook | Throat opening more than 15 per cent over original | `slide 161` |
| Hook | Wear more than 10 per cent of the original dimension | `slide 161` |
| Hook | Heat damage, or an unauthorised repair | `slide 161` |
| Any gear | Lost more than 10 per cent of its breaking strength | `slide 142` |
| Wire rope | 6 broken wires in one lay, or 3 in one strand | standard |
| Wire rope | Diameter loss around 10 per cent; kink, crush or bird-cage | standard |
| Chain sling | Crack, bend, twist, or elongation near 5 per cent | standard |
| Chain sling | Wear more than 10 per cent of the link diameter | standard |
| Clamp | Worn jaw teeth, loose pivot, weak spring, crack at jaw root | standard |

The criteria are percentages rather than sizes because the gear comes in every size. A 5 per cent stretch on a short link and on a long link are the same loss of strength, even though the millimetres differ.

One criterion is enough to condemn. You do not average them, and you do not pass a hook because only the throat is out. Write that in the answer: any single failure removes the item from service.

### 4.4 Sling angles

A two-leg sling does not halve the load. Each leg carries a share that grows as the legs spread. The formula is **tension per leg = W ÷ (2 cos(α/2))**, where α is the included angle between the legs.

| Included angle between legs | Share of the load in each leg |
|---|---|
| 30 degrees | 0.52 W |
| 60 degrees | 0.58 W |
| 90 degrees | 0.71 W |
| 120 degrees | 1.00 W |
| 150 degrees | 1.93 W |

Read the table as a warning. At 120 degrees each leg carries the whole load, so a two-tonne sling lifts two tonnes, not four. At 150 degrees each leg carries nearly twice the load. That is why the rule is **keep the included angle at 90 degrees or less**.

Worked once, with a four-tonne load. At 90 degrees the tension per leg is 0.71 × 4, which is 2.84 tonnes. A pair of 3-tonne slings just covers it. At 150 degrees the same load puts 7.7 tonnes on each leg, so the slings part before the load moves.

The arithmetic also explains the deck's rule on derated gear (`slide 142`). A sling that has lost 10 per cent of its strength, used at a wide angle, fails at a load nobody expected. Two small errors multiply.

## 5. Diagrams to draw

Three sketches cover every diagram mark in this module. Draw them small, label every part, and put the number next to the label.

### 5.1 Four guards on one plate

Draw one horizontal line as the machine frame, and four small panels above it. **Panel 1, fixed:** a belt and pulley inside a sheet-metal box, with a bolt and spanner shown at the corner. Label "tool needed to remove". **Panel 2, interlocked:** a hinged door with a switch at the hinge and a wire running to the motor contactor. Label "opens, power off". **Panel 3, adjustable:** a guard with a slotted bracket and a wing nut, the opening set to the stock thickness. Label "set by hand". **Panel 4, self-adjusting:** a pivoted flap resting on the stock, with a return spring and an arrow showing the flap opening only as wide as the stock.

Two labels carry the marks: "tool needed" on the fixed guard, and "returns to rest" on the self-adjusting one. Those are the phrases that separate the four types.

Add one line under the plate: fixed for the drive, interlocked for access, adjustable for mixed stock, self-adjusting for one product family. That line is the answer to "which guard where".

Draw it in five minutes and keep it crude. Four rectangles and one arrow each is enough. The marker is reading your labels, not your draughtsmanship, so label first and shade later.

### 5.2 The point of operation and the two zones

Draw a press in section. The **bed** is a thick horizontal block at the bottom, the **ram** a block above it, and the **die** between them. Mark the gap as the **point of operation**. Draw a hand approaching the die with a crossed-out arrow, and a light curtain as two vertical posts with dashed beams across the front.

Now add the drive at the top right: **flywheel**, **belt**, **pulley**, with a fixed box around them. Label that box "power transmission apparatus". Add the **two-hand control** as two buttons on a console, with a note "both held, hands away from the die".

Three labels earn the marks: point of operation, power transmission apparatus, and the two-hand control as a device rather than a guard. A fourth, the light curtain's blind spot at the top edge, earns the follow-up.

The common error is drawing the guard only at the die. That picture answers half the question, because the belt and flywheel are still open at the top. Draw both zones and you have answered the second half before it is asked.

Keep the scale honest enough to show the gap. If the die gap is drawn wider than the ram, the sketch stops making sense and the labels stop helping.

### 5.3 The sling angle triangle

Draw a master link at the top, two legs going down and out, and a load block at the bottom joining them. Mark the **included angle** α between the legs. Put an arrow on each leg labelled T, and an arrow on the load labelled W.

Write the values beside the triangle: 60 degrees gives 0.58 W per leg, 90 gives 0.71 W, 120 gives 1.00 W. Add the formula **T = W ÷ (2 cos(α/2))** in the corner.

Then draw the same triangle with α at 150 degrees, legs almost horizontal, and the labels 1.93 W. The pair of drawings makes the point that widening the angle raises the tension, which is the mark the question is really after.

Work the numbers once on the sketch. A four-tonne load at 90 degrees puts 2.84 tonnes on each leg, so 3-tonne slings are just adequate. The same load at 150 degrees puts 7.7 tonnes on each leg, so the sling fails. Two numbers beside two triangles say more than a paragraph.

Label the angle as the **included** angle, not the angle to the horizontal. Most textbooks draw it one way and most riggers say it the other, and the examiner will mark the number you compute.

**Mark anchor.** Every diagram in this module is worth more with one number on it than with three pretty labels. Put 1/8 inch on the grinder, 35 feet on the welding sketch, and 120 degrees on the sling.

---

## 6. Say-this-if-grilled

### 6.1 The sentences to have ready

Short, defensible sentences. Each one answers a follow-up question that a marker or an interviewer actually asks. Say them as statements, not as quotations.

- The guard has to work on the day the operator is tired, rushed and looking away. That is the design test, not the average day.
- Guard blocks, device reacts, distance removes the reach, feeding removes the hand. Four strategies, one purpose.
- The drive needs guarding as much as the die does. A sleeve caught in a coupling is the same amputation.
- An interlock can be defeated, and the deck shows one taped down. So the control is maintenance and supervision.
- A two-hand control protects the hands on the buttons. It does not protect the person loading from the side.
- A light curtain protects the plane it crosses. A hand over the top or round the side is not in that plane.
- A ring test finds a cracked wheel. It does not test strength, and saying it does is a wrong answer.
- A hook is scrap at 15 per cent throat opening, whatever the latch looks like. The latch carries no load.
- A hook repaired by welding is an unapproved hook, not a repaired one. The deck says it twice.
- Two legs at 120 degrees means each leg carries the whole load. A two-tonne sling then lifts two tonnes.
- Sparks reach 35 feet, so the fire watch is 35 feet wide and 30 minutes long.
- Manual handling is a design problem before it is a technique problem. Remove the lift, then teach the lift.
- Push before pull, because pushing puts the load in front of your legs and your weight behind it.
- Guarding and inspection are planned activities. If they depend on good intentions, they stop on the busy shift.

If the follow-up is what you would do first, answer with the hierarchy. Eliminate the hazard by design, then guard it. Then add a device, then warn, then protect the person. Guarding sits above PPE, and saying so ends the argument.
