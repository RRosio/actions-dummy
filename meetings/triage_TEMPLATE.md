---
title: "Jupyter Issue Triage Meeting"
description: |
  A weekly gathering of the Jupyter Issue Triage Group.
date: "{{ date.strftime('%Y-%m-%d') }}"
author:
  - name: "The Jupyter Issue Triage Group"
categories:
  - "Meeting notes"
tags: [meeting-notes]
---

# Jupyter Issue Triage Meeting ({{ date.strftime("%Y-%m-%d") }})

Triage issues in JupyterLab and corresponding projects.

Meeting is typically held at 09:00 US Pacific time on Tuesdays.

Meeting info: https://zoom.us/j/95228013874?pwd=Ep7HIk8t9JP6VToxt1Wj4P7K5PshC0.1

Notes on GitHub: https://github.com/jupyterlab/frontends-team-compass/issues/268

Previous notes:
* https://github.com/jupyterlab/frontends-team-compass/issues/268 (Jan–Dec 2025)
* https://github.com/jupyterlab/frontends-team-compass/issues/250#issuecomment-2441830653 (Jul–Dec 2024)
* https://github.com/jupyterlab/frontends-team-compass/issues/228 (2024-01 through 2024-06)
* https://github.com/jupyterlab/frontends-team-compass/issues/203 (2023-07 through 2023-12)
* https://github.com/jupyterlab/frontends-team-compass/issues/169 (2023-01 through 2023-06)
* https://github.com/jupyterlab/frontends-team-compass/issues/151 (2022-07 through 2022-12)
* https://github.com/jupyterlab/frontends-team-compass/issues/137 (2022-01 through 2022-06)


## Goals

Act on long-running, highly demanded, or highly discussed issues to get them ready for development work.

### Resources

* https://jupyterlab.readthedocs.io/en/latest/developer/contributing.html#submitting-a-pull-request-contribution

* There is a script to pull all current issues here: https://github.com/danyeaw/jupyter-triage-tool

### Triage Process

All requested information, where applicable, is provided. From the templates in JupyterLab’s issues:

For a bug:

* Description, preferably including screen shots
* Steps to reproduce
* Expected behavior
* Context, such as OS, browser, JupyterLab version, and output or log excerpts

For a feature request:
* Description of the problem
* Description of the proposed solution
* Additional context

The issue should represent real, relevant, feasible work. In short, if a knowledgeable person were to be assigned this issue, they would be able to complete it with a reasonable amount of effort and assistance, and it furthers the goals of the Jupyter project.

* Issues should be unique; triage is the best time to identify duplicates.
* Bugs represent valid expectations for use of Jupyter products and services.
* Expectations for security, performance, accessibility, and localization match generally-accepted norms in the community that uses Jupyter products.
* The issue represents work that one developer can commit to owning, even if they collaborate with other developers for feedback. Excessively large issues should be split into multiple issues, each triaged individually, or into team-compass issues to discuss more substantive changes.

1. Read issues
2. Tag issues; remove `status:Needs Triage` from issues we accept. Other useful tags include:
    a. good first issue
    b. bug
    c. feature parity
    d. Tag milestones
3. Identify duplicates
4. Respond to issues
5. Assign another person

Add milestone if you can achieve the goal.

### Primary focus

* [JupyterLab untriaged issues](https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aissue+is%3Aopen+label%3A%22status%3ANeeds+Triage%22%20sort%3Acreated-asc)
* [Notebook untriaged issues](https://github.com/jupyter/notebook/issues?q=is%3Aissue+is%3Aopen+label%3A%22status%3ANeeds+Triage%22%20sort%3Acreated-asc)
* [JupyterLab Desktop untriaged issues](https://github.com/jupyterlab/jupyterlab-desktop/issues?q=is%3Aissue+is%3Aopen+label%3A%22status%3ANeeds+Triage%22%20sort%3Acreated-asc)
* [nbclassic untriaged issues](https://github.com/jupyter/nbclassic/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3ANeeds%20Triage%22%20sort%3Acreated-asc)


## Attendees
| Name | Organization | Username |
|------|--------------|----------|
||||

## Meeting Notes

{{ triage_issues }}