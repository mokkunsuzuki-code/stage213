# QSP Stage213 – Signed Evidence Bundle

MIT License © 2025 Motohiro Suzuki

---

## Overview

Stage213 introduces **cryptographically signed evidence bundles** for protocol verification.

While Stage212 linked **security claims to CI-generated evidence**, Stage213 adds **cryptographic integrity and authenticity guarantees** to that evidence.

This ensures that verification artifacts cannot be modified after generation without detection.

---

## Motivation

Security evidence is often generated automatically in CI pipelines, but without cryptographic protection it can be altered after the fact.

Stage213 solves this by introducing a **Signed Evidence Bundle**.

This bundle binds together:

- Security claims
- CI test results
- Attack simulation outputs
- Evidence artifacts

and protects them with:

- SHA256 hashing
- RSA signatures
- Public verification

This provides **tamper-evident security evidence**.

---

## Evidence Integrity Model

Stage212 provided:


Claim
↓
CI Job
↓
Evidence Artifact
↓
CI Run ID


Stage213 extends this with cryptographic verification:


Claim
↓
CI Job
↓
Evidence Artifact
↓
CI Run ID
↓
SHA256
↓
Signature
↓
Verification


This creates a **verifiable evidence chain**.

---

## Repository Structure


stage213
│
├─ evidence_bundle/
│ ├─ evidence_bundle.json
│ ├─ evidence_bundle.sha256
│ └─ summary.md
│
├─ signatures/
│ ├─ evidence_bundle.sig
│ └─ evidence_bundle.signature.json
│
├─ keys/
│ └─ evidence_signing_public.pem
│
├─ tools/
│ ├─ build_signed_evidence_bundle.py
│ ├─ write_bundle_sha256.py
│ ├─ sign_evidence_bundle.py
│ └─ run_stage213_bundle.sh
│
├─ verification/
│ └─ verify_signature.py
│
├─ claims/
├─ tests/
├─ docs/
└─ out/


---

## How the Signed Evidence Bundle Works

Stage213 performs four steps.

### 1. Evidence Bundle Generation

All relevant artifacts are collected:

- CI results
- attack logs
- claim files
- reports

and assembled into a structured JSON bundle.


tools/build_signed_evidence_bundle.py


---

### 2. SHA256 Integrity Hash

The bundle is hashed using SHA256.


tools/write_bundle_sha256.py


Output:


evidence_bundle/evidence_bundle.sha256


---

### 3. Cryptographic Signature

The bundle is signed with a private RSA key.


tools/sign_evidence_bundle.py


Outputs:


signatures/evidence_bundle.sig
signatures/evidence_bundle.signature.json


---

### 4. Public Verification

Anyone can verify the bundle using the public key.


verification/verify_signature.py


Verification command:


python3 verification/verify_signature.py


Expected result:


[OK] signature verification passed


---

## Quick Start

Generate and verify the signed evidence bundle.


./tools/run_stage213_bundle.sh


This executes:


build evidence bundle
→ generate SHA256
→ sign bundle
→ verify signature


---

## Security Properties

Stage213 provides:

- **tamper-evident evidence**
- **cryptographic authenticity**
- **verifiable CI outputs**
- **reproducible security validation**

If any artifact is modified, verification fails.

---

## Relation to Previous Stages

| Stage | Feature |
|------|------|
| Stage210 | Claim → Evidence mapping |
| Stage211 | Evidence bundle generation |
| Stage212 | CI run linkage |
| **Stage213** | **Signed Evidence Bundle** |

Stage213 ensures that **security evidence cannot be modified without detection**.

---

## Research Relevance

Signed evidence bundles support:

- reproducible security research
- tamper-evident verification
- traceable claim validation

This aligns with emerging practices in:

- reproducible cryptographic research
- CI-based verification pipelines
- verifiable security artifacts

---

## License

MIT License

Copyright (c) 2025 Motohiro Suzuki