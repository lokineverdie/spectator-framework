# Development Guide

## Development Practices and Guidelines

This document covers practical development practices, validation processes, and optimization techniques for the Spectator Framework.

## Requirements Documentation Process

### Before Writing Requirements
1. **Check existing specs** in `.kiro/specs/` to understand current system
2. **Review agent definitions** to understand roles and responsibilities  
3. **Examine data models** to understand current data structures
4. **Check existing prompts** to understand agent behaviors
5. **Validate assumptions** against existing system architecture
6. **Use correct terminology** from established names
7. **Avoid contradictions** with existing system design

### EARS Pattern Validation

#### Automated Validation Process
The framework provides AI agents that automatically:
- Identify EARS pattern compliance
- Check INCOSE quality rules
- Generate correction suggestions
- Provide compliant requirement alternatives

#### Common Corrections

**Vague Terms**
- Before: `The system should quickly process requests when possible`
- After: `WHEN user submits request, THE System SHALL process within 2 seconds`

**Multiple Requirements**
- Before: `The application must be user-friendly and provide good performance`
- After: Split into separate requirements with measurable criteria

**Passive Voice**
- Before: `Data should be validated before processing`
- After: `THE Input_Validation_System SHALL validate all data before processing`

## Agent Guidance and Challenge Policy

### When to Challenge User Decisions

#### Framework Violations
- Direct agent-to-agent communication requests (violates orchestrator-only pattern)
- Over-engineering that conflicts with "Simplicity First" principle
- Technology-specific implementations in neutral specifications

#### How to Challenge Constructively
1. **Acknowledge the request** - Show understanding of goals
2. **Identify the conflict** - Reference specific framework guidelines
3. **Present alternatives** - Offer framework-compliant approaches
4. **Ask for confirmation** - Let user choose final approach

#### Example Challenge
```
User Request: "Make search agent communicate directly with analysis agent"

Response: "I understand you want efficient agent cooperation. However, this conflicts 
with the orchestrator-only communication principle. Instead, I can design:

Search Agent → Orchestrator → Analysis Agent

This maintains loose coupling while achieving your goal. Would you prefer this approach?"
```

## Modular Prompt Development

### Modular Prompt Approach
The framework supports modular prompt development for complex agents, allowing you to:
- **Break down complex prompts** into manageable, focused components
- **Reuse common components** across multiple agents
- **Maintain consistency** in agent behavior patterns
- **Optimize for caching** by separating static and dynamic content

### Modular Prompt Structure
```
agent-name/
├── agent_prompt_modular.xml    # Template with component references
├── agent_prompt.xml           # Final assembled prompt (generated)
└── prompt-parts/              # Modular components
    ├── metadata-and-role.xml  # Agent identity and capabilities
    ├── core-behavior.xml      # Core behavioral instructions
    ├── communication-rules.xml # Communication patterns
    ├── error-handling.xml     # Error handling strategies
    └── [domain-specific].xml  # Domain-specific components
```

### Component Reference Pattern
In your template file, reference components using:
```xml
<!-- REFERENCE: prompt-parts/component-name.xml -->
<!-- Description of what this component provides -->
```

### Building Modular Prompts
Use the provided build script:
```bash
# Build a modular prompt
python build-modular-prompt.py agent-name

# With validation and verbose output
python build-modular-prompt.py agent-name --validate --verbose

# Custom template and output files
python build-modular-prompt.py agent-name --template custom.xml --output final.xml
```

### Modular Component Guidelines
- **metadata-and-role.xml**: Agent identity, version, capabilities, communication interface
- **core-behavior.xml**: Primary behavioral instructions and response requirements
- **communication-rules.xml**: Hub-and-spoke compliance and response formatting
- **error-handling.xml**: Error handling patterns and fallback strategies
- **domain-specific components**: Specialized logic for your agent's domain

### Benefits of Modular Prompts
- **Maintainability**: Update specific behaviors without touching entire prompt
- **Reusability**: Share common components across agents
- **Testing**: Test individual components in isolation
- **Caching Optimization**: Separate static components from dynamic content
- **Collaboration**: Multiple developers can work on different components

