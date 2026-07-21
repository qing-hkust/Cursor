# Literature review: Solid electrolyte–Li metal contact during stripping/plating

**Focus:** Interfacial contact between a **solid electrolyte (SE)** and **Li metal** in all-solid-state batteries (ASSBs); competition between **creep under stack pressure** vs **surface / vacancy diffusion** under **low pressure**; role of **wetting** and **interlayers**.

**Hypothesis context (yours):** Contact is often attributed to **creep** at **MPa-level** stack pressure, but high pressure is hard to implement in practical cells. **Surface diffusion** (and related vacancy transport) may dominate contact maintenance at **lower pressure**, especially if the metal **wets** the SE (or an interlayer).

**Generated:** 2026-07-12

---

## Executive summary

During **Li stripping**, Li is removed faster than the interface can be replenished → **vacancies accumulate** → **voids** → **contact loss** → higher impedance and localized current focusing (often linked to dendrite initiation on subsequent plating). The field has converged on two mass-transport pathways to heal or prevent voids:

| Mechanism | Typical enabler | Pressure scale | Key literature |
|-----------|-----------------|----------------|----------------|
| **Power-law creep / plastic flow** | Stack pressure, elevated *T* | Often **~3–15 MPa** for Li on LLZO at practical currents | Krauskopf *et al.*; Yan *et al.*; Fleck–Deshpande–McMeeking; Li *et al.* (phase-field + creep) |
| **Vacancy / surface diffusion** | Temperature, **lithiophilic adhesion**, coherent interface, alloy chemistry | Can matter at **low or zero MPa** if adhesion and diffusivity are high | Seymour & Aguadero; Yang & Mo (MD); Feng & Yang & Qi (KMC); Krauskopf (diffusion-limited delithiation); Banerjee & Mukherjee (terrace/step diffusion, 2025) |

**Wetting / adhesion** is not cosmetic: theory and DFT link **work of adhesion** $`W_\mathrm{ad}`$ to **vacancy segregation** at the interface. A widely cited criterion is that void-suppressing vacancy injection into the bulk is favored when **$`W_\mathrm{ad} \gtrsim 2\gamma_\mathrm{Li}`$** (complete wetting / lithiophilicity)—Seymour & Aguadero. **Interlayers** (Au, Ag, Mg-alloy, oxides, artificial SEI) are used to raise adhesion, improve wetting, and change whether creep or diffusion is rate-limiting.

**Implication for your hypothesis:** Literature supports that **low-pressure operation** is viable when **(i)** Li **surface/vacancy diffusivity** is high (elevated *T*, coherent interface, or fast surface paths), and **(ii)** the interface is **lithiophilic** so vacancies do not pin at the SE. Creep is still important when adhesion is poor or currents are high, but it is **not the only** contact-healing mechanism—and recent modeling explicitly elevates **terrace, step, and interlayer surface diffusion** on Li metal (Banerjee *et al.*, 2025).

---

## 1. Problem framing: voids, contact loss, and morphological instability

### 1.1 Stripping vs plating asymmetry

- **Stripping** removes Li from the interface; if the **flux of Li atoms back to the interface** (via diffusion or creep) is insufficient, **voids nucleate and grow** along the Li|SE boundary.
- **Plating** can partially **rewet** voids, but contact loss during stripping often dominates cell resistance rise; plating-induced cracking of SE is a separate failure mode (Porz *et al.*, *Nature Materials* 2021).

### 1.2 Critical stripping current / diffusion limitation

