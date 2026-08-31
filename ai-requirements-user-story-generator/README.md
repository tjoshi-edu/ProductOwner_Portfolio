# AI Requirements & User Story Generator

An AI-powered Product Owner assistant that transforms business
requirements into structured product artifacts.

## Product Overview

The application uses Generative AI to convert natural-language
business requirements into:

- Epics
- Features
- User Stories
- Acceptance Criteria
- Functional Requirements
- Non-Functional Requirements
- Dependencies
- Risks
- Assumptions
- Story Points
- INVEST Quality Assessment

## Business Problem

Product Owners and Business Analysts spend significant time
transforming high-level business requirements into detailed,
testable Agile requirements.

This application accelerates that process while maintaining
human Product Owner review.

## Technology

- Python
- Streamlit
- Ollama
- Llama 3.2
- Pydantic
- GitHub

## Architecture

Business Requirement
        |
        v
Streamlit UI
        |
        v
Prompt Engineering
        |
        v
Ollama
        |
        v
Llama 3.2
        |
        v
Structured Product Requirements

## Example

Input:

Customers should be able to reset their password using their
registered email address.

Output:

- Epic
- Feature
- User Story
- Acceptance Criteria
- Requirements
- Dependencies
- Risks
- Story Points
- INVEST Score

## Product Owner Responsibilities

This project demonstrates end-to-end AI Product Ownership:

### Product Discovery
- Identified requirements-engineering pain points
- Defined target users and personas
- Documented user journeys
- Defined MVP scope

### Product Strategy
- Created product vision
- Defined product goals and outcomes
- Developed product roadmap
- Prioritized features

### Requirements
- Created epics and features
- Defined user stories
- Created Gherkin acceptance criteria
- Defined functional and non-functional requirements

### AI Product Design
- Designed LLM interaction
- Defined prompt strategy
- Established human-in-the-loop workflow
- Defined AI quality metrics
- Identified hallucination and reliability risks

### Agile Delivery
- Created product backlog
- Defined acceptance criteria
- Prioritized MVP features
- Defined release increments

### AI Governance
- Identified AI risks
- Defined evaluation criteria
- Designed human review
- Planned responsible AI controls

## Future Enhancements

- Excel export
- Word export
- Test case generation
- Duplicate story detection
- Requirement traceability
- RAG-based requirements knowledge base
- AI-generated sprint planning
- Story prioritization
