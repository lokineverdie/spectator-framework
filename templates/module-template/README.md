# Module Template Usage

## Quick Start

1. **Copy this template**: `cp -r templates/module-template modules/your-module-name`
2. **Replace placeholders**: Change `{MODULE_NAME}` to your actual module name in all files
3. **Customize content**: Update architecture, data models, and prompts for your domain

## Files in This Template

### README.md (this file)
Usage instructions and customization guide

### architecture.puml
Simple PlantUML diagram showing:
- Module components
- Orchestrator communication
- Tool integrations
- Data flow

### data-models.puml
PlantUML class diagrams for:
- Input/output interfaces
- Core data entities
- Configuration models

### agent-prompts.xml
XML definitions for:
- Agent role and capabilities
- Communication rules
- Behavior patterns

### Optional: Modular Prompt Structure
For complex agents, you can use modular prompts:
```
your-module-name/
├── agent_prompt_modular.xml    # Template with component references
├── prompt-parts/               # Modular components
│   ├── metadata-and-role.xml
│   ├── core-behavior.xml
│   ├── communication-rules.xml
│   └── [domain-specific].xml
└── agent_prompt.xml           # Final assembled prompt (generated)
```

## Customization Examples

### Replace Module Name
```bash
# In all files, replace:
{MODULE_NAME} → DataProcessor
{AGENT_NAME} → DataProcessingAgent
{DOMAIN} → data processing
```

### Update Architecture
- Add your specific components
- Define tool integrations
- Show data flow patterns
- Maintain orchestrator-only communication

### Modify Data Models
- Replace example entities with your data structures
- Update interface definitions
- Add domain-specific properties

### Customize Agent Prompts
- Define agent's specific role
- List domain capabilities
- Set behavior rules
- Include examples

## Validation Checklist

- [ ] All placeholders replaced with actual names
- [ ] Architecture shows orchestrator-only communication
- [ ] Data models follow standard interface patterns
- [ ] Agent prompts enforce framework rules
- [ ] PlantUML syntax is valid
- [ ] XML is well-formed

## Advanced: Modular Prompts

For complex agents, consider using modular prompts:

### 1. Create Modular Structure
```bash
mkdir your-module-name/prompt-parts
```

### 2. Break Down Prompt Components
- **metadata-and-role.xml**: Agent identity and capabilities
- **core-behavior.xml**: Primary behavioral instructions
- **communication-rules.xml**: Hub-and-spoke compliance rules
- **domain-specific.xml**: Your agent's specialized logic

### 3. Create Template with References
```xml
<?xml version="1.0" encoding="UTF-8"?>
<agent-definition>
  <!-- REFERENCE: prompt-parts/metadata-and-role.xml -->
  <!-- Agent metadata and role definition -->
  
  <behavior>
    <!-- REFERENCE: prompt-parts/core-behavior.xml -->
    <!-- Core behavioral instructions -->
    
    <!-- REFERENCE: prompt-parts/communication-rules.xml -->
    <!-- Communication rules and response formatting -->
  </behavior>
</agent-definition>
```

### 4. Build Final Prompt
```bash
python build-modular-prompt.py your-module-name --validate
```

## Prompt Optimization

### Cache Optimization
This template is structured for optimal prompt caching:
- **Static content first**: Role, principles, capabilities (high cache value)
- **Framework rules**: Consistent compliance patterns (high cache value)
- **Examples**: Reusable interaction patterns (medium cache value)
- **Dynamic content**: Place user input and session data last (no cache value)

### Token Minimization Tips
- Remove filler words: "please", "kindly", "I would like"
- Use bullet points instead of paragraphs
- Keep examples concise but complete
- Use abbreviations for repeated concepts

### Performance Guidelines
- Target 1024+ tokens for cache activation
- Maintain consistent structure across requests
- Use temperature 0.1-0.3 for consistent outputs
- Monitor cache hit rates (target >80%)

**📖 For comprehensive optimization strategies, see [PROMPT_OPTIMIZATION_GUIDE.md](../../PROMPT_OPTIMIZATION_GUIDE.md)**

## Framework Compliance

- **Orchestrator-Only Communication**: Agent communicates only with orchestrator
- **Technology Neutrality**: No implementation-specific details
- **Standard Interfaces**: Uses ModuleInput/ModuleOutput patterns
- **EARS Compliance**: Any requirements follow EARS patterns
- **Simplicity First**: Minimal viable implementation

## Getting Help

- Check `FRAMEWORK_CORE.md` for core principles
- Review `DEVELOPMENT_GUIDE.md` for development practices
- See main README.md for framework overview