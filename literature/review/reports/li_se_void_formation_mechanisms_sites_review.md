# Literature review: Void formation at the Li metal | solid electrolyte interface

**Focus:** Mechanisms of **voiding during Li stripping** in all-solid-state batteries (ASSBs), with emphasis on **where voids nucleate and grow** and how those sites are tied to the governing physics.

**Relation to prior note:** Companion to [`solid_electrolyte_li_contact_surface_diffusion_review.md`](solid_electrolyte_li_contact_surface_diffusion_review.md) (2026-07-12), which framed contact loss as a competition between **creep under stack pressure** and **surface/vacancy diffusion** under wetting. This document zooms in on **voiding mechanisms** and the **nature of voiding sites**.

**Generated:** 2026-07-18

---

## Executive summary

During **discharge (stripping)**, Li is oxidized at the Li|SE contact and leaves the anode as $`\mathrm{Li}^+`$. If atoms/vacancies cannot rearrange fast enough to keep a continuous solid–solid contact, **voids** open, interfacial resistance rises, current constricts at remaining contact patches, and subsequent **plating** is more likely to form filaments/dendrites near those patches (Kassem & McCarthy 2019; Raj *et al.* 2022).

The literature does **not** agree on a single nucleation story. Competing (and sometimes complementary) pictures are:

| Mechanism class | Core idea | Preferred / implied sites | Key refs |
|-----------------|-----------|---------------------------|----------|
| **Vacancy accumulation / coalescence** | Stripping injects vacancies at the interface faster than they leave; vacancies cluster into pores | Flat contact → bulk injection if adhesion high; otherwise interfacial segregation; facet-dependent | Krauskopf 2019; Seymour & Aguadero 2021; Venturi & Viswanathan 2022 |
| **Growth of pre-existing interfacial defects** | As-assembled pores/asperities trap vacancies and grow; creep-enhanced vacancy flux needed to heal | **Pre-existing pores**, roughness pits, imperfect contact patches on SE | Yan *et al.* 2021; Lu *et al.* 2022 |
| **Flux focusing + creep around imperfections** | Current concentrates at edges of contact / impurities; power-law creep grows voids | **Impurity particles**, contact-patch perimeters, micro-void edges | Shishvan / Fleck / Deshpande / McMeeking series |
| **Solute / insulating deposit coverage** | Impurities/solutes left behind by stripping reduce contact area (may not need classical void growth) | **Deposited solute islands** on the SE face | Agier *et al.*; Shishvan failure reviews |
| **Heterogeneous kinetics (GB, facets, chemistry)** | Local $`k`$, $`D`$, adhesion vary in space → pits form where stripping is fast or healing is slow | **Li grain interiors** (not Li GBs as sinks); SE GBs as current hotspots; lithiophobic chemistries (LiF-like); specific Li facets | Fuchs EBSD; Yoon MD; Banerjee 2025–2026; Feng & Qi 2022 |

**Site–mechanism rule of thumb:**  
- If voids grow from **as-built gaps / SE roughness**, think **defect-trapping + creep healing** (Yan).  
- If voids appear inside **Li grains** while Li GBs stay in contact longer, think **GB-mediated vacancy conduits** (Fuchs; Yoon).  
- If voids track **SE grain-boundary projections** or current hotspots, think **electrochemical nonuniformity** in the ceramic.  
- If voids correlate with **facet / SEI chemistry**, think **vacancy phase separation thermodynamics** (Venturi).  
- If models deny bulk vacancy driving force in a thinning electrode, think **mechanical flux focusing / impurity-centered growth** (Shishvan *et al.* 2023).

---

## 1. Problem statement and stripping–plating asymmetry

### 1.1 What fails during stripping

