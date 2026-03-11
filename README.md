# QSP Stage211 — Claim-Bound CI Evidence

MIT License © 2025 Motohiro Suzuki

Stage211 introduces **Claim-Bound CI Evidence**, a structure that explicitly links:

Claim  
↓  
CI Job  
↓  
Evidence Artifact

This creates a **traceable and reproducible verification chain** between security claims and the artifacts produced by continuous integration.

The goal is to make security claims **inspectable, reproducible, and evidence-backed**.

---

# Core Concept

Traditional CI verifies whether tests pass.

Stage211 goes further:

Security **claims themselves** are bound to CI jobs and their generated evidence.


Claim → CI Job → Evidence Artifact


This structure ensures that:

- Each claim is backed by executable validation
- CI outputs are preserved as verifiable artifacts
- Reviewers can directly inspect evidence

---

# Claim-Bound Evidence Mapping

| Claim | CI Job | Evidence Artifact |
|------|------|------|
| A2 Replay Protection | attack_replay | evidence/replay_attack.log |
| A3 Downgrade Protection | attack_downgrade | evidence/downgrade_attack.log |
| A4 Session Integrity | session_integrity | evidence/session_integrity.log |
| A5 Fail-Closed Behavior | fail_closed | evidence/fail_closed.log |

Each CI job produces artifacts stored in the **evidence/** directory.

These artifacts serve as **direct verification outputs** for the corresponding claim.

---

# Evidence Artifacts

Example evidence files:


evidence/
replay_attack.log
downgrade_attack.log
session_integrity.log
fail_closed.log


These logs provide the **observable outputs of adversarial tests** executed by CI.

---

# Repository Structure


stage211/
├── claims/
├── crypto/
├── docs/
├── evidence/
│ ├── replay_attack.log
│ ├── downgrade_attack.log
│ ├── session_integrity.log
│ └── fail_closed.log
├── protocol/
├── tests/
├── tools/
└── README.md


---

# Design Goal

Stage211 aims to strengthen protocol validation by making security claims:

- explicit
- testable
- evidence-linked
- reproducible

Instead of relying on narrative claims, the system exposes a **claim → validation → artifact pipeline**.

---

# Relation to Stage210

Stage210 introduced a conceptual structure:


Claim → Test → Evidence


Stage211 refines this by binding claims **directly to CI jobs and artifacts**:


Claim → CI Job → Evidence Artifact


This ensures that every security claim has:

- a corresponding automated test
- a CI execution record
- a verifiable artifact

---

# Security Philosophy

The QSP project emphasizes:

- explicit security assumptions
- adversarial testing
- fail-closed protocol behavior
- reproducible verification

Claim-Bound CI Evidence is designed to reduce ambiguity between:

- protocol design
- implementation
- validation results

---

# License

MIT License

Copyright (c) 2025 Motohiro Suzuki