- **Kassem & McCarthy** (*Nature Materials* 2019): **critical stripping current** concept—above a threshold, transport cannot sustain flat interface → dendrite formation on subsequent plating. [DOI 10.1038/s41563-019-0438-9](https://doi.org/10.1038/s41563-019-0438-9)
- **Krauskopf, Mogwitz, Janek *et al.*** (*Advanced Energy Materials* 2019): operando GEIS on Li and Li–Mg | LLZO shows pore formation is tied to **slow vacancy/Li diffusion**; temperature and pressure strongly shift time-to-contact-loss. [DOI 10.1002/aenm.201902568](https://doi.org/10.1002/aenm.201902568)

### 1.3 Reviews (mechanics + interfaces)

- **Porz, Swamy, Chiang** (*Science* 2023): “critical role of **mechanics**” in SSE cells. [DOI 10.1126/science.abg5998](https://doi.org/10.1126/science.abg5998)
- **Wang *et al.*** (*Nature Energy* 2021): **pressure-tailored** Li deposition/dissolution. [DOI 10.1038/s41560-021-00917-3](https://doi.org/10.1038/s41560-021-00917-3)

---

## 2. Creep and stack pressure (dominant paradigm)

### 2.1 Experimental pressure dependence

| Study | System | Main finding |
|-------|--------|--------------|
| **Krauskopf *et al.* 2019** | Li, Li–Mg \| LLZO | **~3.8 MPa** mitigates contact loss at 0.2 mA cm⁻²; **15 MPa** stabilizes capacitance; **Li–Mg** avoids macroscopic pores **without** pressure but hits **diffusion-limited delithiation** |
| **Lu *et al.* 2022** | Working ASSB | In situ void imaging; stack pressure and current jointly control voids. [DOI 10.1126/sciadv.add0510](https://doi.org/10.1126/sciadv.add0510) |
| **Lee, Kazyak, Sakamoto 2022** | Thin Li on LLZO | Void formation and **rewetting** on plating. [DOI 10.1016/j.joule.2022.09.009](https://doi.org/10.1016/j.joule.2022.09.009) |
| **Zaman *et al.* 2023** | Li \| SE | **Temperature + pressure** map of **unrecoverable** voids. [DOI 10.1021/acsami.3c05886](https://doi.org/10.1021/acsami.3c05886) |
| **Asakura *et al.* 2023** | Sulfide SSE | Stack-pressure dependence of stripping/plating. [DOI 10.1021/acsami.3c03552](https://doi.org/10.1021/acsami.3c03552) |
| **Doux *et al.* 2020** | Room-temperature ASSB | Stack pressure design considerations. [DOI 10.1002/aenm.201903253](https://doi.org/10.1002/aenm.201903253) |

### 2.2 Modeling: creep-driven vacancy flux into bulk

- **Yan, Tantratian, Harrison *et al.*** (*Advanced Energy Materials* 2021): **Creep/contact electro-chemo-mechanical** model—on **non-ideal** interfaces with pre-existing defects, **creep-enhanced vacancy flux into Li bulk** dominates over simple interfacial vacancy migration; explains why **~10 MPa** appears in many experiments. [DOI 10.1002/aenm.202102283](https://doi.org/10.1002/aenm.202102283)
- **Fleck, Deshpande, McMeeking** (*J. Power Sources* 2021; *Acta Materialia* 2022; *Electrochimica Acta* 2023; *Mech. Mater.* 2024): void **initiation** and **growth** during stripping; **vacancy diffusion** vs creep competition. [DOI 10.1016/j.jpowsour.2020.229437](https://doi.org/10.1016/j.jpowsour.2020.229437), [DOI 10.1016/j.electacta.2023.143081](https://doi.org/10.1016/j.electacta.2023.143081)
- **Li *et al.* 2025**: coupled **electrochemical–diffusion–mechanical (creep)–phase-field** for void evolution at Li|LLZO; **P–T phase diagram** for void healing. [DOI 10.1021/acsami.4c13564](https://doi.org/10.1021/acsami.4c13564)
- **Zhao, Wang, Martínez-Pañeda 2022**: phase-field void evolution. [DOI 10.1016/j.jmps.2022.104999](https://doi.org/10.1016/j.jmps.2022.104999)

**Takeaway:** Creep is well supported as the **high-pressure** remedy, but models distinguish **ideal flat** vs **defected** interfaces—mechanism shifts between **interfacial vacancy migration** and **creep-fed bulk diffusion**.

---

## 3. Surface diffusion, vacancy transport, and low-pressure regimes

### 3.1 Atomistic and multiscale simulations

| Study | Method | Surface diffusion / diffusion message |
|-------|--------|--------------------------------------|
| **Yang, Liu, Nolan, Mo 2021** | Large-scale **MD** | Stripping/plating on SE; **coherent** vs **incoherent** interfaces; pore nucleation when **Li flux** cannot replenish interface; **pressure–adhesion** map. [DOI 10.1002/adma.202008081](https://doi.org/10.1002/adma.202008081) |
| **Seymour & Aguadero 2021** | DFT + **bond-breaking model** | **Surface → subsurface** vacancy hop barrier **≫** bulk hop (0.24 eV vs ~0.04 eV in Li); segregation suppressed when **$`W_\mathrm{ad} \gtrsim 2\gamma_\mathrm{m}`$**. [DOI 10.1039/d1ta03254b](https://doi.org/10.1039/d1ta03254b) |
| **Feng, Yang, Qi 2022** | DFT + **KMC** + analytics | **Li/Li₂O** (lithiophilic) vs **Li/LiF** (lithiophobic): lithiophobic needs **much higher** pressure to flatten surface; pressure tilts hopping barriers → mimics creep bias on vacancy motion. [DOI 10.1149/1945-7111/ac91aa](https://doi.org/10.1149/1945-7111/ac91aa) |
| **Yang, Qi 2021** | Interface design (*Chem. Mater.*) | Maintaining flat Li during stripping via engineered interfacial chemistry. [DOI 10.1021/acs.chemmater.0c04814](https://doi.org/10.1021/acs.chemmater.0c04814) |
| **Banerjee, Vishnugopi, Mukherjee 2025** | Continuum + kinetics | Explicit **terrace, step, and interlayer surface diffusion** on Li; temperature expands stable-contact regime; links surface diffusivity to overcoming contact loss at high reaction rates. [DOI 10.1002/advs.202515827](https://doi.org/10.1002/advs.202515827) |

### 3.2 “Surface diffusion” in electrodeposition literature (conceptual link)

- **Tang *et al.*** (*Phys. Chem. Chem. Phys.* 2020): **Surface diffusion manifestation** in metal electrodeposition—relevant analogy for how adatom/vacancy mobility smooths interfaces. [DOI 10.1039/d0cp01352h](https://doi.org/10.1039/d0cp01352h)
- **Nature Commun. 2023** (*Li crystallization at solid interfaces*): crystallization kinetics at solid|solid boundaries. [DOI 10.1038/s41467-023-38757-2](https://doi.org/10.1038/s41467-023-38757-2)

### 3.3 Experiments emphasizing diffusion over creep

- **Krauskopf 2019**: Estimates **Li diffusivity** from temperature-dependent delithiation; **50 °C** greatly delays full depletion—**Arrhenius** behavior parallels faster **surface/vacancy** transport.
- **Krauskopf *et al.* (*Joule* 2019)**: Li growth kinetics on LLZO. [DOI 10.1016/j.joule.2019.06.013](https://doi.org/10.1016/j.joule.2019.06.013)
- **Venturi & Viswanathan 2022** (*ACS Energy Lett.*): thermodynamics of **initial void formation** steps. [DOI 10.1021/acsenergylett.2c00550](https://doi.org/10.1021/acsenergylett.2c00550)
- **Barai *et al.* 2024** (*Chem. Mater.*): void formation study with modeling/experiment comparison. [DOI 10.1021/acs.chemmater.3c01708](https://doi.org/10.1021/acs.chemmater.3c01708)

**Synthesis for low pressure:** When **$`W_\mathrm{ad}`$** is high (wetting) and **T** is elevated, **vacancy submergence** and **surface diffusion** can maintain contact **without MPa creep**. When adhesion is poor (LiF-like, lithiophobic), literature consistently shows **creep pressure must rise** toward **10–20 MPa** in KMC-informed estimates (Feng & Qi 2022)—matching the “creep-only” narrative in those systems.

---

## 4. Wetting, lithiophilicity, and interlayers

### 4.1 Why wetting matters (beyond initial contact)

Bare **garnet (LLZO)** is often **poorly wetted** by Li → high interfacial impedance and inhomogeneous current.

| Strategy | Example work | Mechanism |
|----------|--------------|-----------|
| **Ultrathin lithiophilic coating** | **Han *et al.*** (*Science Advances* 2017): ALD **Al₂O₃** or similar on garnet reduces impedance, enables cycling. [DOI 10.1126/sciadv.1601659](https://doi.org/10.1126/sciadv.1601659) |
| **Negating impedance** | **Han *et al.*** (*Nature Materials* 2016). [DOI 10.1038/nmat4821](https://doi.org/10.1038/nmat4821) |
| **Chemical wetting tuning** | **Tuning wettability of molten Li** (*Nature Commun.* 2019). [DOI 10.1038/s41467-019-12938-4](https://doi.org/10.1038/s41467-019-12938-4) |
| **Intrinsic lithiophilicity** | Li–garnet interfacial engineering (*Adv. Funct. Mater.*). [DOI 10.1002/adfm.201906189](https://doi.org/10.1002/adfm.201906189) |
| **Alloy anode (Li–Mg)** | **Krauskopf 2019**: **no macroscopic pores** without external pressure vs pure Li; trade-off is **compositional diffusion limit** |
| **Metal interlayer (Au, Ag, ZnO, etc.)** | Multiple ASSB studies; interlayer converts incoherent Li|SE to **adhesion-controlled** vacancy landscape (linked to Seymour criterion) |
| **Anode-free / interlayer insert** | Recent *Joule*, *Nature Mater.*, *Nature Commun.* 2023–2025 on **alloy interfacial layers** stabilizing plating/stripping |

### 4.2 Coherent vs incoherent interface (MD + DFT)

- **Yang & Mo 2021**: **Coherent** Li|SE interfaces sustain stripping longer at **zero pressure** because vacancy/interstitial carriers form readily and migrate into bulk.
- **Seymour 2021**: **Incoherent** Li|LiCl interfaces break simple $`W_\mathrm{ad}`$ rules—local site energies matter; interlayer design must target **atomic structure**, not just average adhesion.

### 4.3 Transient interfacial behavior

- **Sharafi *et al.* (*Angew. Chem.* 2017)**: **Transient** Li|garnet interface behavior during early cycling. [DOI 10.1002/anie.201708637](https://doi.org/10.1002/anie.201708637)

---

## 5. Temperature effects (often underweighted vs pressure)

- **Yonemoto *et al.* 2017** (*J. Power Sources*): **Temperature** strongly affects Li plating/stripping stability on Ta-doped LLZO.
- **Krauskopf 2019**: Strong **T** dependence of Li diffusivity and time-to-depletion; modest warming above RT can be as impactful as moderate pressure increases.
- **Zaman 2023**: Identifies **unrecoverable** void regimes—some voids cannot be healed by pressure alone at low *T*.
- **Banerjee 2025**: **Temperature** explicitly expands Li **surface diffusivity**-limited stable stripping window.

**Design insight:** For **low-pressure** cells, **elevated operating temperature** (within SE stability window) is a recurring experimental strategy to activate **diffusion-limited** contact healing when creep is weak.

---

## 6. Mapping literature to your hypothesis

| Your claim | Literature support | Caveats |
|------------|-------------------|---------|
| Creep under pressure stabilizes contact | Extensive (Krauskopf, Yan, Fleck group, Li phase-field 2025) | Requires **MPa** scale for pure Li on LLZO at mA cm⁻² currents |
| High pressure is practically challenging | Acknowledged in Seymour 2021; Doux 2019; Porz 2023 | Pouch/cylindrical formats need external fixtures or swelling management |
| **Surface diffusion** important at **low pressure** | Supported by MD (Yang & Mo), KMC (Feng & Qi), Seymour adhesion theory, Banerjee 2025 terrace/step diffusion, Krauskopf diffusion-limited delithiation | Must distinguish **Li metal surface diffusion** from **vacancy bulk diffusion**; both appear in models |
| **Wetting** helps contact | Strong: Han garnet coatings, $`W_\mathrm{ad} \gtrsim 2\gamma`$ criterion, lithiophilic Li₂O vs LiF KMC | Wetting improves **initial** and **thermodynamic** vacancy injection; kinetics still need sufficient **T** or current below CCD |
| **Interlayers** enable low-pressure operation | Li–Mg (Krauskopf), Au/Ag/oxide coatings, artificial SEI—each changes diffusion vs creep balance | Alloys may shift failure to **compositional depletion** rather than voids |

### Proposed research gaps (where your work could contribute)

1. **Quantitative regime map** on one SE system: axes = **stack pressure (0–5 MPa)**, **temperature**, **current density**; metric = contact area fraction / interfacial impedance—separate **creep-dominated** vs **surface-diffusion-dominated** regions (Banerjee 2025 begins this; few operando experiments validate at **sub-MPa**).
2. **Direct operando measurement** of Li **surface diffusion** (e.g., tracer methods, grain-boundary-sensitive probes) at Li|SE during stripping—most evidence is inferential via void morphology.
3. **Wetting metrics linked to kinetics:** $`W_\mathrm{ad}`$ from DFT/contact angle vs **critical stripping current** at **fixed low pressure**—systematic interlayer library (Seymour + Feng & Qi framework).
4. **Non-Li metals / Zn** analogies: surface diffusion in electrodeposition (d0cp01352h) may translate to **Zn|solid electrolyte** if such systems are in scope.

---

## 7. Recommended reading order

1. **Krauskopf *et al.* 2019** (*Adv. Energy Mater.*) — operando T, P, alloy; diffusion limitation  
2. **Seymour & Aguadero 2021** — adhesion, vacancy segregation, wetting criterion  
3. **Yan *et al.* 2021** — creep vs vacancy migration on defected interfaces  
4. **Yang & Mo 2021** (*Adv. Mater.*) — atomistic stripping/plating, coherent interfaces  
5. **Feng & Yang & Qi 2022** (JES) — lithiophilic vs lithiophobic KMC + pressure  
6. **Lu *et al.* 2022** (*Sci. Adv.*) — voids in working cells  
7. **Banerjee *et al.* 2025** (*Adv. Sci.*) — explicit Li surface diffusion modes  
8. **Han *et al.* 2016/2017** — garnet wetting / interlayer prototype  

---

## 8. References (selected, with DOI)

1. Krauskopf T. *et al.*, *Adv. Energy Mater.* **2019**, [10.1002/aenm.201902568](https://doi.org/10.1002/aenm.201902568)  
2. Kassem M., McCarthy D.T., *Nature Mater.* **2019**, [10.1038/s41563-019-0438-9](https://doi.org/10.1038/s41563-019-0438-9)  
3. Seymour I.D., Aguadero A., *J. Mater. Chem. A* **2021**, [10.1039/d1ta03254b](https://doi.org/10.1039/d1ta03254b)  
4. Yang M. *et al.*, *Adv. Mater.* **2021**, [10.1002/adma.202008081](https://doi.org/10.1002/adma.202008081)  
5. Yan H. *et al.*, *Adv. Energy Mater.* **2021**, [10.1002/aenm.202102283](https://doi.org/10.1002/aenm.202102283)  
6. Feng M., Yang C.-T., Qi Y., *J. Electrochem. Soc.* **2022**, [10.1149/1945-7111/ac91aa](https://doi.org/10.1149/1945-7111/ac91aa)  
7. Yang C.-T., Qi Y., *Chem. Mater.* **2021**, [10.1021/acs.chemmater.0c04814](https://doi.org/10.1021/acs.chemmater.0c04814)  
8. Shishvan S.S., Fleck N.A., Deshpande V.S., *J. Power Sources* **2021**, [10.1016/j.jpowsour.2020.229437](https://doi.org/10.1016/j.jpowsour.2020.229437)  
9. Shishvan S.S. *et al.*, *Electrochimica Acta* **2023**, [10.1016/j.electacta.2023.143081](https://doi.org/10.1016/j.electacta.2023.143081)  
10. Lu Y. *et al.*, *Science Advances* **2022**, [10.1126/sciadv.add0510](https://doi.org/10.1126/sciadv.add0510)  
11. Lee K. *et al.*, *Joule* **2022**, [10.1016/j.joule.2022.09.009](https://doi.org/10.1016/j.joule.2022.09.009)  
12. Zaman W. *et al.*, *ACS Appl. Mater. Interfaces* **2023**, [10.1021/acsami.3c05886](https://doi.org/10.1021/acsami.3c05886)  
13. Li K. *et al.*, *ACS Appl. Mater. Interfaces* **2025**, [10.1021/acsami.4c13564](https://doi.org/10.1021/acsami.4c13564)  
14. Han F. *et al.*, *Nature Mater.* **2016**, [10.1038/nmat4821](https://doi.org/10.1038/nmat4821)  
15. Han F. *et al.*, *Science Advances* **2017**, [10.1126/sciadv.1601659](https://doi.org/10.1126/sciadv.1601659)  
16. Barai P. *et al.*, *Chem. Mater.* **2024**, [10.1021/acs.chemmater.3c01708](https://doi.org/10.1021/acs.chemmater.3c01708)  
17. Banerjee S. *et al.*, *Adv. Science* **2025**, [10.1002/advs.202515827](https://doi.org/10.1002/advs.202515827)  
18. Porz L. *et al.*, *Science* **2023**, [10.1126/science.abg5998](https://doi.org/10.1126/science.abg5998)  
19. Wang C. *et al.*, *Nature Energy* **2021**, [10.1038/s41560-021-00917-3](https://doi.org/10.1038/s41560-021-00917-3)  
20. Tang Y. *et al.*, *Phys. Chem. Chem. Phys.* **2020**, [10.1039/d0cp01352h](https://doi.org/10.1039/d0cp01352h)  

---

<!-- provenance: curated review, Li|solid-electrolyte contact, creep vs surface diffusion, 2026-07-12 -->
