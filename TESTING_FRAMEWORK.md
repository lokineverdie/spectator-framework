# Testing Framework Guide

## AI Agent-Based Testing Overview

The Spectator Framework uses AI agents for specification-driven testing that works across any implementation platform.

### Testing Philosophy

- Testing agents operate based on specifications and prompts
- Technology-agnostic testing that works across platforms
- Specification-driven rather than code-driven testing
- AI agents generate test scenarios from interface definitions

### Testing Hierarchy

#### 1. Specification-Based Unit Testing
- AI agents test individual module operations against interface specifications
- Agents generate test inputs based on module interface definitions
- Agents validate outputs against expected schema and behavior patterns

#### 2. Integration Testing
- AI agents simulate orchestrator-to-module interactions
- Agents generate realistic data flows through orchestrator intermediary
- Agents validate integration points through specification-based testing
- No direct module-to-module communication testing (prohibited pattern)

#### 3. System Testing
- AI agents execute complete workflows using orchestrator + multiple modules
- Agents validate end-to-end scenarios through orchestrator-mediated communication
- Agents test system behavior under various conditions
- Agents verify that no direct inter-module communication occurs

### Basic Test Specification Template

```yaml
module_test:
  module_name: "data-processor"
  test_type: "unit"
  
  test_scenarios:
    - scenario: "valid_data_processing"
      description: "Test successful data processing operation"
      
      input_specification:
        operation: "processData"
        parameters:
          data: "sample input data"
          format: "json"
        context:
          userId: "test-user-123"
          sessionId: "test-session-456"
        
      expected_output_pattern:
        status: "success"
        data: "processed data object"
        errors: "empty array"
        nextActions: "array of suggested actions"
        
      validation_prompts:
        - "Verify that the output contains processed data"
        - "Confirm all required fields are present"
        - "Validate processing metadata is included"
```

### AI Agent Testing Prompts

#### Basic Testing Agent Prompt
```xml
<test_execution_prompt>
  <role>Module Testing Agent</role>
  
  <task>
    Test the {module_name} module according to the provided specification.
    Generate appropriate test inputs, execute the module operation, and validate outputs.
  </task>
  
  <input_generation_instructions>
    - Create test inputs based on the module interface specification
    - Generate both valid and invalid input scenarios
    - Include edge cases and boundary conditions
  </input_generation_instructions>
  
  <validation_instructions>
    - Compare actual output against expected output patterns
    - Verify all required fields are present and correctly typed
    - Check error handling for invalid inputs
    - Validate performance characteristics
  </validation_instructions>
</test_execution_prompt>
```

### Validation Criteria

#### Functional Readiness
- [ ] All operations implement required input/output interfaces
- [ ] Error handling follows standardized patterns
- [ ] Timeout and retry behavior is implemented
- [ ] Authentication patterns are supported

#### Performance Requirements
- [ ] Operations complete within defined timeout limits
- [ ] Memory usage stays within bounds
- [ ] Concurrent operation handling works
- [ ] Resource cleanup is implemented

#### Security Compliance
- [ ] Input sanitization prevents injection attacks
- [ ] Sensitive data is properly handled
- [ ] Authentication tokens are secure
- [ ] Access controls are implemented

### EARS Compliance Validation

#### Automated EARS Pattern Recognition
AI agents automatically validate requirements against EARS patterns:

- **Ubiquitous**: THE [system] SHALL [response]
- **Event-driven**: WHEN [trigger], THE [system] SHALL [response]
- **State-driven**: WHILE [condition], THE [system] SHALL [response]
- **Unwanted event**: IF [condition], THEN THE [system] SHALL [response]
- **Optional feature**: WHERE [option], THE [system] SHALL [response]

#### Quality Rule Checking
- Active voice usage
- No vague terms
- No escape clauses
- Single requirement per statement
- Measurable criteria
- Consistent terminology

### Integration with Development Workflow

#### Continuous Validation Process
```yaml
validation_workflow:
  trigger_events:
    - "requirement_created"
    - "requirement_modified"
    - "module_implementation_changed"
  
  validation_steps:
    1. pattern_recognition: "Identify EARS pattern compliance"
    2. quality_assessment: "Check INCOSE quality rules"
    3. interface_validation: "Verify module interfaces"
    4. integration_testing: "Test module interactions"
```

### Communication Architecture Testing

#### Orchestrator-Only Communication Validation
```yaml
communication_test:
  test_type: "architecture_compliance"
  
  validation_rules:
    - rule: "no_direct_peer_communication"
      description: "Verify agents never communicate directly with each other"
      test_method: "Monitor all communication channels during test execution"
      
    - rule: "orchestrator_mediated_only"
      description: "All inter-agent data flows through orchestrator"
      test_method: "Trace data flow paths in integration scenarios"
      
    - rule: "hub_and_spoke_topology"
      description: "Communication topology follows hub-and-spoke pattern"
      test_method: "Validate network topology during system tests"
```

#### Testing Agent Prompt for Communication Validation
```xml
<communication_validation_agent>
  <role>Communication Architecture Validation Agent</role>
  
  <task>
    Verify that all agent modules follow the orchestrator-only communication pattern.
    Detect and report any direct peer-to-peer communication attempts.
  </task>
  
  <validation_criteria>
    - All agent communications go through orchestrator
    - No direct agent-to-agent message passing
    - Data flows follow hub-and-spoke topology
    - Integration points respect communication boundaries
  </validation_criteria>
</communication_validation_agent>
```

### Getting Started with Testing

1. **Define Test Specifications** - Create YAML test definitions for your modules
2. **Set Up Testing Agents** - Configure AI agents with appropriate prompts
3. **Validate Communication Architecture** - Ensure orchestrator-only communication
4. **Run Validation** - Execute specification-based testing
5. **Review Results** - Analyze test outputs and compliance reports
6. **Iterate** - Refine specifications based on test feedback

For implementation examples and advanced testing patterns, see the `examples/testing/` directory.