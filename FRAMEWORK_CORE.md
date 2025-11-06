# Framework Core Principles

## Overview

Spectator Framework is a system for creating technology-agnostic agent specifications through spec-driven development. This document defines the core principles that govern all framework usage.

## Core Architecture

### Multi-Agent System Design

#### Orchestrator Agent Pattern
- **Central Coordination**: Orchestrator manages all workflow and agent interactions
- **Single Point of Control**: All communication flows through orchestrator
- **State Management**: Orchestrator maintains session state and user context
- **Result Aggregation**: Combines outputs from multiple agents

#### Specialized Agent Design
- **Domain-Specific**: Each agent handles specific capabilities (search, analysis, communication)
- **Tool Integration**: Agents have their own tool ecosystems
- **Independent Operation**: Agents can be developed and tested separately

#### Communication Rules (CRITICAL)
- **Hub-and-Spoke ONLY**: All agent communication flows through orchestrator
- **NO Peer-to-Peer**: Agents NEVER communicate directly with each other
- **Standardized Interfaces**: Common message formats across all agents
- **Event-Driven**: Asynchronous communication through orchestrator

```
✅ Correct: Agent A → Orchestrator → Agent B
❌ Forbidden: Agent A → Agent B (direct communication)
```

## Development Principles

### 1. Simplicity First
- **Keep things simple** - Only add complexity when specifically requested
- **Minimal viable solutions** - Start with simplest implementation that works
- **Essential functionality only** - Avoid over-engineering
- **Simple is better** - Prefer straightforward approaches

### 2. No Assumptions Policy
- **Literal Implementation**: Implement ONLY what is explicitly specified
- **No Implicit Features**: Never add functionality that seems "logical" without confirmation
- **Ask Before Extending**: When identifying potential features, ASK the user
- **Minimal Viable Implementation**: Choose simplest implementation that satisfies requirements

#### Examples of Prohibited Assumptions
- If requirement mentions "UserID", do NOT automatically add user authentication
- If requirement mentions "email field", do NOT automatically add email validation system
- If requirement mentions "job search", do NOT automatically add job application tracking

### 3. Technology Neutrality
- **Platform Independence**: Specifications work across any implementation platform
- **Technology Flexibility**: Choose technologies at appropriate development phase
- **No Tech Assumptions**: Avoid database, framework, or language-specific details
- **Multiple Pathways**: Support various implementation approaches

### 4. Specification-Driven Development
- **Spec-First Approach**: All development starts with comprehensive specifications
- **EARS Compliance**: Use Easy Approach to Requirements Syntax patterns
- **Technology-Neutral Design**: Specifications remain independent of implementation
- **Iterative Refinement**: Specifications evolve through structured feedback

## EARS Requirements Patterns

### The Five Essential Patterns

1. **Ubiquitous**: `THE [system] SHALL [response]`
   - Example: `THE Data_Processing_System SHALL validate all input parameters`

2. **Event-driven**: `WHEN [trigger], THE [system] SHALL [response]`
   - Example: `WHEN user submits data, THE System SHALL acknowledge within 1 second`

3. **State-driven**: `WHILE [condition], THE [system] SHALL [response]`
   - Example: `WHILE processing data, THE System SHALL display progress indicators`

4. **Unwanted event**: `IF [condition], THEN THE [system] SHALL [response]`
   - Example: `IF processing fails, THEN THE System SHALL log error and notify user`

5. **Optional feature**: `WHERE [option], THE [system] SHALL [response]`
   - Example: `WHERE advanced mode enabled, THE System SHALL provide detailed analytics`

### Quality Rules
- Use active voice (system does something)
- No vague terms ("quickly", "user-friendly")
- No escape clauses ("where possible", "if feasible")
- One requirement per statement
- Measurable criteria only

## Data Exchange Standards

### Standard Interface Pattern
```
ModuleInput {
  operation: string           // The requested operation
  parameters: object         // Operation-specific parameters
  context: ExecutionContext  // Shared execution context
  metadata: object          // Optional metadata
}

ModuleOutput {
  status: "success" | "error" | "partial"
  data: object              // Operation results
  errors: ErrorInfo[]       // Any errors encountered
  metadata: object         // Response metadata
  nextActions: string[]    // Suggested follow-up operations
}
```

### Communication Architecture Benefits
- **Simplified Dependencies**: No complex inter-agent dependency management
- **Clear Data Flow**: All communication paths explicit and traceable
- **Easy Testing**: Modules tested in isolation with orchestrator mocks
- **Flexible Composition**: Orchestrator can route between different implementations
- **Centralized Control**: Single point for monitoring and error handling

## Quality Standards

### Requirements Quality
- Follow EARS patterns exactly
- Comply with INCOSE semantic rules
- Include clear acceptance criteria
- Maintain technology-neutral language
- Use active voice, avoid vague terms

### Design Quality
- Focus on system behavior and interfaces
- Avoid implementation-specific details
- Include error handling and edge cases
- Document agent interactions through orchestrator
- Maintain technology neutrality

### Implementation Readiness
- Tasks should be actionable by developers
- Include sufficient detail for technology selection
- Provide clear integration points
- Maintain modularity for extensibility
- Follow hub-and-spoke communication architecture

## Validation and Compliance

### Automated Checking
- EARS pattern compliance validation
- INCOSE quality rule checking
- Interface compatibility verification
- Communication architecture validation

### Manual Review Checklist
- [ ] All system names defined in glossary
- [ ] Each requirement follows exactly one EARS pattern
- [ ] No vague terms or escape clauses used
- [ ] Active voice used throughout
- [ ] One testable requirement per statement
- [ ] Orchestrator-only communication enforced
- [ ] Technology neutrality maintained

## Success Metrics

- Number of modules developed using framework
- Time reduction in specification development
- Quality improvement in specification completeness
- Integration success rates between modules
- Developer satisfaction with framework tools

This document defines the non-negotiable core principles. All framework usage must comply with these standards.