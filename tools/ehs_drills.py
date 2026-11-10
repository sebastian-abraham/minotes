"""ehs_drills.py — 20CET453 Environmental Health and Safety practice.

One combined drill per module: a full 7–8 mark answer prompt, the model answer,
and the marks scheme. Descriptive subject — the tutor grades the structure.
"""

EHS_DRILLS = [
    dict(id="e1", m=1, type="write", topic="occupational disease + prevention",
         q="Describe silicosis and asbestosis, then give the preventive measures for occupational respiratory diseases. (8 marks)",
         model="""Silicosis: fibrosis of the lungs from inhaling free crystalline silica (quartz) dust — quarrying, stone crushing, sand blasting, tunnelling. Particles under 5 microns reach the alveoli; macrophages engulf them and die, releasing fibrogenic factors, so nodular fibrosis develops. Symptoms: progressive dyspnoea, dry cough, reduced chest expansion. Incurable; disability continues after exposure stops.

Asbestosis: fibrosis from inhaled asbestos fibres (longer than 10 microns), with pleural thickening and a latency of 10 to 20 years. Also causes lung cancer, mesothelioma and asbestos warts.

Prevention (the marks are here):
1. Substitution: non-siliceous abrasives, fibre-free insulation.
2. Engineering control: local exhaust ventilation, wet drilling, enclosed blasting cabinets, water suppression.
3. Administrative: job rotation to cut exposure hours, pre-employment and periodic chest X-ray and spirometry, exposure records.
4. PPE: approved respirator (P100 / FFP3), coveralls, no eating or smoking in the area, wash and change before leaving.
5. Health surveillance and notification of occupational disease; statutory exposure limits and dust sampling.""",
         points=["define both diseases with cause and latency", "mechanism of fibrosis",
                 "substitution", "engineering control (LEV, wet methods)", "administrative (rotation, surveillance)",
                 "PPE and respirator", "statutory limits"]),
    dict(id="e2", m=2, type="write", topic="chemical forms + control",
         q="Classify chemical hazards by physical form and give the control measures for each. (8 marks)",
         model="""Six physical forms:
1. Dust: solid particles from crushing, grinding or blasting (silica, cement, coal). Control: water suppression, local exhaust ventilation, enclosure, respirator.
2. Fumes: solid particles from condensation of metal vapour (welding, smelting), usually under 1 micron. Control: LEV at the arc, welding helmet with fume respirator, keep the head out of the plume.
3. Vapour: gaseous form of a liquid or solid at room temperature (solvents, petrol). Control: closed containers, local exhaust, low-volatility solvents, organic-cartridge respirator.
4. Fog: liquid droplets suspended in air (oil mist, acid mist, paint spray). Control: spray booth, mist eliminator, water curtain.
5. Gas: gaseous at normal temperature (CO, H2S, chlorine, ammonia). Control: leak detection and alarms, ventilation, closed systems, SCBA in confined spaces.
6. Aerosol or mist: general term for airborne particles and droplets; controlled by the same hierarchy.

Hierarchy for all forms: eliminate, substitute, engineering control (enclosure, LEV, ventilation), administrative (rotation, training, monitoring), PPE last.
Routes of entry: inhalation (main), skin absorption, ingestion, injection.""",
         points=["six forms named", "one example per form", "control per form",
                 "hierarchy of controls", "routes of entry"]),
    dict(id="e3", m=3, type="write", topic="scaffolding + electrical",
         q="Formulate the safety precautions for scaffolding and working platforms, and explain the common electrical hazards on a construction site. (7 + 8 marks)",
         model="""Scaffolding and working platforms:
- Designed and erected by a competent person; stable base with sole plates; platform width adequate for the work (about 0.9 m).
- Standards, ledgers and transoms braced; diagonal bracing and ties to the building at intervals.
- Guardrails at about 1 m with toe boards; full decking with no gaps; no makeshift planks.
- Inspected before first use, after alteration and after bad weather; tagged safe to use.
- Never overload; stack materials evenly; no work during high wind.
- Access by a tied ladder, not by climbing the frame.
- Fall protection: harness and lanyard, nets, helmets with chin straps.

Electrical hazards on site:
1. Contact with overhead lines: keep clearance, use goalposts and barriers, de-energise first.
2. Damaged temporary wiring: route cables in trenches or on insulated hangers, never on the ground.
3. Defective tools: 110 V site tools, RCD/ELCB protection, portable residual current devices.
4. Wet conditions: water and damp raise conductivity; keep connections off the ground, use IP-rated boxes.
5. Overloading and poor earthing: correct fuses, earthing at every outlet, distribution boards.
6. Voltage fluctuation: surge protection, stabilisers, correct cable sizing, lockout-tagout.
7. Effect of shock on the body: 1 to 5 mA tingling, 10 to 30 mA muscle spasm (no-let-go), 30 to 75 mA respiratory arrest, above 100 mA ventricular fibrillation and burns. Severity depends on current, path, duration and skin condition.
Control summary: isolate, earth, RCD, insulated tools, competent electrician only.""",
         points=["competent person and inspection regime", "guardrails, toe boards, decking, bracing",
                 "overload and wind limits", "overhead lines and cable routing", "RCD/ELCB and 110 V tools",
                 "shock current ranges and effects"]),
    dict(id="e4", m=4, type="write", topic="air pollution + clean coal",
         q="Explain the effects of air pollution on plants and human health, and outline clean coal combustion technology. (7 + 8 marks)",
         model="""Effects on plants:
- SO2 and NOx enter stomata: chlorosis, necrosis, reduced photosynthesis; acid rain acidifies soil and leaches nutrients.
- Ozone damages leaf tissue and cuts yield; fluoride accumulates in leaves and stunts growth.
- Particulates coat leaves and block stomata, reducing light interception and growth.

Effects on human health:
- PM2.5 and PM10: respiratory and cardiovascular disease, asthma, bronchitis, reduced lung function.
- SO2: bronchoconstriction, eye and throat irritation. NOx: smog and respiratory infection.
- CO: binds haemoglobin as carboxyhaemoglobin, impairing oxygen transport.
- Ozone: airway inflammation. Lead and VOCs: neurological and carcinogenic effects.
- Also affects animals (respiratory damage, heavy-metal accumulation) and materials (corrosion, soiling).

Clean coal combustion technology — cut emissions per unit of coal burned:
1. Pulverised coal with staged combustion and low-NOx burners.
2. Fluidised bed combustion (bubbling or circulating): limestone in the bed absorbs SO2; lower bed temperature cuts NOx.
3. Integrated gasification combined cycle: coal gasified to syngas, cleaned, then burned in a gas turbine.
4. Supercritical and ultra-supercritical boilers: higher efficiency, less CO2 per kWh.
5. Post-combustion cleaning: electrostatic precipitator for particulates, flue-gas desulphurisation with limestone slurry for SO2, selective catalytic reduction for NOx.
6. Carbon capture and storage as the final step.""",
         points=["plant effects: chlorosis, necrosis, acid rain, stomata", "human health by pollutant",
                 "animals and materials", "four combustion technologies", "post-combustion cleaning devices",
                 "efficiency and CO2 angle"]),
    dict(id="e5", m=5, type="write", topic="welfare, PPE, inspection",
         q="Describe the welfare facilities and personal protective equipment required at a construction site, and state the purpose and benefits of safety inspection. (8 marks)",
         model="""Safety inspection — purpose: find hazards and unsafe practices before they cause harm; verify statutory compliance; check that controls still work.
Benefits: prevents accidents and lost time; identifies training needs; keeps records for legal defence; shows management commitment; feeds the safety committee; lowers insurance and compensation cost.
Method: planned schedule with a checklist, a competent team (supervisor, safety officer, worker representative), recorded findings, responsibility and deadline, and verification of rectification on the next visit.

Welfare facilities:
- Drinking water: clean, marked, away from latrines, cooled in hot weather.
- Sanitary accommodation: separate for men and women, cleaned daily, lit.
- Washing facilities, changing rooms and lockers; drying of wet clothing.
- Rest rooms and lunch rooms, away from dusty or dangerous work, with tables and benches.
- Shelters against rain and sun; a first-aid room with a stretcher and trained first-aiders.

First-aid appliances: standard box with antiseptic, sterile dressings, adhesive plasters, bandages, scissors, gloves and eye pads; eyewash near chemical work; stretcher and blanket; names of trained first-aiders posted; a record of treatment.

PPE by body part:
- Head: safety helmet. Eyes and face: goggles or face shield, welding screen for welders.
- Ears: plugs or muffs. Respiratory: dust mask or respirator matched to the hazard.
- Hands: gloves per task (cut-resistant, chemical, electrical). Body: coveralls, apron, high-visibility vest.
- Feet: steel-toe boots, gum boots for wet work. Fall protection: full harness with lanyard.
PPE is the last line of defence: provided free, fitted, maintained and replaced, and worn only because the hazard could not be engineered out.""",
         points=["inspection purpose, benefits and follow-up", "welfare: water, sanitation, rest, shelter",
                 "first-aid box contents and trained person", "PPE list by body part", "PPE is the last line of defence"]),
]
