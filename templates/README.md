# Spectator Framework Templates

This directory contains all templates for building modular agent components and specifications following the framework's "keep things simple" principle. This is the central location for all reusable templates in the Spectator Framework.

## Directory Structure

```
templates/
├── specs/                          # Kiro spec workflow templates
│   ├── requirements.md             # EARS-compliant requirements template
│   ├── design.md                   # Architecture and design template
│   └── tasks.md                    # Implementation tasks template
├── modules/
│   └── module-template/            # Module-specific artifacts template
│       ├── diagrams/
│       │   ├── architecture.puml   # Simple architecture diagram
│       │   ├── workflows.puml      # Basic workflow diagram
│       │   └── integration.puml    # Module integration diagram
│       ├── data-models/
│       │   ├── data-models.puml    # Core data entities
│       │   ├── configuration-models.puml  # Configuration classes
│       │   └── interface-models.puml      # Interface definitions
│       └── prompts/
│           ├── agent-prompts.xml   # Agent behavior definitions
│           ├── conversation-flows.xml     # Conversation management
│           └── context-management.xml     # Context and memory management
└── README.md                       # This file
```

## Quick Start

### 1. Create a New Module
```bash
# Copy the template
cp -r templates/modules/module-template modules/your-module-name

# Customize the files
# - Replace "Module" with your actual module name in all files
# - Update class names, methods, and fields
# - Modify diagrams to match your architecture
```

### 2. Create a New Spec
```bash
# Copy spec templates
mkdir .kiro/specs/your-feature-name
cp templates/specs/* .kiro/specs/your-feature-name/

# Follow the workflow
# 1. Fill out requirements.md with EARS patterns
# 2. Create design.md based on requirements
# 3. Generate tasks.md for implementation
```

## Template Files

### Spec Templates (`templates/specs/`)
- **requirements.md**: EARS-compliant requirements with examples
- **design.md**: Architecture and design document structure
- **tasks.md**: Implementation planning with task formatting

### Module Templates (`templates/modules/module-template/`)

#### Diagrams (`diagrams/`)
- **architecture.puml**: Simple component architecture
- **workflows.puml**: Basic process flow
- **integration.puml**: Module integration patterns

#### Data Models (`data-models/`)
- **data-models.puml**: Core entities and relationships
- **configuration-models.puml**: Configuration classes
- **interface-models.puml**: Interface definitions

#### Prompts (`prompts/`)
- **agent-prompts.xml**: Agent behavior and capabilities
- **conversation-flows.xml**: Conversation state management
- **context-management.xml**: Context and memory handling

## Template Principles

### Simplicity First
- Minimal viable templates with essential elements only
- Easy to understand and customize
- No over-engineering or complex abstractions

### Technology Agnostic
- Templates work with various implementation platforms
- No technology-specific assumptions
- Flexible for different database and workflow engines

### Modular Design
- Independent, testable components
- Clear interfaces between modules
- Bottom-up development approach

## Customization Examples

### Data Model
```puml
// Original template
class MainEntity {
  +String id
  +String name
}

// Customized for your domain
class UserProfile {
  +String id
  +String name
  +String email
  +String preferences
}
```

### Agent Prompt
```xml
<!-- Original template -->
<agent-name>AGENT_NAME</agent-name>

<!-- Customized -->
<agent-name>DataProcessingAgent</agent-name>
```

### Requirements
```markdown
# Original template
THE {System_Name} SHALL {response}

# Customized
THE Data_Processing_System SHALL process user requests within 3 seconds
```

## Customization Tips

1. **Keep it simple** - Start with minimal changes
2. **Replace systematically** - Update all placeholder names consistently
3. **Test early** - Validate PlantUML syntax after changes
4. **Document changes** - Note customizations for future reference

## Common Replacements

| Template | Replace | With Example |
|----------|---------|--------------|
| All files | `Module` | `DataProcessor` |
| Data models | `MainEntity` | `UserProfile` |
| Interfaces | `MainInterface` | `ProcessingInterface` |
| Agents | `AGENT_NAME` | `DataProcessingAgent` |
| Requirements | `{System_Name}` | `Data_Processing_System` |

## Best Practices

1. **Keep it simple** - Add only what you need
2. **Start small** - Begin with minimal implementation
3. **Iterate** - Refine based on actual requirements
4. **Document** - Update templates based on learnings
5. **Test independently** - Validate each module separately