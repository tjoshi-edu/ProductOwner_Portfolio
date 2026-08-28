# User Personas

## Product: AI Product Discovery & Requirements Copilot

## 1. Primary Persona — Product Owner

### Persona Overview

- **Name:** Priya — Product Owner
- **Role:** Product Owner / Product Manager
- **Experience:** 5–10 years
- **Environment:** Agile product development
- **Primary Goal:** Convert business needs into clear, prioritized, delivery-ready requirements.

### Responsibilities

- Define product vision and outcomes
- Gather requirements from stakeholders
- Prioritize product backlog
- Create and refine epics and features
- Write and review user stories
- Define acceptance criteria
- Collaborate with engineering and QA
- Manage stakeholder expectations
- Evaluate business value and product risks

### Pain Points

- Requirements arrive incomplete or ambiguous
- Stakeholders use inconsistent terminology
- Important business rules are frequently missed
- Significant time is spent rewriting requirements
- User stories may be created before requirements are sufficiently understood
- Dependencies and risks are discovered late
- Different BAs/POs produce inconsistent documentation
- Large requirements are difficult to decompose
- Maintaining traceability is time-consuming

### Needs

The Product Owner needs an AI assistant that can:

- Analyze raw requirements
- Identify ambiguity
- Detect missing information
- Ask clarifying questions
- Identify stakeholders
- Extract business rules
- Identify risks and dependencies
- Score requirement completeness
- Generate product specifications
- Generate delivery-ready user stories
- Maintain requirement traceability
- Keep the Product Owner in control of final decisions

### Success Criteria

The Product Owner considers the product successful when:

- Requirements require less manual refinement
- Ambiguities are identified earlier
- User stories are more consistent
- Acceptance criteria are more testable
- Requirements have better traceability
- Product decisions can be documented faster
- AI output requires minimal but meaningful human editing

---

## 2. Secondary Persona — Business Analyst

### Persona Overview

- **Name:** Alex — Business Systems Analyst
- **Role:** Business Analyst / Systems Analyst
- **Experience:** 3–10 years

### Goals

- Convert business needs into detailed requirements
- Understand business processes
- Identify system impacts
- Document functional and non-functional requirements
- Support Product Owners and development teams
- Create traceability between requirements and testing

### Pain Points

- Repetitive requirements documentation
- Manually identifying gaps
- Time-consuming impact analysis
- Large volumes of requirements
- Maintaining consistency across documents
- Reworking requirements after stakeholder review

### Needs

- AI-assisted requirement analysis
- Requirement completeness assessment
- Business-rule extraction
- Impact analysis
- Requirement classification
- User-story generation
- Acceptance-criteria generation
- Requirement traceability

### Success Criteria

- Reduced requirements-documentation effort
- Fewer requirement defects
- Improved requirement consistency
- Faster stakeholder review cycles

---

## 3. Secondary Persona — QA Analyst

### Persona Overview

- **Name:** Jordan — QA Analyst
- **Role:** QA Analyst / Test Lead

### Goals

- Understand expected system behavior
- Create effective test scenarios
- Identify edge cases
- Validate acceptance criteria
- Ensure requirements are testable

### Pain Points

- Vague acceptance criteria
- Missing edge cases
- Requirements changing without traceability
- Requirements that are difficult to translate into tests

### Needs

- Testable acceptance criteria
- Gherkin scenarios
- Edge-case identification
- Requirement-to-test traceability
- Requirement quality scoring

### Success Criteria

- Better test coverage
- Fewer requirement-related defects
- Less clarification required during testing

---

## 4. Secondary Persona — Engineering Lead

### Persona Overview

- **Name:** Daniel — Engineering Lead
- **Role:** Engineering Manager / Technical Lead

### Goals

- Understand business requirements
- Identify technical dependencies
- Estimate complexity
- Detect requirements that could cause implementation problems

### Pain Points

- Incomplete requirements entering development
- Hidden dependencies
- Late discovery of technical constraints
- Frequent requirement changes

### Needs

- Clear requirements
- Business rules
- Dependencies
- Non-functional requirements
- Risks
- Acceptance criteria

### Success Criteria

- Reduced requirement churn
- Better sprint predictability
- Fewer implementation clarifications
- Better estimation

---

## 5. Persona Comparison

| Persona | Primary Need | Key Pain Point | Product Value |
|---|---|---|---|
| Product Owner | Requirement clarity | Ambiguous requirements | Requirement intelligence |
| Business Analyst | Documentation efficiency | Manual analysis | AI-assisted analysis |
| QA Analyst | Testability | Poor acceptance criteria | Test-ready requirements |
| Engineering Lead | Implementation clarity | Missing dependencies | Impact and dependency analysis |

---

## 6. Primary Persona Journey

The primary product journey is designed around the Product Owner:

```text
Business Idea
      ↓
Requirement Intake
      ↓
AI Analysis
      ↓
Missing Information
      ↓
Clarifying Questions
      ↓
PO Review
      ↓
Validated Requirement
      ↓
Product Specification
      ↓
Epic / Feature
      ↓
User Stories
      ↓
Acceptance Criteria
      ↓
Jira / Azure DevOps