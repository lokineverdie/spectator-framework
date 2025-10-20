# EARS Compliance System

## Overview

The Spectator Framework includes automated validation for EARS (Easy Approach to Requirements Syntax) patterns and INCOSE quality rules.

## EARS Pattern Reference

### The Six EARS Patterns

#### 1. Ubiquitous Requirements
**Pattern**: `THE [system] SHALL [response]`
**Usage**: Requirements that apply universally to the system
**Example**: `THE Data_Processing_System SHALL validate all input parameters`

#### 2. Event-Driven Requirements
**Pattern**: `WHEN [trigger], THE [system] SHALL [response]`
**Usage**: Requirements triggered by specific events
**Example**: `WHEN a user submits data, THE Processing_System SHALL acknowledge receipt within 1 second`

#### 3. State-Driven Requirements
**Pattern**: `WHILE [condition], THE [system] SHALL [response]`
**Usage**: Requirements active during specific states
**Example**: `WHILE processing data, THE System SHALL display progress indicators`

#### 4. Unwanted Event Requirements
**Pattern**: `IF [condition], THEN THE [system] SHALL [response]`
**Usage**: Requirements for handling unwanted situations
**Example**: `IF processing fails, THEN THE System SHALL log the error and notify the user`

#### 5. Optional Feature Requirements
**Pattern**: `WHERE [option], THE [system] SHALL [response]`
**Usage**: Requirements for optional system features
**Example**: `WHERE advanced mode is enabled, THE System SHALL provide detailed analytics`

#### 6. Complex Requirements
**Pattern**: `[WHERE] [WHILE] [WHEN/IF] THE [system] SHALL [response]`
**Usage**: Complex requirements combining multiple conditions
**Example**: `WHERE premium features are active WHILE user is authenticated WHEN data is submitted, THE System SHALL apply enhanced processing`

## INCOSE Quality Rules

### Critical Quality Rules
1. **Active Voice** - Requirements must specify who does what
2. **No Vague Terms** - Avoid "quickly", "adequate", "user-friendly"
3. **No Escape Clauses** - Avoid "where possible", "if feasible"
4. **Single Thought** - Each requirement expresses exactly one requirement
5. **Measurable Criteria** - All conditions must be explicit and measurable

### Additional Quality Guidelines
- Use consistent, defined terminology
- Avoid pronouns like "it", "them", "they"
- Avoid absolutes like "never", "always" unless truly absolute
- Focus on what the system must do, not how it should do it

## Validation Process

### Automated Checking
The framework provides AI agents that automatically:
- Identify EARS pattern compliance
- Check INCOSE quality rules
- Generate correction suggestions
- Provide compliant requirement alternatives

### Manual Review Checklist
- [ ] All system names defined in Glossary
- [ ] Each requirement follows exactly one EARS pattern
- [ ] No vague terms used
- [ ] No escape clauses present
- [ ] Active voice used throughout
- [ ] No negative statements (SHALL not)
- [ ] One testable thought per requirement
- [ ] Measurable criteria specified
- [ ] Consistent terminology maintained
- [ ] No pronouns used
- [ ] No inappropriate absolutes
- [ ] Solution-free (what, not how)

## Common Corrections

### Before and After Examples

#### Vague Terms
**Before**: `The system should quickly process user requests when possible.`
**Issues**: Uses "should", contains "quickly", has escape clause "when possible"
**After**: `WHEN a user submits a request, THE Request_Processing_System SHALL process the request within 2 seconds.`

#### Multiple Requirements
**Before**: `The application must be user-friendly and provide good performance.`
**Issues**: Two requirements, vague terms, uses "must"
**After**: 
- `THE User_Interface_System SHALL complete 90% of common tasks within 3 clicks.`
- `THE Application_System SHALL respond to user interactions within 200 milliseconds.`

#### Passive Voice
**Before**: `Data should be validated before processing.`
**Issues**: Passive voice, uses "should", unclear actor
**After**: `THE Input_Validation_System SHALL validate all data before processing begins.`

## Integration with Templates

### Requirements Template Usage
The framework's requirements templates include:
- EARS pattern examples for each type
- Quality rule reminders
- Validation checklists
- Common correction examples

### Automated Validation
When using the framework:
1. Write requirements using EARS patterns
2. Run automated validation
3. Review and apply suggested corrections
4. Verify compliance before proceeding to design

## Best Practices

1. **Start with User Stories** - Convert user stories to EARS-compliant requirements
2. **Use the Glossary** - Define all system names and technical terms
3. **Keep It Simple** - One clear requirement per statement
4. **Be Specific** - Use measurable, testable criteria
5. **Stay Solution-Free** - Focus on what, not how
6. **Validate Early** - Check compliance before moving to design phase