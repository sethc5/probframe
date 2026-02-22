# Oversight Capture

Purpose: Documents the structural pattern by which a monitored actor gains influence over the body responsible for monitoring and sanctioning its behavior, converting an external check into a captured function.

Status: draft

Tags: capture, oversight, regulatory, principal-agent, monitoring, revolving-door, accountability, hierarchy, information-asymmetry

Pattern class: 07 Hierarchical and Delegative Patterns

Outline: see `outline.md`

Contributors:

Related patterns: 045, 048, 050, 071, 037
Often combined with: 045, 029, 075
Degrades into: 048, 072
Modframe instances: [pending — plausible grounding in agency inspector general relationships, OMB OIRA review process, congressional committee oversight of executive agencies, and financial regulatory architecture — requires Modframe INDEX review before advancing to sourced]
Last reviewed: 2026-02

Domains:
  - political
  - economic
  - organizational
  - biological

Actors:
  - name: Monitored actor / regulatee
    type: deployer
  - name: Oversight body
    type: target
  - name: Appointing authority
    type: enabler
  - name: Whistleblower / external auditor
    type: regulator

How to contribute:

- Populate Modframe instances from Modframe INDEX before advancing to sourced
- Revolving door data (OGE filings, FARA registrations) would strengthen [Observed] claims on appointment vector
- Run: python3 scripts/validate_metadata.py patterns/07_Hierarchical_and_Delegative_Patterns/047_Oversight_Capture/README.md