- Continuous Li|SE contact is required for ion transfer. Stripping removes Li from the contacting plane.
- **Voids** = regions of lost solid–solid contact (vacuum / free surface inside the anode side of the interface).
- Consequences: higher interfacial impedance, **current constriction**, elevated local overpotential, and lowered critical current for filament growth on the next charge (Kassem & McCarthy, *Nat. Mater.* 2019, [10.1038/s41563-019-0438-9](https://doi.org/10.1038/s41563-019-0438-9); Raj *et al.*, *Nat. Mater.* 2022, [10.1038/s41563-022-01264-8](https://doi.org/10.1038/s41563-022-01264-8)).

### 1.2 Operando picture

- **Krauskopf, Mogwitz, Janek *et al.*** (*Adv. Energy Mater.* 2019): operando GEIS on Li and Li–Mg | LLZO — pore formation tied to **slow vacancy/Li transport**; $`T`$ and stack pressure shift time-to-contact-loss. [10.1002/aenm.201902568](https://doi.org/10.1002/aenm.201902568)
- **Lu *et al.*** (*Sci. Adv.* 2022): voids in working cells; stack pressure and current jointly control void evolution. [10.1126/sciadv.add0510](https://doi.org/10.1126/sciadv.add0510)
- **Lee, Kazyak, Sakamoto** (*Joule* 2022): void formation and partial **rewetting** on plating for thin Li on LLZO. [10.1016/j.joule.2022.09.009](https://doi.org/10.1016/j.joule.2022.09.009)
- **Zaman *et al.*** (*ACS Appl. Mater. Interfaces* 2023): some voids become **unrecoverable** depending on $`T`$–$`P`$ history. [10.1021/acsami.3c05886](https://doi.org/10.1021/acsami.3c05886)

Plating can partially heal contact, but stripping-induced morphology often sets where filaments nucleate later.

---

## 2. Mechanism taxonomy (how voids form and grow)

### 2.1 Flux balance at the interface

A useful bookkeeping picture (used by Yan, Barai, Banerjee, and related models) compares:

$$
J_{\mathrm{migration}} \quad\text{(Li removed electrochemically)}
$$

against healing fluxes

$$
J_{\mathrm{diffusion}} + J_{\mathrm{creep}} + J_{\mathrm{surface}}
\quad\text{(vacancies / atoms rearranged)}.
$$

Voids grow when $`J_{\mathrm{migration}}`$ persistently exceeds the sum of healing fluxes over a contact region.

### 2.2 Vacancy generation and diffusion (classical stripping narrative)

**Hypothesis:** Oxidation leaves vacant lattice sites at the interface; if vacancies diffuse into the Li bulk slower than they are created, they coalesce into pores (Fig. 2-style cartoon in many papers; Krauskopf 2019).

**Adhesion modifies the sink:**

- **Seymour & Aguadero** (*J. Mater. Chem. A* 2021): surface→subsurface vacancy hops can be much harder than bulk hops; vacancy **segregation at the interface** is suppressed when the work of adhesion is high,

$$
W_{\mathrm{ad}} \gtrsim 2\gamma_{\mathrm{Li}},
$$

favoring injection into the bulk (lithiophilic / complete wetting). [10.1039/d1ta03254b](https://doi.org/10.1039/d1ta03254b)

- **Yang & Mo** (*Adv. Mater.* 2021): MD — coherent interfaces sustain stripping longer at low pressure because carriers form and migrate into bulk; incoherent interfaces pore earlier. [10.1002/adma.202008081](https://doi.org/10.1002/adma.202008081)

- **Feng, Yang & Qi** (*J. Electrochem. Soc.* 2022): Li/Li$`_2`$O (lithiophilic) vs Li/LiF (lithiophobic) KMC — lithiophobic chemistry needs much higher pressure to keep the interface flat. [10.1149/1945-7111/ac91aa](https://doi.org/10.1149/1945-7111/ac91aa)

**Challenge to homogeneous vacancy coalescence:**

- **Shishvan, Fleck, McMeeking & Deshpande** (*Electrochim. Acta* 2023): Onsager variational analysis — in a **homogeneous** thinning electrode there is **no driving force** for vacancies to diffuse into the bulk in the way many models assume; thinning/drift annihilates interfacial vacancies. They argue that literature “vacancy coalescence in homogeneous Li” is incomplete. [10.1016/j.electacta.2023.143081](https://doi.org/10.1016/j.electacta.2023.143081)

This does **not** erase vacancy physics; it pushes the field toward **heterogeneous sites** (defects, impurities, GBs, facets) where gradients and flux focusing exist.

### 2.3 Pre-existing defects + creep-enhanced vacancy transport

**Yan *et al.*** (*Adv. Energy Mater.* 2021) distinguish:

| Interface type | Dominant healing path | Implication for sites |
|----------------|----------------------|------------------------|
| Ideal flat | Interfacial vacancy diffusion into bulk can suffice even at low $`P`$ (KMC-like) | Nucleation hard; uniform thinning |
| Non-ideal with **pre-existing pores** | Vacancies are **trapped by defect surfaces** (TLK-like); $`J_{\mathrm{diffusion}}`$ drops; **$`J_{\mathrm{creep}}`$** under stack pressure must carry vacancies into bulk | Voids grow from **as-built interfacial defects** |

[10.1002/aenm.202102283](https://doi.org/10.1002/aenm.202102283)

**Site nature here:** geometric imperfections of the **assembled Li|SE contact** (pores, roughness valleys, incomplete wetting patches)—not necessarily crystallographic special sites.

### 2.4 Flux focusing and power-law creep around imperfections

Fleck–Deshpande–McMeeking / Shishvan line (*J. Power Sources* 2021; *Acta Mater.* 2022; reviews ~2023):

- Pre-existing **micro-voids or impurity particles** concentrate the stripping current at their periphery.
- Modified Butler–Volmer kinetics coupled to creep (local resistance ↓ as dislocation density ↑) **amplifies flux focusing**.
- Void **growth** is then largely a **creep** problem around those foci.

**Site nature:** **impurities / particles / micro-void edges** at the interface; growth morphology reflects contact-line mechanics more than homogeneous spinodal-like vacancy clustering.

Related phase-field electro-chemo-mechanics: Zhao, Wang & Martínez-Pañeda (*JMPS* 2022); Li *et al.* (*ACS Appl. Mater. Interfaces* 2025) $`P`$–$`T`$ maps for void healing. [10.1016/j.jmps.2022.104999](https://doi.org/10.1016/j.jmps.2022.104999), [10.1021/acsami.4c13564](https://doi.org/10.1021/acsami.4c13564)

### 2.5 Solute / insulating deposits (contact loss without classical voids)

Shishvan / Agier analyses propose that **solutes or insulating species** dissolved in Li can be left on the SE interface as stripping proceeds, reducing active contact fraction and raising cell voltage—even when classical void growth around large particles is weak. Sites are then **chemically deposited patches**, not necessarily open cavities.

### 2.6 Surface diffusion modes on Li (terrace / step / interlayer)

**Banerjee, Vishnugopi & Mukherjee** (*Adv. Sci.* 2025; follow-on *ACS Appl. Mater. Interfaces* 2026): explicit **terrace, step, and interlayer** vacancy/surface diffusion control morphological evolution; temperature expands the stable-contact window; **surface heterogeneities (e.g. Li GBs)** induce spatial variations in local rates and **rapid surface pits**. [10.1002/advs.202515827](https://doi.org/10.1002/advs.202515827), [10.1021/acsami.5c14957](https://doi.org/10.1021/acsami.5c14957)

**Barai *et al.*** (*Chem. Mater.* 2024): phase-field — relative bulk vs surface Li diffusivities + current set final pore morphology; $`T`$ and pressure mitigate voids. [10.1021/acs.chemmater.3c01708](https://doi.org/10.1021/acs.chemmater.3c01708)

---

## 3. Nature of voiding sites (tied to mechanism)

This section is the core mapping from **where** to **why**.

### 3.1 Pre-existing interfacial contact defects (SE topography / assembly)

| Observation / claim | Mechanistic link |
|---------------------|------------------|
| SE surfaces are rarely atomically flat; residual pores after stack assembly are common | Provide free surfaces that **trap vacancies** and act as ready-made nuclei (Yan 2021) |
| Stack pressure reduces void growth | Creep closes gaps and enhances vacancy flux away from defects |
| Ideal-flat simulations underpredict voiding vs experiment | Real cells are in the **non-ideal defect** regime |

**Site identity:** geometric **contact imperfections** at Li|SE (pores, asperities, incomplete-wetting islands).

### 3.2 Grain boundaries in the Li metal anode

| Finding | Mechanistic link |
|---------|------------------|
| **Fuchs *et al.***: electrodeposited Li/Na show large columnar grains; **voids initiate within grains**, not preferentially at Li GBs | Li GBs act as **fast vacancy diffusion conduits** ($`D_{\mathrm{GB}} \gg D_{\mathrm{bulk}}`$), delaying contact loss at GBs |
| **Yoon *et al.*** atomistics: Li GB diffusion **3–6 orders** faster than bulk; finer Li grains extend stripping time before contact loss | Microstructure engineering of **anode grain size** changes effective diffusivity |
| Banerjee 2026: Li GBs as surface heterogeneities → **spatial variation of rates → pits** | GBs can also **destabilize morphology** by nonuniform kinetics even if they transport vacancies well |

**Site identity:** often **grain interiors** (slow bulk paths) and **pit sites tied to kinetic contrast** at GBs—not simple “GB = void nucleus” like ceramic fracture.

Reviewed in the broader GB context: arXiv grain-boundary review for ceramic SSBs (2025), [arxiv.org/html/2508.06866](https://arxiv.org/html/2508.06866v1).

### 3.3 Grain boundaries and electronic inhomogeneity in the solid electrolyte

SE GBs matter more for **plating / filament** pathways (electronic shorts, lower band gap at LLZO GBs—Liu, Song, etc.), but they also **modulate voiding indirectly**:

- Nonuniform Li$`^+`$ conductivity at grains vs GBs → **current focusing** → spatially uneven stripping → contact inhomogeneity after cycles (reported for LLZO systems).
- Argyrodite GB excess volume / soft regions may promote local delamination precursors (Sadowski & Albe).

**Site identity:** **projections of SE microstructural heterogeneity** onto the anode contact plane (hotspots), rather than voids sitting “inside” the ceramic during stripping.

### 3.4 Crystallographic facets of Li (thermodynamic vacancy clustering)

**Venturi & Viswanathan** (*ACS Energy Lett.* 2022; earlier arXiv stripping thermodynamics):

- Initial step of voiding = **vacancy congregation** (regular-solution critical temperature for vacancy solubility).
- Bare Li slabs: **(111)** least prone to pitting; **(100)/(110)** favor vacancy phase separation / step roughening.
- With SEI interfaces, only **Li(110)|Li$`_2`$CO$`_3`$** among studied pairs retains void-suppressing character in their analysis.

[10.1021/acsenergylett.2c00550](https://doi.org/10.1021/acsenergylett.2c00550)

**Site identity:** **facet-specific surface sites** and vacancy–vacancy interaction geometry; plating texture becomes a voiding control variable.

### 3.5 Interfacial chemistry (lithiophilic vs lithiophobic)

| Chemistry | Site tendency | Mechanism |
|-----------|---------------|-----------|
| High $`W_{\mathrm{ad}}`$ (Li$`_2`$O-like, good interlayers) | Vacancies less pinned at interface | Injection into bulk / easier healing |
| Low $`W_{\mathrm{ad}}`$ (LiF-like, contaminated garnet) | Vacancies segregate; pores cling to interface | Needs high creep pressure (Feng & Qi) |
| Metallic interlayers (Au, Ag, …) | Shift critical current; alter vacancy barriers | Raj *et al.*: materials with higher CCD also have larger barriers to Li-vacancy accumulation at the interlayer|Li interface |

**Site identity:** **chemically distinct patches** (native SEI, contamination, coatings)—voids track adhesion contrast.

### 3.6 Impurities and solute deposits

| Picture | Site |
|---------|------|
| Flux-focusing void growth (Agier / Shishvan early) | **Impurity particles** on the interface |
| Later solute-coverage failure mode | **Sub-nm solute islands** reducing active area without large cavities |

**Site identity:** foreign-phase / solute **decorations** of the SE surface exposed by stripping.

### 3.7 Contact-patch perimeters and current constriction

Once contact is patchy, remaining contacts carry higher local current → faster local stripping → **perimeter attack** and coalescence of dry regions. Sites are **edges of surviving contact islands**—a morphological instability of the contact pattern, fed by whatever nucleation path started the first gaps (Lu; Lee; constriction literature).

---

## 4. Site–mechanism map (synthesis)

```mermaid
flowchart TD
  S[Stripping current at Li|SE] --> H{Homogeneous ideal contact?}
  H -->|Yes| V[Vacancy injection vs diffusion / surface diffusion]
  V --> F[Facet + adhesion decide clustering vs bulk sink]
  H -->|No| D{Dominant heterogeneity}
  D -->|Pre-existing pores / roughness| P[Vacancy trapping + defect growth]
  P --> C[Creep pressure sets healing]
  D -->|Impurity / solute| I[Flux focusing or coverage loss]
  D -->|Li grain structure| G[Voids in grain interiors; GBs as fast paths]
  D -->|SE GB / conductivity contrast| E[Current hotspots → uneven stripping]
  D -->|Lithiophobic chemistry| L[Interfacial vacancy pinning]
  P --> X[Contact loss / constriction]
  I --> X
  G --> X
  E --> X
  L --> X
  F --> X
  X --> Y[Filament risk on next plating]
```

| If your experiment shows… | Preferentially test… |
|---------------------------|----------------------|
| Voids grow from polishing scratches / SE roughness | Yan-type pre-existing defect + creep |
| Voids inside Li grains; GBs still contacting | Fuchs/Yoon GB-conduit picture; grain-size sweeps |
| Strong chemistry dependence at fixed roughness | Seymour / Feng–Qi adhesion; interlayer library |
| Facet texture correlates with pit density | Venturi facet thermodynamics + plating control |
| Voltage rise without large cavities in SEM | Solute/deposit coverage hypothesis |
| Need ~MPa to cycle pure Li on LLZO | Creep-dominated healing of non-ideal contact |

---

## 5. Connection to the prior contact / creep vs diffusion review

From [`solid_electrolyte_li_contact_surface_diffusion_review.md`](solid_electrolyte_li_contact_surface_diffusion_review.md):

- **Creep** (~3–15 MPa on LLZO-class systems) remains the practical knob when contact is **non-ideal**.
- **Surface/vacancy diffusion** and **wetting** matter most when adhesion is high and $`T`$ activates $`D`$; Banerjee 2025 elevates terrace/step paths at low pressure.
- This voiding-site review adds: **which heterogeneities act as nuclei** and why **homogeneous vacancy coalescence** is contested (Shishvan 2023)—so low-pressure strategies must engineer **sites** (smoother SE, finer Li grains, lithiophilic chemistry, controlled facets), not only average diffusivity.

---

## 6. Open questions

1. **Primary nucleus in a given cell chemistry:** as-built SE pores vs Li-grain-interior pits vs impurity foci—few studies measure all three on one sample set.
2. **Reconcile vacancy thermodynamics with Onsager “no bulk driving force” critiques** under realistic roughness and GB networks.
3. **Operando site attribution:** combine EBSD (Li grains), SE microstructure maps, and void tomography (e.g. X-ray / FIB-SEM) during stripping.
4. **Interlayer design metrics:** link $`W_{\mathrm{ad}}`$, vacancy barriers (Raj), and measured void nucleation density at fixed low stack pressure.
5. **Plating texture → stripping voids:** can intentional Li(111) or Li(110)|carbonate interfaces suppress pits as Venturi suggests?

---

## 7. Suggested reading order

1. Krauskopf *et al.* 2019 — operando stripping voids, $`T`$/$`P`$/alloy  
2. Kassem & McCarthy 2019 — critical stripping current  
3. Yan *et al.* 2021 — pre-existing defects vs ideal interface; creep flux  
4. Seymour & Aguadero 2021 — adhesion and vacancy segregation  
5. Venturi & Viswanathan 2022 — facet-level vacancy clustering  
6. Shishvan *et al.* 2023 (*Electrochim. Acta*) — critique of homogeneous vacancy diffusion  
7. Lu 2022 + Lee 2022 — voids in working / thin-Li cells  
8. Fuchs + Yoon (via GB review 2025) — Li GB vs grain-interior sites  
9. Banerjee 2025/2026 — surface diffusion modes and surface heterogeneities  
10. Raj *et al.* 2022 — voids precede dendrites with interlayers  

---

## 8. Key papers

| Topic | Reference | DOI / link |
|-------|-----------|------------|
| Operando pores Li\|LLZO | Krauskopf *et al.*, *AEM* 2019 | [10.1002/aenm.201902568](https://doi.org/10.1002/aenm.201902568) |
| Critical stripping current | Kassem & McCarthy, *Nat. Mater.* 2019 | [10.1038/s41563-019-0438-9](https://doi.org/10.1038/s41563-019-0438-9) |
| Defects + creep flux | Yan *et al.*, *AEM* 2021 | [10.1002/aenm.202102283](https://doi.org/10.1002/aenm.202102283) |
| Adhesion / vacancy segregation | Seymour & Aguadero, *JMCA* 2021 | [10.1039/d1ta03254b](https://doi.org/10.1039/d1ta03254b) |
| Atomistic stripping | Yang & Mo, *Adv. Mater.* 2021 | [10.1002/adma.202008081](https://doi.org/10.1002/adma.202008081) |
| Facet void thermodynamics | Venturi & Viswanathan, *ACS Energy Lett.* 2022 | [10.1021/acsenergylett.2c00550](https://doi.org/10.1021/acsenergylett.2c00550) |
| Voids precede dendrites | Raj *et al.*, *Nat. Mater.* 2022 | [10.1038/s41563-022-01264-8](https://doi.org/10.1038/s41563-022-01264-8) |
| Working-cell voids | Lu *et al.*, *Sci. Adv.* 2022 | [10.1126/sciadv.add0510](https://doi.org/10.1126/sciadv.add0510) |
| Vacancy diffusion critique | Shishvan *et al.*, *Electrochim. Acta* 2023 | [10.1016/j.electacta.2023.143081](https://doi.org/10.1016/j.electacta.2023.143081) |
| Phase-field voids | Barai *et al.*, *Chem. Mater.* 2024 | [10.1021/acs.chemmater.3c01708](https://doi.org/10.1021/acs.chemmater.3c01708) |
| Surface diffusion / pits | Banerjee *et al.*, *Adv. Sci.* 2025; *ACS AMI* 2026 | [10.1002/advs.202515827](https://doi.org/10.1002/advs.202515827) |
| GB roles (SE + anode) | Ceramic SSB GB review 2025 | [arXiv:2508.06866](https://arxiv.org/abs/2508.06866) |
| Prior companion note | Contact: creep vs surface diffusion | [local review](solid_electrolyte_li_contact_surface_diffusion_review.md) |

---

## References (BibTeX snippet)

```bibtex
@article{Krauskopf2019,
  author  = {Krauskopf, Thorsten and others},
  title   = {Lithium Metal Anode Materials Design: Coupling of Creep and Vacancy Diffusion for Contact Maintenance},
  journal = {Advanced Energy Materials},
  year    = {2019},
  doi     = {10.1002/aenm.201902568}
}
@article{Yan2021,
  author  = {Yan, Hanghang and others},
  title   = {How Does the Creep Stress Regulate Void Formation at the Lithium--Solid Electrolyte Interface during Stripping?},
  journal = {Advanced Energy Materials},
  year    = {2021},
  doi     = {10.1002/aenm.202102283}
}
@article{Seymour2021,
  author  = {Seymour, Ieuan D. and Aguadero, Ainara},
  title   = {Connecting Vacancy Segregation and Work of Adhesion at Metal--Solid Electrolyte Interfaces},
  journal = {Journal of Materials Chemistry A},
  year    = {2021},
  doi     = {10.1039/d1ta03254b}
}
@article{Venturi2022,
  author  = {Venturi, Victor and Viswanathan, Venkatasubramanian},
  title   = {Thermodynamic Analysis of Initial Steps for Void Formation at Lithium/Solid Electrolyte Interphase Interfaces},
  journal = {ACS Energy Letters},
  year    = {2022},
  doi     = {10.1021/acsenergylett.2c00550}
}
@article{Shishvan2023,
  author  = {Shishvan, Siamak S. and Fleck, N. A. and McMeeking, Robert M. and Deshpande, V. S.},
  title   = {Vacancy diffusion and its consequences for void growth at the interface of a stripping metal electrode and solid electrolyte},
  journal = {Electrochimica Acta},
  year    = {2023},
  doi     = {10.1016/j.electacta.2023.143081}
}
@article{Raj2022,
  author  = {Raj, Vikalp and others},
  title   = {Direct correlation between void formation and lithium dendrite growth in solid-state electrolytes with interlayers},
  journal = {Nature Materials},
  year    = {2022},
  doi     = {10.1038/s41563-022-01264-8}
}
```
