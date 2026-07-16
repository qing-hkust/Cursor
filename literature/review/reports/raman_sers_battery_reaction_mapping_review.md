# Literature review: Raman / SERS mapping of electrochemical reactions in batteries

**Scope:** Spatial or operando mapping of where electrochemical reactions occur in battery electrodes, with emphasis on **surface-enhanced Raman spectroscopy (SERS)** at electrode–electrolyte interfaces. **Excluded:** tip-enhanced Raman spectroscopy (TERS) and shell-isolated nanoparticle-enhanced Raman spectroscopy (SHINERS / Au@SiO₂).

**Generated:** 2026-06-03

---

## Executive summary

The literature splits into two tiers:

1. **2D spatial mapping of reactions, SOC, or redox intermediates** — mature with **confocal Raman** on intercalation cathodes (NMC, LCO, NCA) and Li–S systems; maps lithiation heterogeneity, phase fractions, or polysulfide distributions at µm resolution.
2. **Interface-sensitive SERS for CEI/SEI chemistry** — growing body of **operando** work at a **single enhanced hotspot** (Au nanocubes, electrodeposited Au/Ag); tracks CEI/SEI species vs potential or time, but **full-field SERS reaction maps** across composite electrodes remain uncommon.

A combined approach—**plasmonic decoration for SERS sensitivity** (e.g. electrodeposited Au on oxide particles) plus **coin-cell or mapping-cell Raman optics**—is underdeveloped relative to either technique alone. That gap is relevant for mechanism-to-design work on Zn/Li interfaces where interfacial reaction localization matters.

---

## Research questions addressed

