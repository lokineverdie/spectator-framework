# {MODULE_NAME} - Requirements Document

## Introduction

{BRIEF_DESCRIPTION_OF_MODULE_PURPOSE}

## Glossary

- **{System_Name}**: {Definition of the primary system or component}
- **{Technical_Term_1}**: {Definition}
- **{Technical_Term_2}**: {Definition}

## Requirements

### Requirement 1

**User Story:** As a {role}, I want {feature}, so that {benefit}

#### Acceptance Criteria

1. THE {System_Name} SHALL {response}
2. WHEN {trigger}, THE {System_Name} SHALL {response}
3. WHILE {condition}, THE {System_Name} SHALL {response}
4. IF {undesired_condition}, THEN THE {System_Name} SHALL {response}
5. WHERE {optional_feature}, THE {System_Name} SHALL {response}

### Requirement 2

**User Story:** As a {role}, I want {feature}, so that {benefit}

#### Acceptance Criteria

1. THE {System_Name} SHALL {response}
2. WHEN {trigger}, THE {System_Name} SHALL {response}
3. WHERE {configuration_option} WHILE {state_condition}, THE {System_Name} SHALL {response}

### Requirement 3

**User Story:** As a {role}, I want {feature}, so that {benefit}

#### Acceptance Criteria

1. THE {System_Name} SHALL {response}
2. IF {error_condition}, THEN THE {System_Name} SHALL {error_response}
3. WHILE {processing_state}, THE {System_Name} SHALL {continuous_behavior}

## EARS Pattern Reference

### Pattern Examples

**Ubiquitous Requirements:**
- THE Search_Agent SHALL return job listings within 5 seconds

**Event-Driven Requirements:**
- WHEN a user submits search criteria, THE Search_Agent SHALL validate input parameters

**State-Driven Requirements:**
- WHILE processing search requests, THE Search_Agent SHALL display progress indicators

**Unwanted Event Requirements:**
- IF search results exceed timeout threshold, THEN THE Search_Agent SHALL return partial results

**Optional Feature Requirements:**
- WHERE advanced filtering is enabled, THE Search_Agent SHALL apply additional criteria

**Complex Requirements:**
- WHERE premium features are active WHILE user is authenticated WHEN search is initiated, THE Search_Agent SHALL access enhanced job databases

## Quality Checklist

- [ ] All system names defined in Glossary
- [ ] Each requirement follows exactly one EARS pattern
- [ ] No vague terms (quickly, adequate, user-friendly)
- [ ] No escape clauses (where possible, as appropriate)
- [ ] Active voice used throughout
- [ ] No negative statements (SHALL not)
- [ ] One testable thought per requirement
- [ ] Measurable criteria specified
- [ ] Consistent terminology
- [ ] No pronouns (it, them, this)
- [ ] No absolutes (never, always, 100%)
- [ ] Solution-free (what, not how)