# Module Development Guidelines

## Technology-Neutral Specification Patterns

### Core Principles

1. **Simplicity First** - Keep specifications minimal and focused
2. **Technology Agnostic** - Avoid implementation-specific details
3. **Modular Design** - Create independent, testable components
4. **Clear Interfaces** - Define explicit input/output contracts
5. **Orchestrator-Only Communication** - Agent modules communicate only with the orchestrator, never directly with each other

### Interface Design Patterns

#### Standard Interface Pattern
```
ModuleInput {
  operation: string           // The requested operation/action
  parameters: object         // Operation-specific parameters
  context: ExecutionContext  // Shared execution context
  metadata: object          // Optional metadata for the operation
}

ModuleOutput {
  status: "success" | "error" | "partial"
  data: object              // Operation results
  errors: ErrorInfo[]       // Any errors encountered
  metadata: object         // Response metadata
  nextActions: string[]    // Suggested follow-up operations
}
```

#### Error Handling Pattern
```
ErrorInfo {
  code: string             // Standardized error code
  message: string          // Human-readable error message
  severity: "low" | "medium" | "high" | "critical"
  recoverable: boolean     // Whether the error can be retried
  context: object         // Additional error context
}
```

### Data Exchange Standards

#### Supported Data Types
- **Primitive**: string, number, boolean, null
- **Composite**: object, array
- **Specialized**: datetime (ISO 8601), uuid (RFC 4122)

#### JSON Schema Pattern
```json
{
  "schemaVersion": "1.0",
  "dataType": "ModuleName_OperationType",
  "properties": {
    "propertyName": {
      "type": "string|number|boolean|object|array",
      "required": true|false,
      "description": "Property purpose and constraints"
    }
  }
}
```

### Naming Conventions

#### Module Names
- Format: `{domain}-{function}-{type}`
- Examples: `data-processor-service`, `content-analyzer-engine`
- Use lowercase with hyphens
- Maximum 50 characters

#### Operation Names
- Format: `{verb}{Object}` in camelCase
- Examples: `processData`, `analyzeContent`, `validateInput`
- Use clear, action-oriented verbs

#### Entity Names
- Use PascalCase: `UserProfile`, `ContentItem`, `ProcessingResult`
- Use singular nouns
- Prefix with module domain when needed

### Communication Architecture

#### Orchestrator-Centric Pattern
All agent modules follow a hub-and-spoke communication model:

- **Agent → Orchestrator**: Modules send results, status updates, and requests to orchestrator
- **Orchestrator → Agent**: Orchestrator sends commands, data, and coordination instructions to modules
- **Agent ↛ Agent**: Modules NEVER communicate directly with other modules
- **Data Flow**: All inter-module data flows through the orchestrator as intermediary

#### Benefits of Orchestrator-Only Communication
- **Simplified Dependencies**: No complex inter-agent dependency management
- **Clear Data Flow**: All communication paths are explicit and traceable
- **Easy Testing**: Modules can be tested in isolation with orchestrator mocks
- **Flexible Composition**: Orchestrator can dynamically route between different module implementations
- **Centralized Control**: Single point for workflow coordination, error handling, and monitoring

#### Implementation Guidelines
```
✅ Correct Pattern:
Module A → Orchestrator → Module B

❌ Incorrect Pattern:
Module A → Module B (direct communication)
```

### Platform Compatibility

#### Universal Requirements
1. **Data Format Flexibility**
   - Primary support for JSON input/output
   - Configurable schema validation
   - Support for multiple serialization formats

2. **Authentication Adaptability**
   - Pluggable authentication mechanisms
   - Configurable authentication providers
   - Support for various credential types

3. **Error Handling Universality**
   - Platform-agnostic error codes
   - Configurable retry policies
   - Graceful degradation strategies

4. **Integration Flexibility**
   - Adapter pattern support for any workflow system
   - Configurable communication protocols
   - Support for sync and async operations

### Validation Framework

#### Basic Validation Requirements
- All inputs must validate against defined schemas
- Support for both strict and permissive validation modes
- Clear error messages for validation failures
- Contract testing for expected behavior

#### Quality Checklist
- [ ] Interface compliance verified
- [ ] Data validation implemented
- [ ] Error handling follows patterns
- [ ] Performance requirements met
- [ ] Security requirements addressed
- [ ] Documentation complete

### Module Structure Template

```
modules/{module-name}/
├── specifications/
│   ├── requirements.md      # EARS-compliant requirements
│   ├── design.md           # Architecture and design
│   └── interfaces.md       # Interface definitions
├── data-models/
│   ├── {entity-name}.puml  # Data structure definitions
│   └── schemas/            # JSON schema files
├── diagrams/
│   ├── architecture.puml   # Module architecture
│   └── workflows.puml      # Process flows
└── prompts/
    ├── {agent-type}-prompts.xml  # Agent behavior definitions
    └── conversation-flows.xml    # Interaction patterns
```

### Implementation Guidelines

1. **Start Simple** - Begin with minimal viable implementation
2. **Orchestrator-Only** - Design all communication to go through orchestrator
3. **Iterate** - Refine based on actual requirements
4. **Test Early** - Validate each component independently with orchestrator mocks
5. **Document** - Maintain clear interface documentation
6. **Stay Neutral** - Avoid technology-specific assumptions

For advanced topics including AI agent-based testing, see the separate [Testing Framework Guide](TESTING_FRAMEWORK.md).