## Prompt Optimization and Caching

### Overview
Effective prompt optimization reduces costs by up to 90% and improves response times by up to 80%. The framework supports advanced optimization techniques for all major LLM providers.

**📖 For comprehensive optimization strategies, see [PROMPT_OPTIMIZATION_GUIDE.md](PROMPT_OPTIMIZATION_GUIDE.md)**

### Quick Reference: Caching Best Practices

#### OpenAI (GPT-4o and newer)
- **Minimum**: 1024+ tokens for cache activation
- **Structure**: Static content first, variable content last
- **Increments**: 128-token cache increments (1024, 1152, 1280...)
- **Rate limits**: <15 requests/minute per prefix for optimal caching

#### Claude (All models)
- **Minimum**: 1024-4096 tokens (model dependent)
- **Control**: Use `cache_control: {"type": "ephemeral"}`
- **Hierarchy**: Tools → System → Messages caching order
- **TTL**: 5 minutes default, 1 hour option available

#### Meta/Llama (Open source)
- **Focus**: Consistent structure and clear delimiters
- **Context**: Manage context windows efficiently
- **Format**: Use explicit instruction formatting

### Framework-Optimized Template Structure
```
# STATIC SECTION (CACHED) - Use modular components
[Agent metadata and role] - metadata-and-role.xml
[Core behavior instructions] - core-behavior.xml  
[Communication rules] - communication-rules.xml
[Tool definitions and schemas] - tool-definitions.xml
[Domain-specific logic] - domain components

# DYNAMIC SECTION (NOT CACHED)
Current request: {{user_input}}
Session context: {{session_data}}
Timestamp: {{timestamp}}
```

### Token Minimization Strategies

#### Content Optimization
- Remove filler words: "please", "kindly", "I would like"
- Use abbreviations: "e.g." vs "for example"
- Eliminate redundancy in instructions
- Compress examples to minimal viable format

#### Structural Efficiency
```xml
<!-- INEFFICIENT -->
<instructions>
Please carefully analyze the following data and provide a comprehensive analysis that includes trends, patterns, and actionable recommendations for future business decisions.
</instructions>

<!-- EFFICIENT -->
<instructions>
Analyze data: identify trends, patterns, recommendations.
</instructions>
```

### Cache Hit Rate Optimization

#### Consistent Structure Patterns
- Maintain identical prompt ordering across requests
- Use standardized formatting and spacing
- Implement version control for prompt templates
- Separate static from dynamic content clearly

#### Strategic Content Placement
1. **High Cache Value** (place first): Role definitions, tool schemas, examples
2. **Medium Cache Value** (place middle): User preferences, session context  
3. **No Cache Value** (place last): Current request, real-time data, timestamps

### Performance Monitoring

#### Key Metrics to Track
- Cache hit rates (target: >80%)
- Token usage reduction (target: 25-40%)
- Response time improvement (target: 50-70%)
- Cost reduction (target: up to 90% with high cache hits)

#### Implementation Validation
```python
# Example cache performance validation
def validate_cache_performance(prompt_template):
    """Validate prompt template for cache optimization"""
    checks = {
        'min_tokens': len(prompt_template.split()) * 1.3 >= 1024,
        'static_first': prompt_template.startswith(STATIC_CONTENT),
        'consistent_structure': validate_structure(prompt_template),
        'proper_separation': has_clear_dynamic_section(prompt_template)
    }
    return all(checks.values()), checks
```

### Integration with Modular Prompts

The modular prompt system is designed for optimal caching:
- **metadata-and-role.xml**: High cache value (rarely changes)
- **core-behavior.xml**: High cache value (stable instructions)
- **communication-rules.xml**: High cache value (framework compliance)
- **domain-specific.xml**: Medium cache value (may evolve)
- **Dynamic content**: No cache value (request-specific)

### Cost Impact Examples

