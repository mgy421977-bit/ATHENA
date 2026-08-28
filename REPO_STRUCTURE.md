# ATHENA Repository Structure Proposal (V15.3.3)

This document defines the target organisation for the controlled research release.

## Guiding Principles

1. **Honest status first** — README and docs must reflect DERIVED / CONDITIONAL / OPEN / NO-GO.
2. **Frozen core vs. exploratory** — Algebraic identities and source-free limits live in the core package; observational fits and speculative modules are clearly separated.
3. **Reproducibility** — Every numerical claim that is not purely algebraic must eventually carry data version, checksum, environment lock, and reference output.
4. **Historical preservation** — Older versions (V14 and earlier) are archived, not deleted.

## Target Tree

```text
ATHENA/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── REPO_STRUCTURE.md          # this file
├── requirements.txt
├── environment.yml            # conda/mamba lock (to be added)
├── setup.py / pyproject.toml
│
├── docs/
│   ├── physics.md             # High-level physics overview (cautious language)
│   ├── status_ledger.md       # Condensed machine-readable status table
│   ├── quickstart.md
│   ├── installation.md
│   ├── falsification.md
│   └── api_reference.md
│
├── monograph/
│   ├── V15.3.3/
│   │   ├── ATHENA_Ultimate_V15.3.3.pdf
│   │   ├── src/               # LaTeX sources
│   │   └── README.md          # Version-specific notes + status summary
│   ├── V14/                   # Archived release
│   └── historical/            # Pre-V14 material
│
├── athena/                    # Installable core package
│   ├── __init__.py
│   ├── disformal.py           # Pure-disformal metric, inverse, determinant, connection
│   ├── flrw.py                # Homogeneous equations, source-free limits
│   ├── stability.py           # Quadratic action checks (minimal sector)
│   ├── constants.py           # β₀, Z₀, … with clear provenance comments
│   └── utils.py
│
├── simulations/
│   ├── source_free/           # Exact scalar backgrounds, limit-set checks
│   ├── algebraic/             # Identity verifications
│   └── exploratory/           # Non-core numerical experiments
│
├── scripts/
│   ├── run_algebraic_tests.py
│   └── make_status_table.py
│
├── tests/
│   ├── test_disformal_identities.py
│   ├── test_source_free_limits.py
│   └── test_constants_provenance.py
│
└── data/                      # Optional, for future reproducible fits
    ├── README.md              # Explains that observational data are external
    └── checksums.sha256       # When data are added
```

## Migration Notes (from current V14 layout)

| Current                    | Action                                      |
|---------------------------|---------------------------------------------|
| `v14/`                    | Move under `monograph/V14/`                 |
| `manifesto/`              | Move under `monograph/historical/` or keep  |
| Top-level simulation scripts | Reorganise into `simulations/`           |
| README                    | Replaced by the V15.3.3 honest version      |

## Immediate Next Actions

1. Create `monograph/V15.3.3/` and upload the PDF + LaTeX source.
2. Add `environment.yml` and pin exact dependency versions.
3. Implement the minimal algebraic test suite under `tests/`.
4. Update Zenodo with a new DOI for the V15.3.3 controlled release (keep V14 DOI as archival).
5. Add a short `docs/status_ledger.md` that mirrors the monograph’s Stage 5 / Appendix F tables.

---

*This structure proposal accompanies the V15.3.3 controlled research release.*