| Question | Finding in literature |
|----------|------------------------|
| Can Raman map *where* reactions happen in a battery? | Yes, extensively for **SOC / lithiation** (cathodes) and **polysulfide / sulfur** (Li–S); less for **anode SEI** spatial maps. |
| Does SERS add interface specificity? | Yes: CEI on cathodes, SEI on Si/Au/Ag model electrodes; enhancement isolates surface species vs bulk electrolyte. |
| Is SERS used for 2D reaction distribution maps? | Rare; mostly **potential- or time-resolved spectra** at one spot. **Tornheim (2017)** discusses spatial heterogeneity of SERS enhancement on NCM523. |
| What to avoid (per scope)? | TERS (nanoscale tip); SHINERS (SiO₂-shell Au) — see [Excluded works](#excluded-works-ters--shiners). |

---

## Tier A — Spatial mapping (confocal Raman, typically non-SERS)

These papers establish that **Raman imaging** can resolve inhomogeneous electrochemistry at particle or electrode scale. They are the main precedent for “mapping reaction distribution,” even when SERS is not used.

### State-of-charge (SOC) and lithiation heterogeneity

| Authors (year) | Venue | DOI | Contribution |
|----------------|-------|-----|--------------|
| Nanda et al. (2011) | *Adv. Funct. Mater.* | [10.1002/adfm.201100157](https://doi.org/10.1002/adfm.201100157) | µm-resolved **local SOC** on Li₁₋ₓ(Ni_y Co_z Al₁₋ᵧ₋₂)O₂; links particle-level composition to macroscopic SOC. |
| Nishi & Nakai (2013) | *J. Electrochem. Soc.* | [10.1149/2.061310jes](https://doi.org/10.1149/2.061310jes) | **In situ Raman imaging** of **SOC distribution** in LiCoO₂ cathode. |
| Fang, Yan & Hamers (2017) | *J. Power Sources* | [10.1016/j.jpowsour.2017.03.055](https://doi.org/10.1016/j.jpowsour.2017.03.055) | Coin-cell **in situ Raman mapping**; MgO window design; **NMC532** A₁g frequency maps reveal **SOC inhomogeneity** at single-particle level. |

### Redox intermediates and multi-step reactions (Li–S)

| Authors (year) | Venue | DOI | Contribution |
|----------------|-------|-----|--------------|
| Lang et al. (2022) | *Nature Communications* | [10.1038/s41467-022-32139-w](https://doi.org/10.1038/s41467-022-32139-w) | **Operando confocal Raman microscopy** maps **spatial distribution** of S, long-chain and short-chain polysulfides, and Li₂S; quantifies reaction kinetics and stepwise vs parallel pathways during discharge/charge. |

### Mesoscale “active reaction area” (NMC)

| Authors (year) | Venue | DOI | Contribution |
|----------------|-------|-----|--------------|
| (ECS meeting abstract, 2022) | *ECS Meet. Abstr.* | [10.1149/MA2022-02195mtgabs](https://doi.org/10.1149/MA2022-02195mtgabs) | Benchtop **in situ Raman** on porous **NMC532**; deconvolution separates empty / lithiated / partially lithiated phases; **maps active reaction fraction** (~18–50% of particle area) and estimates **local current density** an order of magnitude above global average. |

### Reviews and cross-section mapping

| Authors (year) | Venue | DOI | Contribution |
|----------------|-------|-----|--------------|
| Streich et al. (2018) | *Front. Energy Res.* | [10.3389/fenrg.2018.00082](https://doi.org/10.3389/fenrg.2018.00082) | Compares spectro-electrochemical cells; emphasizes **(1) lateral/axial Raman mapping** for inhomogeneous LiMO₂ reactions and **(2) single-particle operando** spectra; cites ex situ **electrode cross-section** maps (cracked vs intact NCM523 particles). Discusses **SERS** as future tool (see Tier B/C). |

**Takeaway (Tier A):** Confocal Raman is the workhorse for **where** intercalation or redox intermediates vary spatially. Acquisition can be slow; EMCCD and careful cell design (Fang 2017) reduce artifacts.

---

## Tier B — Operando SERS at battery interfaces (chemistry vs potential/time)

These studies use **plasmonic enhancement** to probe **CEI, SEI, or electric double layer** species that bulk Raman misses. Most report **spectra vs voltage or cycle time** at one probed region, not a 2D map over the electrode.

### Cathode–electrolyte interface (CEI)

| Authors (year) | Venue | DOI | Substrate | Contribution |
|----------------|-------|-----|-----------|--------------|
| Chen et al. (2019) | *Nano Letters* | [10.1021/acs.nanolett.9b00179](https://doi.org/10.1021/acs.nanolett.9b00179) | **Au nanocube monolayer** on binder-free **LNMC** | **Operando SERS** under cycling (3–4.5 V); CEI bands (ether/ester) vs potential; compared to non-SERS operando Raman; DFT+U model for CEI–SOC coupling. |

### Anode / model electrodes (SEI, EDL)

| Authors (year) | Venue | DOI | Substrate | Contribution |
|----------------|-------|-----|-----------|--------------|
| Piernas-Muñoz et al. (2021) | *Chem. Commun.* | [10.1039/d0cc08001b](https://doi.org/10.1039/d0cc08001b) | **Electrodeposited Au** on **Si** | SERS detects **SEI** composition (incl. organophosphate-like bands) on Si anode. |
| (JPCL, 2020) | *J. Phys. Chem. Lett.* | [10.1021/acs.jpclett.0c01089](https://doi.org/10.1021/acs.jpclett.0c01089) | **Au SERS** (model) | **Operando SERS** + OEMS + EQCM: **EDL charging** (EC·Li⁺ at surface), then **SEI** (LiF, Li₂CO₃); carbonate–LiPF₆ electrolyte. |
| (J. Electrochem., 2023) | *J. Electrochem.* | [10.13208/j.electrochem.2301261](https://doi.org/10.13208/j.electrochem.2301261) | **Ag nanoparticles** on **Ag** (“borrowing SERS”) | **In situ SERS** SEI in EC-DMC; double-layer SEI picture; not shell-isolated. |

**Takeaway (Tier B):** SERS is established for **which interfacial molecules appear when**, tied to potential. Chen 2019 is the reference for **true cathode + operando + direct Au SERS** (not silica shell).

---

## Tier C — SERS toward spatial sensitivity (heterogeneity, not full maps)

| Authors (year) | Venue | DOI | Contribution |
|----------------|-------|-----|--------------|
| Tornheim et al. (2017) | *J. Electrochem. Soc.* | [10.1149/2.0461713jes](https://doi.org/10.1149/2.0461713jes) | **Electrodeposited sub-µm Au clusters** on **NCM523** laminate; ~100× Raman intensity; discusses **spatial variation** of enhancement from random cluster placement and laminate heterogeneity — step toward faster mapping, not a published 2D reaction map. |

Streich et al. (2018) note that Tornheim-style enhancement could reduce map acquisition from **~hours toward seconds**, but bare Au may be unstable at high cathode potential; they discuss **SHINERS** as a remedy — outside this review’s scope.

---

## Gap analysis (opportunity)

| Capability | Maturity | Representative work |
|------------|----------|---------------------|
| 2D SOC / phase maps (cathode) | High | Nanda 2011; Nishi 2013; Fang 2017 |
| 2D redox intermediate maps (Li–S) | High (niche chemistry) | Lang 2022 |
| Operando SERS CEI/SEI chemistry | Medium | Chen 2019; JPCL 2020; Piernas-Muñoz 2021 |
| 2D **SERS** maps of reaction distribution on composite electrodes | **Low** | Tornheim 2017 (heterogeneity); no standard benchmark paper |
| Zn-aqueous / mossy Zn interface SERS maps | **Very low** | Not found in this scoped search |

**Suggested experimental stack (from literature):**

1. Cell: Fang-style **in situ coin cell** with validated uniform potential in optical window.  
2. Sensitivity: Tornheim-style **electrodeposited Au** or Chen-style **Au nanocubes** on model oxide (evaluate stability at operating potential).  
3. Readout: Confocal map of SERS-active bands + simultaneous oxide phonon mode (SOC proxy), as in Chen 2019 comparison of with/without Au.

---

## Excluded works (TERS & SHINERS)

Listed for navigation only — **not** summarized as methods in scope.

| Work | DOI | Reason excluded |
|------|-----|-----------------|
| Zhu et al., *J. Mater. Chem. A* (2021) | [10.1039/D1TA04218A](https://doi.org/10.1039/D1TA04218A) | **SiO₂-encapsulated Au** (SHINERS-type) on graphite |
| LiCoO₂ interface monitoring (2022) | [10.1002/sia.7097](https://doi.org/10.1002/sia.7097) | **Au@SiO₂** nanoparticles |
| Hy et al., Li-rich NCM (cited in Streich 2018) | — | **SHINERS** |
| Gajan et al., enhanced Raman / SHINERS line (ECS, *ACS Energy Lett.*) | [10.1149/MA2021-021133mtgabs](https://doi.org/10.1149/MA2021-021133mtgabs) | **SHINERS** framing |
| Operando **TERS** on LMO / LFP (2024–2025 literature) | — | **TERS** |

---

## References (quick list)

1. Nanda J. et al., *Adv. Funct. Mater.* **2011**, [10.1002/adfm.201100157](https://doi.org/10.1002/adfm.201100157)  
2. Nishi T., Nakai H., *J. Electrochem. Soc.* **2013**, [10.1149/2.061310jes](https://doi.org/10.1149/2.061310jes)  
3. Fang S., Yan M., Hamers R.J., *J. Power Sources* **2017**, [10.1016/j.jpowsour.2017.03.055](https://doi.org/10.1016/j.jpowsour.2017.03.055)  
4. Lang S.-Y. et al., *Nat. Commun.* **2022**, [10.1038/s41467-022-32139-w](https://doi.org/10.1038/s41467-022-32139-w)  
5. Streich D. et al., *Front. Energy Res.* **2018**, [10.3389/fenrg.2018.00082](https://doi.org/10.3389/fenrg.2018.00082)  
6. Chen D. et al., *Nano Lett.* **2019**, [10.1021/acs.nanolett.9b00179](https://doi.org/10.1021/acs.nanolett.9b00179)  
7. Piernas-Muñoz M.J. et al., *Chem. Commun.* **2021**, [10.1039/d0cc08001b](https://doi.org/10.1039/d0cc08001b)  
8. Operando SERS SEI/EDL, *J. Phys. Chem. Lett.* **2020**, [10.1021/acs.jpclett.0c01089](https://doi.org/10.1021/acs.jpclett.0c01089)  
9. Tornheim A. et al., *J. Electrochem. Soc.* **2017**, [10.1149/2.0461713jes](https://doi.org/10.1149/2.0461713jes)  
10. ECS abstract NMC532 active area Raman, **2022**, [10.1149/MA2022-02195mtgabs](https://doi.org/10.1149/MA2022-02195mtgabs)  
11. In situ SERS SEI on Ag, *J. Electrochem.* **2023**, [10.13208/j.electrochem.2301261](https://doi.org/10.13208/j.electrochem.2301261)  

---

## Related project files

- General background-driven agent: `literature/review/lit_review.py`, `literature/review/config.yaml`  
- Latest automated report (electrochemistry portfolio): `literature/review/reports/literature_review_2026-06-03.md`  

<!-- provenance: manual curated review, Raman/SERS battery mapping scope, 2026-06-03 -->