#### Token Reduction Results
- **Verbose removal**: 25-40% token reduction
- **Example optimization**: 15-30% token reduction  
- **Schema efficiency**: 10-20% token reduction
- **Smart formatting**: 5-15% token reduction

#### Cache Hit Savings
```
Monthly cost with 80% cache hit rate:
Base cost: $1000/month
With caching: $200/month (80% reduction)
Annual savings: $9,600
```

For detailed implementation examples, provider-specific optimizations, and advanced techniques, refer to the comprehensive [PROMPT_OPTIMIZATION_GUIDE.md](PROMPT_OPTIMIZATION_GUIDE.md).

## Testing and Validation

### AI Agent-Based Testing
- **Specification-driven**: Tests based on interface definitions
- **Technology-agnostic**: Works across any implementation platform
- **Automated validation**: AI agents generate test scenarios

### Testing Hierarchy
1. **Unit Testing**: Individual module operations against specifications
2. **Integration Testing**: Orchestrator-to-module interactions
3. **System Testing**: Complete workflows through orchestrator
4. **Communication Testing**: Verify orchestrator-only patterns

### Basic Test Template
```yaml
module_test:
  module_name: "data-processor"
  test_scenarios:
    - scenario: "valid_processing"
      input_specification:
        operation: "processData"
        parameters: {data: "sample", format: "json"}
      expected_output_pattern:
        status: "success"
        data: "processed object"
```

### Communication Architecture Testing
```yaml
communication_test:
  validation_rules:
    - rule: "no_direct_peer_communication"
      test_method: "Monitor all communication channels"
    - rule: "orchestrator_mediated_only"  
      test_method: "Trace data flow paths"
```

## Naming Conventions

### Simple Naming Rules
- **Directories**: kebab-case (`web-search`, `resume-analysis`)
- **Files**: descriptive names (`requirements.md`, `architecture.puml`)
- **Classes**: PascalCase (`UserProfile`, `JobPosting`)
- **Operations**: camelCase (`processData`, `analyzeContent`)
- **Agents**: `{Domain}Agent` (`SearchAgent`, `AnalysisAgent`)

### File Organization
```
modules/{module-name}/
├── README.md              # Usage instructions
├── architecture.puml      # System architecture
├── data-models.puml       # Data structures
└── agent-prompts.xml      # Agent behaviors
```

## Version Control Best Practices

### Branch Strategy
- `main` - Stable releases
- `develop` - Integration branch
- `feature/{module-name}` - New development

### Commit Messages
```
{type}({scope}): {description}

Types: feat, fix, docs, refactor, test
Scopes: framework, module, template
```

### Quality Gates
- [ ] EARS pattern compliance
- [ ] Technology neutrality maintained
- [ ] Orchestrator-only communication
- [ ] Documentation complete
- [ ] Tests passing

## Development Workflow

### Spec-Driven Process
1. **Requirements**: Write EARS-compliant requirements
2. **Design**: Create technology-neutral architecture
3. **Tasks**: Generate actionable implementation steps
4. **Validate**: Use AI agents for specification validation
5. **Implement**: Build following specifications
6. **Test**: Validate using specification-based testing

### Template Usage
1. **Copy templates** from `templates/` directory
2. **Replace placeholders** systematically
3. **Validate compliance** against framework standards
4. **Test independently** before integration

### Quality Assurance
- Automated EARS pattern validation
- Interface compatibility checking
- Communication architecture verification
- Performance and security validation

## Common Pitfalls to Avoid

1. **Direct agent communication** - Always use orchestrator
2. **Technology assumptions** - Keep specifications neutral
3. **Over-engineering** - Start simple, add complexity only when needed
4. **Vague requirements** - Use specific, measurable criteria
5. **Assumption creep** - Implement only what's specified

## Getting Started Checklist

- [ ] Read framework core principles
- [ ] Understand orchestrator-only communication
- [ ] Practice EARS pattern writing
- [ ] Copy and customize templates
- [ ] Validate against framework standards
- [ ] Test with AI agents before implementation